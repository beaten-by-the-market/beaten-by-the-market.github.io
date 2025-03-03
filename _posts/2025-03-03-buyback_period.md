---
layout: single
title:  "자기주식 취득 결정 후 실제 취득까지 얼마나 걸릴까?"
categories: 한국시장
tag: [insight, opendart, 자기주식]
toc: true
author_profile: false
---
<head>
  <style>
    table.dataframe {
      white-space: nowrap;     /* 기본적으로 줄바꿈 방지 */
      width: auto;             /* 컨텐츠에 맞게 너비 자동 조정 */
      min-width: 100%;         /* 최소 너비는 컨테이너 크기 */
      max-width: 400%;         /* 최대 너비 제한 400% */
      max-height: 300px;       /* 최대 높이 */
      display: block;          /* 블록 요소로 표시 */
      overflow-x: auto;        /* 가로 스크롤 */
      overflow-y: auto;        /* 세로 스크롤 */
      font-family: Arial, sans-serif;
      font-size: 0.9rem;
      line-height: 20px;
      text-align: center;
      border: 0px !important;
      margin-bottom: 10px;     /* 하단 여백 */
    }

    /* 모든 셀에 대한 기본 스타일 */
    table.dataframe td, 
    table.dataframe th {
      max-width: 400px;        /* 셀 최대 너비 제한 */
      overflow: hidden;        /* 셀 내용 넘침 처리 */
      text-overflow: ellipsis; /* 넘친 텍스트는 말줄임표로 표시 */
      white-space: nowrap;     /* 기본적으로 줄바꿈 방지 */
      box-sizing: border-box;  /* 패딩과 테두리를 너비에 포함 */
    }

    /* 테이블 헤더 스타일 */
    table.dataframe th {
      text-align: center;
      font-weight: bold;
      padding: 8px;
      position: sticky;        /* 헤더 고정 */
      top: 0;                  /* 헤더 고정 위치 */
      background: #e6f2ff;     /* 파스텔 블루 배경색 */
      z-index: 2;              /* 헤더가 컨텐츠 위에 표시되도록 */
      border-bottom: 1px solid #c6d9f1; /* 헤더 하단 경계선 */
      white-space: nowrap !important; /* 헤더는 항상 줄바꿈 없음 */
    }

    /* 헤더 호버 스타일 */
    table.dataframe th:hover {
      background-color: #d0e4ff; /* 호버 시 약간 더 진한 파스텔 블루 */
      white-space: nowrap !important; /* 호버 시에도 줄바꿈 없음 */
      overflow: visible;
      position: relative;
      z-index: 3;
    }

    /* 데이터 셀 스타일 */
    table.dataframe td {
      text-align: center;
      padding: 8px;
      position: relative; /* 호버 효과를 위한 위치 설정 */
    }

    /* 데이터 셀 호버 스타일 - JavaScript로 긴 내용 감지 및 클래스 추가 */
    table.dataframe td.long-content:hover {
      white-space: normal; /* 긴 내용이 있는 셀만 호버 시 줄바꿈 허용 */
      overflow: visible;
      z-index: 1;
      background-color: white; /* 내용이 다른 셀을 가릴 때 배경색 */
      box-shadow: 0 0 5px rgba(0,0,0,0.1); /* 약간의 그림자 효과 */
    }

    /* 일반 셀 호버 스타일 */
    table.dataframe td:not(.long-content):hover {
      white-space: nowrap !important; /* 짧은 내용이 있는 셀은 호버 시에도 줄바꿈 없음 */
    }

    /* 짝수 행 배경색 */
    table.dataframe tr:nth-child(even) {
      background-color: #f8fbff;
    }

    /* 모든 행에 호버 효과 적용 - 우선순위를 높게 설정 */
    table.dataframe tr:hover {
      background-color: #b8d1f3 !important; /* !important로 짝수행 스타일보다 우선 적용 */
    }

    /* 정렬 가능한 헤더에 대한 스타일 추가 */
    table.dataframe th.sortable {
      cursor: pointer;
      position: relative;
      padding-right: 18px; /* 화살표 공간 확보 */
    }
    
    table.dataframe th.sortable::after {
      content: "↕";
      position: absolute;
      right: 5px;
      top: 50%;
      transform: translateY(-50%);
      opacity: 0.5;
    }
    
    table.dataframe th.sortable.asc::after {
      content: "↑";
      opacity: 1;
    }
    
    table.dataframe th.sortable.desc::after {
      content: "↓";
      opacity: 1;
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
        margin: 0 0 10px !important;
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
  
  <!-- 테이블 정렬을 위한 JavaScript 추가 -->
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      // 모든 dataframe 테이블의 헤더에 정렬 기능 추가
      const tables = document.querySelectorAll('table.dataframe');
      
      tables.forEach(function(table) {
        const headers = table.querySelectorAll('thead th');
        
        // 긴 내용이 있는 셀 감지하여 클래스 추가
        const dataCells = table.querySelectorAll('tbody td');
        dataCells.forEach(function(cell) {
          // 셀의 실제 내용 길이와 표시 너비 비교
          const cellContent = cell.textContent;
          
          // 임시 요소를 만들어 내용 너비 측정
          const tempSpan = document.createElement('span');
          tempSpan.style.visibility = 'hidden';
          tempSpan.style.position = 'absolute';
          tempSpan.style.whiteSpace = 'nowrap';
          tempSpan.style.font = window.getComputedStyle(cell).font;
          tempSpan.textContent = cellContent;
          document.body.appendChild(tempSpan);
          
          // 내용 너비가 셀 최대 너비(400px)를 초과하면 long-content 클래스 추가
          const contentWidth = tempSpan.getBoundingClientRect().width;
          if (contentWidth > 380) { // 약간의 여유 제공 (400px - 패딩)
            cell.classList.add('long-content');
          }
          
          // 임시 요소 제거
          document.body.removeChild(tempSpan);
        });
        
        headers.forEach(function(header, index) {
          // 헤더에 정렬 가능 클래스 추가
          header.classList.add('sortable');
          
          // 헤더 클릭 이벤트 리스너 추가
          header.addEventListener('click', function() {
            const isAsc = this.classList.contains('asc');
            const direction = isAsc ? 'desc' : 'asc';
            
            // 모든 헤더에서 정렬 클래스 제거
            headers.forEach(h => {
              h.classList.remove('asc', 'desc');
            });
            
            // 클릭된 헤더에 정렬 방향 클래스 추가
            this.classList.add(direction);
            
            // 테이블 정렬 실행
            sortTable(table, index, direction);
          });
        });
      });
      
      // 테이블 정렬 함수
      function sortTable(table, colIndex, direction) {
        const tbody = table.querySelector('tbody');
        if (!tbody) return; // tbody가 없으면 중단
        
        const rows = Array.from(tbody.querySelectorAll('tr'));
        
        // 행 정렬
        rows.sort(function(rowA, rowB) {
          // 현재 열의 셀 가져오기
          const cellsA = rowA.querySelectorAll('td, th');
          const cellsB = rowB.querySelectorAll('td, th');
          
          // index 범위 확인
          if (colIndex >= cellsA.length || colIndex >= cellsB.length) return 0;
          
          const cellA = cellsA[colIndex].textContent.trim();
          const cellB = cellsB[colIndex].textContent.trim();
          
          // 날짜 형식 확인 (YYYY-MM-DD 또는 YYYY/MM/DD)
          const dateRegex = /^(\d{4}[-\/]\d{2}[-\/]\d{2}|\d{2}[-\/]\d{2}[-\/]\d{4})$/;
          if (dateRegex.test(cellA) && dateRegex.test(cellB)) {
            const dateA = new Date(cellA);
            const dateB = new Date(cellB);
            return direction === 'asc' ? dateA - dateB : dateB - dateA;
          }
          
          // 숫자인 경우 숫자 정렬
          if (!isNaN(parseFloat(cellA)) && !isNaN(parseFloat(cellB))) {
            return direction === 'asc' 
              ? parseFloat(cellA) - parseFloat(cellB)
              : parseFloat(cellB) - parseFloat(cellA);
          }
          
          // 일반 문자열 정렬
          return direction === 'asc'
            ? cellA.localeCompare(cellB)
            : cellB.localeCompare(cellA);
        });
        
        // 정렬된 행을 테이블에 다시 추가
        rows.forEach(function(row) {
          tbody.appendChild(row);
        });
        
        // 정렬 후 다시 길이 검사 (필요한 경우)
        const dataCells = table.querySelectorAll('tbody td');
        dataCells.forEach(function(cell) {
          if (!cell.classList.contains('long-content')) return;
          
          // 셀 내용이 여전히 길면 long-content 클래스 유지, 아니면 제거
          const cellContent = cell.textContent;
          const tempSpan = document.createElement('span');
          tempSpan.style.visibility = 'hidden';
          tempSpan.style.position = 'absolute';
          tempSpan.style.whiteSpace = 'nowrap';
          tempSpan.style.font = window.getComputedStyle(cell).font;
          tempSpan.textContent = cellContent;
          document.body.appendChild(tempSpan);
          
          const contentWidth = tempSpan.getBoundingClientRect().width;
          if (contentWidth <= 380) {
            cell.classList.remove('long-content');
          }
          
          document.body.removeChild(tempSpan);
        });
      }
    });
  </script>
