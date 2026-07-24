# 07_07 CH5 Event List

CH5(6~7세) 이벤트 카탈로그. 시스템 규칙은 07_01, 작성 규칙은 07_02를 따른다.
CH5 감정 목표: 떠나보냄의 예감(`letting_go`), 뿌듯함(`fulfillment`), 상실감(`loss`) — 01_04.
CH5는 최종 회수 챕터다: CH1~CH2 `memory_tag`를 트리거 조건으로 회수하는 이벤트 4종(2절)을 포함하며,
마지막은 입학 전날 밤(`ch5_ev_last`) → 입학식(`ch5_ev_013`, `ch5_day_12` transition)으로 끝나 엔딩 시퀀스(02_04)에 직결된다.

## 1. 이벤트 카탈로그

| event_id | 제목 | class | 트리거 (유형 · 조건 요약) | emotion_tags | 대표 memory_tag | 회수 계획 |
|---|---|---|---|---|---|---|
| `ch5_ev_001` | 취학통지서 도착 | minor | scheduled · day 2380~2390 | letting_go | `mem_ch5_school_notice` | CH5 (`ch5_ev_002` 예비소집일 지참 서류 라인) |
| `ch5_ev_002` | 예비소집일 | major | scheduled · day 2400~2410 | letting_go | `mem_ch5_preliminary_call` | CH5 (`ch5_ev_013` — 처음 "학생"으로 불린 순간의 재생, 06_03 `npc_school_teacher`) |
| `ch5_ev_003` | 입학 준비물 구매 | minor | scheduled · day 2415~2425 | fulfillment | `mem_ch5_school_shopping` | CH5 (`ch5_ev_last` 가방 싸기 장면) |
| `ch5_ev_004` | 책상 조립 | minor | scheduled · day 2425~2435 | fulfillment | `mem_ch5_desk_build` | CH5 (엔딩 편지 — 그 책상에서 그린 그림, 02_04) |
| `ch5_ev_005` | 이름 쓰기 연습 | minor | random · weight 20 | fulfillment | `mem_ch5_name_writing` | 엔딩 (편지의 삐뚤빼뚤한 글씨체 근거, 02_04) |
| `ch5_ev_006` | 혼자 자기 선언 | major | conditional · independence>=55 AND time_block=night | letting_go, loss | `mem_ch5_sleep_alone` | CH5 (`ch5_ev_last` — "오늘만 같이 자도 돼?" 라인 분기) |
| `ch5_ev_007` | 어린이집 졸업식 | major | scheduled · day 2460~2468 | fulfillment, loss | `mem_ch5_graduation` | 엔딩 몽타주 후보 (02_04) |
| `ch5_ev_008` | 마지막 등원 | major | scheduled · day 2469~2475 | loss | `mem_ch5_last_dropoff` | 엔딩 몽타주 후보 (02_04) |
| `ch5_ev_009` | 엄마 손 놓고 걷기 | minor | conditional · has `mem_ch2_first_steps` AND independence>=50 | letting_go | `mem_ch5_letting_hand` | 엔딩 (첫 걸음 컷과 병치, 02_04) |
| `ch5_ev_010` | 같은 학교, 같은 이름 | minor | conditional · has `mem_ch1_cohort_meetup` | fulfillment | `mem_ch5_cohort_reunion` | CH5 (`ch5_ev_013` 교문 앞 — 하늘·하율 모자와 재회, 06_03 아크) |
| `ch5_ev_011` | 역전된 돌봄 | major | conditional · has `mem_ch1_grandma_visit` | loss | `mem_ch5_caring_reversed` | 엔딩 몽타주 후보 (06_03 `npc_grandma` 아크 완결) |
| `ch5_ev_012` | 같은 가방 | minor | conditional · has `mem_ch1_leaving_center` | letting_go | `mem_ch5_same_bag` | CH5 (`ch5_ev_013` s1 현관 구도로 직결) |
| `ch5_ev_last` | 입학 전날 밤 | major | scheduled · day 2500 (ch5_day_11) AND time_block=night | letting_go, fulfillment | `mem_ch5_last_night` | CH5 (`ch5_ev_013` 아침 라인 분기) + 엔딩 몽타주 |
| `ch5_ev_013` | 입학식 | major | scheduled · day 2501 (ch5_day_12, transition) | letting_go, fulfillment, loss | `mem_ch5_entrance_day` | 종착점 — `callback_plan: []` (엔딩 시퀀스가 회수를 대체, 02_04) |

