# MOTHER data/

정적 게임 데이터의 루트. 배치·명명·포맷 규약은 `docs/13_JSON/13_01_json_conventions.md`가 정본이다.

## 폴더 구조

```
data/
├── events/
│   └── ch1/                  # CH1 이벤트. 파일명 = event_id + ".json"
│       ├── ch1_ev_001.json … ch1_ev_016.json   # 07_03 카탈로그 16종
│       ├── ch1_ev_night_feeding.json           # 시스템 예약 (02_02 night 블록)
│       └── ch1_ev_borrow_money.json            # 시스템 예약 (03_02 money_debt_event)
├── schemas/
│   └── event.schema.json     # 13_02 §1에서 추출한 이벤트 JSON Schema (draft-07)
├── validate_events.py        # 이벤트 검증 스크립트 (아래 참조)
└── README.md
```

- 파일 1개 = 이벤트 1개. `event_id`는 카탈로그형 `ch{n}_ev_{nnn}` 또는 시스템 예약 슬러그형 `ch{n}_ev_{slug}` (D-015).
- `scenes`는 `ch{n}_sc_{nnn}` 씬 참조 배열이다. 씬 본문은 `data/dialogues/ch{n}/`(13_03)에 별도 제작한다 — 아직 미제작이며, 참조 무결성 린트(`lint_ref_integrity`)는 씬 파일 제작 시점에 활성화한다.
- 인코딩 UTF-8(BOM 없음), 들여쓰기 2칸, 파일 끝 개행 1개, 주석 금지 (13_01 §5).

## 검증 실행

```bash
python3 MOTHER/data/validate_events.py
```

- `data/events/` 아래 전체 `*.json`을 `schemas/event.schema.json`으로 검증한다.
- `jsonschema` 패키지가 있으면 draft-07 검증기를 사용하고, 없으면 표준 라이브러리만으로 동일 규칙(필수 필드·패턴·enum·범위)을 직접 검사한다.
- 스키마로 표현되지 않는 추가 린트: 파일명=event_id, 디렉터리=chapter=id 접두, 전 choice `memory_tag` 필수(07_02), `trigger.weight`는 random 전용(13_02).
- 종료 코드: 전 파일 통과 0, 위반 1. 경고 등급 없음 — 모든 위반은 오류다 (13_01 §6).

## 작성 시 주의 (요약)

- `emotion_tags`는 소속 챕터의 01_04 목표 감정만 사용 (CH1: `overwhelmed` / `wonder` / `isolation`).
- 성격 축 효과(`confidence`/`empathy`/`independence`/`expressiveness`)는 1회 ±3 상한 (D-008).
- NPC 관계 효과는 `"rel": {"npc_husband": 3}` 형식의 중첩 객체로 기술하며 대상은 06_03 명부의 `npc_id`만 허용.
- 정답 선택지 금지 — 모든 선택은 트레이드오프 (07_02 금지 패턴 1).
- `callback_plan`·`event_class` 등 07_EVENT 기획 메타는 현행 13_02 스키마(`additionalProperties: false`)에 없으므로 데이터 파일이 아닌 07_03 카탈로그 문서에서 관리한다.
