# 06_02 Locations

장소 카탈로그의 단일 기준. 카탈로그성 문서로 표 중심 구성 (7섹션 의무 대상 아님).
상위 지리 맥락은 06_01, 장소에서 발생하는 이벤트 정의는 07_EVENT를 따른다.

## 1. 식별자 규칙

- `location_id` 명명: `loc_{구역}_{이름}` (집 내부) / `loc_{이름}` (외부). 영어 snake_case.
- 이벤트 JSON의 장면(`scenes[].location_id`)과 트리거 조건(`{"type":"location", ...}`)에서 참조한다.
- 행동 카테고리는 00_01 핵심 루프의 4분류를 따른다: `care`(돌봄), `chore`(가사), `work`(일), `self`(자기 돌봄).
- "해금 챕터"는 장소가 처음 등장 가능한 챕터. 해금 이후에도 등장은 이벤트·행동 배분에 따른다.

## 2. 집 내부 (한솔아파트 3단지, 24평 전세)

| location_id | 이름 | 해금 챕터 | 가능 행동 카테고리 | 연결 이벤트 풀 |
|---|---|---|---|---|
| `loc_home_living` | 거실 | CH1 | care, chore, self | 놀이·훈육 일상, 층간소음 항의, 남편 대화, 돌잔치 준비 |
| `loc_home_bedroom` | 안방 | CH1 | care, self | 밤중 수유, 재우기 전쟁, 부부 갈등·화해, 혼자 자기(CH4) |
| `loc_home_kitchen` | 주방 | CH1 | chore, care | 이유식 시작, 편식 갈등, 살림 지출, 명절 음식 준비 |
| `loc_home_bathroom` | 욕실 | CH1 | care, chore, self | 목욕 전쟁, 배변 훈련(CH2), 혼자 우는 엄마 연출(수치 UI 숨김, D-004) |
| `loc_home_child_room` | 작은방(아이 방) | CH1 | care, chore | 창고→아이 방 전환(06_01 4절), 유아 책상 조립, 입학 준비 |

## 3. 동네·외부

| location_id | 이름 | 해금 챕터 | 가능 행동 카테고리 | 연결 이벤트 풀 |
|---|---|---|---|---|
| `loc_postpartum_center` | 산후조리원 | CH1 | care, self | 퇴소(CH1 오프닝), 조리원 동기 인연 형성, 이후 회상 전용 |
| `loc_pediatric_clinic` | 단지 상가 소아과 | CH1 | care | 예방접종, 열 감기, 영유아 건강검진, 독감철 대기실 |
| `loc_daycare` | 국공립 어린이집 | CH2 | care | 입소 대기 신청(CH1), 첫 등원 분리불안, 교사 상담, 재롱잔치 |
| `loc_playground` | 단지 놀이터 | CH1 | care, self | 또래 접촉, 놀이터 서열·비교, 다툼과 사과, 이웃 대화 |
| `loc_mart` | 상가 마트 / 대형마트 | CH1 | chore | 장보기 지출, 장난감 조르기(CH2~), 카트 실랑이 |
| `loc_grandma_home` | 친정 (KTX 2시간) | CH1 | care, self | 친정엄마 방문·역방문, 김치 택배, "몸조리 해라" 통화 |
| `loc_inlaw_home` | 시댁 (버스 30분) | CH1 | care, chore | 명절 방문(`holiday:seollal`/`chuseok`), 훈육 방식 갈등 |
| `loc_office` | 회사 (광역버스 50분) | CH1 | work | 복직 압박 통화, 육아휴직 눈치, 복직 후 조퇴 갈등(CH2~) |
| `loc_momcafe` | 맘카페 "한솔맘 이야기" (온라인) | CH1 | self | 정보 검색, 발달 비교 불안, 중고 거래, 익명 위로 |
| `loc_community_center` | 행정복지센터·문화센터 | CH2 | care, self | 문센 수업, 양육수당·보육료 신청(Korea-first 행정 디테일) |
| `loc_elementary_school` | 초등학교 | CH5 | care | 예비소집일, 입학식(CH5 피날레), 등굣길 연습 |

## 4. 운용 규칙

| 규칙 | 내용 |
|---|---|
| 블록 이동 비용 | 외부 장소는 시간 블록(`time_block`) 1개를 소비한다. 원거리(친정·회사)는 2개 — 자원 부족 설계(Pillar 2) |
| 해금 처리 | 챕터 시작 시 자동 해금. 별도 해금 이벤트 없음 (단, `loc_daycare`는 CH1 대기 신청 이벤트가 선행 연출) |
| 온라인 장소 | `loc_momcafe`는 이동 비용 0, `night` 블록에서만 진입 가능 — 밤에 혼자 스마트폰 보는 연출 고정 |
| 회상 전용 전환 | `loc_postpartum_center`는 CH2부터 물리 진입 불가, `memory_log` 회상 연출에서만 재사용 |
| 데이터화 | 장소별 이동 비용·지출 상수는 12_DATABASE 상수 테이블로 이관 |

## 5. QA 체크 (15_QA 연동)

- 모든 이벤트의 `scenes[].location_id`는 본 카탈로그에 존재해야 한다. 미등록 ID는 리젝.
- 해금 챕터 이전의 장소를 참조하는 이벤트는 리젝 (예: CH1 이벤트가 `loc_elementary_school` 참조 불가).
- 신규 장소는 본 문서에 행을 추가한 뒤에만 이벤트에서 사용한다 (00_04 표기 규칙 상속).
