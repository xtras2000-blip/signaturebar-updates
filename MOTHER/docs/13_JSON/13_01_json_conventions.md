# 13_01 JSON Conventions

모든 정적 데이터 파일(12_01 §3.1)의 배치·명명·버전·로컬라이즈 규약. 13_02(이벤트), 13_03(대사)의 스키마는 본 문서의 규약을 전제로 한다.

## 1. 디렉터리 배치

```
data/
├── events/
│   ├── ch1/          # ch1_ev_001.json … 파일명 = event_id + ".json"
│   ├── ch2/ … ch5/
├── dialogues/
│   ├── ch1/          # ch1_sc_001.json … 파일명 = scene_id + ".json"
│   └── ch2/ … ch5/
├── constants/
│   ├── constants_kr.json   # 12_02 §7 상수 테이블
│   └── presets.json        # preset_worker / preset_freelancer / preset_fulltime
└── ai/
    ├── child_behaviors.json  # 14_01 행동 정의
    └── npc_schedules.json    # 14_02 스케줄 정의
```

- 파일 1개 = 최상위 개체 1개(이벤트 1개, 씬 1개). 목록형 파일은 `constants/`·`ai/`만 허용.
- 챕터 디렉터리(`ch1`~`ch5`)와 파일 내 `chapter` 필드는 반드시 일치해야 한다(빌드 린트에서 검증).

## 2. 명명 규칙 (snake_case 강제)

- 모든 JSON 키·식별자·파일명은 소문자 snake_case만 허용한다. camelCase·PascalCase·하이픈은 빌드 린트에서 리젝.
- 식별자 패턴의 단일 기준:

| 대상 | 패턴 | 예시 |
|---|---|---|
| 이벤트 | `^ch[1-5]_ev_[0-9]{3}$` | `ch1_ev_001` |
| 선택지 | `^ch[1-5]_ev_[0-9]{3}_c[0-9]+$` | `ch1_ev_001_c2` |
| 씬 | `^ch[1-5]_sc_[0-9]{3}$` | `ch1_sc_001` |
| 라인 | `^ch[1-5]_sc_[0-9]{3}_l[0-9]{2}$` | `ch1_sc_001_l01` |
| 기억 태그 | `^mem_ch[1-5]_[a-z0-9_]+$` | `mem_ch1_first_smile` |
| 마일스톤 | `^ms_ch[1-5]_[a-z0-9_]+$` | `ms_ch2_first_steps` |
| NPC | `^npc_[a-z_]+$` | `npc_husband` |
| 행동(아이 AI) | `^bhv_[a-z0-9_]+$` | `bhv_cry` |
| 상수 | `^[a-z][a-z0-9_]+$` | `formula_can_price` |

- 번호(`[0-9]{3}`)는 제작 순서이며 의미를 갖지 않는다. 결번 허용, 재사용 금지(삭제된 id는 99_ARCHIVE에 기록).

## 3. 스키마 버전 (schema_version)

- 모든 데이터 파일의 루트에 `"schema_version": "MAJOR.MINOR"` 문자열 필드를 필수로 둔다. 현재 기준 버전: `"1.0"`.
- MINOR 증가: 하위 호환 추가(선택 필드 추가). 로더는 모르는 선택 필드를 무시한다.
- MAJOR 증가: 비호환 변경(필수 필드 추가·삭제, 타입 변경). 로더는 MAJOR 불일치 파일을 로드 거부하고 빌드를 실패시킨다.
- 세이브의 `schema_version`(12_02 §1)과는 별개 축이다. 데이터 파일 버전은 빌드 시점에만 검증한다.

## 4. 로컬라이즈 정책

- 표시 문자열 키는 언어 접미사를 갖는다: 현재는 `text_kr`, `title_kr`, `note_kr`만 존재.
- 추후 영어 지원 시 같은 위치에 `text_en`, `title_en`을 **병렬 추가**한다. 키 이름 변경·구조 변경 금지 — 로더는 `text_{locale}` 조회 후 없으면 `text_kr`로 폴백한다.
- `*_kr` 값 안에 식별자·수치를 하드코딩하지 않는다. 수치 삽입은 `{money}` 형태의 치환 토큰만 허용하고, 토큰 목록은 08_DIALOGUE에서 관리한다.
- 식별자(`event_id`, `speaker` 등)는 로컬라이즈 대상이 아니다(00_04 표기 규칙: 한국어 표기와 영어 식별자 병기).

## 5. 공통 포맷 규칙

1. 인코딩 UTF-8(BOM 없음), 들여쓰기 2칸, 파일 끝 개행 1개.
2. 주석 금지 — JSON 표준을 따른다. 설명이 필요하면 `note_kr` 필드 또는 소관 문서에 기록한다. (문서 내 무효 예시 설명에만 예외적으로 ```jsonc 표기 사용, 13_02 참조)
3. `effects`의 성격 축 4종(confidence, empathy, independence, expressiveness) 값은 −3~+3 정수만 허용(D-008). 린트에서 검증.
4. `emotion_tags` 값은 01_04의 태그 목록만 허용하며 최소 1개(D-005).
5. 배열 순서는 의미를 갖는다(scenes 재생 순서, choices 표시 순서). 로더는 순서를 보존해야 한다.

## 6. 검증 파이프라인

빌드 시 `data/` 전체를 13_02·13_03의 JSON Schema(draft-07)로 검증하고, 스키마로 표현 불가한 규칙은 아래 린트 규칙으로 검사한다. 실패 시 QA 리젝(D-005, 15_QA 연동).

| 린트 규칙 id | 검사 내용 | 근거 |
|---|---|---|
| `lint_snake_case` | 모든 키·식별자·파일명 snake_case | §2 |
| `lint_filename_id` | 파일명 = 최상위 id + `.json` | §1 |
| `lint_chapter_dir` | 디렉터리 `ch{n}`과 파일 내 `chapter`·id 접두 일치 | §1 |
| `lint_ref_integrity` | `scenes`·`memory_tag`·`npc_id`·`target_event_id` 참조 대상 존재 | 12_01 §3.1 |
| `lint_emotion_chapter` | `emotion_tags`가 소속 챕터의 01_04 목표 감정에 부합 | D-005 |
| `lint_trait_cap` | 성격 축 effects 절대값 ≤ 3 | D-008 |
| `lint_schema_version` | 루트 `schema_version` 존재·MAJOR 일치 | §3 |
| `lint_no_orphan_locale` | `text_en` 존재 시 동일 위치 `text_kr` 필수 | §4 |

- 린트는 CI와 로컬 커밋 훅에서 동일 스크립트로 실행한다. 규칙 추가 시 이 표에 먼저 등록한다.
- 경고(warning) 등급은 없다 — 모든 위반은 오류이며 빌드를 실패시킨다(Production-ready documentation 원칙).
