---
layout: single
title:  "자사주 취득의 데이터는 어디서 구할까? (2편)"
categories: 한국시장
tag: [data background, opendart, 자기주식]
toc: true
author_profile: false
---

<head>
  <style>
    table.dataframe {
      white-space: normal;
      width: 100%;
      height: 240px;
      display: block;
      overflow: auto;
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

  </style>
</head>


**[관련 포스팅]** [자사주 매매 프로세스](https://beaten-by-the-market.github.io/%ED%95%9C%EA%B5%AD%EC%8B%9C%EC%9E%A5/buybackexplanation/)
{:.notice--success}

<br>
<br>

# 자사주 매매 프로세스별 데이터를 구하는 곳은?
---

자사주 매매 프로세스별 데이터를 어디서 구할 수 있을까요? 의사결정에 대한 데이터, 매매체결에 대한 데이터, 결과보고에 대한 데이터 순으로 보겠습니다.<br>
<br>
<br>   
   
#### 1. 의사결정에 대한 데이터
---
   
회사는 자기주식을 취득/처분하기로 이사회에서 결정하면, 당일 금융감독원에 **"주요사항보고서"**{: style="color: #4682B4;"}를 제출한다고 하였습니다. 개별 공시를 하나씩 까봤다면 데이터를 확인할 엄두도 못냈겠지만, 고맙게도 금감원은 [**OpenDart**{: style="color: #4682B4;"}](https://opendart.fss.or.kr/)라는 서비스를 운영중입니다. (OpenDart에서 사용할 수 있는 다양한 데이터들의 활용사례는 향후 포스팅에서 차차 풀어보도록 하겠습니다.) <br>
<br>
자사주 매매 의사결정에 대한 데이터는 OpenDart에 접속하면 보이는 아래의 두 개 메뉴를 통해서 확인이 가능합니다. "개발가이드" 부분은 OpenDart API를 사용하는 방식이고, "공시정보활용마당" 부분은 웹으로 조회하고 엑셀 다운로드가 되는 기능입니다. <br>
OpenDart API의 경우 회사코드가 필수 입력인자라서 상장사 개수만큼 loop을 돌려야 하는 부담이 있습니다. 따라서 "공시정보활용마당"을 이용해보도록 하겠습니다.
<br>

![opendartmenu]({{site.url}}/assets/images/2025-01-22-buybackexpl2/opendartmenu.png)<br>

<br>

"공시정보활용마당-주요사항보고서 주요정보조회"에서 볼 수 있는 화면입니다. 필수로 입력해야 하는 인자가 "기간"뿐이고, 전체 상장사를 대상으로 조회 및 엑셀 다운로드가 가능하도록 되어있습니다. ***(정말 편리하네요!)***<br><br>


![search]({{site.url}}/assets/images/2025-01-22-buybackexpl2/search.png)<br>

<br>

"검색"버튼 클릭만으로 이렇게 시장 전체의 공시이력을 모아볼 수 있습니다. 단, 제공하는 데이터의 범위는 공시의 주요사항이 들어있는 본문의 첫번째 표에 기재된 내용입니다. 
* 취득예정주식수
* 취득예정금액
* 취득예정기간
* 취득목적
* 취득방법
* 위탁중개투자업자
* 취득전 자기주식 보유현황 : 배당가능이익범위 내 주식, 기타취득 주식
* 취득결정일
* 사외이사, 감사 참석여부
* 1일 매수 주문수량 한도(장내에서 취득하는 경우)
* 비고
<br>

![searchresult]({{site.url}}/assets/images/2025-01-22-buybackexpl2/searchresult.png)<br>

한편, 제공되는 데이터는 **회사가 작성한**{: style="color: #4682B4;"} 데이터입니다. 즉, 만약에 회사가 오타를 냈다면... 그부분의 정합성까지는 담보될 수 없습니다. <br>
<br>

   
#### 2. 실행단계의 데이터
    
실행단계, 즉 매매를 하는 과정은 크게 **장내취득**{: style="color: #4682B4;"}과 **장외취득**{: style="color: #4682B4;"}으로 이뤄진다고 말씀드린 바 있습니다. **장내취득의 경우 KRX 정보데이터시스템을 통해 확인이 가능**{: style="color: #4682B4;"}하나, **장외의 경우 확인할 수 있는 방법은 없습니다.**{: style="color: #4682B4;"}<br>

###### 장내에서 취득하는 경우

<br>
[**KRX 정보데이터시스템**{: style="color: #4682B4;"}](http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0202) 의 의 "이슈통계 - 자사주추득/처분"메뉴에서는 전체 상장사의 자사주 관련 누적 매매실적을 확인할 수 있습니다. <br>

제공되는 데이터중 "공시일"과 "취득(처분)예정기간"은 금감원에 제출된 공시의 내용을 기반으로 합니다. 따라서 자기주식을 취득/처분하겠다는 **각 의사결정별로 실제로 얼마나 이행했는지를 확인**{: style="color: #4682B4;"}해볼 수 있는 부분입니다. 물론 장내에 한정해서요.<br>
<br>

![krxresult]({{site.url}}/assets/images/2025-01-22-buybackexpl2/krxresult.png)


##### 3. 결과보고에 대한 데이터


자기주식 취득에 대한 결과는 금융감독원에 제출되는 **1)결과보고서와 2)정기보고서(사업보고서, 분/반기 보고서)**를 통해 확인이 가능하다고 말씀드린 바 있습니다.<br>

###### 결과보고서
아쉽게도 자기주식취득/처분 결과보고서는 OpenDart에서 제공하고 있지 않습니다. 표준화된 표 형태로 잘 정리되어 있지만, 일괄로 받을 수 있는 방법은 현재는 없습니다. 그래도 표준화가 되어있으니, OpenAPI로 각 URL을 받은 후 크롤링을 통해 데이터를 수집하는 것은 가능합니다. 추후에 기회가 되면 진행해 보도록 하겠습니다. <br>
<br>

###### 정기보고서(사업, 분/반기보고서)
비록 적시성은 떨어지지만(45~90 이후 제출), 개별 정기보고서 화면에서는 이렇게 기재되는 내용이 있습니다. (**"Ⅰ. 회사의 개요 - 4. 주식의 총수 등 - 나. 자기주식 취득 및 처분 현황"**{: style="color: #4682B4;"}) 기초수량과 변동수량(취득, 처분, 소각), 그리고 기말수량이 잘 정리되어 기재되어 있습니다.<br><br>
![annualreportex]({{site.url}}/assets/images/2025-01-22-buybackexpl2/annualreportex.png)

<br><br>

다행히도 OpenDart에서는 사업보고서와 분/반기보고서에 기재된 자기주식 취득/처분 데이터를 일괄로 받아볼 수 있습니다. OpenAPI로도 수집은 가능하지만 회사별로 loop을 돌려야 하는 관계로, **"공시정보활용마당 - 정기보고서 주요정보조회"**{: style="color: #4682B4;"}에서 데이터를 확인해보았습니다. 
<br>
<br>

![annualreportmenu]({{site.url}}/assets/images/2025-01-22-buybackexpl2/annualreportmenu.png)
<br>
<br>
정기보고서에 기재된 내용 전체가 일괄 조회가 되며, 엑셀 형태로도 다운이 가능합니다. ***(정말 편리하네요!)***
<br>

![annualsearchresult]({{site.url}}/assets/images/2025-01-22-buybackexpl2/annualsearchresult.png)
<br>
<br>
하지만 한 가지 아쉬운 점이 있습니다. 통상 상장되어 있는 보통주를 기준으로 데이터를 뽑아보고 싶을텐데, **"주식의 종류" 칼럼을 살펴보면 회사마다 기재하는 방식이 천차만별**{: style="color: #4682B4;"}입니다. 오타와 오기재 사항도 상당수 있습니다. 2023년 사업보고서 코스피, 코스닥 전체를 대상으로 다운받은 엑셀파일에서 "주식의종류"를 확인해보니 아래와 같이 다양한 사례가 존재합니다. ***표현이 통일이 되지 않았으며, 오타도 있고, "기초수량"을 "주식의종류"에 실수로 기재한 경우도 있습니다.*** 오기재된 부분이 엄청난 양은 아니다 보니 어느정도의 수작업 보정을 통해서 처리할 수 있는 수준이긴합니다만... 10년치를 분석하고자 하는 경우, 향후에도 계속 수집하고자 하는 경우에는 상당히 번거로워질 수 있습니다.<br>

![type]({{site.url}}/assets/images/2025-01-22-buybackexpl2/typo.png)
<br><br>


##### 4. 각 데이터의 품질
앞에서는 의사결정단계, 실행단계, 결과보고단계별 데이터 출처를 살펴보았습니다. 품질이라는 표현이 맞을진 모르겠으나, 각 출처의 특성에 따라서 ***어느 수준의 cleansing***을 해야할지가 차이가 날 것으로 보입니다.
<br><br>
**1. 주요사항보고서**{: style="color: #4682B4;"}<br>
* 취득방법(장내, 장외)을 기재할 때 선택지에서 선택하는 방식이 아닌 free text로 기재하는 방식이기 때문에, 일부 표준화가 덜된 항목이 있습니다.
* 회사가 수기로 입력한다는 면에서 오타 등의 가능성을 배제할 수는 없습니다.
* ***그러나 제출된 공시의 수량과 기간 정보는 KRX 정보데이터시스템에 등재되는 과정이 있으므로, 숫자상 오류가 날 가능성은 적습니다.*** 
<br><br>

**2. 거래소 데이터**{: style="color: #4682B4;"}<br>
* 주문정보와 체결정보는 모두 숫자로 전산화된 과정을 거치기 때문에 데이터를 바로 사용가능합니다.
* ***그러나 거래소의 관할영역 밖인 장외 데이터가 없다는 단점은 여전히 있습니다.*** 
<br><br>

**3. 정기보고서**{: style="color: #4682B4;"}<br>
* 취득/처분 뿐만 아니라 소각 수량까지 함께 갖고 있기에 활용성이 높습니다.
* 장내 뿐만 아니라 장외 수량까지 있기 때문에 전체를 파악하기에 유용합니다.
* ***그러나 수기로 입력되고 있으며, 표준화가 덜된 부분이 있어서 전처리가 필요합니다.***