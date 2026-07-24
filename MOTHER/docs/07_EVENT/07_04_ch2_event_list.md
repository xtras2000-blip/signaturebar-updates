# 07_04 CH2 Event List

CH2(1~3세) 이벤트 카탈로그. 시스템 규칙은 07_01, 작성 규칙은 07_02를 따른다.
CH2 감정 목표: 벅참(`joy`), 소진(`burnout`), 첫 보람(`reward`) — 01_04.
게임 내 일차(day)는 CH1 카탈로그와 연속: CH2는 day 366~1095 (만 1~3세).

## 1. 이벤트 카탈로그

| event_id | 제목 | class | 트리거 (유형 · 조건 요약) | emotion_tags | 대표 memory_tag | 회수 챕터 |
|---|---|---|---|---|---|---|
| `ch2_ev_001` | 첫 걸음 | major | scheduled · day 390~420 | joy, reward | `mem_ch2_first_steps` | CH5 (입학식 첫 등굣길 걸음과 병치) |
| `ch2_ev_002` | 통잠 첫날 | minor | conditional · memory `mem_ch1_night_feeding` AND day 380~500 | reward | `mem_ch2_first_full_sleep` | CH4 (혼자 자기 시작하는 밤 회상) |
| `ch2_ev_003` | 첫 말 — "엄마" | major | scheduled · day 430~460 | joy | `mem_ch2_first_word` | CH5 (예비소집일, "네" 하고 대답하는 목소리) |
| `ch2_ev_004` | 복직 결정 | major | scheduled · day 430~440 · `preset_worker` 전용(04_01 5절) | burnout, reward | `mem_ch2_return_to_work` | CH5 (npc_boss 아크 종착 — 인정 또는 이직) |
| `ch2_ev_005` | 입소 대기 순번 통보 | minor | conditional · memory `mem_ch1_daycare_waitlist` AND day 450~460 | burnout | `mem_ch2_waitlist_number` | CH3 (유치원 추첨 대기와 대비) |
| `ch2_ev_006` | 입소 탈락 | minor | scheduled · day 470~480 | burnout | `mem_ch2_daycare_rejected` | CH3 (기관 옮기기 고민의 기원) |
| `ch2_ev_007` | 어린이집 입소 첫날 | major | scheduled · day 500~510 | joy, burnout | `mem_ch2_daycare_first_goodbye` | CH5 (입학식 교문 앞, 같은 구도의 이별) |
| `ch2_ev_008` | 등원 거부 | minor | conditional · memory `mem_ch2_daycare_first_goodbye` AND day 520~600 | burnout | `mem_ch2_daycare_refusal` | CH3 (스스로 가방 메는 아침과 대비) |
| `ch2_ev_009` | 떼쓰기 — 자아의 등장 | major | conditional · day 540~620 AND time_block=evening | joy, burnout | `mem_ch2_tantrum_self` | CH4 (훈육 갈등에서 "내가!"의 재등장) |
| `ch2_ev_010` | 배변 훈련 | minor | scheduled · day 700~760 | reward | `mem_ch2_potty_training` | CH5 (입학 준비 체크리스트 "혼자 화장실") |
| `ch2_ev_011` | 놀이터 데뷔 | minor | random · day 450~600, weight 20 | joy | `mem_ch2_playground_debut` | CH3 (같은 놀이터의 서열 발견과 대비) |
| `ch2_ev_012` | 남편 독박 실험 | major | conditional · mind<40 AND rel_npc_husband>=50 | reward | `mem_ch2_husband_solo_day` | CH4 (화해 장면, 남편이 그 하루를 언급) |
| `ch2_ev_013` | 번아웃 위기 | major | conditional · mind<30 | burnout | `mem_ch2_burnout_edge` | CH4 (죄책감 장면의 원점) |
| `ch2_ev_014` | 문화센터 첫 수업 | minor | scheduled · day 480~520 | joy | `mem_ch2_munsen_class` | CH3 (문센 레벨 비교 대화로 재점화) |
| `ch2_ev_015` | 이앓이 밤 | minor | conditional · child_condition<55 AND day 380~500 AND time_block=night | burnout | `mem_ch2_teething_night` | CH3 (아픈 밤에 의연해지는 과정의 기원) |
| `ch2_ev_016` | 열경련 응급실 밤 | major | conditional · child_condition<40 AND day 550~700 AND time_block=night | burnout | `mem_ch2_febrile_seizure` | CH3 (수족구 격리의 밤에서 회수) |
| `ch2_ev_017` | 복직 첫날 조퇴 | major | conditional · memory `mem_ch2_return_to_work` AND day 515~530 | burnout | `mem_ch2_first_day_early_leave` | CH5 (npc_boss 인정/결별 대사 분기) |

