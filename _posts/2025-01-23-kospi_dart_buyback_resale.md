---
layout: single
title:  "10년간 코스피 자사주 직접 '처분' 현황(시사점)"
categories: 한국시장
tag: [python, opendart, insight, 자기주식]
toc: true
author_profile: false
---

<head>
  <style>
    table.dataframe {
      white-space: normal;
      width: 300%;
      max-width: 600%;
      height: 300px;  /* 고정 높이 유지 */
      display: inline-block;
      overflow-x: scroll;  /* 가로 스크롤 */
      overflow-y: scroll;  /* 세로 스크롤 */
      font-family: Arial, sans-serif;
      font-size: 0.9rem;
      line-height: 20px;
      text-align: center;
      border: 0px !important;
    }

    table.dataframe th {
      text-align: center;
      font-weight: bold;
      padding: 8px;
    }

    table.dataframe td {
      text-align: center;
      padding: 8px;
    }

    table.dataframe tr:hover {
      background: #b8d1f3; 
    }

    .output_prompt {
      overflow: auto;
      font-size: 0.9rem;
      line-height: 1.45;
      border-radius: 0.3rem;
      -webkit-overflow-scrolling: touch;
      padding: 0.8rem;
      margin-top: 0;
      margin-bottom: 15px;
      font: 1rem Consolas, "Liberation Mono", Menlo, Courier, monospace;
      color: $code-text-color;
      border: solid 1px $border-color;
      border-radius: 0.3rem;
      word-break: normal;
      white-space: pre;
    }

  .dataframe tbody tr th:only-of-type {
      vertical-align: middle;
  }

  .dataframe tbody tr th {
      vertical-align: top;
  }

  .dataframe thead th {
      text-align: center !important;
      padding: 8px;
  }

  .page__content p {
      margin: 0 0 0px !important;
  }

  .page__content p > strong {
    font-size: 1.0rem !important;
  }

  .notice--success a {
  font-size: 1.2rem !important; 
  }

  .notice--info a {
  font-size: 1.2rem !important; 
  }

  </style>
</head>


## 데이터 수집 및 시각화 방향


**1. OpenDART를 통해 자기주식 관련 금감원 공시 내용 수집하기**{: style="color: #4682B4;"}

전체 자사주 **"직접"**{: style="color: #4682B4;"} 처분하기로 **결정한**{: style="color: #4682B4;"} 수량의 추이를 확인



**2. 금감원 공시에서 자사주 처분방법을 구분하기**{: style="color: #4682B4;"}

장내 수량이 얼마나 많을까? 다른 처분방법별 특징은 어떻게 될까?


## 금감원 공시를 통해 자사주 **직접 처분**{: style="color: #4682B4;"} 통계 불러오기
이 데이터는 주요사항보고서(자사주처분) 공시기준 데이터이기 때문에, 실제 처분수량과는 차이가 있습니다.<br>



#### 검색기준 설정하기

검색 기준은 "유가", "2015~2024"년으로 하였습니다. 참고로 **OpenDart는 2015년부터 데이터를 제공**{: style="color: #4682B4;"}합니다.<br>


#### 총 1,007건 확인

위의 검색기준으로 조회한 결과, 코스피 상장사들이 자사주를 직접처분한다고 제출한 공시건수는 총 1,007건이 있었습니다.<br>

#### 수집된 데이터프레임 형태 확인

데이터프레임이 어떤 형태인지 한번 확인해 보겠습니다.


