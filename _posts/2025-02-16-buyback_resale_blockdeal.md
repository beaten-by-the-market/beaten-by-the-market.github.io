---
layout: single
title:  "자사주 처분: 시간외대량매매의 비중은 얼마일까?"
categories: 한국시장
tag: [자기주식, opendart]
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
**[관련 포스팅]** [10년간 코스피 자사주 직접취득 현황(시사점)](https://beaten-by-the-market.github.io/%ED%95%9C%EA%B5%AD%EC%8B%9C%EC%9E%A5/kospi-buyback-insight/)<br>
**[관련 포스팅]** [10년간 코스피 자사주 직접 ‘처분’ 현황(시사점)](https://beaten-by-the-market.github.io/%ED%95%9C%EA%B5%AD%EC%8B%9C%EC%9E%A5/kospi_dart_buyback_resale/)<br>
**[관련 포스팅]** [자사주 매입: 시간외대량매매의 비중은 얼마일까?](https://beaten-by-the-market.github.io/%EA%B5%AD%EB%82%B4%EC%8B%9C%EC%9E%A5/buyback_blockdeal/)
{:.notice--success}



## 자사주 **처분**{: style="color: #4682B4;"}에서 시간외대량매매는 얼마나 있을까?

앞서 우리는 자기주식을 **매입**{: style="color: #4682B4;"}하는 사유로 기업이 가장 많이 공시하는 것은 **주식 가치 제고**{: style="color: #4682B4;"}이므로 **장내에서 많이 매수할 것이라 추측해보았습니다.**{: style="color: #4682B4;"} 그리고 **실제로 전수조사를 통해 자기주식 매입에 시간외대량매매는 사실상 이용되지 않는다는 것을 확인했습니다.**{: style="color: #4682B4;"}<br>

이번에는 자기주식을 처분할 때 시간외대량매매의 비중이 얼마나 될지를 알아보도록 하겠습니다. 자기주식을 부득이하게 처분해야할 때 회사는 주가가 최대한 하락하지 않길 원하기 때문에 **자사주를 매도할 때는 장내가 아닌 방식으로, 예를 들어 시간외대량매매를 활용할 수 있겠다는 추측을 해볼 수 있습니다.**{: style="color: #4682B4;"} 시장 전수조사를 통해 확인해보도록 하겠습니다.



### (복습) **시간외대량매매**란?

이전 포스팅의 [**시간외대량매매란?(링크)**{: style="color: #4682B4;"}](https://beaten-by-the-market.github.io/%EA%B5%AD%EB%82%B4%EC%8B%9C%EC%9E%A5/buyback_blockdeal/#%EC%8B%9C%EA%B0%84%EC%99%B8%EB%8C%80%EB%9F%89%EB%A7%A4%EB%A7%A4%EB%9E%80) 를 통해 확인하실 수 있습니다.


## 코스피 자기주식 **직접 처분** 통계 불러오기

우리는 이전에 포스팅한 [**10년간 코스피 자사주 직접 ‘처분’ 현황(링크)**{: style="color: #4682B4;"}](https://beaten-by-the-market.github.io/%ED%95%9C%EA%B5%AD%EC%8B%9C%EC%9E%A5/kospi_dart_buyback_resale/)에서 코스피시장의 자기주식 처분현황을 확인한 바 있었습니다. 처분현황을 조사하는 과정에서 확인한 포인트를 짧게 wrap-up해보겠습니다.

1. 취득공시와 달리 **처분공시**{: style="color: #4682B4;"}는 **주식의 매매방법을 세분화**{: style="color: #4682B4;"}해놓았습니다.<br>
* 자사주취득공시 : 처분방식을 ***하나의 칸에 free text로 기재***합니다.
* 자사주처분공시 : 처분방식을 ***시장, 시간외대량, 장외, 기타로 구분***을 하였고, 각각의 방식으로 처분할 수량을 기재하도록 하였습니다.<br>
↪ **처분공시 서식에서는 데이터 활용성이 높아졌습니다!**<br>
2. 최종공시에도 **오타가 존재**{: style="color: #4682B4;"}하였습니다.<br>***가장 중요한 숫자(처분예정수량 합계와 처분예정금액 합계)***에는 오타가 없었습니다만, **처분방법별 수량을 기재하는 과정에서 2개의 상장사가 오타**{: style="color: #4682B4;"}를 냈습니다. 그 오타의 수준이 매우 커서 데이터 전체가 왜곡되었습니다. <br>

어떤 사유로 오타를 냈는지 확인이 불가능했다면 데이터 분석 자체를 진행하기 힘들었겠지만, **다행히도 두 케이스 모두 오타의 사유가 추정가능했고, 데이터를 전처리하여 분석을 진행**했습니다.




### 자사주 직접처분 데이터 시각화

우선 코스피시장의 전체적인 처분수량과 처분금액의 시각화 결과는 다음과 같았습니다.

![kospi_resale]({{site.url}}/assets/images/2025-02-16-blockdeal/kospi_resale.png)



### 공시에서 발견된 오타들!

이전 포스팅의 [**공시에서 발견된 오타들!(링크)**{: style="color: #4682B4;"}](https://beaten-by-the-market.github.io/%ED%95%9C%EA%B5%AD%EC%8B%9C%EC%9E%A5/kospi_dart_buyback_resale/#%EA%B3%B5%EC%8B%9C%EC%97%90%EC%84%9C-%EB%B0%9C%EA%B2%AC%EB%90%9C-%EC%98%A4%ED%83%80%EB%93%A4)에서는 카카오와 TP의 공시에 오타가 있어 시각화 결과가 왜곡되는 것을 발견한 적이 있습니다. 우선 카카오의 사례입니다.<br>


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
      <td>2021-11-04</td>
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
      <td>2021-11-16</td>
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
      <td>2021-09-01</td>
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
      <td>2021-07-23</td>
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
      <td>2021-10-15</td>
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
<br>
그다음은 TP의 사례입니다.


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
      <td>2023-04-20</td>
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
      <td>2023-04-11</td>
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
      <td>2023-09-22</td>
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
      <td>2023-03-31</td>
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
      <td>2023-05-12</td>
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

<br>
처분예정금액을 기타 수량에 기재한 실수로 확인되어, 카카오와 TP의 오타를 각각 수정해주었습니다.



### 처분방법별 자사주 처분 시각화

이제 시각화를 실행해 봅니다.

![kospi_resale_with_label]({{site.url}}/assets/images/2025-02-16-blockdeal/kospi_resale_with_label.png)

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
      <td>7,806,748</td>
      <td>16,664,682</td>
    </tr>
    <tr>
      <td>2016</td>
      <td>294,003</td>
      <td>25,968,389</td>
      <td>18,712,752</td>
      <td>12,111,177</td>
    </tr>
    <tr>
      <td>2017</td>
      <td>2,326,848</td>
      <td>54,013,232</td>
      <td>7,990,151</td>
      <td>9,580,392</td>
    </tr>
    <tr>
      <td>2018</td>
      <td>40,406</td>
      <td>34,524,186</td>
      <td>7,851,419</td>
      <td>18,768,732</td>
    </tr>
    <tr>
      <td>2019</td>
      <td>1,284,314</td>
      <td>19,285,874</td>
      <td>21,949,696</td>
      <td>6,989,774</td>
    </tr>
    <tr>
      <td>2020</td>
      <td>564,590</td>
      <td>45,215,194</td>
      <td>25,351,606</td>
      <td>13,683,181</td>
    </tr>
    <tr>
      <td>2021</td>
      <td>126,896</td>
      <td>16,399,457</td>
      <td>12,301,222</td>
      <td>22,556,112</td>
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
      <td>39,982,108</td>
    </tr>
    <tr>
      <td>2024</td>
      <td>24,167</td>
      <td>22,883,456</td>
      <td>19,154,271</td>
      <td>26,316,389</td>
    </tr>
  </tbody>
</table>
</pre>

### 시간외대량매매의 목적

자사주 취득시에는 사용되지 않던 시간외대량매매가 자사주를 처분할 때는 상당히 많이 쓰인 것을 확인할 수 있습니다. <br>
참고차원에서 전체 처분금액이 많은 상위 10개의 데이터를 한번 확인해 보겠습니다. 금액 상위의 경우, **파트너십 구축**{: style="color: #4682B4;"}을 위한 자기주식 시간외대량매매가 많았던 것을 확인할 수 있습니다. 그리고 **자금조달을 위한 목적**{: style="color: #4682B4;"}도 2건 있습니다.

<pre>
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>회사명</th>
      <th>접수일</th>
      <th>처분예정금액(억원)</th>
      <th>처분예정주식</th>
      <th>시간외대량매매</th>
      <th>연도</th>
      <th>처분시작일</th>
      <th>처분종료일</th>
      <th>처분목적</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>고려아연</td>
      <td>2022-11-24</td>
      <td>7,868</td>
      <td>1,195,760</td>
      <td>406,994</td>
      <td>2022</td>
      <td>2022-11-24</td>
      <td>2023년 02월 23일</td>
      <td>사업 제휴 강화를 위한 전략적 파트너십 관계 구축 및 중장기 사업계획 추진을 위한 투자자금 확보</td>
    </tr>
    <tr>
      <td>NAVER</td>
      <td>2020-10-26</td>
      <td>5,999</td>
      <td>2,094,240</td>
      <td>1,570,680</td>
      <td>2020</td>
      <td>2020-10-27</td>
      <td>2020년 11월 27일</td>
      <td>CJ 대한통운, CJ ENM, 스튜디오 드래곤과의 자사주 교환 및 현물출자를 통해 전략적 사업제휴 관계를 강화하고 유지하기 위함</td>
    </tr>
    <tr>
      <td>미래에셋증권</td>
      <td>2017-06-26</td>
      <td>4,999</td>
      <td>47,393,364</td>
      <td>47,393,364</td>
      <td>2017</td>
      <td>2017-06-27</td>
      <td>2017년 06월 27일</td>
      <td>네이버(주)와의 전략적 제휴를 위한 자기주식 상호매입</td>
    </tr>
    <tr>
      <td>NAVER</td>
      <td>2017-06-26</td>
      <td>4,999</td>
      <td>563,063</td>
      <td>563,063</td>
      <td>2017</td>
      <td>2017-06-27</td>
      <td>2017년 06월 27일</td>
      <td>미래에셋대우㈜와의 전략적 제휴를 통한 글로벌 진출 및 공동사업 추진 등</td>
    </tr>
    <tr>
      <td>CJ대한통운</td>
      <td>2020-10-26</td>
      <td>2,999</td>
      <td>1,791,044</td>
      <td>1,791,044</td>
      <td>2020</td>
      <td>2020-10-27</td>
      <td>2020년 10월 27일</td>
      <td>네이버(주)와의 자사주 교환을 통한 전략적 사업제휴 관계 강화 및 유지</td>
    </tr>
    <tr>
      <td>엘앤에프</td>
      <td>2022-05-24</td>
      <td>2,766</td>
      <td>1,000,000</td>
      <td>1,000,000</td>
      <td>2022</td>
      <td>2022-05-24</td>
      <td>2022년 08월 23일</td>
      <td>해외투자자금 및 시설/운영자금의 조달</td>
    </tr>
    <tr>
      <td>LG화학</td>
      <td>2022-11-23</td>
      <td>2,524</td>
      <td>367,529</td>
      <td>367,529</td>
      <td>2022</td>
      <td>2022-11-24</td>
      <td>2023년 02월 23일</td>
      <td>2차 전지소재 사업 제휴 강화를 위한 전략적 파트너십 관계 구축</td>
    </tr>
    <tr>
      <td>NAVER</td>
      <td>2021-03-16</td>
      <td>2,500</td>
      <td>648,510</td>
      <td>648,510</td>
      <td>2021</td>
      <td>2021-03-17</td>
      <td>2021년 03월 17일</td>
      <td>온·오프라인 커머스 역량 강화를 위한 전략적 제휴</td>
    </tr>
    <tr>
      <td>롯데케미칼</td>
      <td>2017-02-21</td>
      <td>2,202</td>
      <td>583,388</td>
      <td>583,388</td>
      <td>2017</td>
      <td>2017-02-22</td>
      <td>2017년 05월 19일</td>
      <td>2012년 12월 27일 (舊)호남석유화학(주)와 (주)케이피케미칼 합병 시 케이피케미칼 주주의 주식매수청구권행사에 의하여 취득한 자기주식의 처분</td>
    </tr>
    <tr>
      <td>신풍제약</td>
      <td>2020-09-22</td>
      <td>2,153</td>
      <td>1,289,550</td>
      <td>1,289,550</td>
      <td>2020</td>
      <td>2020-09-22</td>
      <td>2020년 09월 22일</td>
      <td>생산설비 개선 및 연구개발과제 투자 자금 확보</td>
    </tr>
  </tbody>
</table>
</pre>

## 코스닥 자기주식 **직접 처분** 통계 불러오기

이번에는 코스닥시장의 자기주식 직접처분 통계를 보겠습니다. 코스닥 시장의 자기주식 처분 포스팅은 따로 한적이 없으므로 그 과정을 좀 더 설명하겠습니다.



### 자사주 직접처분 데이터 시각화

 코스피 시장과 마찬가지 절차로 데이터를 불러오고 시각화를 바로 실행하겠습니다.

![2106plot]({{site.url}}/assets/images/2025-02-16-blockdeal/2106plot.png)

<br>
헉... 처분시점을 무려 2106년으로 기재한 경우가 보입니다. 어느 회사일까요?



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
      <td>알티캐스트</td>
      <td>2016-01-08</td>
      <td>58772.0</td>
      <td>2.915091</td>
      <td>2106-01-08</td>
      <td>2016년 01월 21일</td>
      <td>2014년 약정분 주식보상성과급 지급(2014년 직원 성과급 중 주식보상분을 자기주식으로 지급)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>58772</td>
      <td>2106</td>
    </tr>
  </tbody>
</table>
</pre>

알티캐스트입니다. 2016을 오타낸 것으로 추정이 가능하므로 수정해주도록 하겠습니다.


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
      <td>알티캐스트</td>
      <td>2016-01-08</td>
      <td>58772.0</td>
      <td>2.915091</td>
      <td>2016-01-08</td>
      <td>2016년 01월 21일</td>
      <td>2014년 약정분 주식보상성과급 지급(2014년 직원 성과급 중 주식보상분을 자기주식으로 지급)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>58772</td>
      <td>2016</td>
    </tr>
  </tbody>
</table>
</pre>

오타를 수정했으니 다시 그래프를 확인해보겠습니다.

![kosdaq_resale]({{site.url}}/assets/images/2025-02-16-blockdeal/kosdaq_resale.png)

<br>
그래프의 이 모습을 기억해놓아야 합니다. 앞으로 처분방식별로 구분한 그래프를 그렸을 때 그 합계가 지금의 그래프와 모양이 다르다면 다른 오타가 존재한다는 것입니다.




### 공시에서 발견된 오타들!

시각화를 해서 보던 중, 아래와 같은 그림이 그려졌습니다.

![kosdaq_resale_error]({{site.url}}/assets/images/2025-02-16-blockdeal/kosdaq_resale_error.png)

<br>

그래프가 앞서 그렸던 것과 다릅니다. 그래프의 모양은 동일하고 그 안에서만 색깔이 달라야 하는데, 이렇게 형태 자체가 달라져버린 것은 왜일까요? 처분방식별 수량을 입력하는 과정에서 오타가 난 것이라고 추정해볼 수 있습니다. 일단 2020년의 장외매매 수량이 상당히 높은 수치를 나타내고 있으니 이걸 확인해보겠습니다. <br>



따라서 아래와 같이 필터를 적용해서 데이터를 직접 확인해보겠습니다. 2020년 데이터 중, 처분방법이 시간외대량매매인 것을 기준으로 내림차순으로 정리해 봅니다.


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
      <td>유아이디</td>
      <td>2020-07-02</td>
      <td>94787.0</td>
      <td>1.000003</td>
      <td>2020-07-03</td>
      <td>2020년 10월 02일</td>
      <td>운영자금 확보</td>
      <td>0</td>
      <td>0</td>
      <td>100,000,285</td>
      <td>0</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>한성크린텍</td>
      <td>2020-12-15</td>
      <td>9243937.0</td>
      <td>52.320683</td>
      <td>2020-12-16</td>
      <td>2020년 12월 31일</td>
      <td>운영자금 및 투자자금 확보</td>
      <td>0</td>
      <td>0</td>
      <td>9,243,937</td>
      <td>0</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>동일스틸럭스</td>
      <td>2020-12-15</td>
      <td>1000000.0</td>
      <td>55.800000</td>
      <td>2020-12-16</td>
      <td>2020년 12월 16일</td>
      <td>유통주식수 확대 및 거래활성화</td>
      <td>0</td>
      <td>0</td>
      <td>1,000,000</td>
      <td>0</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>하이즈항공</td>
      <td>2020-12-14</td>
      <td>900000.0</td>
      <td>49.320000</td>
      <td>2020-12-14</td>
      <td>2020년 12월 14일</td>
      <td>투자재원 확보</td>
      <td>0</td>
      <td>0</td>
      <td>900,000</td>
      <td>0</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>디엔에프</td>
      <td>2020-06-15</td>
      <td>600000.0</td>
      <td>79.200000</td>
      <td>2020-06-16</td>
      <td>2020년 07월 01일</td>
      <td>사업 다각화 및 경쟁력 강화를 위한 피인수회사 주식 취득 목적의 당사 자기주식 교환</td>
      <td>0</td>
      <td>0</td>
      <td>600,000</td>
      <td>0</td>
      <td>2020</td>
    </tr>
  </tbody>
</table>
</pre>

2020.7.2에 제출된 유아이디의 공시에 오타가 있음을 알 수 있습니다. 전체 처분예정 주식수를 94,787주라고 기재하고선, 장외매매 수량을 100,000,285주라고 하였네요. 100,000,285는 처분예정금액을 나타내는 수치입니다. 코스피시장의 카카오, TP와 동일한 실수를 저질렀습니다. 숫자를 수정해주도록 하겠습니다.


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
      <td>유아이디</td>
      <td>2020-07-02</td>
      <td>94787.0</td>
      <td>1.000003</td>
      <td>2020-07-03</td>
      <td>2020년 10월 02일</td>
      <td>운영자금 확보</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>94787.0</td>
      <td>0.0</td>
      <td>2020</td>
    </tr>
  </tbody>
</table>
</pre>

### 처분방법별 자사주 처분 시각화

잘 반영된 것 같으니, 이제 다시 시각화를 실행해 보겠습니다.



![comparison]({{site.url}}/assets/images/2025-02-16-blockdeal/comparison.png)<br><br>



오! 이전에 그렸던 그림과 비교하니 이제 맞는 바차트가 나왔습니다. 데이터레이블을 추가해 보겠습니다.

![kosdaq_resale_with_label]({{site.url}}/assets/images/2025-02-16-blockdeal/kosdaq_resale_with_label.png)<br><br>



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
      <td>3,823,928</td>
      <td>13,963,064</td>
      <td>9,141,530</td>
      <td>12,542,702</td>
    </tr>
    <tr>
      <td>2016</td>
      <td>8,063,229</td>
      <td>15,264,438</td>
      <td>12,933,541</td>
      <td>9,209,855</td>
    </tr>
    <tr>
      <td>2017</td>
      <td>2,247,160</td>
      <td>14,735,479</td>
      <td>5,559,840</td>
      <td>8,830,739</td>
    </tr>
    <tr>
      <td>2018</td>
      <td>4,901,213</td>
      <td>6,340,944</td>
      <td>10,539,369</td>
      <td>12,446,373</td>
    </tr>
    <tr>
      <td>2019</td>
      <td>406,028</td>
      <td>6,374,341</td>
      <td>10,676,697</td>
      <td>5,364,892</td>
    </tr>
    <tr>
      <td>2020</td>
      <td>3,430,470</td>
      <td>21,012,520</td>
      <td>14,575,183</td>
      <td>19,176,158</td>
    </tr>
    <tr>
      <td>2021</td>
      <td>3,518,210</td>
      <td>34,561,401</td>
      <td>7,707,742</td>
      <td>32,449,538</td>
    </tr>
    <tr>
      <td>2022</td>
      <td>60,089</td>
      <td>6,788,534</td>
      <td>4,254,270</td>
      <td>28,435,726</td>
    </tr>
    <tr>
      <td>2023</td>
      <td>155,152</td>
      <td>6,052,966</td>
      <td>8,573,757</td>
      <td>39,186,479</td>
    </tr>
    <tr>
      <td>2024</td>
      <td>3,357,693</td>
      <td>13,035,518</td>
      <td>16,707,420</td>
      <td>47,777,189</td>
    </tr>
    <tr>
      <td>2025</td>
      <td>6,211</td>
      <td>0</td>
      <td>0</td>
      <td>894,217</td>
    </tr>
  </tbody>
</table>
</pre>

### 시간외대량매매의 목적

코스피와 마찬가지입니다. 자사주 취득시에는 사용되지 않던 시간외대량매매가 자사주를 처분할 때는 상당히 많이 쓰인 것을 확인할 수 있습니다. <br>
참고차원에서 전체 처분금액이 많은 상위 10개의 데이터를 한번 확인해 보겠습니다. 금액 상위의 경우 처분목적이 코스피와 차이가 있습니다. 코스닥의 경우에는 **자금조달**{: style="color: #4682B4;"}을 위한 자기주식 시간외대량매매가 많았던 것을 확인할 수 있습니다. 그리고 **파트너십**{: style="color: #4682B4;"}도 1건(CJ ENM) 있습니다.


<pre>
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>회사명</th>
      <th>접수일</th>
      <th>처분예정금액(억원)</th>
      <th>처분예정주식</th>
      <th>시간외대량매매</th>
      <th>연도</th>
      <th>처분시작일</th>
      <th>처분종료일</th>
      <th>처분목적</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CJ ENM</td>
      <td>2020-10-26</td>
      <td>1,499</td>
      <td>1,095,690</td>
      <td>1,095,690</td>
      <td>2020</td>
      <td>2020-10-27</td>
      <td>2020년 10월 27일</td>
      <td>사업 협력 위한 지분교환</td>
    </tr>
    <tr>
      <td>에스에프에이</td>
      <td>2020-09-25</td>
      <td>1,009</td>
      <td>2,753,092</td>
      <td>2,753,092</td>
      <td>2020</td>
      <td>2020-09-26</td>
      <td>2020년 12월 25일</td>
      <td>금융시장 불확실성 대비 등 유동성 확대</td>
    </tr>
    <tr>
      <td>삼천당제약</td>
      <td>2024-06-17</td>
      <td>609</td>
      <td>500,000</td>
      <td>500,000</td>
      <td>2024</td>
      <td>2024-06-18</td>
      <td>2024년 07월 17일</td>
      <td>- 아일리아 고용량 바이오시밀러 및 경구용 GLP-1 글로벌 임상 비용 - 경구용 GLP-1 생산설비 투자</td>
    </tr>
    <tr>
      <td>동화기업</td>
      <td>2015-05-28</td>
      <td>499</td>
      <td>1,000,000</td>
      <td>1,000,000</td>
      <td>2015</td>
      <td>2015-05-28</td>
      <td>2015년 06월 30일</td>
      <td>자본효율성 제고 및 유통주식 물량증대를 통한 주식거래 활성화</td>
    </tr>
    <tr>
      <td>에스에프에이</td>
      <td>2017-05-22</td>
      <td>435</td>
      <td>489,367</td>
      <td>489,367</td>
      <td>2017</td>
      <td>2017-05-23</td>
      <td>2017년 08월 22일</td>
      <td>자사 주식가격의 안정 등 취득목적 달성, 운영자금의 조달</td>
    </tr>
    <tr>
      <td>고영</td>
      <td>2018-01-19</td>
      <td>424</td>
      <td>505,200</td>
      <td>505,200</td>
      <td>2018</td>
      <td>2018-01-22</td>
      <td>2018년 01월 22일</td>
      <td>경영권 안정 및 재무건전성 강화</td>
    </tr>
    <tr>
      <td>덕산하이메탈</td>
      <td>2022-01-14</td>
      <td>269</td>
      <td>1,380,123</td>
      <td>1,380,123</td>
      <td>2022</td>
      <td>2022-01-17</td>
      <td>2022년 01월 17일</td>
      <td>설비 증설 및 운영자금확보</td>
    </tr>
    <tr>
      <td>천보</td>
      <td>2021-09-14</td>
      <td>261</td>
      <td>95,877</td>
      <td>95,877</td>
      <td>2021</td>
      <td>2021-09-15</td>
      <td>2021년 09월 15일</td>
      <td>(주)천보BLS 새만금 투자자금 확보</td>
    </tr>
    <tr>
      <td>원익IPS</td>
      <td>2023-11-30</td>
      <td>258</td>
      <td>800,327</td>
      <td>800,327</td>
      <td>2023</td>
      <td>2023-12-01</td>
      <td>2023년 12월 01일</td>
      <td>주식매수청구권 행사로 취득한 자기주식의 기한 내 처분 (자본시장법 제165조의5)</td>
    </tr>
    <tr>
      <td>티케이케미칼</td>
      <td>2021-04-20</td>
      <td>249</td>
      <td>4,675,998</td>
      <td>4,675,998</td>
      <td>2021</td>
      <td>2021-04-20</td>
      <td>2021년 05월 19일</td>
      <td>재무구조 개선 및 대한해운 유상증자 재원 확보</td>
    </tr>
  </tbody>
</table>
</pre>

## (결론) 시간외대량매매 방식의 자사주 처분은 꽤 있다.

위의 결과를 보면, 코스피든 코스닥이든 시간외대량매매 방식으로 자사주를 처분하는 것은 매우 자주 사용되는 방식임을 알 수 있습니다.<br><br>

지난 [포스팅(링크)](https://beaten-by-the-market.github.io/%EA%B5%AD%EB%82%B4%EC%8B%9C%EC%9E%A5/buyback_blockdeal/#%EC%9E%90%EA%B8%B0%EC%A3%BC%EC%8B%9D-%EA%B1%B0%EB%9E%98%EC%97%90%EC%84%9C-%EC%8B%9C%EA%B0%84%EC%99%B8%EB%8C%80%EB%9F%89%EB%A7%A4%EB%A7%A4%EC%9D%98-%EC%9D%98%EC%9D%98)에서 이렇게 추정한 적이 있습니다.<br>

* **자사주 매입**{: style="color: #4682B4;"} : 자사주 매입을 통해 **주가를 끌어올릴 수 있으려면 아무래도 호가 제출을 통한 장내매매가 주요한 방법**{: style="color: #4682B4;"}이고, **시간외대량매매는 적을 것이다.**{: style="color: #4682B4;"}<br>

* **자사주 매각**{: style="color: #4682B4;"} : **'우리회사의 주가'를 떨어뜨리지 않기 위해 장내매매는 많이 사용되지 않을 것이다. 주가에 영향을 미치지 않는 시간외대량매매가 많이 사용될 것**{: style="color: #4682B4;"}이다.


시장 전수조사를 통해 결과를 보니 정말 그러합니다!