- `ch5_ev_last`는 시스템 예약 형식(`ch{n}_ev_{slug}`, D-015)이다. 챕터 마지막 밤에 강제 트리거되는 시스템 소유 이벤트라 숫자 카탈로그와 분리했다.
- `ch5_ev_013`의 evening 블록 종료 시 `ending_trigger`로 진입한다 — night 블록·day_end_summary 생략 (02_04 State Machine).
- `once`는 전 이벤트 true. 회수 조건 이벤트(009~012)는 해당 태그 미보유 세이브에서 영구 미발생일 수 있으며 의도된 설계다 (D-002).
- 교차 챕터 태그(`mem_ch2_first_steps`, `mem_ch3_recital_stage`)는 07_04/07_05 확정 태그와 일치함을 확인했다(2026-07-24, Doc QA).

## 2. 이전 챕터 memory_tag 회수 매트릭스

| 회수 이벤트 | 조건으로 요구하는 태그 | 원천 | 회수 방식 |
|---|---|---|---|
| `ch5_ev_009` 엄마 손 놓고 걷기 | `mem_ch2_first_steps` | CH2 첫 걸음 | 처음 손을 놓고 걸어오던 방향의 반대로, 이번엔 아이가 걸어간다 |
| `ch5_ev_010` 같은 학교, 같은 이름 | `mem_ch1_cohort_meetup` | 07_03 `ch1_ev_014` | 조리원 동기 하늘 모자와 같은 학교 배정 — 비교가 동행으로 바뀐다 (06_03) |
| `ch5_ev_011` 역전된 돌봄 | `mem_ch1_grandma_visit` | 07_03 `ch1_ev_007` | 산후조리를 와 주던 친정엄마의 병원에 이번엔 딸이 간다 |
| `ch5_ev_012` 같은 가방 | `mem_ch1_leaving_center` | 07_03 `ch1_ev_001` | 조리원 퇴소 가방을 현관에서 다시 꺼낸다 — 입학식 아침 구도의 사전 설치 |
| `ch5_ev_013` 입학식 (라인 조건) | `mem_ch1_doljanchi_wait` 계열 | 07_03 `ch1_ev_010` | 돌잡이에서 잡은(쥐여 준) 물건을 책가방에 넣어 주는 라인 분기 — 트리거 조건 아님 |
| `ch5_ev_007` 졸업식 (라인 조건) | `mem_ch3_recital_stage` | CH3 유치원 발표회 | 같은 강당 단상 구도의 재사용 — 트리거 조건 아님 |

## 3. 대표 이벤트 전체 JSON

### 3.1 ch5_ev_last 입학 전날 밤

```json
{
  "event_id": "ch5_ev_last", "chapter": 5, "title_kr": "입학 전날 밤", "event_class": "major",
  "emotion_tags": ["letting_go", "fulfillment"], "priority": 98, "once": true, "cooldown_days": 0,
  "trigger": { "type": "scheduled", "conditions": [
    { "type": "day_range", "min": 2500, "max": 2500 },
    { "type": "time_block", "value": "night" } ] },
  "scenes": [
    { "scene_id": "ch5_ev_last_s1", "location_id": "loc_home_child_room", "time_block": "night",
      "script_kr": ["책상 위, 이름표 붙은 연필 다섯 자루. 삐뚤빼뚤한 이름 석 자.",
        "가방을 쌌다가 풀었다가, 세 번째다. 빠진 물건은 없다. 빠진 물건이 없는데도 손이 멈추지 않는다.",
        "아이가 앞주머니에 종이 한 장을 접어 넣는다. 손을 잡은 두 사람이 그려진 그림이다."] },
    { "scene_id": "ch5_ev_last_s2", "location_id": "loc_home_bedroom", "time_block": "night",
      "script_kr": ["불 꺼진 복도. 제 방으로 가던 아이가 문 앞에서 돌아본다.",
        "\"엄마. 오늘만, 같이 자도 돼?\""] }
  ],
  "choices": [
    { "choice_id": "ch5_ev_last_c1", "text_kr": "오늘만. 이불을 들춰 자리를 내준다",
      "effects": { "attachment": 5, "stamina": -3, "independence": -1 }, "memory_tag": "mem_ch5_last_night_together" },
    { "choice_id": "ch5_ev_last_c2", "text_kr": "손을 잡고 아이 방으로 가서, 잠들 때까지 곁에 앉아 있는다",
      "effects": { "attachment": 3, "independence": 1, "stamina": -4 }, "memory_tag": "mem_ch5_last_night_beside" },
    { "choice_id": "ch5_ev_last_c3", "text_kr": "\"내일부터 학생이잖아\" — 이불만 덮어 주고 방을 나온다",
      "effects": { "independence": 2, "attachment": -1, "mind": -3 }, "memory_tag": "mem_ch5_last_night_door" }
  ],
  "callback_plan": [
    { "chapter": 5, "memory_tag": "mem_ch5_last_night_together",
      "usage_kr": "다음 날 아침 ch5_ev_013 s1의 기상 구도(한 이불/각자의 방)가 전날 선택으로 갈린다 — 같은 챕터 보조 회수(07_02 2절), 최종 종착은 엔딩 몽타주(02_04)" }
  ]
}
```

