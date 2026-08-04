---
layout: single
title:  "밤 7시 50분의 정체는 주식병합이었습니다"
categories: 미국시장
tag: [data background, 미국시장, 거래정지, 나스닥, NYSE, 주식병합]
toc: true
author_profile: false
---

## 지난 편에서 남긴 숙제

지난 글에서 나스닥의 뉴스 거래정지 920건을 세어보니 **537건(58.4%)이 밤 7시 50분 정각**{: style="color: #4682B4;"}에 걸려 있었습니다. 그리고 그중 526건이 다음 거래일 아침 9시 정각에 일제히 풀렸습니다.

뉴스 관련 정지 코드가 붙어 있는데 뉴스의 성격이 아니었습니다. 1년 동안 251개 거래일 중 193일에, 그것도 늘 같은 1분에 터지는 뉴스라는 것은 존재할 수 없습니다.

**[관련 포스팅]** [나스닥 거래정지의 절반이 밤 7시 50분에 걸립니다]({{site.url}}/미국시장/us-halt-session/)<br>
{:.notice--success}

그래서 이번에는 **이 정지들이 각각 무슨 사건이었는지 전건을 추적**{: style="color: #4682B4;"}해 보겠습니다. 1년치가 아니라 수집해 둔 데이터 전 기간이 대상입니다.

## 나스닥은 기업행위 공지를 따로 발행합니다

추적의 단서는 나스닥 트레이더 사이트에 있습니다. 나스닥은 거래정지 기록과는 **별도로**{: style="color: #4682B4;"} 기업행위 공지(Equity Corporate Actions Alert)를 발행합니다. 액면분할, 주식병합, 합병, 종목코드 변경, CUSIP 변경 같은 일이 생기면 시장 참가자들에게 미리 알려주는 게시물입니다.

쉽게 말해 **"이 종목에 이런 변화가 예정되어 있으니 시스템을 준비하라"**{: style="color: #4682B4;"}는 공지입니다. 헤드라인은 이런 식으로 생겼습니다.

> Information Regarding the Reverse Stock Split and CUSIP Number Change for Wheeler Real Estate Investment Trust, Inc. (WHLR)

헤드라인 끝에 티커가 괄호로 붙어 있습니다. **거래정지 기록에도 티커와 날짜가 있으니, 두 자료를 붙여볼 수 있습니다.**{: style="color: #4682B4;"} 어떤 종목이 언제 정지되었는지, 그 무렵 그 종목에 어떤 기업행위 공지가 나갔는지를 대조하는 것입니다.

이 아카이브를 2019년부터 2026년까지 전 연도 수집했습니다. 총 3,999건입니다.

## 데이터를 어떻게 잡았는지

* 대상: 수집된 나스닥 거래정지 데이터 전 기간(**2019년 2월 22일 ~ 2026년 7월 29일**{: style="color: #4682B4;"}, 원본 70,348건)
* 조건: 정지 시각이 **미국 동부시간 19시 50분 00초**{: style="color: #4682B4;"}, 나스닥 상장 종목, 사유 코드 `T1/T2/T3`, 운영기업의 보통주·ADR, 실제 거래 재개 시각이 기록된 건
* 이렇게 걸러내면 **1,267건**{: style="color: #4682B4;"}이 남습니다. 기간은 2021년 8월 31일부터 2026년 7월 29일까지입니다.
* 대조: 나스닥 기업행위 공지 아카이브에서 정지일 기준 직전 14일 이내에 해당 티커가 등장하는 공지를 찾습니다. 티커로 직접 붙지 않는 건은 발행사명·관련 증권·후속 공지로 수동 연결하고, 그래도 안 붙는 건은 회사 IR과 SEC 원문으로 확인했습니다.

결과는 다음과 같습니다.

| 근거 | 건수 |
|---|---:|
| 나스닥 기업행위 공지로 확인 | 1,260 |
| 회사 IR·SEC 원문으로 확인 | 7 |
| **확인 못 한 건** | **0** |

**1,267건 전부에 근거를 붙였습니다.**{: style="color: #4682B4;"} 각 행에 근거 문서의 URL을 함께 기록했습니다.

## 97%가 주식병합이었습니다

![원인분류]({{site.url}}/assets/images/2026-08-02-us-halt-reverse-split/2_cause_mix.png)<br><br>

