---
layout: single
title:  "자사주 매입: 시간외대량매매의 비중은 얼마일까?"
categories: 국내시장
tag: [자기주식, opendart]
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

  .notice--success {
  font-size: 1.2rem !important; 
  }

  .notice--info {
  font-size: 1.2rem !important; 
  }

  .notice--warning {
  font-size: 1.0rem !important;
  }


  </style>
</head>



**[관련 포스팅]** [자사주 매매 프로세스](https://beaten-by-the-market.github.io/%ED%95%9C%EA%B5%AD%EC%8B%9C%EC%9E%A5/buybackexplanation/)<br>
**[관련 포스팅]** [자사주 매매 데이터출처](https://beaten-by-the-market.github.io/%ED%95%9C%EA%B5%AD%EC%8B%9C%EC%9E%A5/buybackexplanation2/)<br>
**[관련 포스팅]** [10년간 코스피 자사주 직접 ‘처분’ 현황(시사점)](https://beaten-by-the-market.github.io/%ED%95%9C%EA%B5%AD%EC%8B%9C%EC%9E%A5/kospi_dart_buyback_resale/)
{:.notice--success}


## 자사주 매입에서 시간외대량매매는 얼마나 있을까?



[**10년간 자사주 매입현황 포스팅(링크)**{: style="color: #4682B4;"}](https://beaten-by-the-market.github.io/%ED%95%9C%EA%B5%AD%EC%8B%9C%EC%9E%A5/kospi-buyback-insight/#%EC%9E%90%EC%82%AC%EC%A3%BC%EC%B7%A8%EB%93%9D-%EC%9E%A5%EB%82%B4-vs-%EC%9E%A5%EC%99%B8-%EA%B5%AC%EB%B6%84%EC%9E%90-%EB%8B%AC%EA%B8%B0)을 작성할 때 '장내'와 '장외'를 구분하면서 개인적으로는 특이하다고 생각한 부분이 있었습니다.



### **시간외대량매매**란?

주식 시장은 보통 정규 거래 시간(오전 9시 ~ 오후 3시 30분) 동안 거래가 이루어집니다. 하지만 때로는 이 시간 외에도 큰 규모의 주식 거래가 필요할 때가 있습니다. 바로 이럴 때 **"시간외대량매매"**가 사용됩니다.<br>



시간외대량매매는 말 그대로 정규 거래 시간이 아닌 시간에, 대량으로 주식을 매매하는 거래 방식을 뜻합니다. 여기서 중요한 핵심은 **'대량'**이라는 점입니다. 즉, 일반 투자자들이 주식을 소량으로 사고파는 것이 아니라, 기관 투자자, 대규모 투자자, 혹은 기업 간에 이루어지는 거대한 규모의 주식 거래를 말하는 거죠.<br>



> **많은 경우, 거래는 양 당사자(매수자와 매도자) 사이에서 사전 합의를 통해 진행됩니다.**{: style="color: #4682B4;"}



여기에 시간외대량매매의 장점이 있습니다. 정규 거래 시간 안에서 대량의 주식을 사고판다면, **주가에 큰 영향을 미칠 수 있습니다.**{: style="color: #4682B4;"} 예를 들어, 갑자기 많은 주식을 사려고 하면 주가가 급등할 수 있고, 반대로 크게 매도하면 주가가 급락할 수 있습니다. 그런데 시간외대량매매를 사용하면 이런 영향을 최소화하면서 매매를 할 수 있습니다.



### 자기주식 거래에서 시간외대량매매의 의의

자기주식을 매입하는 사유로 기업이 가장 많이 공시하는 것은 **주식 가치 제고**{: style="color: #4682B4;"}입니다. 이러한 사유로 **장내에서 많이 매수할 것이라 추측해볼 수 있습니다.**{: style="color: #4682B4;"}<br>

반면, 자기주식을 부득이하게 처분해야할 때 회사는 주가가 최대한 하락하지 않길 원할 것입니다. 따라서 **자사주를 매도할 때는 장내가 아닌 방식으로, 예를 들어 시간외대량매매를 활용할 수 있겠다는 추측을 해볼 수 있습니다.**{: style="color: #4682B4;"}

## 코스피 시장에서 시간외대량매매 방식으로 자사주 매입 사례를 찾기


### 금감원 공시에서 자사주 데이터 수집하기

### 금감원 공시 기준 데이터 시각화

![all_buyback]({{site.url}}/assets/images/2025-01-22-buybackinsight/all_buyback.png)<br><br>


### 금감원 공시에서 시간외대량매매 구분자 달기


```python
# 정규식 패턴 정의 |
pattern_blockdeal = re.compile(r'대량|시간\s?외')  # 대량, 시간외가 있으면 포함
pattern_otc_exclude = re.compile(r'시장\s?외')  # '시장 외'와 '시장외'를 모두 포함

# method 열 생성
def categorize_method_blockdeal(method):
    if pattern_blockdeal.search(method) and not pattern_otc_exclude.search(method):
        return 'blockdeal'
    else:
        return 'not_bd'

# 새로운 열에 카테고리 할당
df_dart_buyback['blockdeal'] = df_dart_buyback['취득방법'].apply(categorize_method_blockdeal)

# 확인해보기
df_dart_buyback[df_dart_buyback['blockdeal'] ==  'blockdeal']
```

<pre><table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>회사명</th>
      <th>접수일</th>
      <th>취득예정주식</th>
      <th>취득예정금액</th>
      <th>취득시작일</th>
      <th>취득종료일</th>
      <th>보유시작일</th>
      <th>보유종료일</th>
      <th>취득목적</th>
      <th>취득방법</th>
      <th>연도</th>
      <th>method</th>
      <th>blockdeal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>우리금융지주</td>
      <td>2024-03-13</td>
      <td>9357960.0</td>
      <td>1366.262160</td>
      <td>2024-03-14</td>
      <td>2024년 03월 14일</td>
      <td>-</td>
      <td>-</td>
      <td>자기주식 취득 및 소각을 통한 주주가치 제고</td>
      <td>시간외대량매매</td>
      <td>2024</td>
      <td>mkt</td>
      <td>blockdeal</td>
    </tr>
    <tr>
      <td>한화생명</td>
      <td>2015-10-29</td>
      <td>65139750.0</td>
      <td>5202.711833</td>
      <td>2015-10-28</td>
      <td>2015년 10월 29일</td>
      <td>-</td>
      <td>-</td>
      <td>주가 안정을 통한 주주가치 제고</td>
      <td>시간외 대량매매</td>
      <td>2015</td>
      <td>mkt</td>
      <td>blockdeal</td>
    </tr>
  </tbody>
</table>
</pre>
2015년부터 2024년 사이에 자사주 매입을 '시간외대량매매'방식으로 한 경우는 두 번이었습니다. **우리금융지주**와 **한화생명**이었네요. 둘다 공통적으로 **예금보험공사**로부터 사들이는 경우였습니다.

<br>

따라서 이러한 특수한 경우를 제외하고는, **자사주 매입을 시간외대량매매로 하는 경우는 사실상 없다고 봐도 되겠습니다.**



<br>



![woori]({{site.url}}/assets/images/2025-02-15-blockdeal/woori.png)

<br>



![hanhwa]({{site.url}}/assets/images/2025-02-15-blockdeal/hanhwa.png)


<br>

혹시 모르니, '취득방법'으로 기재한 내용 전체를 확인해 볼까요? 시간외대량매매에 해당하는 내용은 정말 두 케이스 밖에 없는 것 같습니다.

<br>

```python
sorted(df_dart_buyback['취득방법'].unique())
```

<pre>
['-',
 '거래소 유가증권시장을 통한 매수',
 '공개매수',
 '무상 수증',
 '무상수증',
 '시간외 대량매매',
 '시간외대량매매',
 '유가시장을 통한 직접 취득',
 '유가증권 시장을 통한 장내 매수',
 '유가증권 시장을 통한 장내 직접 취득',
 '유가증권 시장을 통한 장내매매',
 '유가증권 시장을 통한 장내매수',
 '유가증권 시장을 통한 직접 매수',
 '유가증권 시장을 통한 직접 취득',
 '유가증권 시장을 통한 직접취득',
 '유가증권시장 장내매수',
 '유가증권시장에서 장내매수',
 '유가증권시장에서의 장내직접취득',
 '유가증권시장에서의 직접 취득',
 '유가증권시장에서의 취득',
 '유가증권시장을 통한 매수',
 '유가증권시장을 통한 장내 매수',
 '유가증권시장을 통한 장내 직접 취득',
 '유가증권시장을 통한 장내 직접매수',
 '유가증권시장을 통한 장내 직접취득',
 '유가증권시장을 통한 장내매수',
 '유가증권시장을 통한 장내매수 (직접취득)',
 '유가증권시장을 통한 장내매수(장중취득)',
 '유가증권시장을 통한 장내매수(직접 취득)',
 '유가증권시장을 통한 장내매수(직접취득)',
 '유가증권시장을 통한 장내직접취득',
 '유가증권시장을 통한 직접 취득',
 '유가증권시장을 통한 직접취득',
 '유가증권시장을 통한장내매수',
 '유가증권을 통한 장내매수',
 '자본시장법 등 관계법령에서 정한 방법에 따라 장내 매수',
 '장내 매수',
 '장내 직접 매수',
 '장내 직접 취득',
 '장내 직접취득',
 '장내매수',
 '장내매수(직접취득)',
 '장내취득',
 '장외 직접 거래',
 '장외 직접 매수',
 '장외 취득',
 '장외매수',
 '장외직접매수',
 '장외취득',
 '장외회수(직접취득)',
 '증권시장 장내 직접취득',
 '증권시장 장내취득',
 '증권시장에서 장내취득',
 '증권시장에서의 장내 직접취득',
 '증권시장에서의 취득',
 '증권시장을 통한 장내매수',
 '증권시장을 통한 직접취득',
 '증여',
 '창업주 김정식 회장의 무상 출연']
</pre>

## 코스닥 시장에서 시간외대량매매 방식으로 자사주 매입 사례를 찾기
이번에는 코스닥시장을 한번 살펴보겠습니다.

### 금감원 공시에서 자사주 데이터 수집하기
코스닥시장의 자사주 취득현황에 대한 포스팅은 아직 작성한 적이 없지만, 코스피 시장과는 실행코드가 같습니다. 일단 코드를 실행하여 시각화 결과물만 먼저 보도록 하겠습니다.



### 금감원 공시 기준 데이터 시각화

![kosdaq_buyback]({{site.url}}/assets/images/2025-02-15-blockdeal/kosdaq_buyback.png)


### 금감원 공시에서 시간외대량매매 구분자 달기



```python
# 정규식 패턴 정의 |대량|시간\s?외
pattern_blockdeal = re.compile(r'대량|시간\s?외')  # 대량, 시간외가 있으면 포함
pattern_otc_exclude = re.compile(r'시장\s?외')  # '시장 외'와 '시장외'를 모두 포함

# method 열 생성
def categorize_method_blockdeal(method):
    if pattern_blockdeal.search(method) and not pattern_otc_exclude.search(method):
        return 'blockdeal'
    else:
        return 'not_bd'

# 새로운 열에 카테고리 할당
df_dart_buyback['blockdeal'] = df_dart_buyback['취득방법'].apply(categorize_method_blockdeal)

# 확인해보기
df_dart_buyback[df_dart_buyback['blockdeal'] ==  'blockdeal']
```
<pre>
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>회사명</th>
      <th>접수일</th>
      <th>취득예정주식</th>
      <th>취득예정금액</th>
      <th>취득시작일</th>
      <th>취득종료일</th>
      <th>보유시작일</th>
      <th>보유종료일</th>
      <th>취득목적</th>
      <th>취득방법</th>
      <th>연도</th>
      <th>method</th>
      <th>blockdeal</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</pre>
<br>
코스닥의 경우에는 2015~2024년 동안 **시간외대량매매로 자사주 매입을 한 경우가 한번도 없었습니다. 코스피와 코스닥을 통틀어 '시간외대량매매'방식을 통한 자사주 매입은 사실상 없다고 봐도 될 것같습니다.**<br>
코스피와 마찬가지로, 코스닥에서도 상장사가 기재한 '취득방법'을 전부 확인해보도록 하겠습니다. 시간외대량매매가 없습니다.


```python
sorted(df_dart_buyback['취득방법'].unique())
```

<pre>
['-',
 'KOSDAQ 시장에서 직접 취득',
 '계좌이체',
 '공개매수',
 '기타 장외매수',
 '기타취득',
 '당사 직접취득',
 '당사자 사이의 상환전환우선주 계약에 의한 매수(장외매수)',
 '당사자간 계약에 의한 직접매수',
 '대물상환계약에 따른 실물인수',
 '무상 수증',
 '무상 증여',
 '무상수증',
 '상환우선주 및 우선주 보유주주로 부터 장외 직접 매수',
 '상환우선주 보유주주로 부터 장외 직접매수',
 '상환전환우선주 보유주주로 부터 장외 직접 매수',
 '상환전환우선주 보유주주로부터 장외 직접 매수',
 '상환전환우선주식을 보유한 우선주주로부터 상환청구통지 수령 및 상환대금 납입',
 '실물 취득',
 '유가증권 시장을 통한 직접 취득',
 '유가증권시장을 통한 장내 매수',
 '장내',
 '장내 매수',
 '장내 직접 취득',
 '장내 직접취득',
 '장내 취득',
 '장내매매',
 '장내매수',
 '장내매수 (직접취득)',
 '장내매수(직접 취득)',
 '장내매수(직접취득)',
 '장내매수방식',
 '장내직접취득',
 '장내취득',
 '장외 직접 매수',
 '장외 취득(계좌간 대체)',
 '장외매수',
 '장외직접매수',
 '장외취득',
 '전환상환우선주 보유주주로부터 직접매수',
 '전환우선주 보유주주로 부터 장외 직접 매수',
 '증권계좌 대체로 장외 직접취득',
 '증권시장 내 장내취득',
 '증권시장 장내 직접취득',
 '증권시장내 매수',
 '증권시장내 직접 취득',
 '증권시장에서 장내 취득',
 '증권시장에서 장내취득',
 '증권시장에서 직접 취득',
 '증권시장에서 취득',
 '증권시장에서의 장내취득',
 '증권시장에서의 취득',
 '증권시장을 통한 장내 직접 취득',
 '증권시장을 통한 장내 직접취득',
 '증권시장을 통한 직접취득',
 '질권말소 후 입고',
 '최대주주로부터 무상수증',
 '코넥스시장을 통한 장내 직접취득',
 '코스닥 시장 장내 매수',
 '코스닥 시장 장내 직접 취득',
 '코스닥 시장 장내 직접취득',
 '코스닥 시장에서 직접취득',
 '코스닥 시장에서의 취득',
 '코스닥 시장을 통한 장내 매수',
 '코스닥 시장을 통한 장내 직접 취득',
 '코스닥 시장을 통한 장내 직접취득',
 '코스닥 시장을 통한 장내매수',
 '코스닥 시장을 통한 직접 매수',
 '코스닥 시장을 통한 직접 취득',
 '코스닥 시장을 통한 직접매수',
 '코스닥 시장을 통한 직접취득',
 '코스닥 증권시장에서 장내취득',
 '코스닥 증권시장에서 직접취득',
 '코스닥 증권시장에서의 직접 취득',
 '코스닥 증권시장에서의 취득',
 '코스닥 증권시장을 통한 장내 당사 직접취득',
 '코스닥 증권시장을 통한 장내 매수',
 '코스닥 증권시장을 통한 장내 직접 취득',
 '코스닥 증권시장을 통한 장내 직접취득',
 '코스닥 증권시장을 통한 장내매수',
 '코스닥 증권시장을 통한 장내매수 (직접 취득)',
 '코스닥 증권시장을 통한 직접 취득',
 '코스닥시장 내에서 직접 취득',
 '코스닥시장 장내 직접 취득',
 '코스닥시장 장내 직접취득',
 '코스닥시장 장내매수',
 '코스닥시장내에서 직접취득',
 '코스닥시장에서의 장내매수',
 '코스닥시장에서의 직접 취득',
 '코스닥시장을 통한 장내 매수',
 '코스닥시장을 통한 장내 매수 (직접취득)',
 '코스닥시장을 통한 장내 직접 취득',
 '코스닥시장을 통한 장내 직접매수',
 '코스닥시장을 통한 장내 직접취득',
 '코스닥시장을 통한 장내 취득',
 '코스닥시장을 통한 장내매수',
 '코스닥시장을 통한 장내직접취득',
 '코스닥시장을 통한 장내취득',
 '코스닥시장을 통한 직접 취득',
 '코스닥시장을 통한 직접취득',
 '코스닥시장의 장내 취득',
 '코스닥증권 시장을 통한 장내 취득',
 '코스닥증권 시장을 통한 장내매수',
 '코스닥증권시장 장내매수',
 '코스닥증권시장에서 장내 직접취득',
 '코스닥증권시장을 통한 매수',
 '코스닥증권시장을 통한 매수 (직접취득)',
 '코스닥증권시장을 통한 장내 매수',
 '코스닥증권시장을 통한 장내매수',
 '한국거래소를 통한 장내 매입',
 '한국거래소를 통한 장내 직접취득',
 '한국거래소를 통한 장내매입']
</pre>

<br>
다음 포스팅에서는 자사주 처분의 경우를 확인해보도록 하겠습니다.