- s1의 그림은 `mem_ch4_reconcile_drawing`(07_06 `ch4_ev_002`)의 라인 조건 회수다. 미보유 시 "종이 한 장" 라인은 이름 연습장으로 대체된다.
- s2는 `mem_ch5_sleep_alone`(`ch5_ev_006`) 보유 시 "혼자 자기로 해 놓고"라는 자기 인용 라인이 붙는다.

### 3.2 ch5_ev_013 입학식

```json
{
  "event_id": "ch5_ev_013", "chapter": 5, "title_kr": "입학식", "event_class": "major",
  "emotion_tags": ["letting_go", "fulfillment", "loss"], "priority": 100, "once": true, "cooldown_days": 0,
  "trigger": { "type": "scheduled", "conditions": [
    { "type": "day_range", "min": 2501, "max": 2501 },
    { "type": "time_block", "value": "morning" } ] },
  "scenes": [
    { "scene_id": "ch5_ev_013_s1", "location_id": "loc_home_living", "time_block": "morning",
      "script_kr": ["현관. 7년 전 조리원에서 들고 온 가방 옆에, 오늘 처음 메는 가방이 나란히 놓여 있다.",
        "가방 하나는 그때보다 작아 보이고, 하나는 아이의 등보다 크다."] },
    { "scene_id": "ch5_ev_013_s2", "location_id": "loc_elementary_school", "time_block": "morning",
      "script_kr": ["교문. 같은 방향으로 걷는 아이들과, 반 발짝 뒤의 어른들.",
        "명단을 든 선생님이 이름을 찾아 부른다. 성과 이름 석 자 뒤에, 처음으로 \"학생\"이 붙는다."] },
    { "scene_id": "ch5_ev_013_s3", "location_id": "loc_elementary_school", "time_block": "morning",
      "script_kr": ["아이가 교문 앞에서 돌아본다.", "손을 흔드는 방식은, 7년 동안 쌓인 것들의 모양대로 아이마다 다르다."] }
  ],
  "choices": [
    { "choice_id": "ch5_ev_013_c1", "text_kr": "교실 앞까지 같이 들어간다",
      "effects": { "attachment": 3, "independence": -1, "stamina": -2 }, "memory_tag": "mem_ch5_entrance_walk_in" },
    { "choice_id": "ch5_ev_013_c2", "text_kr": "교문 앞에서 멈춰 서서, 손을 흔들어 보낸다",
      "effects": { "independence": 2, "attachment": 1, "mind": -3 }, "memory_tag": "mem_ch5_entrance_wave" },
    { "choice_id": "ch5_ev_013_c3", "text_kr": "돌아서는 아이를 한 번만 더 불러서 안는다",
      "effects": { "attachment": 4, "independence": -1, "stamina": -2 }, "memory_tag": "mem_ch5_entrance_last_hug" }
  ],
  "callback_plan": []
}
```

- `callback_plan`이 빈 배열인 사유: 회수 종착점 이벤트 — 이 이벤트의 evening 블록 종료가 곧 `ending_trigger`이며, 회수는 엔딩 몽타주·아이 초상·편지(02_04)가 전담한다 (07_02 2절 예외 조항).
- s1은 `mem_ch1_leaving_center`(가방)·`mem_ch1_doljanchi_wait` 계열(돌잡이 물건을 가방에 넣는 추가 라인)의 라인 조건 회수. s3의 연출은 성격 축 4종 밴드 매핑(02_04 UI 표)을 그대로 사용한다.

## 4. QA 메모 (15_QA 연동)

- 카탈로그 14종의 `emotion_tags`는 전부 CH5 태그 집합 `{letting_go, fulfillment, loss}`의 부분집합임을 빌드 검증에 포함한다 (D-005).
- `npc_daycare_teacher`의 등장 챕터는 CH4까지다 (06_03) — 졸업식(`ch5_ev_007`)·마지막 등원(`ch5_ev_008`)은 교사 npc_id를 참조하지 않고 장소·소품(신발장 이름표 떼기)으로만 연출한다. 위반 시 리젝 (06_03 6절).
- `loc_elementary_school`은 CH5 해금 장소 — CH5 이전 참조 리젝 (06_02 7절). `ch5_ev_002`·`013`만 사용한다.
- `ch5_ev_013`은 D-004 적용 대표 케이스: 진입부터 엔딩 시퀀스 종료까지 수치·성격 축 숫자 완전 비노출 (02_04 UI).
- day 값(2380~2501)은 CH5 재생일 캘린더(`ch5_day_01`~`ch5_day_12`) 확정 시 재생일 매핑으로 조정한다 (02_03 1절). `ch5_ev_last`=ch5_day_11, `ch5_ev_013`=ch5_day_12 대응은 고정.
- `money` 효과(준비물 구매 등 상세 JSON 제작 시)는 12_DATABASE 물가 상수 확정 후 상수 참조로 작성한다.
