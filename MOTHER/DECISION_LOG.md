# Decision Log

|ID|Decision|Reason|Affected Systems|Status|
|---|---|---|---|---|
|D-001|플레이 기간을 0세~만 7세(초등 입학)로 한정, 5개 챕터 구성|감정 곡선을 완결 가능한 범위로 압축. 7세 이후는 v2 후보|02, 05, 07|Confirmed|
|D-002|게임오버·실패 상태 없음. 선택의 누적 결과만 존재|Pillar 1(감정 우선)·부 타깃(비게이머) 접근성|03, 15|Confirmed|
|D-003|핵심 수치 5종 확정: attachment, child_condition, stamina, mind, money|시스템 복잡도 상한 설정. 추가 수치는 로그 승인 필요|03, 04, 05, 12, 13|Confirmed|
|D-004|감정 장면에서 UI 수치 숨김. 수치는 행동·연출로 간접 표현|수치 최적화 플레이 방지 (Pillar 1)|09|Confirmed|
|D-005|모든 이벤트에 emotion_tags 필수. 누락 시 QA 리젝|챕터 감정 목표와 콘텐츠의 정합성 강제|07, 13, 15|Confirmed|
|D-006|1차 플랫폼 PC(Steam), 게임 내 1일 = 1세션(20~40분)|타깃 분석(01_03) 근거|09, 03|Superseded(세션 정의는 D-016, 플랫폼은 D-017로 대체)|
|D-007|하루를 5개 시간 블록으로 분할: morning, midday, afternoon, evening, night|세션 20~40분 목표와 선택 밀도의 균형|02, 03, 09|Confirmed|
|D-008|아이 성격 축 4종 확정: confidence, empathy, independence, expressiveness (0~100, init 50). 선택 누적으로만 변화|Pillar 4(선택의 누적) 구현체. 단일 선택 분기 금지|05, 07, 13|Confirmed|
|D-009|핵심 수치 초기값: attachment 50, child_condition 70, stamina 70, mind 60, money 3,000,000원|CH1 압도됨 감정 목표에 맞는 여유 없는 출발선|03, 04, 05, 12|Confirmed|
|D-010|이벤트 트리거 3유형: scheduled(시기 고정), conditional(수치·기억 조건), random(가중 랜덤)|콘텐츠 제작·QA 단순화|07, 13, 14|Confirmed|
|D-011|보조 수치 husband_support(0~100) 추가. 핵심 수치 5종에는 미포함|남편 분담 이벤트·개입 규칙의 원천 수치 필요|04, 06, 14|Confirmed|
|D-012|NPC 관계도 rel_{npc_id}(0~100, init 50) 도입. NPC 캐스트는 06_03의 12명이 정본|관계 반응·개입 규칙(14_02) 데이터화|06, 12, 14|Confirmed|
|D-013|배경 프리셋 3종 최종 확정: preset_worker/preset_freelancer/preset_fulltime (04_01 정본). 03_02 초안의 dual/single_income 계열은 폐기|중복 정의 충돌 해소. 프리셋은 소득 형태가 아닌 '엄마의 상황' 기준|03, 04, 12, 13|Confirmed|
|D-014|챕터별 재생일: CH1 16 / CH2 18 / CH3 16 / CH4 14 / CH5 12 (총 76일). 의미 있는 날만 압축 샘플링|총 플레이 6~10시간 목표(01_03) 역산|02, 07|Confirmed|
|D-015|event_id 2형식 허용: 카탈로그 ch{n}_ev_{nnn} + 시스템 예약 ch{n}_ev_{slug}. ch*_ev_{slug}는 문서 산문 전용|시스템 강제 이벤트(밤중 수유·강제 대출 등)를 숫자 카탈로그와 분리|07, 13, 15|Confirmed|
|D-016|세션 재정의: 1세션(20~40분)=재생일 3~5일, 재생일 체감 5~8분(milestone 10~15분, routine 3~5분). 총 플레이 약 7~10시간|76 재생일(D-014)×세션 20~40분 = 25~50시간이 되어 총 플레이 6~10시간(01_03)과 모순 → 해소|01, 02, 09|Confirmed|
|D-017|최종 목표 플랫폼 모바일 앱(iOS/Android, 세로 화면·한 손 탭 조작). PC(Steam)는 모바일 출시 후 이식 예정(포스트 런칭). D-006의 PC 1차 결정 폐기|사용자 확정: 최종 모바일 게임 목표 + 추후 스팀 예정. 재생일 5~8분 단위(D-016)도 모바일 세션 패턴과 부합|01, 09, 10|Confirmed|
|D-018|이벤트 스키마 v1.1: event_class(major/minor/system) 필수 필드 승격, 조건식에 ctx 유형(time_block/holiday/preset/seed) 추가, stat에 husband_support 등록. callback_plan은 데이터 제외·07 카탈로그 문서 관리|실데이터 생성에서 드러난 스키마-문서 모순 해소. 슬롯 시스템(07_01)의 데이터 원천 확보|07, 13, 14, 15|Confirmed|
