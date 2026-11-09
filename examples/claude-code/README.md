# V부 실습에 쓴 파일

교과서 V부(Claude Code 실전)와 23.4 실습에 나오는 파일을 그대로 모아 두었어요. 책의 "직접 확인했어요"라는 말이 무엇을 뜻하는지 이 파일로 다시 확인할 수 있어요.

| 파일 | 쓰인 페이지 | 확인한 방법 |
|---|---|---|
| `check-page.sh` | 5.6 훅: 실습 | 가짜 입력(JSON)으로 "출처와 기준" 절이 없을 때 종료 코드 2, 있을 때 0, docs 밖 파일은 0 |
| `check-build.sh` | 23.4 검증 루프 | 연습용 사이트에서 깨진 링크가 있을 때(`stop_hook_active`가 거짓) 2, 참이면 0, 정상이면 0. `mkdocs build --strict`를 `-q` 없이 써야 해요 |
| `check-hard-words.sh` | 5.10 CLI 자동화 | 가짜 `claude` 명령으로 반복 구조와 결과 파일 저장만 확인. 실제 모델을 부른 결과는 확인하지 않았어요 |
| `studio/` | 5.10 플러그인, 슈퍼 스킬 | `claude plugin validate ./studio`가 통과(`Validation passed`)했어요. README·라이선스·아이콘이 없다는 안내는 공식 디렉터리 등록용이에요. 실제 설치와 `/studio:episode` 실행은 확인하지 않았어요 |

확인한 날짜: 2026-11-07, Claude Code 2.1.319.

## 영어판(English edition) 파일 (2026-11-09 추가)

| 파일 | 쓰인 페이지 | 확인한 방법 |
|---|---|---|
| `check-page-en.sh` | 17.2.2 Hands-on: add an automatic checker | 가짜 입력으로 `docs-en` 페이지에 "Sources and date checked" 절이 없을 때 2, 있을 때 0, `docs-en` 밖 파일은 0 |
| `check-hard-words-en.sh` | 18.2.3 command line automation | 가짜 `claude` 명령으로 반복 구조, 공백이 든 파일 이름, 결과 파일 저장을 확인. 실제 모델 호출 결과는 확인하지 않았어요 |
| `studio-en/` | 18.2 plugins, super skill | `claude plugin validate ./studio-en`가 통과(`Validation passed`, 아이콘 없음 안내만). 실제 설치와 `/studio:episode` 실행은 확인하지 않았어요 |

확인한 날짜: 2026-11-09, Claude Code 2.1.319.
