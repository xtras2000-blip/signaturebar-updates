# 04_03 Player Actions

행동 카탈로그 문서다. 플레이어가 `block_allocation` 단계에서 시간 블록(`time_block`)에 배정할 수 있는 행동을 정의한다. 카테고리는 D-003·02_GAME_DESIGN의 5종 고정: `care`(돌봄), `housework`(가사), `work`(일), `selfcare`(자기돌봄), `outing`(외출).

## 1. 공통 규칙

- `action_id` 규칙: `act_{category}_{name}` (snake_case).
- 시간 블록 표기: `mo`=morning, `mi`=midday, `af`=afternoon, `ev`=evening, `ni`=night. `all`=5블록 전체.
- `stamina` 비용은 `normal` 상태 기준. `tired` 상태에서 +20% (04_02).
- 효과 열의 수치는 1회 수행당 변화량. 성격 축 변화는 ±3 상한(05_03)을 따른다.
- 해금 챕터 도달 시 카탈로그에 추가되며, 이전 챕터 행동은 발달상 소멸(예: `act_care_feeding`의 수유는 CH2부터 식사 보조로 명칭·연출만 교체)하지 않는 한 유지된다.
- `work` 카테고리는 프리셋 제약: `act_work_remote_task`는 `preset_worker`(휴직 중 최소 업무)·`preset_freelancer`만, `act_work_fulltime_return` 이후 행동은 복직·재취업 이벤트 완료 후 해금.

## 2. 행동 카탈로그 — CH1 (0~12개월, 12종 이상)

| action_id | 명칭 | category | 가능 블록 | stamina 비용 | 효과 | 해금 |
|---|---|---|---|---|---|---|
| `act_care_feeding` | 수유/이유식 | care | all | 10 | child_condition +6, attachment +1 | CH1 |
| `act_care_diaper` | 기저귀 갈기 | care | all | 8 | child_condition +4 | CH1 |
| `act_care_bathing` | 목욕시키기 | care | ev | 14 | child_condition +5, attachment +2 | CH1 |
| `act_care_lull_sleep` | 재우기 | care | ev, ni | 12 | child_condition +5 (sleep 하위 요소, 05_03) | CH1 |
| `act_care_tummy_time` | 터미타임 놀이 | care | mi, af | 10 | attachment +2, 발달 마일스톤 판정 보너스(05_02) | CH1 |
| `act_care_lullaby` | 안고 어르기 | care | all | 9 | attachment +2, mind +1 | CH1 |
| `act_housework_laundry` | 빨래 | housework | mo, mi, af | 10 | 가사 누적치 해소, money −5,000 (세제 등) | CH1 |
| `act_housework_cleaning` | 청소 | housework | mo, mi, af | 12 | 가사 누적치 해소 | CH1 |
| `act_housework_cooking` | 식사 준비 | housework | mo, ev | 12 | stamina 회복 식사 전제, money −12,000 | CH1 |
| `act_work_remote_task` | 재택 업무 처리 | work | mi, af, ni | 16 | money +80,000 (freelancer 건별 40,000~120,000), mind −2 | CH1 |
| `act_selfcare_nap` | 쪽잠 | selfcare | mi, af | 0 | stamina +12 | CH1 |
| `act_selfcare_shower` | 느긋한 샤워 | selfcare | ev, ni | 5 | mind +4 | CH1 |
| `act_selfcare_calling_friend` | 친구와 통화 | selfcare | ni | 5 | mind +6 (isolation 계열 이벤트 확률 감소) | CH1 |
| `act_outing_stroller_walk` | 유아차 산책 | outing | mo, af | 14 | child_condition +3, mind +3 | CH1 |
| `act_outing_clinic` | 소아과 방문 | outing | mo, mi | 16 | child_condition(health) +10, money −25,000 | CH1 |

## 3. 행동 카탈로그 — CH2 (1~3세, 추가 8종)

| action_id | 명칭 | category | 가능 블록 | stamina 비용 | 효과 | 해금 |
|---|---|---|---|---|---|---|
| `act_care_play_blocks` | 블록 놀이 | care | mi, af | 12 | attachment +2, confidence +1 | CH2 |
| `act_care_reading_picturebook` | 그림책 읽어주기 | care | ev, ni | 8 | attachment +2, expressiveness +1 | CH2 |
| `act_care_tantrum_soothing` | 떼쓰기 달래기 | care | all | 15 | attachment +1, mind −3, empathy +1 | CH2 |
| `act_housework_babyproofing` | 안전용품 설치 | housework | mi, af | 12 | 가정 내 사고 random 이벤트 가중치 −50%, money −60,000 | CH2 |
| `act_work_parttime` | 단시간 근무 | work | mi, af | 18 | money +60,000, mind −2 | CH2 |
| `act_selfcare_exercise` | 홈트레이닝 | selfcare | mo, ni | 10 | stamina 최대 회복 효율 +10% (7일 지속), mind +3 | CH2 |
| `act_outing_playground` | 놀이터 나들이 | outing | af | 15 | child_condition +3, independence +1 | CH2 |
| `act_outing_daycare_dropoff` | 어린이집 등하원 | outing | mo, af | 10 | 등원일 mi·af 블록 해방(엄마 자유 블록화), attachment 판정은 하원 연출(05_04) | CH2 |

## 4. 행동 카탈로그 — CH3 (3~5세, 추가 8종)

