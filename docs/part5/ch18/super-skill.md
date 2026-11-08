# 실습: 영상 제작 슈퍼 스킬

!!! abstract "이 페이지에서 배우는 것"
    - 5B에서 만든 **스킬 + 조수 셋 + 훅**을 `studio` 플러그인 하나로 묶고, `/studio:episode`로 부르는 슈퍼 스킬을 만들어요.
    - 슈퍼 스킬은 새로운 기술이 아니라 ==앞에서 만든 것들의 순서를 적은 글==이에요.
    - 부작용이 있는 스킬은 항상 내가 직접 부르게 해요.

## 1. 설계도를 상자에 담기

5.8 마지막에서 만든 표를 기억해요? 그 표가 설계도였어요. 이제 상자에 담아요.

| 부품 | 파일 | 어디서 만들었나 |
|---|---|---|
| 대본 기준 | `skills/make-short/SKILL.md` | 5.5 |
| 조사·대본·검토 조수 | `agents/researcher.md` 외 2개 | 5.8 |
| 형식 검사관 | `hooks/hooks.json` + `scripts/check-page.sh` | 5.6 |
| **슈퍼 스킬** | `skills/episode/SKILL.md` | 이 페이지 |

## 2. 슈퍼 스킬 만들기

`skills/episode/SKILL.md`는 이렇게 써요.

```markdown
---
name: episode
description: 영상 한 편을 조사, 대본, 검토 순서로 만든다. 사용자가 직접 부를 때만 쓴다.
disable-model-invocation: true
argument-hint: [페이지 경로]
---

대상 페이지: $ARGUMENTS

아래 순서를 지켜 영상 한 편의 대본을 만든다. 각 단계의 결과를 다음 단계에 넘기고,
중간에 문제가 보이면 멈추고 사용자에게 알린다.

1. researcher 에이전트로 대상 페이지를 읽고 핵심 3가지와 출처를 정리한다.
2. scriptwriter 에이전트에게 그 정리만 넘겨 장면표를 쓰게 한다.
   장면표 작성 기준은 make-short 스킬을 따른다.
3. reviewer 에이전트로 장면표를 대상 페이지와 비교해 원본에 없는 말을 찾는다.
4. 검토 결과를 목록으로 사용자에게 보여 주고, 고칠 곳은 사용자의 결정을 받은 뒤 고친다.
```

이 글에서 중요한 부분은 이거예요.

- **`disable-model-invocation: true`**: 파일이 만들어지고 시간이 드는 일이니 내가 부를 때만 실행돼요.
- **"문제가 보이면 멈추고 알린다"** 와 **"사용자의 결정을 받은 뒤"**: 슈퍼 스킬이 알아서 끝까지 달리지 않고 내가 결정하는 지점을 지켜요. 자동화일수록 사람이 끼는 지점이 필요해요.
- 조수의 지시문을 바꾸지 않고, 슈퍼 스킬은 **순서와 연결**만 맡아요.

## 3. 쓰기

플러그인을 불러온 대화에서 이렇게 불러요.

```bash
claude --plugin-dir ./studio
```

```text
/studio:episode docs/part1/ch01/tokens.md
```

플러그인의 스킬 이름 앞에는 `studio:`가 붙어요. 이 실습의 플러그인 구조는 `claude plugin validate`로 검증했고, 같은 파일을 다시 쓰는 과정은 아래 "직접 해보기"에서 직접 확인하세요.

!!! tip "10살 눈높이 한 줄 요약"
    슈퍼 스킬은 새 마법이 아니라, 앞에서 만든 도구들을 순서대로 부르는 안내문이에요.

!!! note "★ 한 걸음 더 (심화)"
    같은 일을 한 단계 더 자동화하려면 `claude -p`로 부르는 스크립트(다음 페이지)와 이어 붙일 수 있어요. 다만 한 줄 모드에서는 `--bare`가 플러그인의 훅을 읽지 않으니, 훅 검사가 꼭 필요하면 `--bare` 없이 믿을 수 있는 폴더에서만 돌려요. 그리고 슈퍼 스킬이 길어지면 `references/` 같은 별도 파일로 기준을 빼서 "필요할 때만" 읽히게 해요.

## 직접 해보기

1. 위 구조대로 `studio` 폴더를 만들어요(5B 파일을 복사하면 돼요).
2. `claude plugin validate ./studio`를 돌려 `Validation passed`가 나오는지 확인해요.
3. `claude --plugin-dir ./studio`로 열고 `/studio:episode`로 짧은 페이지 하나를 돌려요.
4. 결과 장면표의 근거 표시와 reviewer의 지적 목록을 읽고, 내 눈으로 원본과 대조해요.
5. 이상한 점이 있으면 어느 파일의 어느 줄 때문인지 찾아 고쳐요. 슈퍼 스킬 고치기가 곧 도구 고치기예요.

## 오늘 바로 써먹기

- 슈퍼 스킬에는 순서, 멈출 곳, 내가 결정할 곳 세 가지를 쓰기
- 처음에는 짧은 페이지 하나로만 시험하기
- 결과는 항상 `git diff`나 파일로 확인할 수 있게 저장하기

## 자주 하는 오해

- "슈퍼 스킬이 영상을 알아서 올려 준다?" 아니에요. 이 스킬은 대본까지만 만들고 판단은 내가 해요.
- "스킬 안에서 조수 이름을 쓰면 반드시 그 조수가 실행된다?" 이름을 쓰는 것은 요청이에요. 의도대로 불리는지는 결과를 보며 확인해야 해요. 필요하면 지시문에서 "researcher 에이전트를 반드시 사용"처럼 더 분명히 써요.

## 출처와 기준

- 기준: Claude Code 2.1.319, 확인일 2026-11-07. `studio` 플러그인 구조는 `claude plugin validate`로 통과를 확인했고, 슈퍼 스킬을 실제 모델로 돌린 결과는 이 책에 싣지 않았어요.
- 이 페이지의 실습 파일은 저장소의 `examples/claude-code/`에 그대로 있어요(확인한 방법은 그 폴더의 README에 적었어요).
- 사실 기준: [공식 문서: 플러그인 만들기](https://code.claude.com/docs/en/plugins/create.md), [플러그인 구성요소](https://code.claude.com/docs/en/plugins/components.md), [스킬](https://code.claude.com/docs/en/skills.md), [서브에이전트](https://code.claude.com/docs/en/sub-agents.md)
- 학습 순서 참고: [claude-howto 07-plugins](https://github.com/luongnv89/claude-howto/tree/main/07-plugins) (MIT, 다시 씀)
