---
layout: single
title:  "나스닥은 거래시간을 늘리면서, 거래를 더 길게 멈추기로 했습니다"
categories: 미국시장
tag: [data background, 미국시장, 거래정지, 나스닥, 거래시간연장]
toc: true
author_profile: false
---

## 밤 7시 50분에 정지가 몰려 있었습니다

나스닥이 운영하는 NasdaqTrader의 RSS피드에서 거래정지 이력을 받아 시각별로 세어보면 이상한 칸이 하나 있습니다. **밤 7시 50분**{: style="color: #4682B4;"}입니다.

수백 개 회사가 각자 사정으로 낸 뉴스가 초까지 같은 분에 모일 수는 없습니다. 정체를 확인해보니 **뉴스가 아니었습니다.** 확보한 19시 50분 정지 **2,003건**(2021-08-25 ~ 2026-07-29) 중 **1,608건(80.3%)이 주식병합(Reverse Stock Split)**{: style="color: #4682B4;"}이었습니다.

SEC가 승인한 나스닥 규정에 시각이 그대로 적혀 있습니다. **병합 효력일 전날 애프터마켓 종료 직전에 정지하고, 다음 날 아침에 재개한다.** 거래소에 재량이 없는 **의무 정지**{: style="color: #4682B4;"}입니다.

## 주식병합은 원래 많았습니다

나스닥 기업행위 공지 3,999건에서 주식병합 공지 2,044건을 추리고, 그중 **보통주와 ADR만 남기고 「UPDATED」 재공지를 뺀 1,930건**{: style="color: #4682B4;"}을 연도별로 세면 이렇습니다.

| 연도 | 주식병합 공지 | 19시 50분 정지 |
|---|---:|---:|
| 2019 | 107 | *(정지 자료 없음)* |
| 2020 | 91 | *(정지 자료 없음)* |
| 2021 | 26 | **0** |
| **2022** | **177** | **0** |
| 2023 | 366 | 59 |
| **2024** | **388** | **401** |
| 2025 | 419 | 420 |
| 2026 (7월까지) | 356 | 351 |

*(양쪽 모두 **보통주와 ADR만**, **사건 1건 = 1개**로 셌습니다. 워런트·우선주·ETF·ETN은 양쪽에서
제외했고, 「UPDATED」 재공지도 뺐습니다. 2023년이 낮은 것은 규정 승인이 그해 11월 7일이기
때문입니다. 2024년이 공지보다 약간 많은 것은 연말 공지의 정지가 이듬해에 걸리는 경계 누수이고,
2026년이 약간 적은 것은 정지 자료가 7월 31일에 끊겨서입니다.)*


**19시 50분에 세워 아침에 여는 형태는 이전에도 있었지만, 주식병합에는 쓰지 않았습니다.**{: style="color: #4682B4;"} 승인 이후에는 1,936건 중 **1,606건이 주식병합**입니다.

절차의 일관성도 함께 바뀌었습니다. 규정 이후 체결 재개가 확인된 1,618건에서 **09시 00분이 1,300건(80%), 09시 05분까지 합치면 99%**{: style="color: #4682B4;"}입니다. 「대략 아침에 연다」가 「09시 00분에 연다」가 되었습니다.

즉 **규정이 만든 것은 주식병합 관련 거래정지를「전건에 예외 없이, 정해진 시각에」로 바꾼 것**{: style="color: #4682B4;"}입니다.

### 규정 전에는 정지 없이 새벽 4시에 열었습니다

그러면 원래는 어떻게 처리했을까요. 승인명령서에 적혀 있습니다.

> Nasdaq **currently processes reverse stock splits overnight**, with the security **opening for trading at 4 a.m. ET** in the pre-market hours … **on a split-adjusted basis.**

**밤새 시스템이 주식 수와 가격을 조정하고, 새벽 4시에 조정된 값으로 그냥 열었습니다.**{: style="color: #4682B4;"} 거래를 멈추지 않았습니다. 그렇게 수백 건이 처리됐고 시장은 돌아갔습니다.
그리고 나스닥은 이러한 현행방식에 문제가 있음을 인정했습니다(`it is not optimal`).

> **Recently, market participants have expressed concerns** with allowing trading on an adjusted basis at 4 a.m., noting that **it is not optimal** because **system errors or problems with orders may go unnoticed for a period of time** when a security that has undergone a reverse stock split opens for trading with the other thousands of securities.

근거로 사고 한 건을 들었는데 내용을 보겠습니다.

> For example, **in one recent instance** problems in connection with the processing of a reverse stock split resulted in **a broker executing trades selling more shares than customers held in their accounts**, resulting in a temporary short position.

