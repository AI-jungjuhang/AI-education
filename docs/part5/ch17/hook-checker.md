# 실습: 자동 검사관 달기

!!! abstract "이 페이지에서 배우는 것"
    - 책 페이지를 고칠 때마다 **"출처와 기준" 절이 있는지 자동으로 검사**하는 훅을 만들어요.
    - 훅 스크립트는 ==입력을 읽고, 끝날 때 숫자(종료 코드)로 답==해요. 2는 "문제 있음"이에요.
    - 그 전에 스크립트를 먼저 혼자 돌려 보는 것이 요령이에요.

## 1. 우리 책의 약속을 지키는 검사관

이 책의 약속 하나는 "페이지마다 출처와 기준 날짜를 적는다"예요. 사람(과 AI)은 가끔 잊어요. 그래서 파일을 고친 직후 검사관이 확인하게 해 볼게요.

## 2. 검사 스크립트 만들기

`.claude/hooks/check-page.sh`에 저장해요.

```bash
#!/bin/bash
# 페이지를 고친 뒤 "출처와 기준" 절이 있는지 확인한다.
INPUT=$(cat)
FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

case "$FILE" in
  */docs/*.md) ;;
  *) exit 0 ;;
esac

if ! grep -q "^## 출처와 기준" "$FILE"; then
  echo "이 페이지에는 '## 출처와 기준' 절이 없어요. 출처와 기준 날짜를 추가해 주세요: $FILE" >&2
  exit 2
fi
exit 0
```

읽는 법을 한 줄씩 볼게요.

- `INPUT=$(cat)`: 훅은 일어난 일을 JSON 글자로 받아요. 그걸 변수에 담아요.
- `jq -r '.tool_input.file_path'`: 그 JSON에서 "고친 파일 경로"만 꺼내요. (`jq`가 없으면 설치해야 해요.)
- `case … */docs/*.md`: docs 폴더 안의 마크다운이 아니면 아무것도 안 하고 끝나요.
- `exit 2`와 `>&2`: 문제를 알리는 말은 오류 출력(`>&2`)에 쓰고 2로 끝내요. 이 글이 Claude에게 전달돼요.

실행 권한을 줘요.

```bash
chmod +x .claude/hooks/check-page.sh
```

## 3. 혼자 먼저 돌려 보기 (중요!)

훅은 Claude가 부르기 전에 내가 직접 돌려 봐요. 가짜 입력을 넣으면 돼요.

```bash
echo '{"tool_input":{"file_path":"/경로/docs/test.md"}}' | .claude/hooks/check-page.sh; echo "종료 코드: $?"
```

"출처와 기준" 절이 없는 파일이면 메시지가 나오고 종료 코드 2가, 있으면 0이 나와야 해요. 이 글을 쓸 때도 같은 모양의 스크립트로 두 경우를 모두 확인했어요.

## 4. 등록하기

`.claude/settings.json`에 다음을 넣어요.

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/check-page.sh"
          }
        ]
      }
    ]
  }
}
```

`Edit|Write`는 "파일을 고치거나 새로 쓸 때"를 뜻해요. `PostToolUse`는 도구가 끝난 직후라 파일은 이미 바뀐 상태예요. 이때 2로 끝내면 Claude는 막지는 못하지만 내 메시지를 읽고 스스로 고쳐요.

!!! tip "10살 눈높이 한 줄 요약"
    검사관 훅은 "문제 있어요(2)" 또는 "괜찮아요(0)"로만 대답하는 짧은 프로그램이에요.

!!! note "★ 한 걸음 더 (심화)"
    "하기 전에 막는" 훅은 `PreToolUse`예요. 예를 들어 `.env` 같은 비밀 파일을 고치려 하면 막는 스크립트가 있어요. `PostToolUse`는 일이 끝난 뒤 알려 주고, `PreToolUse`는 일이 일어나기 전에 막아요. 2로 끝냈을 때의 의미는 이벤트마다 달라서(막는 이벤트도 있고, 알려 주기만 하는 이벤트도 있어요) 훅 레퍼런스의 표를 확인해야 해요.

## 직접 해보기

1. 위 스크립트를 만들고 **혼자 먼저** 돌려서 0과 2가 나오는지 확인해요.
2. 설정에 등록하고 `/hooks`에서 `PostToolUse`에 보이는지 확인해요.
3. Claude에게 "docs 폴더에 test.md를 만들고 제목만 적어 줘"라고 시켜요. 검사관 메시지를 받고 Claude가 "출처와 기준" 절을 추가하는지 봐요.

## 오늘 바로 써먹기

- 매번 같은 말로 부탁하던 점검이 있다면 훅으로 옮기기
- 새 훅은 항상 혼자 돌려 본 뒤 등록하기
- 무거운 검사(전체 빌드 등)는 파일을 고칠 때마다 돌리지 말고 Claude가 답을 마칠 때(`Stop`)로 미루기

## 자주 하는 오해

- "훅이 오류를 내면 작업이 멈춘다?" 종료 코드 0과 2 외의 숫자는 대부분 그냥 지나가요. 하지만 꼭 막아야 하는 검사는 설정을 따로 해야 해요.
- "검사관이 있으니 내가 안 봐도 된다?" 검사관은 '절이 있는지'만 봐요. 출처가 맞는지는 사람이 열어 봐야 해요.
- "`Edit|Write` 훅은 모든 파일 변경을 본다?" 아니에요. Claude는 명령창(Bash)으로도 파일을 만들거나 고칠 수 있어서, 그런 변경은 이 훅이 못 볼 수 있어요. 모든 변경을 확인해야 하면 공식 문서는 Claude가 답을 마칠 때(`Stop`) 작업 폴더를 한 번 훑는 훅을 권해요.

## 출처와 기준

- 기준: Claude Code 2.1.319, 확인일 2026-11-07. 스크립트는 `jq`가 있는 리눅스·맥 환경에서 직접 돌려 확인했어요.
- 사실 기준: [공식 문서: 훅 가이드](https://code.claude.com/docs/en/hooks-guide.md), [훅 레퍼런스](https://code.claude.com/docs/en/hooks.md)
- 학습 순서 참고: [claude-howto 06-hooks](https://github.com/luongnv89/claude-howto/tree/main/06-hooks) (MIT, 다시 씀)