<pre>
<table border="1" class="dataframe dataframe">
  <thead>
    <tr>
      <th>회사명</th>
      <th>접수일</th>
      <th colspan="2" halign="left">처분예정주식(주)</th>
      <th colspan="2" halign="left">처분 대상 주식가격(원)</th>
      <th colspan="2" halign="left">처분예정금액(원)</th>
      <th colspan="2" halign="left">처분예정기간</th>
      <th>처분목적</th>
      <th colspan="4" halign="left">처분방법</th>
      <th>위탁투자중개업자</th>
      <th colspan="8" halign="left">처분 전 자기주식 보유현황</th>
      <th>처분결정일</th>
      <th colspan="2" halign="left">사외이사참석여부</th>
      <th>감사 (사외이사가 아닌 감사위원) 참석여부</th>
      <th colspan="2" halign="left">1일 매도 주문수량 한도</th>
      <th>비고</th>
    </tr>
    <tr>
      <th>회사명</th>
      <th>접수일</th>
      <th colspan="2" halign="left">처분예정주식(주)</th>
      <th colspan="2" halign="left">처분 대상 주식가격(원)</th>
      <th colspan="2" halign="left">처분예정금액(원)</th>
      <th colspan="2" halign="left">처분예정기간</th>
      <th>처분목적</th>
      <th>시장을 통한 매도(주)</th>
      <th>시간외대량매매(주)</th>
      <th>장외처분(주)</th>
      <th>기타(주)</th>
      <th>위탁투자중개업자</th>
      <th colspan="4" halign="left">배당가능이익 범위 내 취득(주)</th>
      <th colspan="4" halign="left">기타취득(주)</th>
      <th>처분결정일</th>
      <th colspan="2" halign="left">사외이사참석여부</th>
      <th>감사 (사외이사가 아닌 감사위원) 참석여부</th>
      <th colspan="2" halign="left">1일 매도 주문수량 한도</th>
      <th>비고</th>
    </tr>
    <tr>
      <th>회사명</th>
      <th>접수일</th>
      <th>보통주식</th>
      <th>기타주식</th>
      <th>보통주식</th>
      <th>기타주식</th>
      <th>보통주식</th>
      <th>기타주식</th>
      <th>시작일</th>
      <th>종료일</th>
      <th>처분목적</th>
      <th>시장을 통한 매도(주)</th>
      <th>시간외대량매매(주)</th>
      <th>장외처분(주)</th>
      <th>기타(주)</th>
      <th>위탁투자중개업자</th>
      <th>보통주식</th>
      <th>비율(%)</th>
      <th>기타주식</th>
      <th>비율(%).1</th>
      <th>보통주식</th>
      <th>비율(%)</th>
      <th>기타주식</th>
      <th>비율(%).1</th>
      <th>처분결정일</th>
      <th>참석(명)</th>
      <th>불참(명)</th>
      <th>감사 (사외이사가 아닌 감사위원) 참석여부</th>
      <th>보통주식</th>
      <th>기타주식</th>
      <th>비고</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>유AJ네트웍스</td>
      <td>2023-06-20</td>
      <td>484943</td>
      <td>-</td>
      <td>4720</td>
      <td>-</td>
      <td>2288930960</td>
      <td>-</td>
      <td>2023년 05월 15일</td>
      <td>2023년 08월 14일</td>
      <td>직원에 대한 상여금 지급</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>484943</td>
      <td>한국투자증권(주)</td>
      <td>1586257</td>
      <td>3.4</td>
      <td>-</td>
      <td>-</td>
      <td>468222</td>
      <td>1.0</td>
      <td>-</td>
      <td>-</td>
      <td>2023년 05월 12일</td>
      <td>2</td>
      <td>0</td>
      <td>참석</td>
      <td>-</td>
      <td>-</td>
      <td>2023년 06월 20일 최종보고서</td>
    </tr>
    <tr>
      <td>유AK홀딩스</td>
      <td>2018-04-12</td>
      <td>150000</td>
      <td>-</td>
      <td>37491</td>
      <td>-</td>
      <td>5623650000</td>
      <td>-</td>
      <td>2018년 04월 23일</td>
      <td>2018년 04월 23일</td>
      <td>우리사주조합원에 대한 회사이익공유 및 근로의욕 고취를 위하여 우리사주조합에 유상 매각</td>
      <td>-</td>
      <td>-</td>
      <td>150000</td>
      <td>-</td>
      <td>없음.</td>
      <td>198777</td>
      <td>1.5</td>
      <td>-</td>
      <td>-</td>
      <td>153289</td>
      <td>1.2</td>
      <td>-</td>
      <td>-</td>
      <td>2018년 03월 23일</td>
      <td>3</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>2018년 04월 12일 최종보고서</td>
    </tr>
    <tr>
      <td>유BNK금융지주</td>
      <td>2020-02-06</td>
      <td>14855</td>
      <td>-</td>
      <td>6940</td>
      <td>-</td>
      <td>103093700</td>
      <td>-</td>
      <td>2020년 02월 07일</td>
      <td>2020년 05월 06일</td>
      <td>(주)경남은행과 주식교환에 따라 취득한 자기주식 처분</td>
      <td>14855</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>한국투자증권 (Korea Investment & Securities Co.,Ltd)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>14855</td>
      <td>0.00</td>
      <td>-</td>
      <td>-</td>
      <td>2020년 02월 06일</td>
      <td>7</td>
      <td>0</td>
      <td>-</td>
      <td>183764</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>유CJ</td>
      <td>2019-12-09</td>
      <td>1140809</td>
      <td>-</td>
      <td>121450</td>
      <td>-</td>
      <td>138551253050</td>
      <td>-</td>
      <td>2019년 12월 27일</td>
      <td>2019년 12월 27일</td>
      <td>씨제이올리브네트웍스(주)와 주식의포괄적 교환을 통하여 씨제이올리브네트웍스(주)를 씨제이(주)의 완전자회사(주식100% 취득)로 편입하기 위함. 상법 제360조의2에 의거 주식의 포괄적 교환의 대가로 신주 발행에 갈음하여 씨제이(주)의 자기주식을 교부할 예정임.</td>
      <td>-</td>
      <td>-</td>
      <td>1140809</td>
      <td>-</td>
      <td>-</td>
      <td>1421770</td>
      <td>4.0</td>
      <td>-</td>
      <td>-</td>
      <td>1837575</td>
      <td>5.2</td>
      <td>14252</td>
      <td>-</td>
      <td>2019년 04월 29일</td>
      <td>4</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>2019년 12월 09일 최종보고서</td>
    </tr>
    <tr>
      <td>유CJ대한통운</td>
      <td>2015-10-02</td>
      <td>202338</td>
      <td>-</td>
      <td>196513</td>
      <td>-</td>
      <td>39762047394</td>
      <td>-</td>
      <td>2015년 12월 16일</td>
      <td>2015년 12월 16일</td>
      <td>한국복합물류(주)와 주식교환방식에 의하여 한국복합물류(주)를 완전자회사(주식100% 취득)로 편입할 예정이며, 상법 제360조의6에 의거 주식교환의 대가로 신주발행에 갈음하여 씨제이대한통운(주)의 자기주식을 교부할 예정임</td>
      <td>-</td>
      <td>-</td>
      <td>202338</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>5390620</td>
      <td>23.6</td>
      <td>-</td>
      <td>-</td>
      <td>2015년 10월 02일</td>
      <td>4</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
  </tbody>