**고객이 보유한 것보다 많이 팔았습니다.**{: style="color: #4682B4;"} 주식병합으로 주식 수가 줄었는데 주문 시스템이 이전 수량을 들고 있었던 것입니다. 결과는 의도하지 않은 공매도였습니다.


### 그리하여 현재의 19:50~익일09:00 의무적·기계적 거래정지 규정이 도입되었습니다

> A trading halt due to a reverse stock split will be **mandatory** pursuant to proposed Rule 4120(a)(14).

> The proposed new rule will allow for Nasdaq and market participants to better detect any errors or problems with orders for the security **before trading in the security begins.**

나스닥은 문제를 해결하기 위해 의무적, 기계적인 거래정지를 거는 것으로 규정을 개정했습니다. 여기서 방향이 중요합니다. **시간 제약 하에서 오류를 더 빨리 찾는 쪽이 아니라, 차라리 거래정지를 함으로써 충분한 시간을 주고 오류를 찾는 쪽**{: style="color: #4682B4;"}을 택했습니다. (`before trading in the security begins`)

## 거래시간을 연장하면 무조건 "맞춰봐야죠"가 아니라, 안되는 건 안된다고 말합니다

2026년, 나스닥은 **주 5일 23시간 거래(23/5)**{: style="color: #4682B4;"}를 준비하면서 이 정지 규정을 다시 개정했습니다.

> **In conjunction with plans for operating 23 hours a day, 5 days a week ("23/5 Trading")**, the Exchange proposes to amend Rule 4120 …

논리는 이렇게 전개됩니다.

> Under 23/5 Trading, however, Nasdaq's non-trading window will be **reduced to a one-hour pause.** Consequently, Nasdaq will **no longer have a substantial non-trading window** during which it can process such corporate actions without potentially impacting ongoing trading.

거래시간이 연장되면 주식병합 같은 기업행위를 처리할 **충분한 시간이 남지 않기 때문에**(`no longer have a **substantial** non-trading window`), 의무적·기계적 거래정지 대상을 더 확대하겠다는 것입니다. 눈여겨볼 점은 단순히「연장할 것인가」가 아니라 **「연장하면 무엇이 현실적으로 불가능해지는가」**{: style="color: #4682B4;"}를 생각했다는 것입니다.


### 그냥 안된다는 게 아닙니다. 시장의 관점에서도 안된다는 것입니다

거래시간 연장에 "맞춰봐야죠"라고 방치했을 때 생기는 결과를 열거한 문장이 있습니다.

> the continued trading of securities undergoing such corporate actions could potentially result in **price dislocations, investor confusion, erroneous executions, and general operational risk.**

**네 가지 모두 시장 기준의 불편함 입니다.**{: style="color: #4682B4;"}

| 열거된 위험 | 피해가 발생하는 곳 |
|---|---|
| **price dislocations** - 가격 왜곡 | 그 종목을 사고파는 투자자 |
| **investor confusion** - 투자자 혼란 | 조정 전후 가격을 구분하지 못하는 투자자 |
| **erroneous executions** - 잘못된 체결 | 되돌릴 수 없는 체결을 받은 양쪽 |
| **general operational risk** - 전반적 운영 리스크 | 시장 전체 |

**이것들은 충분히 시장조치를 처리할 시간이 확보되지 않은 상태로 거래가 계속되면 시장에서 무슨 일이 벌어지는지를 말하고 있습니다.**{: style="color: #4682B4;"}


## 나스닥이 말하는 "거래시간을 연장하면 무엇을 잃게 되는가"

> The Exchange believes these changes would provide important operational safeguards by ensuring that both the Exchange and market participants have adequate time to process such corporate actions in a nearly continuous trading environment, thereby **preserving a protection that has historically been implicit in a market structure with limited trading hours.**

**「거래시간이 짧았던 시장구조에서 역사적으로 암묵적이었던 보호장치를 보전한다.」**{: style="color: #4682B4;"}라고 나스닥은 말합니다.

거래시간이 짧으면 장종료후 충분한 시간을 갖고 시장조치를 처리할 시간이 저절로 생깁니다. **아무도 설계하지 않았는데 존재하는 보호장치**{: style="color: #4682B4;"}입니다. 규정에도 없고 시스템에도 없고, 그저 시장이 닫혀 있기 때문에 있는 것입니다.

그런데 거래시간을 늘리면 그것이 사라집니다. **나스닥은 이러한 사실을 인지하고 없어질뻔한 보호장치에 이름을 붙여 규정으로 다시 만들었습니다.**{: style="color: #4682B4;"}

## 대상을 늘리면서, 시각을 통일해 자동화했습니다

