---
layout: single
title:  "자사주 취득의 데이터는 어디서 구할까? (1편)"
categories: 한국시장
tag: [data background, opendart, 자기주식]
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




## 자사주 매매의 프로세스는?


![buyback_process]({{site.url}}/assets/images/2025-01-21-buybackexpl/buyback_process.png)
   
> "의사결정 → 실행 → 결과확인"의 기본적인 틀로 이루어집니다.
   
   
## 1. 의사결정

   
회사는 자기주식을 취득/처분하기로 이사회에서 결정하면, 당일 금융감독원에 **"주요사항보고서"**{: style="color: #4682B4;"}를 제출합니다. 이는 자본시장법에 따른 의무사항입니다. 거래소 공시규정상 의무사항이기도 하지요. 자기주식 취득결정에 따른 주요사항보고서의 사례를 하나 보겠습니다.    
금융감독원 전자공시시스템에서 주요사항보고서를 선택하고, 공시명에 "자기주식"을 입력하여 검색하면 관련 공시들을 확인할 수 있습니다.   <br>

![search_example]({{site.url}}/assets/images/2025-01-21-buybackexpl/search_example.jpg)<br>
<br>
예시로 2025년 1월 20일에 제출된 엠씨넥스라는 코스피 상장법인의 공시를 클릭해보겠습니다.<br>

![example1]({{site.url}}/assets/images/2025-01-21-buybackexpl/example1.jpg)
<br>
<br>

**취득예정주식수, 취득예정금액, 취득예상기간, 취득목적, 취득방법**{: style="color: #4682B4;"} 등이 기재되어 있습니다.     
한편, 장내에서 취득하는 경우 주가는 계속 변할 수 있습니다. 따라서 취득예정금액의 경우, 이사회 결의시점에 기준이 되는 주가를 정하여 산정한 금액입니다. 따라서 실제 취득금액과는 당연히 차이가 날 수밖에 없는 부분입니다. 예시로 본 공시에서는 이사회결의일 전일 종가를 기준으로 곱하였네요.<br>
<br>

***공시내용 中***{: style="color: gray;"}<br>
***"11. 기타 투자판단에 참고할 사항: 상기'2. 취득예정금액'은 이사회결의일 전일 종가에 취득예정 주식수를 곱한 금액이며, 향후 주가의 변동에 따라 실제 취득금액은 변경될 수 있습니다. (2025년 01월 17일 종가: 20,850원)"***{: style="color: gray;"}<br>
<br>
취득예정주식수도 이사회의 결정시점의 수량입니다. 실제로 취득하는 수량은 약 3개월의 기간동안 회사의 사정으로 인해 그만큼 취득하지 않을 수도 있습니다.   
   
## 2. 실행
    
실행단계, 즉 매매를 하는 과정은 크게 **장내취득**{: style="color: #4682B4;"}과 **장외취득**{: style="color: #4682B4;"}으로 이뤄집니다. 장내에서 취득할지, 장외에서 취득할지는 앞선 '1. 의사결정' 단계에서 정해서 공시가 됩니다.<br>

### 장내에서 취득하는 경우
거래소는 시장입니다. 시장은 물건의 가격이 결정되는 곳입니다. 그리고 시장의 가격은 공정해야 합니다. 회사가 단기적으로 주가를 부양하기 위해서 계속 높은 호가로 자기주식을 매수하면 가격이 올라갈텐데, 이러한 일은 발생해서는 안됩니다. 이러한 점을 고려하여, 회사가 자기주식을 장내에서 취득/처분하는 경우, **불공정거래를 예방**{: style="color: #4682B4"}하고 **시장에 미치는 영향을 최소화**{: style="color: #4682B4;"}하기 위해서 지켜야 할 사항들이 있습니다. <br>
<br>
아래의 한국거래소 홈페이지 내용에 따르면 취득·처분 전일 18시까지 자기주식매매신청서를 거래소에 제출해야 한다고 합니다. 그리고 시각, 호가, 수량, 체결여부는 거래소가 접수하고 관리하는 데이터입니다. <br>