</table>
</pre>

확인해보니 칼럼이 3층으로 되어 있습니다. 이런 경우 분석을 하기 번거로워지는 점이 있으니, 칼럼을 1층으로 포개 주도록 하겠습니다.

3층을 1층으로 포갤때 칼럼명이 어떻게 되는지를 먼저 확인하고, 중복된 내용은 없애서는 방식으로 칼럼명을 수정하도록 하겠습니다.


#### '취득'공시와 '처분'공시 다른점
매매방식을 기재하는 방식에서 취득공시와 다른 점이 있습니다.

* 자사주취득공시 : 처분방식을 ***하나의 칸에 free text로 기재***{: style="color: #4682B4;"}합니다.

* 자사주처분공시 : 처분방식을 ***시장, 시간외대량, 장외, 기타로 구분***{: style="color: #4682B4;"}을 하였고, 각각의 방식으로 처분할 수량을 기재하도록 하였습니다.



<br>

취득공시보다 처분공시에서 데이터 활용성이 높아졌습니다!


#### 데이터프레임 전처리



데이터프레임에 몇가지의 조치를 더 취합니다.
<br><br>

 **1) 분석에 필요한 칼럼만 남깁니다.**<br>

물론 우선주에 대한 자기주식 처분도 있지만, 우선주가 상장되지 않은 경우가 더 많기 때문에, 보통주에 관한 것으로 한정합니다.
<br><br>

 **2) 단위를 조정합니다.**<br>

칼럼이 현재는 일괄로 str타입으로 되어있습니다. 따라서 분석을 위해 날짜, 숫자 형태 등으로 변경합니다. 또한 주단위(주 → 백만주), 원단위(원 → 억원)를 변환합니다.
<br><br>

 **3) 회사명을 조정합니다.**<br>

OpenDart API가 아닌 웹페이지에서 크롤링해오다보니, 회사명에 다음과 같은 수식어들이 붙어있습니다. 이러한 수식어들을 제거하는 절차를 수행합니다. <br>
참고로 OpenDart API를 통해 데이터를 수집하는 경우, 이런 구분자가 불필요하게 붙지 않고, 종목코드가 딸려오기 때문에 더 정확하게 회사를 식별할 수 있는 장점이 있습니다.<br>

  * 시장구분자(***유, 코, 넥, 기***)가 회사명의 앞부분에 있습니다.

  * IR홈페이지가 있는 경우, 회사명 뒷부분에 ***'IR'***이 붙어있습니다.



#### 전처리한 데이터프레임 확인