</head>



**[관련 포스팅]** [자사주 매매 프로세스](https://beaten-by-the-market.github.io/%ED%95%9C%EA%B5%AD%EC%8B%9C%EC%9E%A5/buybackexplanation/)<br>
**[관련 포스팅]** [자사주 매매 데이터출처](https://beaten-by-the-market.github.io/%ED%95%9C%EA%B5%AD%EC%8B%9C%EC%9E%A5/buybackexplanation2/)<br>
**[관련 포스팅]** [10년간 코스피 자사주 직접취득 현황(시사점)](https://beaten-by-the-market.github.io/%ED%95%9C%EA%B5%AD%EC%8B%9C%EC%9E%A5/kospi-buyback-insight/)
{:.notice--success}



## 코스피 상장사들의 자기주식 취득 결정 후 취득시작시점까지 기간은 어떻게 될까?

자기주식 취득은 아무래도 이런저런 궁금증이 드는 이벤트입니다. 

* ***주주가치 제고(주가 상승)를 위해 회사의 주식을 회사가 스스로 취득한다..?***

* ***근데 장내에서 호가를 내서 취득한다..?***

* ***그렇다면 자기주식 취득과정에서 휘사는 주가가 상승하도록 할 유인이 있지 않나..?***

* ***자기주식 취득 시점을 아는 회사의 내부자들도 있을텐데..?***

<br>

자본시장법 집행기관들에 의해서 불공정거래는 잘 통제되고 있을 것입니다. 그래도 위와 같은 궁금증을 바탕으로 다음을 해보고자 합니다. 불공정거래 기업을 찾는다는 목적이 아니라 **위법이 아닌 영역에서 전수조사**{: style="color: #4682B4;"}를 해본다는 것입니다.<br>

> **자기주식 취득을 결정한 시점부터 실제 취득까지의 Timeline 단계별로 상장사들은 어떠한 양상을 보일까?**{: style="color: #4682B4;"} 

<br>

자기주식 취득의 Timeline 중에서 정보의 기점이 되는 주요 구간들을 한번 생각해봤습니다.<br><br>
![timeline]({{site.url}}/assets/images/2025-03-02-buybackperiod/timeline.png)<br>

**① 자기주식 취득 "결정공시"시점 직전**{: style="color: #4682B4; text-decoration: underline;"} <br>
- (취득규모, 취득후 소각여부에 따라 다르겠지만) **자기주식을 취득할 것이라는 정보는 통상 호재**입니다.<br>
- 따라서 공시시점 전에 우연히 매수를 할 수 있다면 호재성 정보 덕분에 수익을 얻을 수 있습니다.

<br>

**② 자기주식 취득결정공시 시점 ~ 자기주식 "취득기간 시작"시점**{: style="color: #4682B4; text-decoration: underline;"}<br>
- 공시는 되었습니다. 즉, **'자기주식을 취득할 것이다'라는 정보는 이제 public**해졌습니다.<br>
- 그래도 아직 자기주식 취득을 시작하지 않았다면 기회는 있습니다. **자기주식 매수를 위해 호가를 제출하는 과정에서 가격이 상승할 수 있기 때문**입니다.<br>
- 따라서 공시시점부터 자기주식 취득기간이 시작하기 전까지의 구간에 주식을 매수한다면 수익을 얻을 수도 있습니다.

<br>

**③ 자기주식 취득결정공시 시점 ~ 체결되는 자기주식 매수호가 제출시점**{: style="color: #4682B4; text-decoration: underline;"}<br>
- 통상 3개월가량 되는 취득기간 중에서 **회사가 언제 매수주문을 제출할지 알 수 없습니다.**<br>
- 따라서 회사가 매수주문을 내기 전에 우연히 주식을 매수한다면 수익을 볼 수도 있을 것입니다.<br>
- 한편 '매매체결'이라는 전제를 달은 것은 관련 규제상(불성실공시 등) 매매체결을 의도하지 않은 주문을 낼 수도 있기 때문입니다.

<br>
세가지 구간에 대해 투자자의 매매데이터를 갖고 들여다보는 것은 차차 진행해보겠습니다. 그 전에, **각 구간이 얼마나 길었는지**{: style="color: #4682B4;"}를 알아보는 것이 필요합니다.<br>

①의 경우 외부인의 입장에서는 며칠짜리 기간이었는지 알 수 없습니다.<br>

②는 공시를 통해 확인할 수 있는 기간입니다. 한편, **취득결정 공시 바로 다음날에 취득시작시점이 도래한다면 두번째 구간은 애초에 0일**{: style="color: #4682B4;"}이 됩니다. 그러면 그 기간동안 매수를 한 투자자가 0명일 것이고 분석의 의미는 없습니다.<br>

③는 공시와 거래소 정보데이터시스템에서 공개하는 데이터를 통해 확인할 수 있는 기간입니다. **취득결정 공시 바로 다음날에 실제 매수호가를 제출했다면, 세번째 구간은 애초에 0일이 되고, ②와 마찬가지로 분석의 의미는 없어집니다.**{: style="color: #4682B4;"}<br>


## 수행절차

이전 포스팅에서 했던 대로 동일하게 2015~2024년의 기간동안 데이터를 금감원 OpenDart에서 수집하고, 장내vs장외취득 구분자를 달고, 장내중에서도 시간외대량매매 구분자를 달아보겠습니다. 리마인드차, 장내취득 vs 장외취득을 비교해보겠습니다. 수량(바차트)와 금액(라인차트)를 통해 보면 전반적으로 장외취득은 미미한 수준이나, 2024년에는 고려아연에서 발생한 경영권분쟁 관련 공개매수 때문에 유달리 높았습니다.

<br>
![mktvsotc]({{site.url}}/assets/images/2025-03-02-buybackperiod/mktvsotc.png)<br><br>

[***자사주 매입: 시간외대량매매의 비중은 얼마일까?(링크)***{: style="color: #4682B4;"}](https://beaten-by-the-market.github.io/%ED%95%9C%EA%B5%AD%EC%8B%9C%EC%9E%A5/buyback_blockdeal/) 포스팅에서도 확인했지만, 장내매매 중에서 시간외대량매매는 예금보험공사로부터 매입한 두 가지 사례밖에 없었습니다. 이 둘을 제외한 장내매매 내용을 일단 10개 확인해보겠습니다. 

<pre>
시간외대량매매가 아닌 장내매매 건수 : 613
상위 10개 행만 확인해보기
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
      <th>취득결정일</th>
      <th>취득목적</th>
      <th>취득방법</th>
      <th>연도</th>
      <th>method</th>
      <th>blockdeal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CJ</td>
      <td>2018-07-05</td>
      <td>287770.0</td>
      <td>400.0003</td>
      <td>2018-07-06</td>
      <td>2018년 10월 05일</td>
      <td>-</td>
      <td>-</td>
      <td>2018-07-05</td>
      <td>주가 안정을 통한 주주가치 제고</td>
      <td>유가증권 시장을 통한 직접 취득</td>
      <td>2018</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>DB금융투자</td>
      <td>2022-03-08</td>
      <td>650000.0</td>
      <td>39.7150</td>
      <td>2022-03-10</td>
      <td>2022년 06월 08일</td>
      <td>-</td>
      <td>-</td>
      <td>2022-03-08</td>
      <td>주가안정 및 주주가치 제고</td>
      <td>장내 매수</td>
      <td>2022</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>DB금융투자</td>
      <td>2024-09-10</td>
      <td>650000.0</td>
      <td>38.5450</td>
      <td>2024-09-11</td>
      <td>2024년 12월 10일</td>
      <td>-</td>
      <td>-</td>
      <td>2024-09-10</td>
      <td>기업가치제고 계획상 주주환원정책 이행</td>
      <td>장내 매수</td>
      <td>2024</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>DB손해보험</td>
      <td>2020-01-30</td>
      <td>708000.0</td>
      <td>305.8560</td>
      <td>2020-01-31</td>
      <td>2020년 04월 30일</td>
      <td>-</td>
      <td>-</td>
      <td>2020-01-30</td>
      <td>주가안정을 통한 주주가치 제고</td>
      <td>유가증권시장을 통한 장내매수(직접취득)</td>
      <td>2020</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>DB손해보험</td>
      <td>2020-03-19</td>
      <td>3540000.0</td>
      <td>925.7100</td>
      <td>2020-03-20</td>
      <td>2020년 06월 19일</td>
      <td>-</td>
      <td>-</td>
      <td>2020-03-19</td>
      <td>주가안정을 통한 주주가치 제고</td>
      <td>유가증권시장을 통한 장내매수(직접취득)</td>
      <td>2020</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
  </tbody>
</table>
</pre>

## 거래일 기준으로 취득결정일과 취득시작일 차이를 확인

![period]({{site.url}}/assets/images/2025-03-02-buybackperiod/period.png)<br><br>


시각화를 해보니 대부분 결정일 다음날 취득을 개시했습니다.(하루 차이) 그러나 그렇지 않은 경우도 꽤 보입니다. 케이스별로 하나씩 보도록 하겠습니다. **거래일 차이가 0인경우는 왜일까요?**{: style="color: #4682B4;"} 공시를 제출한 날부터 바로 취득을 시작했다는 얘기인데... 


> **자본시장법 시행령 제176조의2(자기주식의 취득ㆍ처분기준)**{: style="color: #4682B4;"} ③ 주권상장법인이 법 제165조의3제1항 및 제2항에 따라 자기주식을 취득하려는 경우에는 법 제391조에 따라 **이사회 결의 사실이 공시된 날의 다음 날부터**{: style="color: #4682B4;"} 3개월 이내에 금융위원회가 정하여 고시하는 방법에 따라 증권시장에서 자기주식을 취득하여야 한다.

법으로는 공시 다음날부터 취득할 수있게 되어있습니다. 우선 '거래일 기준'으로는 0일이지만, calendar day가 1일이상인 경우가 있겠죠. 아래 표를 보시면, 주말, 공휴일, 임시공휴일 등이 끼어있어서 거래일은 0일로 산정된 경우들이었습니다. **법에서는 calendar day를 기준**{: style="color: #4682B4;"}으로 하기 때문에 이경우는 문제가 되지 않습니다.

<pre>
시작일vs결정일이 다른데 날짜차이가 0으로 뜬 경우 : 17
상위 10개 행만 확인해보기
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>회사명</th>
      <th>접수일</th>
      <th>date_diff</th>
      <th>취득시작일</th>
      <th>시작요일</th>
      <th>취득결정일</th>
      <th>결정요일</th>
      <th>취득예정주식</th>
      <th>취득예정금액</th>
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
      <td>JB금융지주</td>
      <td>2017-02-10</td>
      <td>0</td>
      <td>2017-02-11</td>
      <td>토</td>
      <td>2017-02-10</td>
      <td>금</td>
      <td>2712000.0</td>
      <td>149.973600</td>
      <td>2017년 05월 10일</td>
      <td>-</td>
      <td>-</td>
      <td>주가안정 및 주주가치 제고</td>
      <td>유가증권시장 장내매수</td>
      <td>2017</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>KSS해운</td>
      <td>2018-06-12</td>
      <td>0</td>
      <td>2018-06-13</td>
      <td>수</td>
      <td>2018-06-12</td>
      <td>화</td>
      <td>250000.0</td>
      <td>19.750000</td>
      <td>2018년 09월 12일</td>
      <td>2018년 06월 13일</td>
      <td>-</td>
      <td>주가 안정 및 투자자 보호</td>
      <td>유가증권시장을 통한 직접 취득</td>
      <td>2018</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>SKC</td>
      <td>2016-11-11</td>
      <td>0</td>
      <td>2016-11-12</td>
      <td>토</td>
      <td>2016-11-11</td>
      <td>금</td>
      <td>1876728.0</td>
      <td>537.682572</td>
      <td>2017년 02월 11일</td>
      <td>-</td>
      <td>-</td>
      <td>주가 안정을 통한 주주가치 제고</td>
      <td>장내매수</td>
      <td>2016</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>SK하이닉스</td>
      <td>2018-07-27</td>
      <td>0</td>
      <td>2018-07-28</td>
      <td>토</td>
      <td>2018-07-27</td>
      <td>금</td>
      <td>22000000.0</td>
      <td>18282.000000</td>
      <td>2018년 10월 27일</td>
      <td>-</td>
      <td>-</td>
      <td>적정주가 확보를 통한 주주가치 제고</td>
      <td>장내 매수</td>
      <td>2018</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>경방</td>
      <td>2019-04-05</td>
      <td>0</td>
      <td>2019-04-06</td>
      <td>토</td>
      <td>2019-04-05</td>
      <td>금</td>
      <td>190000.0</td>
      <td>19.475000</td>
      <td>2019년 07월 05일</td>
      <td>-</td>
      <td>-</td>
      <td>주가안정을 통한 주주가치 제고</td>
      <td>증권시장 장내 직접취득</td>
      <td>2019</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>까뮤이앤씨</td>
      <td>2016-05-27</td>
      <td>0</td>
      <td>2016-05-28</td>
      <td>토</td>
      <td>2016-05-27</td>
      <td>금</td>
      <td>84000.0</td>
      <td>9.996000</td>
      <td>2016년 08월 27일</td>
      <td>-</td>
      <td>-</td>
      <td>주가안정 및 주주가치 제고</td>
      <td>장내 매수</td>
      <td>2016</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>무학</td>
      <td>2015-04-30</td>
      <td>0</td>
      <td>2015-05-01</td>
      <td>금</td>
      <td>2015-04-30</td>
      <td>목</td>
      <td>100000.0</td>
      <td>37.850000</td>
      <td>2015년 05월 20일</td>
      <td>-</td>
      <td>-</td>
      <td>주가안정 및 주주가치 제고</td>
      <td>유가증권시장을 통한 직접 취득</td>
      <td>2015</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>미원화학</td>
      <td>2017-02-28</td>
      <td>0</td>
      <td>2017-03-01</td>
      <td>수</td>
      <td>2017-02-28</td>
      <td>화</td>
      <td>37952.0</td>
      <td>25.883264</td>
      <td>2017년 05월 31일</td>
      <td>-</td>
      <td>-</td>
      <td>이익소각</td>
      <td>유가증권시장을 통한 매수</td>
      <td>2017</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>신한지주</td>
      <td>2024-02-08</td>
      <td>0</td>
      <td>2024-02-09</td>
      <td>금</td>
      <td>2024-02-08</td>
      <td>목</td>
      <td>3500583.0</td>
      <td>1500.000000</td>
      <td>2024년 05월 08일</td>
      <td>-</td>
      <td>-</td>
      <td>주식소각</td>
      <td>장내매수</td>
      <td>2024</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>유나이티드</td>
      <td>2016-09-09</td>
      <td>0</td>
      <td>2016-09-10</td>
      <td>토</td>
      <td>2016-09-09</td>
      <td>금</td>
      <td>300000.0</td>
      <td>54.150000</td>
      <td>2016년 12월 09일</td>
      <td>2016년 09월 12일</td>
      <td>-</td>
      <td>자사의 주식 가격 안정</td>
      <td>장내매수</td>
      <td>2016</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
  </tbody>
</table>
</pre>


이번에는 calendar day 기준으로도 결정일과 시작일이 같은 경우를 보겠습니다. 공시를 까보기 전까진 '정정공시를 하면서 이사회결정일을 변경하거나 했겠구나..' 라고 생각했는데, 모두 까보니 전부 최초이자 최종공시였습니다. 음.. 우리의 분석목적은 왜 이렇게 했는지를 확인하는 것은 아니니.. **②번 구간이 없는 경우가 대부분(0일 또는 다음거래일)**{: style="color: #4682B4;"}이라는 것을 확인한 것으로 하고 넘어가도록 하겠습니다.

<pre>
취득결정일vs취득시작일이 같은 경우 : 6
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>회사명</th>
      <th>접수일</th>
      <th>date_diff</th>
      <th>취득시작일</th>
      <th>시작요일</th>
      <th>취득결정일</th>
      <th>결정요일</th>
      <th>취득예정주식</th>
      <th>취득예정금액</th>
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
      <td>HDC현대EP</td>
      <td>2023-10-27</td>
      <td>0</td>
      <td>2023-10-27</td>
      <td>금</td>
      <td>2023-10-27</td>
      <td>금</td>
      <td>1000000.0</td>
      <td>37.100</td>
      <td>2024년 01월 25일</td>
      <td>-</td>
      <td>-</td>
      <td>주주가치 제고 및 주가 안정화</td>
      <td>유가증권시장을 통한 장내매수(직접 취득)</td>
      <td>2023</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>부광약품</td>
      <td>2020-01-08</td>
      <td>0</td>
      <td>2020-01-08</td>
      <td>수</td>
      <td>2020-01-08</td>
      <td>수</td>
      <td>1916000.0</td>
      <td>250.038</td>
      <td>2020년 04월 07일</td>
      <td>2020년 04월 07일</td>
      <td>2020년 04월 07일</td>
      <td>자기주식 취득 후 소각 예정</td>
      <td>유가증권 시장을 통한 장내 직접 취득</td>
      <td>2020</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>삼익악기</td>
      <td>2021-12-10</td>
      <td>0</td>
      <td>2021-12-10</td>
      <td>금</td>
      <td>2021-12-10</td>
      <td>금</td>
      <td>2500000.0</td>
      <td>43.750</td>
      <td>2022년 03월 09일</td>
      <td>-</td>
      <td>-</td>
      <td>주주가치 제고 및 주가안정화</td>
      <td>장내매수</td>
      <td>2021</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>삼익악기</td>
      <td>2024-02-22</td>
      <td>0</td>
      <td>2024-02-22</td>
      <td>목</td>
      <td>2024-02-22</td>
      <td>목</td>
      <td>5000000.0</td>
      <td>52.500</td>
      <td>2024년 05월 21일</td>
      <td>-</td>
      <td>-</td>
      <td>주주가치 제고 및 주가안정화</td>
      <td>장내매수</td>
      <td>2024</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>아세아</td>
      <td>2020-08-25</td>
      <td>0</td>
      <td>2020-08-25</td>
      <td>화</td>
      <td>2020-08-25</td>
      <td>화</td>
      <td>26490.0</td>
      <td>20.000</td>
      <td>2020년 11월 24일</td>
      <td>-</td>
      <td>-</td>
      <td>주가안정 및 주주가치 제고</td>
      <td>유가증권시장을 통한 장내매수</td>
      <td>2020</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>한국석유공업</td>
      <td>2015-11-03</td>
      <td>0</td>
      <td>2015-11-03</td>
      <td>화</td>
      <td>2015-11-03</td>
      <td>화</td>
      <td>5000.0</td>
      <td>4.995</td>
      <td>2016년 02월 02일</td>
      <td>-</td>
      <td>-</td>
      <td>주가 안정화 및 임직원에 대한 성과급 지급</td>
      <td>장내매수</td>
      <td>2015</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
  </tbody>
</table>
</pre>

![buybackcapture]({{site.url}}/assets/images/2025-03-02-buybackperiod/buybackcapture.png)<br><br>

### 결정~취득시작 거래일차이가 2일이상인 경우는 어디가 있을까?

취득결정을 하고나서 취득시작기간까지 기간이 2일이상인 경우는 총 43건이었습니다. 2일 차이인경우가 33건, 3일 이상인 경우가 10건입니다. 우선 2일 차이가 나는 경우를 확인해보겠습니다. 

<pre>
거래일 차이가 2일인 경우 : 33

상위 10개 행만 확인해보기
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>회사명</th>
      <th>접수일</th>
      <th>date_diff</th>
      <th>취득시작일</th>
      <th>시작요일</th>
      <th>취득결정일</th>
      <th>결정요일</th>
      <th>취득예정주식</th>
      <th>취득예정금액</th>
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
      <td>NAVER</td>
      <td>2018-01-25</td>
      <td>2</td>
      <td>2018-01-26</td>
      <td>금</td>
      <td>2018-01-24</td>
      <td>수</td>
      <td>133858.0</td>
      <td>1189.997620</td>
      <td>2018년 04월 25일</td>
      <td>-</td>
      <td>-</td>
      <td>주가안정 도모 및 주주가치 환원</td>
      <td>장내매수</td>
      <td>2018</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>NAVER</td>
      <td>2019-01-31</td>
      <td>2</td>
      <td>2019-02-01</td>
      <td>금</td>
      <td>2019-01-30</td>
      <td>수</td>
      <td>735295.0</td>
      <td>1000.001200</td>
      <td>2019년 04월 30일</td>
      <td>-</td>
      <td>-</td>
      <td>주가안정 도모 및 주주가치 환원</td>
      <td>장내매수</td>
      <td>2019</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>NAVER</td>
      <td>2024-09-30</td>
      <td>2</td>
      <td>2024-10-02</td>
      <td>수</td>
      <td>2024-09-27</td>
      <td>금</td>
      <td>2347500.0</td>
      <td>4011.877500</td>
      <td>2024년 12월 28일</td>
      <td>-</td>
      <td>-</td>
      <td>이익소각</td>
      <td>장내매수</td>
      <td>2024</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>SK스퀘어</td>
      <td>2024-11-21</td>
      <td>2</td>
      <td>2024-11-25</td>
      <td>월</td>
      <td>2024-11-21</td>
      <td>목</td>
      <td>1253132.0</td>
      <td>1000.000000</td>
      <td>2025년 02월 24일</td>
      <td>-</td>
      <td>-</td>
      <td>주주가치 제고</td>
      <td>유가증권 시장을 통한 직접 취득</td>
      <td>2024</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>대원제약</td>
      <td>2020-03-24</td>
      <td>2</td>
      <td>2020-03-26</td>
      <td>목</td>
      <td>2020-03-24</td>
      <td>화</td>
      <td>492611.0</td>
      <td>50.000017</td>
      <td>2020년 06월 25일</td>
      <td>-</td>
      <td>-</td>
      <td>주가 안정을 통한 주주가치 제고</td>
      <td>장내매수</td>
      <td>2020</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>무학</td>
      <td>2020-03-26</td>
      <td>2</td>
      <td>2020-03-30</td>
      <td>월</td>
      <td>2020-03-26</td>
      <td>목</td>
      <td>500000.0</td>
      <td>20.450000</td>
      <td>2020년 06월 29일</td>
      <td>-</td>
      <td>-</td>
      <td>주가안정 및 주주가치 제고</td>
      <td>유가증권시장을 통한 직접 취득</td>
      <td>2020</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>무학</td>
      <td>2021-11-09</td>
      <td>2</td>
      <td>2021-11-10</td>
      <td>수</td>
      <td>2021-11-08</td>
      <td>월</td>
      <td>700000.0</td>
      <td>59.850000</td>
      <td>2022년 02월 09일</td>
      <td>-</td>
      <td>-</td>
      <td>주가안정 및 주주가치 제고</td>
      <td>유가증권시장을 통한 직접 취득</td>
      <td>2021</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>미원상사</td>
      <td>2015-04-15</td>
      <td>2</td>
      <td>2015-04-17</td>
      <td>금</td>
      <td>2015-04-15</td>
      <td>수</td>
      <td>4000.0</td>
      <td>6.880000</td>
      <td>2015년 07월 16일</td>
      <td>-</td>
      <td>-</td>
      <td>주가안정 및 주주가치 제고</td>
      <td>유가증권시장을 통한 직접 취득</td>
      <td>2015</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>미원상사</td>
      <td>2015-07-09</td>
      <td>2</td>
      <td>2015-07-10</td>
      <td>금</td>
      <td>2015-07-08</td>
      <td>수</td>
      <td>4000.0</td>
      <td>6.860000</td>
      <td>2015년 10월 09일</td>
      <td>-</td>
      <td>-</td>
      <td>주가안정 및 주주가치 제고</td>
      <td>유가증권시장을 통한 직접 취득</td>
      <td>2015</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>미원상사</td>
      <td>2015-10-15</td>
      <td>2</td>
      <td>2015-10-16</td>
      <td>금</td>
      <td>2015-10-14</td>
      <td>수</td>
      <td>4000.0</td>
      <td>7.060000</td>
      <td>2016년 01월 15일</td>
      <td>-</td>
      <td>-</td>
      <td>이익소각</td>
      <td>유가증권시장을 통한 직접 취득</td>
      <td>2015</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
  </tbody>
</table>
</pre>


거래일 차이가 3일 이상인 경우는 총 10건이었고, 30일이 넘는 경우도 존재하였습니다.


<pre>
거래일 차이가 3일 이상인 경우 : 10

<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>회사명</th>
      <th>접수일</th>
      <th>date_diff</th>
      <th>취득시작일</th>
      <th>시작요일</th>
      <th>취득결정일</th>
      <th>결정요일</th>
      <th>취득예정주식</th>
      <th>취득예정금액</th>
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
      <td>HD현대건설기계</td>
      <td>2018-11-02</td>
      <td>13</td>
      <td>2018-11-21</td>
      <td>수</td>
      <td>2018-11-02</td>
      <td>금</td>
      <td>592000.0</td>
      <td>214.304000</td>
      <td>2019년 02월 01일</td>
      <td>-</td>
      <td>-</td>
      <td>주가 안정 도모 및 주주가치 제고</td>
      <td>유가증권시장을 통한 장내매수</td>
      <td>2018</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>TYM</td>
      <td>2023-08-10</td>
      <td>3</td>
      <td>2023-08-16</td>
      <td>수</td>
      <td>2023-08-10</td>
      <td>목</td>
      <td>809061.0</td>
      <td>49.999970</td>
      <td>2023년 11월 15일</td>
      <td>-</td>
      <td>-</td>
      <td>주주가치 제고</td>
      <td>유가증권 시장을 통한 장내매수</td>
      <td>2023</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>극동유화</td>
      <td>2017-02-28</td>
      <td>3</td>
      <td>2017-03-06</td>
      <td>월</td>
      <td>2017-02-28</td>
      <td>화</td>
      <td>1200000.0</td>
      <td>41.280000</td>
      <td>2017년 06월 05일</td>
      <td>-</td>
      <td>-</td>
      <td>주식가격 안정 및 주주가치 제고</td>
      <td>장내 직접취득</td>
      <td>2017</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>두산밥캣</td>
      <td>2025-02-21</td>
      <td>3</td>
      <td>2024-12-19</td>
      <td>목</td>
      <td>2024-12-16</td>
      <td>월</td>
      <td>4393101.0</td>
      <td>1999.975026</td>
      <td>2025년 02월 19일</td>
      <td>-</td>
      <td>-</td>
      <td>자기주식 소각을 통한 주주가치 제고</td>
      <td>장내매수</td>
      <td>2024</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>아모레퍼시픽</td>
      <td>2021-10-29</td>
      <td>24</td>
      <td>2021-12-02</td>
      <td>목</td>
      <td>2021-10-29</td>
      <td>금</td>
      <td>107817.0</td>
      <td>200.000535</td>
      <td>2022년 01월 28일</td>
      <td>-</td>
      <td>-</td>
      <td>임직원 성과보상 지급 및 장기근속자 포상</td>
      <td>유가증권시장 장내매수</td>
      <td>2021</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>아모레퍼시픽</td>
      <td>2023-10-31</td>
      <td>6</td>
      <td>2023-11-07</td>
      <td>화</td>
      <td>2023-10-30</td>
      <td>월</td>
      <td>85471.0</td>
      <td>100.001070</td>
      <td>2024년 01월 30일</td>
      <td>-</td>
      <td>-</td>
      <td>임직원 성과보상 지급 및 장기근속자 포상</td>
      <td>유가증권시장 장내매수</td>
      <td>2023</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>에이리츠</td>
      <td>2021-10-01</td>
      <td>28</td>
      <td>2021-11-12</td>
      <td>금</td>
      <td>2021-10-01</td>
      <td>금</td>
      <td>90498.0</td>
      <td>10.000029</td>
      <td>2022년 11월 11일</td>
      <td>-</td>
      <td>-</td>
      <td>주가 안정 및 주주가치 제고</td>
      <td>유가증권시장을 통한 장내 직접취득</td>
      <td>2021</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>케이탑리츠</td>
      <td>2020-04-21</td>
      <td>31</td>
      <td>2020-06-08</td>
      <td>월</td>
      <td>2020-04-21</td>
      <td>화</td>
      <td>1852000.0</td>
      <td>15.001200</td>
      <td>2021년 06월 07일</td>
      <td>-</td>
      <td>-</td>
      <td>주가안정 및 주주가치 제고</td>
      <td>유가증권시장을 통한 장내 직접취득</td>
      <td>2020</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>케이탑리츠</td>
      <td>2024-03-07</td>
      <td>18</td>
      <td>2024-04-01</td>
      <td>월</td>
      <td>2024-03-06</td>
      <td>수</td>
      <td>2000000.0</td>
      <td>19.700000</td>
      <td>2025년 03월 31일</td>
      <td>-</td>
      <td>-</td>
      <td>주가안정을 통한 주주가치 제고</td>
      <td>장내 매수</td>
      <td>2024</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
    <tr>
      <td>한익스프레스</td>
      <td>2022-10-26</td>
      <td>4</td>
      <td>2022-11-01</td>
      <td>화</td>
      <td>2022-10-26</td>
      <td>수</td>
      <td>200000.0</td>
      <td>8.570000</td>
      <td>2023년 01월 31일</td>
      <td>-</td>
      <td>-</td>
      <td>주가 안정을 통한 주주가치 제고</td>
      <td>장내매수</td>
      <td>2022</td>
      <td>mkt</td>
      <td>not_bd</td>
    </tr>
  </tbody>
</table>
</pre>


적은 숫자이긴 하지만, 취득 결정부터 취득 시작까지 긴 기간을 둔 회사들은 왜 그런 것일까요? 다음에 차차 확인해보도록 하겠습니다. 