- CH1 memory_tag 회수 이벤트 (5종, 07_03 "회수 챕터" 열과 교차 검증):
  `ch2_ev_001`(`mem_ch1_first_rollover` — 첫 뒤집기와 첫 걸음의 병치), `ch2_ev_002`(`mem_ch1_night_feeding` — 통잠 첫날 회상),
  `ch2_ev_005`(`mem_ch1_daycare_waitlist` — 대기 신청의 결과 전화), `ch2_ev_009`(`mem_ch1_first_babyfood` — 첫 이유식 숟가락과 "내가 먹어!"의 병치),
  `ch2_ev_017`(`mem_ch1_return_pressure` — 복직 압박 전화의 종착).
- `once`는 전 이벤트 true, 단 `ch2_ev_008`(등원 거부)·`ch2_ev_015`(이앓이 밤)는 `once:false, cooldown_days:10`.
- `ch2_ev_004`·`ch2_ev_017`은 `preset_worker` 전용. 프리셋 전용 예약 이벤트 `ch2_ev_040`(worker 조기 복귀 회유)·`ch2_ev_041`(freelancer 클라이언트 이탈)·`ch2_ev_042`(fulltime 경력 공백 불안)는 04_01이 정본 소유하며 본 카탈로그 번호와 충돌하지 않는다.
- 복직 체인: `ch1_ev_030`→`ch1_ev_031`(04_01, CH1 예고)→`ch2_ev_004`(확정)→`ch2_ev_017`(첫날 조퇴)→`ch2_ev_040`(04_01). 어린이집 입소 가점(맞벌이·복직예정확인서) 때문에 복직 결정이 입소보다 앞선다 (Korea-first 행정 순서).

## 2. 대표 이벤트 전체 JSON

### 2.1 ch2_ev_004 복직 결정

```json
{
  "event_id": "ch2_ev_004", "chapter": 2, "title_kr": "복직 결정", "event_class": "major",
  "emotion_tags": ["burnout", "reward"], "priority": 95, "once": true, "cooldown_days": 0,
  "trigger": { "type": "scheduled", "conditions": [
    { "type": "day_range", "min": 430, "max": 440 },
    { "type": "preset", "value": "preset_worker" } ] },
  "scenes": [
    { "scene_id": "ch2_ev_004_s1", "location_id": "loc_home_living", "time_block": "evening",
      "script_kr": ["식탁 위에 서류 세 장. 육아휴직 급여 사후지급 안내, 어린이집 입소 대기 확인서, 회사의 복직 예정 확인 요청 메일 출력본.", "휴대폰이 짧게 운다. 팀장: '천천히 생각해요. 근데 다음 주까지.'"] },
    { "scene_id": "ch2_ev_004_s2", "location_id": "loc_home_bedroom", "time_block": "night",
      "script_kr": ["아이는 잠들었고, 남편은 천장을 본다.", "'입소 가점엔 맞벌이가 유리하대.' 말끝이 서류 넘기는 소리에 묻힌다."] }
  ],
  "choices": [
    { "choice_id": "ch2_ev_004_c1", "text_kr": "복직 확인서에 서명한다 — 3월부터 출근",
      "effects": { "mind": -4, "stamina": -3, "rel_npc_boss": 5, "attachment": -2 },
      "memory_tag": "mem_ch2_return_to_work" },
    { "choice_id": "ch2_ev_004_c2", "text_kr": "육아휴직 연장을 신청한다 — 급여는 절반 이하",
      "effects": { "mind": 3, "money": -700000, "rel_npc_boss": -5 },
      "memory_tag": "mem_ch2_extend_leave" },
    { "choice_id": "ch2_ev_004_c3", "text_kr": "육아기 근로시간 단축을 신청한다 — 눈치와 시간의 교환",
      "effects": { "mind": 1, "money": -400000, "rel_npc_boss": -3, "attachment": 2 },
      "memory_tag": "mem_ch2_reduced_hours" }
  ],
  "callback_plan": [
    { "chapter": 5, "memory_tag": "mem_ch2_return_to_work",
      "usage_kr": "CH5 npc_boss 아크 종착 장면에서 입학식 연차 상신에 대한 팀장의 반응(인정/결별) 대사 분기로 회수" },
    { "chapter": 3, "memory_tag": "mem_ch2_extend_leave",
      "usage_kr": "CH3 재취업·비교 이벤트에서 '그때 연장한 휴직'이 경력 공백 대화의 전제로 회수" }
  ]
}
```