<pre>
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>회사명</th>
      <th>접수일</th>
      <th>처분예정주식</th>
      <th>처분예정금액</th>
      <th>처분시작일</th>
      <th>처분종료일</th>
      <th>처분목적</th>
      <th>장내매매</th>
      <th>시간외대량매매</th>
      <th>장외매매</th>
      <th>기타</th>
      <th>연도</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AJ네트웍스</td>
      <td>2023-06-20</td>
      <td>484943.0</td>
      <td>22.889310</td>
      <td>2023년 05월 15일</td>
      <td>2023년 08월 14일</td>
      <td>직원에 대한 상여금 지급</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>484943</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>AK홀딩스</td>
      <td>2018-04-12</td>
      <td>150000.0</td>
      <td>56.236500</td>
      <td>2018년 04월 23일</td>
      <td>2018년 04월 23일</td>
      <td>우리사주조합원에 대한 회사이익공유 및 근로의욕 고취를 위하여 우리사주조합에 유상 매각</td>
      <td>-</td>
      <td>-</td>
      <td>150000</td>
      <td>-</td>
      <td>2018</td>
    </tr>
    <tr>
      <td>BNK금융지주</td>
      <td>2020-02-06</td>
      <td>14855.0</td>
      <td>1.030937</td>
      <td>2020년 02월 07일</td>
      <td>2020년 05월 06일</td>
      <td>(주)경남은행과 주식교환에 따라 취득한 자기주식 처분</td>
      <td>14855</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>CJ</td>
      <td>2019-12-09</td>
      <td>1140809.0</td>
      <td>1385.512530</td>
      <td>2019년 12월 27일</td>
      <td>2019년 12월 27일</td>
      <td>씨제이올리브네트웍스(주)와 주식의포괄적 교환을 통하여 씨제이올리브네트웍스(주)를 씨제이(주)의 완전자회사(주식100% 취득)로 편입하기 위함. 상법 제360조의2에 의거 주식의 포괄적 교환의 대가로 신주 발행에 갈음하여 씨제이(주)의 자기주식을 교부할 예정임.</td>
      <td>-</td>
      <td>-</td>
      <td>1140809</td>
      <td>-</td>
      <td>2019</td>
    </tr>
    <tr>
      <td>CJ대한통운</td>
      <td>2015-10-02</td>
      <td>202338.0</td>
      <td>397.620474</td>
      <td>2015년 12월 16일</td>
      <td>2015년 12월 16일</td>
      <td>한국복합물류(주)와 주식교환방식에 의하여 한국복합물류(주)를 완전자회사(주식100% 취득)로 편입할 예정이며, 상법 제360조의6에 의거 주식교환의 대가로 신주발행에 갈음하여 씨제이대한통운(주)의 자기주식을 교부할 예정임</td>
      <td>-</td>
      <td>-</td>
      <td>202338</td>
      <td>-</td>
      <td>2015</td>
    </tr>
  </tbody>
</table>
</pre>


### 자사주 직접처분 데이터 시각화


![resaleall]({{site.url}}/assets/images/2025-01-23-buyback-resaleinsight/resaleall.png)<br><br>



표 형태로 숫자를 보면 아래와 같습니다. (주식수는 백만주단위, 금액은 억원 단위입니다.)



<pre>
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>연도</th>
      <th>처분예정주식</th>
      <th>처분예정금액</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2015</td>
      <td>38</td>
      <td>20,064</td>
    </tr>
    <tr>
      <td>2016</td>
      <td>56</td>
      <td>13,843</td>
    </tr>
    <tr>
      <td>2017</td>
      <td>71</td>
      <td>19,165</td>
    </tr>
    <tr>
      <td>2018</td>
      <td>64</td>
      <td>15,890</td>
    </tr>
    <tr>
      <td>2019</td>
      <td>49</td>
      <td>7,946</td>
    </tr>
    <tr>
      <td>2020</td>
      <td>87</td>
      <td>28,746</td>
    </tr>
    <tr>
      <td>2021</td>
      <td>49</td>
      <td>41,963</td>
    </tr>
    <tr>
      <td>2022</td>
      <td>63</td>
      <td>41,669</td>
    </tr>
    <tr>
      <td>2023</td>
      <td>56</td>
      <td>48,976</td>
    </tr>
    <tr>
      <td>2024</td>
      <td>67</td>
      <td>23,924</td>
    </tr>
  </tbody>
</table>
</pre>

#### 자사주 직접처분 vs 취득 비교

아래 그림은 지난 포스팅에서 확인한 자사주 '직접 취득'에 대한 그림입니다. 취득주식수(bar차트)와 처분주식수(bar차트)에서는 뚜렷이 나타나진 않지만, 취득금액(line차트)와 처분금액(line차트)에서는 일부는 반대추세가 보이기도 합니다. <br>
![all_buyback]({{site.url}}/assets/images/2025-01-22-buybackinsight/all_buyback.png)<br><br>

