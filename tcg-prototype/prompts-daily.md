# AURA — 평소 모습 캐릭터 시트 프롬프트 (N 라인)

`characters.md`의 외형 설정을 이미지 생성 프롬프트로 옮긴 시트입니다.
Midjourney / SDXL / Flux 계열 실사 모델 기준으로 작성했습니다.

## 사용법

실사 모델은 "한 장에 정면+측면+뒷면" 멀티뷰 시트를 잘 그리지 못합니다.
캐릭터 시트는 아래 방식으로 만드는 것을 권장합니다.

1. 캐릭터별 **베이스 프롬프트**로 이미지를 여러 장 생성해 마음에 드는 얼굴을 고른다
2. 그 이미지의 **시드를 고정**(또는 페이스 레퍼런스/IP-Adapter 등록)한다
3. 같은 프롬프트에 **샷 변형 접미사**만 바꿔 3~5장을 뽑아 한 세트로 묶는다
4. 확정된 세트를 이후 R/SR/UR 코스튬 생성의 얼굴 레퍼런스로 사용한다

### 공통 프리픽스 (모든 프롬프트 맨 앞에 붙임)

```
photorealistic photography of a fictional Korean woman, original character,
natural skin texture with visible pores, realistic body proportions,
soft film-like color grading, shot on a 50mm lens, shallow depth of field,
```

### 샷 변형 접미사 (한 캐릭터당 이것만 바꿔 3~5장 생성)

```
A) full body shot, standing, looking at camera        — 전신
B) three-quarter body shot, relaxed natural pose      — 무릎 위
C) upper body portrait, looking at camera             — 상반신
D) close-up portrait, subtle smile                    — 표정 클로즈업
E) side profile portrait                              — 옆모습
```

### 공통 네거티브 프롬프트

```
anime, cartoon, illustration, 3d render, plastic skin, over-smoothed face,
extra fingers, deformed hands, watermark, text, logo,
resemblance to real celebrities or idols, lookalike of real person
```

### 공통 파라미터

- 카드용 비율 **5:7** (`--ar 5:7` / 1000×1400), 시트용은 2:3 또는 3:4도 무방
- 스타일라이즈/미화 옵션은 낮게 (실사감 유지)
- **금지**: 실존 인물·연예인 이름을 프롬프트에 넣는 것 (초상권 문제, 절대 금지)

---

## 1. 세라 — 「퇴근길」

```
27-year-old Korean woman, 168cm slender build, long straight black hair
with see-through bangs, cool composed expression, sharp calm eyes,
minimal monochrome outfit: black tailored slacks and a crisp white shirt,
black leather watch, walking home at night in Gangnam Seoul,
neon signs and city lights as bokeh background, cinematic night lighting
```

- 무드 키워드: 서늘함, 절제, 도시의 밤
- 표정 지시: 웃음기 없는 무표정 ~ 아주 옅은 미소까지만

## 2. 유나 — 「강의 끝나고」

```
22-year-old Korean female university student, 165cm athletic build,
dark brown hair in a high ponytail with loose baby hairs,
bright clear eyes, energetic expression,
wearing a grey hoodie zip-up, white t-shirt and a backpack,
walking along a ginkgo tree path on a Korean university campus,
warm afternoon sunlight, autumn leaves, candid snapshot mood
```

- 무드 키워드: 활기, 막내, 오후 햇살
- 표정 지시: 씩씩한 미소, 승부욕 있는 또렷한 눈

## 3. 하린 — 「라스트 오더」

```
29-year-old Korean woman, 170cm elegant build,
dark wine-colored wavy bob hair, languid half-lidded eyes, red lipstick,
wearing an oversized charcoal suit over a satin camisole,
leaning on the counter of a dim jazz bar after closing,
holding a wine glass, warm amber bar lighting, smoky atmosphere
```

- 무드 키워드: 나른함, 여유, 앰버 조명
- 표정 지시: 능글맞은 미소, 시선은 살짝 비스듬히

## 4. 미소 — 「오프 시즌」

```
24-year-old Korean woman, 163cm fit swimmer's build,
sun-tanned healthy skin, light brown pixie-short hair, light freckles,
wide cheerful grin, wearing an oversized white t-shirt over swim shorts,
carrying a surfboard on Haeundae beach at sunset,
golden hour light, sea breeze, candid vacation photo mood
```

- 무드 키워드: 건강함, 직진, 노을
- 표정 지시: 이를 드러낸 활짝 웃음이 기본값

## 5. 다인 — 「마감 도피」

```
26-year-old Korean woman, 161cm petite build,
ash-black medium-length hair slightly messy, pale skin,
sleepy half-moon eyes, quiet introverted mood,
wearing a beige trench coat over a knit sweater,
holding a long black umbrella in a rainy Seoul alley at dusk,
rain droplets, wet asphalt reflections, moody overcast lighting
```

- 무드 키워드: 창백함, 관찰자, 비 오는 골목
- 표정 지시: 무심한 듯 졸린 눈, 카메라를 살짝 경계하는 시선

## 6. 솔 — 「공방의 오후」

```
31-year-old Korean woman, 167cm graceful posture,
long jet-black straight hair tied low, dignified serene expression,
wearing a modernized hanbok in muted ivory and deep green tones,
selecting silk fabric in a traditional hanbok atelier in Bukchon,
wooden interior, soft window light, calm and refined atmosphere
```

- 무드 키워드: 기품, 단정함, 한옥 채광
- 표정 지시: 잔잔한 미소, 흐트러짐 없는 자세

## 7. 리유 — 「방송 켜짐」

```
23-year-old Korean woman, 159cm small and lively build,
black hair with pink streak highlights in half twin-tails,
playful cat-like eyes, mischievous grin, LED ear cuff,
wearing an oversized streetwear hoodie with graphic patches,
sitting in a gaming room with RGB LED lights and a glowing headset,
neon purple and pink lighting, streamer webcam angle
```

- 무드 키워드: 하이텐션, 네온, 게이밍 룸
- 표정 지시: 장난기 가득한 웃음, 브이나 손하트 포즈 허용

## 8. 채아 — 「하산길」

```
28-year-old Korean woman, 172cm tall sturdy athletic build,
ash-grey long hair in a single braid, warm gentle smiling eyes,
faint frostbite mark on one cheek, reliable big-sister aura,
wearing a red and black mountain rescue padded jacket with a coiled rope,
standing on a snowy mountain ridge in Seoraksan,
clear winter sky, snow-covered pine trees, crisp cold daylight
```

- 무드 키워드: 듬직함, 설원, 맑은 겨울빛
- 표정 지시: 서글서글한 눈웃음, 힘든 내색 없는 미소

---

## 세트 관리 체크리스트

- [ ] 캐릭터당 A~E 샷 5장 = 총 40장으로 1차 시트 완성
- [ ] 캐릭터별 확정 시드/레퍼런스 이미지 ID를 이 파일에 기록해둘 것
- [ ] 얼굴 확정 후에만 R/SR/UR 코스튬 생성 시작 (얼굴 재롤 방지)
- [ ] 생성 결과가 특정 실존 인물과 닮았다고 판단되면 그 시드는 폐기
