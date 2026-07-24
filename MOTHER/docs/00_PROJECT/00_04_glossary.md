# 00_04 Glossary

프로젝트 전역에서 사용하는 용어와 식별자의 단일 기준. 모든 문서·JSON 키는 이 표기를 따른다.

## 1. 핵심 개체

| 용어 | 식별자 | 정의 |
|---|---|---|
| 엄마 (플레이어) | `player` | 플레이어가 조작하는 주인공. 스탯 명세는 04_PLAYER |
| 아이 | `child` | 성장하는 자녀. 스탯·상태 머신은 05_CHILD |
| 시간 블록 | `time_block` | 하루를 나누는 행동 단위 (아침/오전/오후/저녁/밤) |
| 이벤트 | `event` | 조건 충족 시 발생하는 연출·선택 단위. 07_EVENT |
| 선택지 | `choice` | 이벤트 내 플레이어 결정. 효과는 JSON `effects`로 기술 |
| 기억 로그 | `memory_log` | 주요 선택·사건의 영구 기록. 엔딩 연출의 원천 |

## 2. 핵심 수치

| 용어 | 식별자 | 범위 | 정의 |
|---|---|---|---|
| 애착도 | `attachment` | 0~100 | 아이-엄마 정서적 유대. 핵심 감정 지표 |
| 아이 컨디션 | `child_condition` | 0~100 | 건강·수면·영양의 종합 |
| 엄마 체력 | `stamina` | 0~100 | 시간 블록 행동의 비용 자원 |
| 엄마 마음 | `mind` | 0~100 | 번아웃 지표. 낮으면 선택지 제한 발생 |
| 가계 | `money` | 정수(원) | 생활비·육아비 자원 |

## 3. 표기 규칙

- 게임 내 한국어 표기(예: "애착도")와 JSON 식별자(`attachment`)를 항상 병기한다.
- 신규 용어는 이 문서에 먼저 등록한 뒤 다른 문서에서 사용한다.
- 수치의 실제 초기값·변화식은 03_GAME_SYSTEM과 각 개체 문서에서 정의하며, 본 문서는 명명만 관리한다.

## 4. 보조 수치 (02~15 작성 과정에서 등록)

| 용어 | 식별자 | 범위 | 정의 | 정본 문서 |
|---|---|---|---|---|
| 성격 축 | `confidence`/`empathy`/`independence`/`expressiveness` | 0~100 | 아이 성격 4축. 선택 누적으로만 변화 (D-008) | 05_03 |
| 남편 육아 참여도 | `husband_support` | 0~100 | 프리셋별 초기값 상이 (D-011) | 04_01 |
| NPC 관계도 | `rel_{npc_id}` | 0~100 | NPC별 관계 수치, init 50 (D-012) | 06_03, 14_02 |
| 컨디션 하위 요소 | `sleep`/`nutrition`/`health` | 0~100 | child_condition 합성 원천 | 05_03 |

## 5. 열거형 (enum)

| 항목 | 값 |
|---|---|
| 배경 프리셋 `background_preset` | `preset_worker` / `preset_freelancer` / `preset_fulltime` |
| 기질 시드 `temperament_seed` | `sensitive` / `easygoing` / `active` |
| 행동 카테고리 `action_category` | `care` / `housework` / `work` / `selfcare` / `outing` |
| 아이 연령 단계 `age_stage` | `infant` / `toddler` / `child` |
| 이벤트 트리거 `trigger.type` | `scheduled` / `conditional` / `random` (D-010) |
| 이벤트 등급 `event_class` | `major` / `minor` (일일 슬롯: major 1 + minor 2) |
| HUD 모드 `hud_mode` | `full` / `minimal` / `hidden` |

## 6. ID 명명 규칙

| 대상 | 규칙 | 예 |
|---|---|---|
| 이벤트 | `ch{n}_ev_{nnn}` | `ch1_ev_004` |
| 씬 / 라인 / 선택지 | `{event_id}_s{n}` / `…_l{nn}` / `…_c{n}` | `ch1_ev_004_s1_l01` |
| 기억 태그 | `mem_{ch1~ch5\|any}_{subject}` | `mem_ch1_first_smile` |
| 행동 | `act_{category}_{name}` | `act_care_feeding` |
| 발달 마일스톤 | `ms_ch{n}_{name}` | `ms_ch1_first_steps` |
| 행동 연출 큐 | `cue_{수치}_{구간}_{age_stage}` | `cue_att_high_toddler` |
| 장소 / NPC | `loc_{name}` / `npc_{name}` | `loc_daycare`, `npc_husband` |
| 아트 에셋 | `spr_` / `bg_` / `ui_` / `pal_ch{n}_{name}` | `pal_ch1_dawn` |
| 사운드 | `sfx_` / `amb_` / `bgm_` / `motif_{name}` | `motif_lullaby` |
| 화면 / 위젯 | `scr_{name}` / `wgt_{name}` | `scr_day_start` |
| QA 케이스 | `QA-{문서번호}-{연번}`, `DOC-{nn}`, `PLAY-E/R{n}`, `RE-{nn}` | `QA-0402-03` |