**1,267건 중 1,230건(97.1%)이 주식병합(액면병합)**{: style="color: #4682B4;"}이었습니다. 나머지는 합병·조직재편 23건, 기타 기업행위 4건, ADR 전환 2건, 상환 1건 등으로 흩어져 있습니다. 뉴스라고 부를 만한 사건은 전체에서 두 건뿐이었습니다.


## 왜 하필 밤 7시 50분정지(익일 09시 재개)인가

답은 추측할 필요 없이 규정 문서에 적혀 있습니다. **두 시각은 밤사이 이뤄지는 병합 조정 작업을 앞뒤에서 감싸는 울타리**{: style="color: #4682B4;"}입니다.

```text
19:50  정지     애프터마켓 마감(20:00)의 10분 전
                병합 전 주식으로 체결되는 거래를 마감 뒤까지 남기지 않으려고
   ↓
  밤사이        주식 수 · 가격 · CUSIP 조정
   ↓
09:00  재개     정규장 개장(09:30)의 30분 전
                조정되지 않은 주문을 장부에서 솎아낼 시간을 두려고
```

목적은 뉴스를 퍼뜨리는 것이 아니라 **병합 처리가 시스템에 제때 반영되지 않아 생기는 오류를 막는 것**{: style="color: #4682B4;"}입니다. 명령서는 그것을 *"fair and orderly markets and the protection of investors"*라고 적습니다.

미국 증권거래위원회(SEC)가 승인한 문서에서 근거를 하나씩 보면 이렇습니다. 먼저 두 시각 자체입니다.

> **SEC Release No. 34-98878 (File No. SR-NASDAQ-2023-036), 2023년 11월 7일**<br>
> In general, Nasdaq expects to **initiate the halt at 7:50 p.m., prior to the close of post-market trading at 8 p.m.** on the day immediately before the split in the security becomes effective, and **resume trading at 9 a.m.** on the day the split is effective.

**19시 50분인 이유**{: style="color: #4682B4;"}는 각주에 있습니다. 애프터마켓이 20시에 닫히는데 그 직전에 세워야 병합 전 주식으로 체결되는 거래가 마감 뒤까지 남지 않기 때문입니다. 20시에 장이 완전히 닫히면 그 종목의 미체결 주문은 전량 취소됩니다.

> Initiating the halt at approximately 7:50 p.m. will provide Nasdaq with **a limited buffer** to ensure that trading in a security that is undergoing a reverse stock split **will not continue after the close of post-market trading.**

**09시인 이유**{: style="color: #4682B4;"}도 적혀 있습니다. 정규장이 열리기 전에 나스닥이 호가장부를 직접 훑어 잘못 조정된 주문을 걸러낼 시간을 두려는 것입니다.

> it is appropriate to re-open the security at 9:00 a.m. using the Nasdaq Halt Cross process … because it gives the Exchange an opportunity to **review its order book and root out any orders … that have not correctly adjusted to the security's new stock price.**

