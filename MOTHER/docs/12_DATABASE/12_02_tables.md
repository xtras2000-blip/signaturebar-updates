# 12_02 Tables

12_01의 ER 다이어그램에 등장하는 테이블의 필드 상세를 정의한다. 초기값은 D-009를 캐논으로 하며, 수치의 변화 규칙은 03_01이 소유한다(본 문서는 저장 구조·제약만 정의).

## 1. save (세이브 루트)

| 필드 | 타입 | 제약 | 초기값 | 설명 |
|---|---|---|---|---|
| `save_id` | string | PK, UUID v4 | 생성 시 발급 | 세이브 레코드 식별자 |
| `slot_type` | string | enum: `auto`/`manual` | `auto` | 자동 1 + 수동 3 슬롯 체계 |
| `slot_index` | int | auto=0, manual=1~3 | 0 | 슬롯 번호 |
| `day_counter` | int | ≥ 1 | 1 | 경과 일수. 요일 = `(day_counter - 1) % 7` (day 1 = 월요일) |
| `chapter` | int | 1~5 | 1 | 현재 챕터(D-001) |
| `schema_version` | string | `MAJOR.MINOR` | `1.0` | 세이브 마이그레이션 기준(12_01 §3.3) |
| `updated_at` | string | ISO 8601 | 저장 시각 | 슬롯 UI 표시용 |

## 2. player_state (엄마)

| 필드 | 타입 | 제약 | 초기값 | 설명 |
|---|---|---|---|---|
| `save_id` | string | PK, FK→save | — | 1:1 |
| `attachment` | int | 0~100 | 50 | 애착도 |
| `stamina` | int | 0~100 | 70 | 엄마 체력 |
| `mind` | int | 0~100 | 60 | 엄마 마음(번아웃 지표) |
| `money` | int | ≥ 0, 원화 | 3,000,000 | 가계 |
| `preset_id` | string | enum: `preset_worker`/`preset_freelancer`/`preset_fulltime` | 시작 시 선택 | 배경 프리셋. 수입 규칙·일부 이벤트 해금에 참조 |

## 3. child_state (아이)

| 필드 | 타입 | 제약 | 초기값 | 설명 |
|---|---|---|---|---|
| `save_id` | string | PK, FK→save | — | 1:1 |
| `child_condition` | int | 0~100 | 70 | 건강·수면·영양 종합 |
| `confidence` | int | 0~100 | 50 | 자신감(성격 축, D-008) |
| `empathy` | int | 0~100 | 50 | 공감(성격 축) |
| `independence` | int | 0~100 | 50 | 자립심(성격 축) |
| `expressiveness` | int | 0~100 | 50 | 표현력(성격 축). 축 4종 모두 1회 변동 상한 ±3 |
| `temperament_seed` | string | enum: `sensitive`/`easygoing`/`active` | 시작 시 결정 | 기질 시드. 14_01 행동 가중치 보정에 사용 |
| `milestones` | string(JSON) | `milestone_id` 배열 | `[]` | 달성한 발달 마일스톤. 명명: `ms_{챕터}_{주제}` |

발달 마일스톤 기준 목록(콘텐츠 추가 시 이 표에 먼저 등록):

| milestone_id | 챕터 | 내용 |
|---|---|---|
| `ms_ch1_first_smile` | 1 | 첫 사회적 미소 |
| `ms_ch1_first_rollover` | 1 | 첫 뒤집기 |
| `ms_ch2_first_steps` | 2 | 첫 걸음마 |
| `ms_ch2_first_word` | 2 | 첫 단어("엄마") |
| `ms_ch3_first_friend` | 3 | 어린이집 첫 친구 |
| `ms_ch4_hangul_interest` | 4 | 한글에 대한 첫 관심 |
| `ms_ch5_school_ready` | 5 | 입학 준비 완료(가방 스스로 싸기) |

## 4. memory_log (기억 로그)