참고로 KOSPI지수를 볼까요. 코로나 이전보다 이후 시기에 주가의 수준이 전반적으로 높기는 합니다. 영향이 있긴 했겠지만 주가 때문에 자사주 처분이 늘어났다고 단언할 수는 없을 것 같습니다. 처분의 방법별 비중이 어떻게 되는지 보면서 추가로 살펴보겠습니다.
![kospichart]({{site.url}}/assets/images/2025-01-23-buyback-resaleinsight/kospichart.png)<br><br>


### 처분방법별 주식수를 통해 분석하기

앞서말씀드렸다시피, 자사주처분공시에서는 '처분방법'을 방법별 주식수로 기재하고 있습니다. 이렇게 장내, 장외를 미리 구분해주었으므로, 이를 바탕으로 붙석을 진행합니다.
<br>
표 형태로 숫자를 보면 아래와 같습니다.


<pre>
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>연도</th>
      <th>장내매매</th>
      <th>시간외대량매매</th>
      <th>장외매매</th>
      <th>기타</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2015</td>
      <td>1,666,192</td>
      <td>16,530,938</td>
      <td>7,844,437</td>
      <td>15,744,490</td>
    </tr>
    <tr>
      <td>2016</td>
      <td>2,419,163</td>
      <td>25,968,389</td>
      <td>18,675,063</td>
      <td>9,884,586</td>
    </tr>
    <tr>
      <td>2017</td>
      <td>2,326,848</td>
      <td>54,013,232</td>
      <td>7,990,151</td>
      <td>7,754,133</td>
    </tr>
    <tr>
      <td>2018</td>
      <td>40,406</td>
      <td>34,524,186</td>
      <td>7,851,419</td>
      <td>22,012,265</td>
    </tr>
    <tr>
      <td>2019</td>
      <td>1,284,314</td>
      <td>19,285,874</td>
      <td>21,949,696</td>
      <td>7,368,980</td>
    </tr>
    <tr>
      <td>2020</td>
      <td>564,590</td>
      <td>45,215,194</td>
      <td>25,351,606</td>
      <td>16,336,791</td>
    </tr>
    <tr>
      <td>2021</td>
      <td>126,896</td>
      <td>16,399,457</td>
      <td>12,301,222</td>
      <td>5,590,723,510</td>
    </tr>
    <tr>
      <td>2022</td>
      <td>33,378</td>
      <td>21,480,163</td>
      <td>31,977,601</td>
      <td>10,051,889</td>
    </tr>
    <tr>
      <td>2023</td>
      <td>1,137,914</td>
      <td>8,749,493</td>
      <td>6,362,146</td>
      <td>851,245,528</td>
    </tr>
    <tr>
      <td>2024</td>
      <td>24,167</td>
      <td>22,883,456</td>
      <td>19,154,271</td>
      <td>25,807,749</td>
    </tr>
  </tbody>
</table>
</pre>


###### 처분방법별 자사주 처분 시각화


###### 공시에서 발견된 오타들!

시각화를 해서 보던 중, 아래와 같은 그림이 그려졌습니다.

![kakaoerror]({{site.url}}/assets/images/2025-01-23-buyback-resaleinsight/kakaoerror.png)<br><br>


원래는 앞서 그려보았던 바차트와 동일한 그림이 나오고, 바차트 안에서만 색깔이 나뉘어야 합니다. <br>

그런데 이렇게 바차트의 형태 자체가 달라져버렸습니다. **2021년의 기타처분 수량이 비정상적으로 높은 수치를 나타내고 있습니다.**{: style="color: #4682B4;"} 왜일까요? <br><br>

> 원래 알던 것과 다르다면, 데이터의 출처가 달라지진 않았는지 한번 확인해 보아야 합니다.





<br>

기존에 그렸던 차트는 ***"처분예정주식수"***{: style="color: #4682B4;"}
에서 가져온 데이터였고, 이번에 그린차트는 ***"처분방법별 처분주식수"***{: style="color: #4682B4;"}
에서 가져온 데이터였습니다.<br>



추정컨대, 처분방법별 처분주식수를 기재하는 가정에서 오타가 났을 가능성이 있습니다.<br><br>



따라서 아래와 같이 필터를 적용해서 데이터를 직접 확인해보겠습니다. 2021년 데이터 중, 처분방법이 기타인 것을 기준으로 내림차순으로 정리해 봅니다.