[***(SEC 승인 명령서 원문(링크))***](https://public-inspection.federalregister.gov/2023-25013.pdf)

그리고 가장 중요한 대목이 하나 더 있습니다.

> Nasdaq will **not have the discretion** of determining whether to declare a trading halt in a security that is subject to a reverse stock split.

**거래소에 재량이 없습니다.**{: style="color: #4682B4;"} 주식병합이 예정되어 있으면 사람이 판단할 것 없이 자동으로 걸립니다. 2023년 승인 당시 신설된 조항은 **Nasdaq Rule 4120(a)(14)**이고, 재개 절차는 Rule 4753(Nasdaq Halt Cross)을 따릅니다.



### 규정이 만든 것은 정지가 아니라 의무입니다

이 규정이 왜 필요했는지는 승인 명령서에 적혀 있습니다. 병합을 하는 회사들의 성격에서 시작합니다.

**병합은 대개 아무도 안 보는 소형주가 합니다.**{: style="color: #4682B4;"}

> Reverse stock splits are often effected by **smaller companies that do not have broad media or research coverage.**

병합 사실이 잘 알려지지 않은 채 밤사이 조정되지 않은 주문이 남아 있으면 다음 날 아침에 사고가 납니다.

**2023년 이전에는 병합을 앞두고 미리 거래를 세우는 조항이 없었습니다.**{: style="color: #4682B4;"} 명령서가 그렇게 적습니다.

> Currently, none of the provisions in Rule 4120 provide authority to **pre-emptively** declare a trading halt in a security undergoing a significant corporate action that could lead to investor or market confusion.

그때까지의 기본 처리는 정지 없이 **밤사이 조정해 다음 날 새벽 4시 프리마켓에 병합 반영가로 그냥 여는 것**{: style="color: #4682B4;"}이었습니다. 그런데 시장 참가자들이 여기에 문제를 제기했습니다.

> Nasdaq **currently processes reverse stock splits overnight**, with the security opening for trading at **4 a.m. ET** in the pre-market hours … on a split-adjusted basis. Recently, market participants have expressed concerns with allowing trading on an adjusted basis at 4 a.m., noting that it is not optimal because **system errors or problems with orders may go unnoticed for a period of time** when a security that has undergone a reverse stock split **opens for trading with the other thousands of securities.** These errors have the potential to adversely affect **investors, market participants and the issuer.**

병합 종목 하나가 다른 수천 종목과 **같이** 열리니 아무도 그 종목만 지켜보고 있지 않고, 그래서 오류가 한동안 묻힙니다.

**추상적인 걱정이 아니었습니다.** 명령서가 실제로 벌어진 사고를 하나 듭니다.

> For example, in one recent instance problems in connection with the processing of a reverse stock split resulted in **a broker executing trades selling more shares than customers held in their accounts, resulting in a temporary short position.**

왜 이런 일이 생기는지는 숫자로 보면 간단합니다. 10주를 1주로 합치는 병합이라면, 1,000주를 갖고 있던 고객의 잔고는 다음 날 100주가 되어 있어야 합니다. **시스템이 이 조정을 놓치면 화면에는 여전히 1,000주로 보입니다.**{: style="color: #4682B4;"} 그 상태에서 매도가 나가면 실제로 있는 100주보다 900주를 더 파는 셈이 되고, 브로커는 **없는 주식을 넘겨야 하는 처지**{: style="color: #4682B4;"}가 됩니다. 명령서가 지목하는 것이 바로 이 *"주문의 잘못된 조정 또는 입력"*(`incorrect adjustment or entry of orders`)입니다.

정지를 걸면 이런 주문을 정리할 시간이 생깁니다. 명령서가 재개를 9시로 잡은 이유를 이렇게 적습니다.

> resuming trading at 9:00 a.m. also promotes fair and orderly markets and the protection of investors by **allowing time to remove any orders that have not adjusted for the security's new reverse stock split price.**

즉 19시 50분 정지의 목적은 뉴스 전파가 아니라 **조정되지 않은 주문을 걸러낼 시간을 벌어두는 것**{: style="color: #4682B4;"}입니다.

**정지를 아예 못 걸었다는 뜻은 아닙니다.**{: style="color: #4682B4;"} 나스닥은 뉴스 정지 권한을 그대로 갖고 있었고, 19시 50분 정지도 규정 이전에 **전 기간 통틀어 22건**{: style="color: #4682B4;"} 있었습니다. 다만 합병 5건, 상환 3건처럼 성격이 제각각이고 **병합과 엮인 것은 2건뿐**{: style="color: #4682B4;"}이며, 전부 뉴스 사유 코드로 걸린 개별 판단이었습니다.

한 가지 헷갈리기 쉬운 지점이 있습니다. **위의 "새벽 4시"는 정지가 걸리지 않은 종목 이야기입니다.** 정지가 걸린 22건은 나스닥이 풀어줄 때 열렸고, 실제 재개는 07시 05분부터 14시 05분까지 흩어져 있습니다. 04시에 재개된 건은 한 건도 없습니다.

그러니 2023년 규정이 만든 것은 정지 자체가 아닙니다. **드물게, 개별 판단으로 쓰이던 것을 전건에 예외 없이 거는 의무로 바꾼 것**{: style="color: #4682B4;"}입니다. 그 전환은 데이터에도 그대로 찍혀 있습니다.

### 데이터로 보면 규정 시행일이 확연히 드러납니다.

규정이 실제로 작동했다면 시행 시점에 데이터가 꺾여야 합니다. 분기별로 세어봤습니다.

![분기별]({{site.url}}/assets/images/2026-08-02-us-halt-reverse-split/1_quarterly_step.png)<br><br>

**승인 시점에 계단이 하나 있습니다.**{: style="color: #4682B4;"} 승인일(2023년 11월 7일) 직전 365일 동안 19시 50분 정지는 17건이었는데, 직후 365일에는 512건으로 **30.1배**{: style="color: #4682B4;"}가 되었습니다.

같은 기간 19시 50분이 **아닌** 뉴스 정지는 587건에서 376건으로 오히려 36% 줄었습니다. 시장에서 뉴스 정지가 늘어난 게 아니라 **이 슬롯만 폭증한 것**{: style="color: #4682B4;"}입니다.

> 이 네 숫자는 나스닥 상장 종목의 `T1`·`T2`·`T3` 정지를 승인일 앞뒤 365일로 끊어 센 것입니다. 같은 정지가 여러 스냅샷에 잡힌 경우는 (종목·시각·코드)로 한 번만 셌습니다.

**바뀐 것은 건수만이 아닙니다.**{: style="color: #4682B4;"} 재개 시각도 같이 모였습니다. 규정 이전 22건은 09시 00분에 열린 것이 6건(27%)이고 09시 05분까지 넓혀도 41%였습니다. 나머지는 08시 45분, 09시 50분, 14시 05분처럼 제각각이었습니다. 규정 이후 1,619건에서는 **09시 00분이 1,300건(80%), 09시 05분까지 합치면 99%**{: style="color: #4682B4;"}입니다.

즉 19시 50분에 세워 아침에 여는 **형태 자체는 이전에도 있었지만 드물었고 시각도 느슨했습니다.** 규정이 한 일은 그것을 **전건 의무로 굳히고 시각을 한 점으로 모은 것**{: style="color: #4682B4;"}입니다.

## 그런데 주식병합은 왜 급증했나

명령서가 규정을 만든 이유로 든 것은 **병합이 급증했다는 사실**{: style="color: #4682B4;"}입니다.

> Nasdaq has observed that the current market environment has led to **an increase in reverse stock split activity. In 2022, Nasdaq processed 196 reverse stock splits, compared to 35 in 2021 and 98 in 2020.**

그런데 **왜 급증했는지는 "current market environment" 한 마디에서 멈춥니다.**{: style="color: #4682B4;"}

그래서 직접 세어봤습니다. 앞에서 쓴 기업행위 공지 아카이브 3,999건에서 **역분할 공지만 연도별로** 추린 것입니다.

| 연도 | 역분할 공지 | 그해 기업행위 공지 중 비중 |
|---|---:|---:|
| 2019 | 112 | 40% |
| 2020 | 93 | 36% |
| **2021** | **27** | **9%** |
| 2022 | 189 | 38% |
| 2023 | 376 | 49% |
| 2024 | 409 | 65% |
| 2025 | 455 | 63% |
| 2026 (7월까지) | 380 | 70% |

밈주식과 SPAC이 시장을 밀어 올려 1달러 밑으로 내려간 종목이 거의 없었던 **2021년(27건)을 제외하면 꾸준히 증가**{: style="color: #4682B4;"}하고 있습니다. 특히 2026년은 7개월 만에 380건인데, 같은 속도면 연 651건으로 **5년 연속 사상 최고**{: style="color: #4682B4;"}입니다.

### 왜 하필 병합인가

여기에는 병합을 부르는 유인 구조가 있습니다. **나스닥 상장유지 기준에는 최저 매수호가 1달러**{: style="color: #4682B4;"}가 있습니다. 그런데 주가가 오르지 않고 그 선을 넘는 방법은 **주식병합 하나뿐**{: style="color: #4682B4;"}입니다. **다만 이 구조는 왜 하필 병합이라는 수단인지를 설명할 뿐, 왜 늘었는지를 설명하지는 않습니다.**{: style="color: #4682B4;"} 최저 매수호가 1달러 요건은 기존에도 있었고, 2019년에도 지금도 같기 때문입니다. 그사이 바뀐 것은 기준이 아니라 **봐주는 기간**{: style="color: #4682B4;"} 쪽일 뿐입니다. 결과적으로 **왜 늘었는지는 이 글의 데이터로 확인할 수 없습니다.**{: style="color: #4682B4;"} 게다가 승인 명령서도 `"current market environment"` 한 마디에서 멈추고 있으며, 규정 심사에 의견을 낸 쪽에서도 *"어떤 요인이 대부분의 역분할의 이유인지는 추가 연구가 필요하다"*고 적었습니다.

### (참고) 거래소도 이 순환을 알고 있습니다

나스닥은 2025년 1월 이 고리를 끊는 규정을 승인받았습니다.

> **SEC Release, File No. SR-NASDAQ-2024-045, 2025년 1월 17일 승인**<br>
> if a company's security fails to meet the Bid Price Requirement and the company **has effected a reverse stock split over the prior one-year period**, then the company **shall not be eligible for any compliance period** … and the Listing Qualifications Department **shall issue a Delisting Determination**

기존에는 종가 매수호가가 30영업일 연속 1달러를 밑돌면 180일의 유예가 자동으로 붙고, 조건을 채우면 180일이 더, 상장폐지 결정이 나온 뒤에도 심판을 청구하면 180일까지 더 받아 최대 540일을 버틸 수 있었습니다. 그러나 규정 개정으로, **1년 안에 병합을 한 회사가 다시 1달러 밑으로 내려가면 유예기간이 없습니다.**{: style="color: #4682B4;"} 앞에서 본 540일이 0일이 되고 곧바로 상장폐지 결정이 나갑니다. 게다가 원래는 심판을 청구하면 매매정지가 미뤄지는데(*"ordinarily **stays** the suspension"*), 두 번째 유예에 실패한 경우에는 *"a request for a hearing **shall not stay the suspension** of the securities from trading"*, 즉 그대로 진행됩니다.

그러니까 이 글이 다룬 19시 50분 정지는 **더 큰 흐름의 한 조각**입니다. 병합이 구조적으로 늘어나는 시장에서, 거래소는 한쪽으로는 **그 처리 절차를 자동화**(19:50 강제정지)하고 다른 쪽으로는 **병합 자체를 제한**(유예 박탈)하고 있습니다.


## 데이터 뒤에 있는 실제 종목들

집계만으로는 감이 잘 오지 않으니 개별 사례를 꺼내 보겠습니다.

* **Wheeler Real Estate Investment Trust(WHLR)**: 2년 남짓 동안 밤 7시 50분에 **12번** 정지되었습니다. 2024년 5월 16일, 6월 27일, 9월 19일, 11월 18일, 2025년 1월 27일, 3월 26일, 5월 23일… 두 달에 한 번꼴로 주식병합을 반복했습니다. 병합으로 주가를 올려도 다시 떨어지고, 또 병합하는 패턴입니다.
* **SMX(SMX Security Matters)**: 같은 방식으로 9번, **NewGenIvf(NIVF)**: 6번 반복했습니다.
* **Honeywell International(HON)**: 소형주만의 이야기는 아닙니다. 2026년 6월 26일 19시 50분에 정지되어 6월 29일 9시에 재개되었습니다. 사유는 **분사와 1대2 주식병합**{: style="color: #4682B4;"}입니다. 다우존스 산업평균지수 구성 종목도 같은 규정을 똑같이 적용받습니다.

**연도별 추이를 보면 이 관행이 어떻게 자리 잡았는지 보입니다.**

![연도별]({{site.url}}/assets/images/2026-08-02-us-halt-reverse-split/3_annual_reverse_split.png)<br><br>

2023년 61건에서 2024년 396건으로 뛴 뒤, 2025년 422건, 2026년은 7월까지만으로 이미 351건입니다. 규정이 생기기 전인 2021~2022년에는 사실상 없었습니다.

## 이번 편에서 확인한 것

밤 7시 50분의 정체는 **주식병합**이었습니다. 그리고 그 시각은 우연이 아니라 **SEC가 승인한 규정에 적힌 숫자**{: style="color: #4682B4;"}였습니다.

첫째, **거래소에 재량이 없습니다.**{: style="color: #4682B4;"} 주식병합이 예정되어 있으면 사람이 판단할 것 없이 자동으로 걸립니다. 승인 명령서가 "Nasdaq will not have the discretion"이라고 명시했습니다. 재량이 없으면 판단이 일관되지 않을 문제도, 늦었다는 책임 문제도 생기지 않습니다.

둘째, **규정은 "대략"이라고 했는데 운영은 초를 맞췄습니다.**{: style="color: #4682B4;"} 승인 명령서도 나스닥이 회사에 내주는 서식도 `approximately 7:50 p.m.`이라고 적어 재량을 조금 열어 두었지만, 1년치 537건은 초 단위까지 전부 `19:50:00`이었고 그중 525건은 재개까지 `09:00:00` 정각이었습니다.

셋째, **드물게 쓰이던 형태를 전건 의무로 굳혔습니다.**{: style="color: #4682B4;"} 19시 50분에 세워 아침에 여는 형태는 규정 이전에도 있었지만 **전 기간 통틀어 22건**{: style="color: #4682B4;"}이었고, 그나마 병합과 엮인 것은 2건뿐이었습니다. 병합을 앞두고 미리 세우는 조항이 없어서 기본 처리는 정지 없이 새벽 4시에 반영가로 여는 것이었기 때문입니다. 규정이 생긴 뒤 **1,619건**{: style="color: #4682B4;"}이 되었고, 재개 시각이 09시 00분 근처로 모인 비율도 41%에서 **99%**{: style="color: #4682B4;"}가 되었습니다.

그런데 아직 설명하지 않은 것이 남아 있습니다. 1편에서 본 나스닥 뉴스 정지 920건 중 19시 50분은 537건이었습니다. **나머지 383건**{: style="color: #4682B4;"}은 주식병합이 아닙니다. 그 383건도 06시 55분, 07시 55분처럼 정각에 몰려 있었습니다.

이쪽은 진짜 뉴스 정지입니다. 회사가 인수합병이나 임상 결과를 발표하기 직전에 걸리는 것입니다. 그런데 **진짜 뉴스인데도 시각이 시계에 맞춰져 있습니다.**{: style="color: #4682B4;"} 다음 편에서 이 383건이 각각 무슨 발표였는지, 그리고 왜 06시 55분인지를 보겠습니다.

## 참고: NYSE도 밤 7시 50분에 멈춥니다

밤 7시 50분에 일괄로 세우는 것이 나스닥만의 처리 방식인지, 아니면 미국 시장이 공유하는 설계인지 궁금할 수 있습니다. **NYSE에도 같은 조항이 있습니다.**{: style="color: #4682B4;"} 나스닥보다 다섯 달 늦게 들어왔습니다.

> **SEC Release No. 34-99974 (File No. SR-NYSE-2024-22), 2024년 4월 11일 제출·즉시 효력**<br>
> In general, the Exchange expects to **initiate the halt at 7:50 p.m.**, prior to the end of post-market trading on other markets at 8:00 p.m. … trading in the security will **resume with a Trading Halt Auction starting at 9:30 a.m.**

[***(NYSE Rule 123D(f) 원문(링크))***](https://public-inspection.federalregister.gov/2024-08569.pdf)

| 구분 | 나스닥 | NYSE |
|---|---|---|
| 규정 조항 | Rule 4120(a)(14) → 현행 (a)(15) | Rule 123D(f) |
| 시행 | 2023년 11월 7일 승인 | 2024년 4월 11일 제출, 즉시 효력 |
| 정지 시각 | **19:50** | **19:50 (동일)** |
| 재개 방식 | 09:00 Halt Cross | 09:30 Trading Halt Auction |
| 재량 | 없음(의무) | 없음(의무) |

정지 시각이 분 단위로 같습니다. 그런데 **두 거래소가 그 시각을 고른 이유는 조금 다릅니다.**{: style="color: #4682B4;"} 나스닥은 자기 애프터마켓이 8시에 닫히기 때문이고, NYSE는 자기에게 애프터마켓이 없으니 **"다른 시장의(on other markets)"**{: style="color: #4682B4;"} 시간외 거래가 8시에 끝나기 때문입니다. 결국 조건은 하나입니다. **밤 8시 이후에는 병합 전 주식 수로 체결되는 거래가 미국 어디에도 남아 있으면 안 된다**{: style="color: #4682B4;"}는 것입니다.

재개 시각이 갈리는 이유도 규정에 나옵니다. 나스닥은 프리마켓이 있으니 정규장 개장 30분 전인 9시에 열고, NYSE는 개장 전 세션이 없으니 정규장이 시작되는 9시 30분 단일가매매로 엽니다. **같은 문제를 각자의 하루 길이에 맞춰 푼 것**{: style="color: #4682B4;"}입니다.

병합 자체를 제한하는 쪽도 비슷한 시기입니다. 나스닥이 유예를 박탈한 2025년 1월, NYSE도 Section 802.01C를 고쳐 병합 사용을 제한했습니다.


**[관련 포스팅]** [나스닥 거래정지의 절반이 밤 7시 50분에 걸립니다]({{site.url}}/미국시장/us-halt-session/)<br>
{:.notice--success}