![example2]({{site.url}}/assets/images/2025-01-21-buybackexpl/example2.jpg)
[출처](https://regulation.krx.co.kr/contents/RGL/03/03010305/RGL03010305.jsp)

<br>
그리고 위의 데이터는 [KRX 정보데이터시스템의 "이슈통계 - 자사주취득/처분"](http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0202) 메뉴에서 확인할 수 있습니다.
<br>

### 장외에서 취득하는 경우
장외의 경우 시장에서 매매하는 것이 아니기 때문에 주가에 영향을 주지는 않습니다. 따라서 거래소에 신고하는 절차는 별도로 없습니다. 그리고 장외에서 실제 매매가 이행된 거래도 거래소 시스템에 기록되지 않습니다. 거래소는 **시장**{: style="color: #4682B4;"}을 운영하는 회사라서 **장외**{: style="color: #4682B4;"}의 내용을 알수는 없으니까요. <br> 
한편, 장외거래의 예시로는 공개매수, 증여, 계좌대체 등이 있습니다. ***(개인적으로 생각하기에)*** 특이한 점은 시간외대량매매는 장내로 구분한다는 점입니다. 거래 쌍방이 협의하여 거래를 하는 것이기 때문에 시장가격에 영향을 미치는 영향은 없을것으로 생각되지만, 거래소 시스템(시장시스템)을 통해 거래되기 때문에 '장내'로 구분되는 것입니다.<br>
여차하여.. **장외**{: style="color: #4682B4;"} 자기주식의 실제 매매수량은 **금감원 서식(자기주식 매매 결과보고서 또는 정기보고서)**{: style="color: #4682B4;"}으로만 확인이 가능합니다. <br>
<br>

## 3. 결과보고


자기주식 취득에 대한 결과는 금융감독원에 제출되는 **1)결과보고서와 2)정기보고서(사업보고서, 분/반기 보고서)**{: style="color: #4682B4;"}를 통해 확인이 가능합니다.

### 결과보고서
회사가 직접 자기주식을 취득/처분한 경우, 그 결과는 금융감독원에 공시로 제출합니다. 주요사항보고서는 아니고 "자기주식취득결과보고서" 형태로 제출합니다. <br>
![example3]({{site.url}}/assets/images/2025-01-21-buybackexpl/example3.jpg)
<br>

<br>
<br>

공시본문의 **"3. 취득내용"**{: style="color: #4682B4;"}을 보면 일자별로 취득한 내용이 기재되어 있습니다.
<br>

**(2025.1.21 현대그린푸드 공시中)**{: style="color: gray;"}
![example4]({{site.url}}/assets/images/2025-01-21-buybackexpl/example4.jpg)

<br>

그리고 공시본문의 **"4. 취득예정내용과 실제취득내용"**{: style="color: #4682B4;"}을 보면 주요사항보고서로 신고한 수량 대비 얼마나 취득했는지도 기재하였습니다. 금액을 기준으로 하였네요. 주가야 시시각각 달라지는 것이다보니, 예정금액과 실제 취득 금액은 자연스럽게 다른 것으로 나타납니다.<br>
![example5]({{site.url}}/assets/images/2025-01-21-buybackexpl/example5.jpg)
<br>

### 정기보고서(사업, 분/반기보고서)
(12월 결산법인을 기준으로) 상장사는 3, 6, 9, 12월말 시점의 정기보고서를 제출해야 합니다. 연결최초작성법인이냐 외국법인이냐에 따라 차이는 있지만, 통상 분/반기기보고서는 3,6,9월말로부터 45일이내, 사업보고서는 12월말로부터 90일 이내 제출해야 합니다. 한달도 더 되는 시점 이후로 보고서가 제출된다니 적시성은 떨어지지만, 그래도 그만큼 해당 기간동안 일어난 내용을 잘 정리해서 보고한다니 유용하게 사용될 수 있는 데이터입니다.<br>
<br>

**(2024년 미래에셋증권 사업보고서中)**{: style="color: gray;"}
![example6]({{site.url}}/assets/images/2025-01-21-buybackexpl/example6.jpg)