### 2.2 ch2_ev_007 어린이집 입소 첫날

```json
{
  "event_id": "ch2_ev_007", "chapter": 2, "title_kr": "어린이집 입소 첫날", "event_class": "major",
  "emotion_tags": ["joy", "burnout"], "priority": 95, "once": true, "cooldown_days": 0,
  "trigger": { "type": "scheduled", "conditions": [{ "type": "day_range", "min": 500, "max": 510 }] },
  "scenes": [
    { "scene_id": "ch2_ev_007_s1", "location_id": "loc_home_living", "time_block": "morning",
      "script_kr": ["낮잠 이불 가방, 여벌 옷 세 벌, 물티슈 두 팩. 전부에 이름 스티커가 붙어 있다.", "아이는 제 가방이 제 몸만 하다는 걸 아직 모른다."] },
    { "scene_id": "ch2_ev_007_s2", "location_id": "loc_daycare", "time_block": "morning",
      "script_kr": ["현관 신발장 앞. 아이의 손이 옷자락을 쥔다.", "선생님이 무릎을 굽힌다. '어머님, 첫 주는 한 시간부터예요.'", "문이 반쯤 닫히고, 울음소리가 복도 길이만큼 따라온다."] }
  ],
  "choices": [
    { "choice_id": "ch2_ev_007_c1", "text_kr": "짧게 안아 주고 돌아선다 — 뒤돌아보지 않기로 한다",
      "effects": { "independence": 2, "attachment": -1, "mind": -4 },
      "memory_tag": "mem_ch2_daycare_first_goodbye" },
    { "choice_id": "ch2_ev_007_c2", "text_kr": "창문 뒤에서 울음이 멎을 때까지 지켜본다",
      "effects": { "mind": 1, "stamina": -5, "independence": -1 },
      "memory_tag": "mem_ch2_daycare_first_goodbye_window" },
    { "choice_id": "ch2_ev_007_c3", "text_kr": "수첩 두 장짜리 당부 목록을 선생님께 건넨다",
      "effects": { "mind": 2, "rel_npc_daycare_teacher": -2, "stamina": -2 },
      "memory_tag": "mem_ch2_daycare_checklist" }
  ],
  "callback_plan": [
    { "chapter": 5, "memory_tag": "mem_ch2_daycare_first_goodbye",
      "usage_kr": "CH5 입학식 교문 앞에서 같은 구도(문 앞의 이별)로 회수 — 이번에는 아이가 먼저 손을 놓는다" }
  ]
}
```

## 3. QA 메모 (15_QA 연동)

- 카탈로그 17종의 `emotion_tags`는 전부 CH2 태그 집합 `{joy, burnout, reward}`의 부분집합 (D-005, 빌드 검증 포함).
- `{"type":"preset"}` 조건 타입은 04_01 프리셋 전용 이벤트 게이트(QA-0401-02)의 데이터화로, 07_01 조건 스키마·13_03 조건식 목록 등록이 필요한 신규 타입이다 (제안 상태로 표기).
- `ch2_ev_007`의 `loc_daycare` 현관 신발장 앞 구도는 06_02 연출 메모의 고정 숏 지시를 따른다.
- `ch2_ev_012`(남편 독박 실험)는 D-011 `husband_support` 변화의 대표 원천 이벤트 — 상세 수치는 14_02 개입 규칙에서 확정.
- `ch2_ev_016`의 응급실 비용, `ch2_ev_004`의 급여 차액(-700,000/-400,000원)은 12_DATABASE 물가 상수 확정 시 상수 참조로 교체한다.
- CH1 회수 5종의 트리거·대본은 07_03 각 이벤트 `callback_plan`과 1:1 교차 검증 완료 (07_02 2절).