| action_id | 명칭 | category | 가능 블록 | stamina 비용 | 효과 | 해금 |
|---|---|---|---|---|---|---|
| `act_care_question_answering` | "왜?" 질문 받아주기 | care | all | 10 | expressiveness +1, confidence +1, mind −1 | CH3 |
| `act_care_pretend_play` | 역할 놀이 | care | af, ev | 12 | empathy +1, attachment +2 | CH3 |
| `act_housework_meal_prep` | 반찬 만들어 두기 | housework | mi | 14 | 이후 3일 `act_housework_cooking` 비용 −50% | CH3 |
| `act_work_fulltime_return` | 복직 근무 | work | mo, mi, af | 20 | money +130,000/일, stamina 회복 행동 제한 | CH3 |
| `act_selfcare_hobby` | 취미 시간 | selfcare | ni | 6 | mind +7 | CH3 |
| `act_outing_culture_center` | 문화센터 수업 | outing | mo, mi | 14 | confidence +1, money −30,000, comparison 이벤트 노출 | CH3 |
| `act_outing_playdate` | 또래 친구 약속 | outing | af | 14 | empathy +1, independence +1 | CH3 |
| `act_outing_kindergarten_event` | 유치원 행사 참석 | outing | mo, mi | 16 | attachment +3, 불참 시 guilt 계열 conditional 이벤트 | CH3 |

## 5. 행동 카탈로그 — CH4 (5~6세, 추가 8종)

| action_id | 명칭 | category | 가능 블록 | stamina 비용 | 효과 | 해금 |
|---|---|---|---|---|---|---|
| `act_care_hangul_play` | 한글 놀이 | care | af, ev | 12 | 학습 압박 선택 시 attachment −2, 놀이 선택 시 confidence +1 | CH4 |
| `act_care_emotion_talk` | 감정 대화 | care | ev, ni | 8 | empathy +2, attachment +2 | CH4 |
| `act_care_apology_talk` | 화해의 대화 | care | ev, ni | 10 | attachment +3 (guilt 이벤트 후 48시간 내에만 활성) | CH4 |
| `act_housework_seasonal` | 계절 살림 정리 | housework | mi, af | 14 | 가사 누적치 대량 해소 | CH4 |
| `act_work_overtime` | 야근 | work | ev, ni | 20 | money +90,000, attachment −2, mind −4 | CH4 |
| `act_selfcare_counseling` | 심리 상담 | selfcare | mi | 8 | mind +10, money −80,000, burnout 회복 가속(04_02) | CH4 |
| `act_outing_library` | 도서관 나들이 | outing | mi, af | 12 | expressiveness +1, money 0 | CH4 |
| `act_outing_family_trip` | 가족 나들이 | outing | mo+mi+af 연속 소비 | 25 | attachment +5, mind +5, money −100,000 | CH4 |

## 6. 행동 카탈로그 — CH5 (6~7세, 추가 8종)

| action_id | 명칭 | category | 가능 블록 | stamina 비용 | 효과 | 해금 |
|---|---|---|---|---|---|---|
| `act_care_school_prep` | 입학 준비물 챙기기 | care | ev | 10 | 입학 준비도 +1 (05_02 CH5 마일스톤 판정) | CH5 |
| `act_care_self_routine_coach` | 스스로 준비 연습 | care | mo | 8 | independence +2, attachment −1 (떨어져 보기) | CH5 |
| `act_care_night_talk` | 잠들기 전 이야기 | care | ni | 6 | attachment +2, memory_log 회수 대사 발생 | CH5 |
| `act_housework_room_reorganize` | 초등생 방 꾸미기 | housework | mi, af | 16 | 입학 준비도 +2, money −150,000 | CH5 |
| `act_work_career_restart` | 재취업 준비/근무 | work | mi, af | 18 | money +100,000, mind −2 (`preset_fulltime` 재취업 이벤트 후) | CH5 |
| `act_selfcare_journal` | 육아 일기 정리 | selfcare | ni | 4 | mind +5, memory_log 열람 연출 | CH5 |
| `act_outing_school_visit` | 예비소집·학교 방문 | outing | mo, mi | 14 | 입학 준비도 +2, letting_go 이벤트 트리거 | CH5 |
| `act_outing_stationery_shopping` | 문구점에서 책가방 사기 | outing | af | 12 | 입학 준비도 +1, attachment +2, money −80,000 | CH5 |

## 7. JSON

행동 정의 데이터 예시 (13_JSON 카탈로그 포맷):

```json
{
  "action_id": "act_care_bathing",
  "category": "care",
  "name_kr": "목욕시키기",
  "allowed_blocks": ["evening"],
  "stamina_cost": 14,
  "effects": {"child_condition": 5, "attachment": 2},
  "unlock_chapter": 1,
  "preset_filter": []
}
```

## 8. QA

| ID | 확인 항목 | 통과 기준 |
|---|---|---|
| QA-0403-01 | 챕터별 사용 가능 행동 수 | CH1 ≥ 12, CH2~CH5 각 신규 ≥ 8 |
| QA-0403-02 | 허용 외 블록에 행동 배정 시도 | 배정 불가, 사유 문구 표시 |
| QA-0403-03 | `tired` 상태 비용 검증 | 표 기재 비용의 1.2배(반올림) 적용 |
| QA-0403-04 | 성격 축 효과 상한 | 어떤 행동도 축 1회 변동 ±3 초과 없음 (05_03) |