| 필드 | 타입 | 제약 | 초기값 | 설명 |
|---|---|---|---|---|
| `save_id` | string | PK(복합), FK→save | — | — |
| `seq` | int | PK(복합), 1부터 증가 | — | 기록 순서. 엔딩 몽타주 재생 순서의 기준 |
| `day` | int | ≥ 1 | — | 발생 일 |
| `event_id` | string | 패턴 `^ch[1-5]_ev_[0-9]{3}$` | — | 발생 이벤트 |
| `choice_id` | string | 해당 이벤트의 choices 내 id | — | 플레이어의 선택 |
| `memory_tag` | string | 패턴 `^mem_ch[1-5]_[a-z0-9_]+$` | — | 회수용 태그(Pillar 4). 태그 없는 선택은 기록 생략 |
| `emotion_tags` | string(JSON) | 01_04 태그 배열 | — | 발생 이벤트의 감정 태그 사본(엔딩 필터링용) |

## 5. event_history (이벤트 이력)

| 필드 | 타입 | 제약 | 초기값 | 설명 |
|---|---|---|---|---|
| `save_id` | string | PK(복합), FK→save | — | — |
| `event_id` | string | PK(복합) 아님(재발생 허용) | — | 발생 이벤트. `once`/`cooldown_days` 판정 근거 |
| `day` | int | ≥ 1 | — | 발생 일 |
| `choice_id` | string | nullable | null | 선택 없이 종료된 연출 이벤트는 null |
| `slot_kind` | string | enum: `major`/`minor` | — | 하루 슬롯 소비 구분(major 1 + minor 2, 07_EVENT) |

## 6. npc_relations (NPC 관계)

| 필드 | 타입 | 제약 | 초기값 | 설명 |
|---|---|---|---|---|
| `save_id` | string | PK(복합), FK→save | — | — |
| `npc_id` | string | PK(복합), 패턴 `^npc_[a-z_]+$` | — | NPC 식별자(초기값은 14_02 명부 표 기준) |
| `rel` | int | 0~100 | NPC별 상이(14_02) | 관계 수치. 대사 톤 3단계·개입 규칙의 입력 |
| `last_interaction_day` | int | ≥ 0 | 0 | 마지막 상호작용 일. 방치 감쇠 판정(14_02)용 |

## 7. constants_kr (한국 물가·제도 상수)

정적 테이블(`data/constants/constants_kr.json`, 13_01). 값은 2025년 전후 실제 근사값이며 밸런싱 튜닝의 출발점이다(Pillar 3). 단위: 금액=KRW, 기간=개월, 비율=%.

| constant_id | category | value | unit | note_kr |
|---|---|---|---|---|
| `formula_can_price` | childcare_goods | 35,000 | KRW/캔(800g) | 분유 1캔, 약 5~7일분 |
| `diaper_pack_price` | childcare_goods | 45,000 | KRW/팩 | 대형 팩 기준 약 2주분 |
| `babyfood_month_cost` | childcare_goods | 150,000 | KRW/월 | 이유식기(6~15개월) 식재료 |
| `postpartum_center_2w` | service | 3,500,000 | KRW/2주 | 산후조리원(수도권 일반실) |
| `doljanchi_cost` | event_cost | 2,000,000 | KRW/회 | 돌잔치(소규모 대관 기준) |
| `daycare_wait_public` | institution | 10 | 개월 | 국공립 어린이집 평균 입소 대기 |
| `daycare_extra_monthly` | institution | 100,000 | KRW/월 | 어린이집 특별활동·필요경비 |
| `parental_leave_pay_rate` | institution | 80 | % | 육아휴직 급여, 통상임금 대비 |
| `parental_leave_pay_cap` | institution | 1,600,000 | KRW/월 | 육아휴직 급여 월 상한(근사) |
| `parent_benefit_age0` | institution | 1,000,000 | KRW/월 | 부모급여, 만 0세 |
| `parent_benefit_age1` | institution | 500,000 | KRW/월 | 부모급여, 만 1세 |
| `child_allowance` | institution | 100,000 | KRW/월 | 아동수당(만 8세 미만) |
| `pediatric_visit_cost` | medical | 15,000 | KRW/회 | 소아과 진료+약(본인부담 근사) |
| `school_prep_cost` | event_cost | 500,000 | KRW/회 | 초등 입학 준비물 일체(CH5) |

- 제도 상수의 실제 값이 개정되면 `note_kr`에 개정 연도를 병기하고 값을 갱신한다. 게임 밸런스용 배율은 이 테이블이 아니라 03_02 정산 규칙에서 곱한다.