<pre>
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>회사명</th>
      <th>접수일</th>
      <th>처분예정주식</th>
      <th>처분예정금액</th>
      <th>처분시작일</th>
      <th>처분종료일</th>
      <th>처분목적</th>
      <th>장내매매</th>
      <th>시간외대량매매</th>
      <th>장외매매</th>
      <th>기타</th>
      <th>연도</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>카카오</td>
      <td>2021-11-03</td>
      <td>43512.0</td>
      <td>55.695360</td>
      <td>2021년 11월 04일</td>
      <td>2022년 01월 03일</td>
      <td>임직원에 대한 상여금 지급</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5,569,536,000</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>한국가스공사</td>
      <td>2021-11-12</td>
      <td>6486050.0</td>
      <td>3353.287850</td>
      <td>2021년 11월 16일</td>
      <td>2021년 11월 16일</td>
      <td>자기주식을 교환대상으로 하는 (사모후순위) 교환사채의 발행</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6,486,050</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>POSCO홀딩스</td>
      <td>2021-08-26</td>
      <td>2932480.0</td>
      <td>14499.650880</td>
      <td>2021년 09월 01일</td>
      <td>2021년 09월 01일</td>
      <td>자기주식을 교환대상으로 하는 교환사채 발행에 따른 처분</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2,932,480</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>남성</td>
      <td>2021-07-21</td>
      <td>2438429.0</td>
      <td>100.000000</td>
      <td>2021년 07월 23일</td>
      <td>2021년 07월 23일</td>
      <td>자기주식을 교환대상으로 하는 사모 교환사채의 발행으로 인한 자기주식 처분</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2,438,429</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>화신</td>
      <td>2021-10-13</td>
      <td>1995600.0</td>
      <td>232.128192</td>
      <td>2021년 10월 15일</td>
      <td>2021년 10월 15일</td>
      <td>자기주식을 교환대상으로 하는 교환사채 발행</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1,995,600</td>
      <td>2021</td>
    </tr>
  </tbody>
</table>
</pre>


**2021년 11월 3일에 최종 제출된 카카오의 자기주식처분공시에서 기타처분 주식수가 엄청나게 큰 것을 확인할 수 있습니다.**{: style="color: #4682B4;"} 55로 시작하는 걸 보니... 처분예정금액(55억원)을 실수로 기재한 것이 아닌가 추론해 볼수 있습니다.
<br>

공시에서 기재한 총 처분주식수가 43,512주이고, 장내,시간외,장외가 모두 0주였으므로 기타도 43,512주여야함을 알 수 있습니다. 그렇게 수정하도록 하겠습니다.



<pre>
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>회사명</th>
      <th>접수일</th>
      <th>처분예정주식</th>
      <th>처분예정금액</th>
      <th>처분시작일</th>
      <th>처분종료일</th>
      <th>처분목적</th>
      <th>장내매매</th>
      <th>시간외대량매매</th>
      <th>장외매매</th>
      <th>기타</th>
      <th>연도</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>카카오</td>
      <td>2021-11-03</td>
      <td>43512.0</td>
      <td>55.69536</td>
      <td>2021년 11월 04일</td>
      <td>2022년 01월 03일</td>
      <td>임직원에 대한 상여금 지급</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>43512.0</td>
      <td>2021</td>
    </tr>
  </tbody>
</table>
</pre>

잘 반영된 것 같으니, 이제 다시 시각화를 실행해 보겠습니다.<br>
![tperror]({{site.url}}/assets/images/2025-01-23-buyback-resaleinsight/tperror.png)<br><br>


이번엔 2023년의 기타처분 주식수가 말썽입니다. 이전과 동일하게 필터를 해서 어떤 회사가 공시에서 오타를 내었는지 확인해 봅니다.




