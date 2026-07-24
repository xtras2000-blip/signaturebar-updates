# SignatureBar Updates

SignatureBar 데스크톱 앱 자동업데이트(electron-updater) 배포용 저장소입니다.
릴리스 에셋으로 설치본(.exe)·blockmap을 호스팅합니다.

---

# MOTHER — Game Documentation Project

이 저장소는 게임 프로젝트 **MOTHER**(아이의 일생을 다루는 내러티브 시뮬레이션)의 문서화 작업 공간을 겸합니다.
모든 프로젝트 파일은 `MOTHER/` 폴더 아래에 있으며,
전체 규칙은 `MOTHER/CLAUDE.md`, `MOTHER/PROJECT_RULES.md`, `MOTHER/STYLE_GUIDE.md`를 참고하세요.

## Repository structure

```
MOTHER/docs/
  00_PROJECT      프로젝트 개요·범위·파이프라인
  01_VISION       비전·디자인 필러·타깃
  02_GAME_DESIGN  핵심 게임 디자인
  03_GAME_SYSTEM  시스템 명세
  04_PLAYER       플레이어(엄마) 명세
  05_CHILD        아이 성장·상태 명세
  06_WORLD        세계관·공간
  07_EVENT        이벤트 시스템
  08_DIALOGUE     대화 시스템
  09_UI           UI 명세
  10_ART          아트 디렉션
  11_SOUND        사운드 디렉션
  12_DATABASE     데이터베이스 스키마
  13_JSON         JSON 데이터 포맷
  14_AI           AI(행동·대화) 명세
  15_QA           QA 체크리스트
  99_ARCHIVE      폐기·보류 문서
```

진행 순서는 `MOTHER/TASK_QUEUE.md`, 주요 결정은 `MOTHER/DECISION_LOG.md`에 기록합니다.