새 규정은 거래정지 대상을 **아홉 가지 기업행위**{: style="color: #4682B4;"}로 열거합니다. 종목코드 변경, CUSIP 변경, 종가의 25% 이상 배당, 주식분할(정·역), De-SPAC 거래, 인적분할, 증권 종류 변경, 합병·강제교환, 그리고 여기 열거되지 않은 그 밖의 기업행위로 확대하는 한편, 23시간 거래체계를 반영하여 거래정지 시각을 21시 직전, 재개시각을 08시로 설정했습니다.
그리고 기존에 이미 거래정지 규정이 었었던 주식병합은 **정지 시각과 재개 시각을 새로 추가된 거래정지 규칙 시간대로 옮깁니다.**

| | 현행 | 23/5 이후 |
|---|---|---|
| 정지 | **19:50** (애프터마켓 종료 전) | **21:00 직전** (야간장 개시 전) |
| 재개 | **09:00** | **08:00** |


왜 하나의 시각으로 모으는지도 적혀 있습니다.

> the Exchange therefore believes that it is reasonable, in the context of 23/5 Trading, to adopt a **single, uniform implementation time for all halts** … which would facilitate consistent treatment of covered corporate actions and **enable the halts to be implemented through an automated process.**

**아홉 가지에 하나의 시각을 적용해 자동 처리가 가능하게 하려는 것**{: style="color: #4682B4;"}입니다. 대상을 늘리면서 사람 손을 늘리는 대신, **시각을 통일해 기계가 처리할 수 있는 형태로 만들었습니다.**

이 개정안은 2026년 6월 29일 제출되어 7월 13일 연방관보에 실렸고, 적용 시점을 23/5 거래 시작에 맞춰 두었습니다.

> The Exchange proposes that the changes in this proposal … would become operative **at the commencement of 23/5 Trading.**

## 시사점

나스닥에 두번의 환경 변화가 있었고, 두번의 대응이 있었습니다.

```text
주식병합이 급증한다 (2021년 35건 → 2022년 196건 → 2023년 1분기 78건)
   → 새벽 4시 개장에서 조정 오류가 한동안 안 보인다는 문제가 제기된다
   → 개장을 09시로 미루고, 그 앞에 19시 50분 정지를 만든다          (2023년)

23시간 거래로 간다
   → 밤새 처리하던 창구가 한 시간으로 줄어든다
   → 대상을 아홉 가지로 넓히고, 정지를 21시 직전 · 재개를 08시로     (2026년, 시행 전)
```

**첫 번째는 조치건수가 다섯 배로 늘자 같은 구조가 위험으로 보이기 시작한 것**{: style="color: #4682B4;"}입니다. 

> Nasdaq has observed that the current market environment has led to **an increase in reverse stock split activity. In 2022, Nasdaq processed 196 reverse stock splits, compared to 35 in 2021 and 98 in 2020.**

**두 번째는 반대입니다.** 조치건수 아니라 **거래시간이라는 전제가 바뀝니다.** 조치건수가 그대로여도 거래시간이 연장되면서 안정적인 조치를 할 시간이 사라집니다.

**즉 나스닥은 두 가지에 모두 대응했습니다** — **① 기존 방식이 감당하던 양을 넘었을 때, ② 기존 방식이 딛고 있던 전제가 바뀔 때.**{: style="color: #4682B4;"} 둘 다 사고가 이미 터진 뒤가 아니라 **감당 범위를 벗어나는 것이 보인 시점**입니다.

**그리고 두 번 모두 거래를 더 오래 멈추는 쪽으로 결정했습니다.**{: style="color: #4682B4;"} 새벽 4시에 열던 것을 09시로 미뤘고, 대상을 주식병합 하나에서 아홉 가지로 넓혔습니다. 23시간 거래에서는 21시 직전에 세워 **다음 날 08시까지 열한 시간**{: style="color: #4682B4;"}을 비웁니다. **거래시간을 늘리는 개편의 부속 조치가 「거래를 더 길게 멈추는 것」이었습니다.**

역설처럼 보이지만 역설이 아닙니다. **연장 자체가 목표라면 멈추는 시간은 손실입니다.** 그러나 나스닥의 문서는 연장을 목표로 놓지 않았습니다. `orderly trading`, `accurate pricing and execution`, `operational safeguards` - 지키려는 것을 먼저 적고, **거기에 필요한 만큼 멈췄습니다.**{: style="color: #4682B4;"} 늘어난 시간에 잘못된 가격으로 체결되는 것보다 열리지 않는 편이 낫다고 판단한 것입니다.

**무조건 연장이 아니라 안정적 연장입니다.**{: style="color: #4682B4;"} 몇 시간을 더 여는지가 아니라, **그 시간에 시장이 제대로 작동하는지**를 기준으로 삼았습니다.