<pre>
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>회사명</th>
      <th>접수일</th>
      <th>처분예정주식</th>
      <th>처분예정금액</th>
      <th>처분시작일</th>
      <th>처분종료일</th>
      <th>처분목적</th>
      <th>장내매매</th>
      <th>시간외대량매매</th>
      <th>장외매매</th>
      <th>기타</th>
      <th>연도</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>TP</td>
      <td>2023-04-21</td>
      <td>493460.0</td>
      <td>8.112482</td>
      <td>2023년 04월 20일</td>
      <td>2023년 04월 28일</td>
      <td>자기주식 상여지급</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>811,248,240</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>SK하이닉스</td>
      <td>2023-04-04</td>
      <td>20126911.0</td>
      <td>22377.100000</td>
      <td>2023년 04월 11일</td>
      <td>2023년 04월 11일</td>
      <td>자기주식을 교환대상으로 하는 교환사채 발행에 따른 처분</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>20,126,911</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>LS네트웍스</td>
      <td>2023-09-22</td>
      <td>5320054.0</td>
      <td>256.799007</td>
      <td>2023년 09월 22일</td>
      <td>2023년 09월 22일</td>
      <td>자기주식을 교환대상으로 하는 교환사채 발행</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5,320,054</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>SK이노베이션</td>
      <td>2023-02-06</td>
      <td>2799970.0</td>
      <td>4815.948400</td>
      <td>2023년 03월 31일</td>
      <td>2023년 04월 30일</td>
      <td>기말 배당</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2,799,970</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>아이마켓코리아</td>
      <td>2023-05-10</td>
      <td>1964500.0</td>
      <td>232.695025</td>
      <td>2023년 05월 12일</td>
      <td>2023년 05월 12일</td>
      <td>자기주식을 교환대상으로 하는 교환사채 발행</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1,964,500</td>
      <td>2023</td>
    </tr>
  </tbody>
</table>
</pre>


**2023년 4월 21일에 최종 제출된 TP의 자기주식처분공시에서 기타처분 주식수가 엄청나게 큰 것을 확인할 수 있습니다.**{: style="color: #4682B4;"} 811로 시작하는 걸 보니... 처분예정금액(8.11억원)을 실수로 기재한 것이 아닌가 추론해 볼수 있습니다. 카카오와 비슷한 실수네요.
<br>

공시에서 기재한 총 처분주식수가 493,460주이고, 장내,시간외,장외가 모두 0주였으므로 기타도 493,460주여야함을 알 수 있습니다. 그렇게 수정하도록 하겠습니다.




<pre>
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>회사명</th>
      <th>접수일</th>
      <th>처분예정주식</th>
      <th>처분예정금액</th>
      <th>처분시작일</th>
      <th>처분종료일</th>
      <th>처분목적</th>
      <th>장내매매</th>
      <th>시간외대량매매</th>
      <th>장외매매</th>
      <th>기타</th>
      <th>연도</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>TP</td>
      <td>2023-04-21</td>
      <td>493460.0</td>
      <td>8.112482</td>
      <td>2023년 04월 20일</td>
      <td>2023년 04월 28일</td>
      <td>자기주식 상여지급</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>493460.0</td>
      <td>2023</td>
    </tr>
  </tbody>
</table>
</pre>


잘 반영된 것 같으니, 이제 다시 시각화를 실행해 보겠습니다.<br>

###### 다시! 처분방법별 자사주 처분 시각화

이제 시각화를 실행해 봅니다.


![resalebymethod]({{site.url}}/assets/images/2025-01-23-buyback-resaleinsight/resalebymethod.png)<br><br>

오! 이전에 그렸던 그림과 비교하니 이제 맞는 바차트가 나왔습니다. 데이터레이블을 추가해 보겠습니다.



![resalebymethod_label]({{site.url}}/assets/images/2025-01-23-buyback-resaleinsight/resalebymethod_label.png)<br><br>



##### 자사주 처분 시사점

* **장매처분 물량**{: style="color: #4682B4;"}<br>
장내에서 자사주를 처분하는 수량은 정말 낮았습니다. 아무래도 시장에 자사주 물량을 풀게 되면, 자사의 주가가 낮아지는 압력을 받을텐데, 쉽지 않은 결정일 것이라는 생각은 들었습니다. 그런 생각이 들었는데, 실제로 수치로 확인하게 되니 신기하기도 합니다.<br>

* **연도별 처분방법 편차**{: style="color: #4682B4;"}<br>
앞서 취득금액 추이와 처분금액 추이를 잠깐 비교했습니다. 연도별로 처분금액의 증감에 영향을 미칠 요소가 무엇이 있을지.. 우선 시장 전체 주가 수준을 생각해보았고, 어느정도 영향은 있을 수 있겠지만 단언하기는 힘든 것으로 보였습니다.<br> 
그러던 중 추가 분석을 통해 처분방법이 연도별로 비중이 다른 것을 보았습니다. 2021년에는 기타, 2022년에는 장외매매, 2023,4년엔 기타였습니다. 각각의 방법들을 좀 더 들여다볼 필요가 있어보입니다. 단순히 주가만이 아니라 기업의 여러 경영상황이 영향을 미쳤음을 유추해 볼수 있습니다.  

* **기타처분은 무엇일까?**{: style="color: #4682B4;"}<br>
주식수 비중 기준으로 기타 처분방식은 꾸준히 상위권이었습니다. 통상 거래상대방이 정해져있는 장외매매와 시간외대량매매를 제외한 **'기타' 처분 방법은 어떤 예시가 있을까요?**{: style="color: #4682B4;"} 한번 확인해보겠습니다.


<pre>
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>회사명</th>
      <th>접수일</th>
      <th>처분예정주식</th>
      <th>처분예정금액</th>
      <th>처분시작일</th>
      <th>처분종료일</th>
      <th>처분목적</th>
      <th>장내매매</th>
      <th>시간외대량매매</th>
      <th>장외매매</th>
      <th>기타</th>
      <th>연도</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>SK하이닉스</td>
      <td>2023-04-04</td>
      <td>20126911.0</td>
      <td>22377.100000</td>
      <td>2023년 04월 11일</td>
      <td>2023년 04월 11일</td>
      <td>자기주식을 교환대상으로 하는 교환사채 발행에 따른 처분</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>20,126,911</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>한국가스공사</td>
      <td>2021-11-12</td>
      <td>6486050.0</td>
      <td>3353.287850</td>
      <td>2021년 11월 16일</td>
      <td>2021년 11월 16일</td>
      <td>자기주식을 교환대상으로 하는 (사모후순위) 교환사채의 발행</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>6,486,050</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>대한전선</td>
      <td>2018-10-11</td>
      <td>6000000.0</td>
      <td>30.000000</td>
      <td>2018년 11월 05일</td>
      <td>2025년 11월 05일</td>
      <td>임직원 주식매수선택권 행사에 따른 자기주식 교부</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>6,000,000</td>
      <td>2018</td>
    </tr>
    <tr>
      <td>LS네트웍스</td>
      <td>2023-09-22</td>
      <td>5320054.0</td>
      <td>256.799007</td>
      <td>2023년 09월 22일</td>
      <td>2023년 09월 22일</td>
      <td>자기주식을 교환대상으로 하는 교환사채 발행</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5,320,054</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>윌비스</td>
      <td>2020-12-09</td>
      <td>5124450.0</td>
      <td>70.000000</td>
      <td>2020년 12월 11일</td>
      <td>2020년 12월 11일</td>
      <td>자기주식을 교환대상으로 하는 사모 교환사채 발행</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5,124,450</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>KB금융</td>
      <td>2020-06-18</td>
      <td>5000000.0</td>
      <td>2400.000000</td>
      <td>2020년 06월 30일</td>
      <td>2020년 06월 30일</td>
      <td>자기주식을 교환대상으로 하는 교환사채 발행에 따른 처분</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5,000,000</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>남성</td>
      <td>2016-02-02</td>
      <td>4938271.0</td>
      <td>100.000000</td>
      <td>2016년 02월 02일</td>
      <td>2016년 02월 02일</td>
      <td>자기주식을 교환대상으로하는 (사모)교환사채발행</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>4,938,271</td>
      <td>2016</td>
    </tr>
    <tr>
      <td>잇츠한불</td>
      <td>2017-02-17</td>
      <td>4837001.0</td>
      <td>1992.505822</td>
      <td>2017년 05월 12일</td>
      <td>2017년 05월 12일</td>
      <td>합병신주에 갈음한 자기주식의 교부</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>4,837,001</td>
      <td>2017</td>
    </tr>
    <tr>
      <td>카카오</td>
      <td>2024-04-23</td>
      <td>4599111.0</td>
      <td>2929.633200</td>
      <td>2024년 04월 29일</td>
      <td>2024년 04월 29일</td>
      <td>자기주식을 교환대상으로 하는 해외 외화표시 교환사채 발행에 따른 처분</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>4,599,111</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>SK네트웍스</td>
      <td>2024-01-04</td>
      <td>3415875.0</td>
      <td>214.892696</td>
      <td>2024년 01월 16일</td>
      <td>2024년 01월 16일</td>
      <td>소규모 주식교환 절차 진행</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3,415,875</td>
      <td>2024</td>
    </tr>
  </tbody>
</table>
</pre>


기타방식으로 처분한 자기주식 상위 10개의 공시문서상 처분목적을 살펴보니 **교환사채를 발행**{: style="color: #4682B4;"}한 경우가 많았습니다. <br>

사채인데, 권리를 행사하면 해당 주식을 배부하는 것이 교환사채입니다. 이런 사채를 발행하면서 자기주식을 처분하게 되는 경우가 '기타'의 주요 사유가 된다는 것을 확인하였습니다.

