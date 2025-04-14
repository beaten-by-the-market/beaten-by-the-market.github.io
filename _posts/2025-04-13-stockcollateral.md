---
layout: single
title:  "대주주가 주식을 담보로 잡은 종목은?"
categories: 한국시장
tag: [data background, 주식담보, 지분공시]
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

## 대주주의 주식담보대출과 반대매매

### **주식담보대출이란? 대주주가 주식담보대출을 하는 이유는?**{: style="color: #4682B4;"}<br>
**주식담보대출**은 대주주 등이 보유한 주식의 일부 또는 전부를 금융기관에 담보로 맡기고 자금을 차입하는 수단입니다. 대주주가 이 방식을 선호하는 이유는 다양한데, 우선 주식을 매도하지 않고도 필요한 유동성을 확보할 수 있으며, 담보로 제공한 주식에 대한 의결권은 그대로 유지할 수 있어 경영권 행사에 지장이 없다는 큰 장점이 있습니다. 또한 자금 조달이 상대적으로 용이하고 신속하게 이루어질 수 있어 경영권 강화나 운영자금 확보 등을 위해 자주 활용됩니다. 대주주 입장에서는 회사 지분을 팔지 않고도 자산의 활용도를 높이는 자금조달 방법인 셈입니다. <br>

**LBO(Leveraged Buy-Out, 차입매수) 관점**에서도 주식담보대출은 중요한 의미를 가집니다. LBO는 기업인수를 위한 자금의 상당부분을 피인수회사의 자산이나 미래 현금흐름을 담보로 차입하여 인수하는 방식입니다. 특히 주식담보제공형 LBO는 인수기업이 직접 대출을 받거나 특수목적회사(SPC)를 설립하여 SPC로 하여금 대출을 받게 하고, 이 대출금을 바탕으로 피인수기업의 주식을 사들여 그 주식을 인수차입금에 대한 담보로 제공하는 유형입니다. 이러한 방식을 통해 인수자는 자신이 부담하는 자금을 최소화하면서 피인수회사를 인수할 수 있는 레버리지 효과를 얻게 됩니다. 대주주가 경영권 인수나 지분 확대를 위해 주식담보대출을 활용할 때 이와 유사한 메커니즘이 작동하며, 이는 적은 자기자본으로 자금조달을 가능하게 합니다.
<br><br>


### **주가와 담보비율은 어떤 관계가 있을까?**{: style="color: #4682B4;"}<br>
주식담보대출에서 가장 중요한 것은 '담보유지비율'입니다. 보통 우리나라에서는 140% 정도로 설정되는데, 이는 담보로 잡힌 주식의 가치가 대출금액의 140% 이상을 항상 유지해야 한다는 의미입니다. 예를 들어 1억원을 대출받았다면, 담보로 제공한 주식의 가치는 최소 1억 4천만원 이상이어야 합니다. 주가가 하락하여 담보 가치가 이 비율 아래로 떨어지면 증권사는 추가 담보를 요구하거나 부족한 금액을 납부하도록 요청합니다. 만약 주가가 지속적으로 하락하여 대주주가 추가 담보를 제공하지 못하면, 금융기관은 대출금 회수를 위해 담보물인 주식을 강제로 처분할 수 있는 권리를 갖게 됩니다.
<br><br>


### **반대매매란?**{: style="color: #4682B4;"}<br>
반대매매는 쉽게 말해서 '강제 매도'입니다. 대주주가 주식담보대출을 받은 후 주가가 크게 하락하여 담보유지비율(보통 140%)을 충족하지 못하거나, 대출 만기에 상환하지 못할 경우 발생합니다. 증권사는 대출금 손실을 방지하기 위해 고객의 동의 없이 담보로 잡힌 주식을 시장에 매도하여 대출금을 회수합니다. 반대매매는 주가가 이미 하락한 상황에서 대량으로 이루어지기 때문에, 주가를 더욱 끌어내리는 악순환을 초래하고 대주주는 경영권까지 잃을 수 있는 최악의 시나리오로 이어질 수 있습니다. 소액주주들도 주가 급락으로 큰 피해를 입게 되는 것이 반대매매의 가장 큰 문제점입니다.
<br><br>


### **실제 반대매매된 사례들**{: style="color: #4682B4;"}
> **엔케이맥스**<br>
엔케이맥스는 2024년 1월 최대주주였던 박상우 대표가 470억원 규모의 주식담보대출을 상환하지 못해 발생했습니다. 반대매매로 인해 박 대표의 지분은 12.94%에서 0.01%로 급감했습니다. 주가는 하한가를 기록했습니다.



![nkmax]({{site.url}}/assets/images/2025-04-14-stockcollateral/nkmax.png)
<br><br>

그외 **씨씨에스**(2024), **이오플로우**(2023~24), **아이엠**(2025)의 사례 등이 있습니다.

## 시장 전체에서 대주주가 주식을 담보로 제공한 케이스는?
### 데이터 확인해보기
데이터사업자인 에프엔가이드의 "DataGuide" 서비스에서는 대주주의 주식담보 비율을 제공하고 있습니다. 어떤 데이터들이 있는지 대략적으로 확인해보니 다음과 같습니다.


* **담보로 제공된 주식수**
* **발행주식수 대비 담보제공 주식수의 비율**
* **담보로 제공한 날의 주가**
* **조회 기준일 주가**

먼저, **담보제공일의 주가와 조회기준일의 주가**{: style="color: #4682B4;"}를 확인하면 **반대매매 가능성이 얼마나 큰지**{: style="color: #4682B4;"}를 알 수 있습니다. 통상 110~140%수준인 담보제공비율을 고려해보았을 때, **만약 오늘의 주가가 담보제공비율 수준보다 낮아질 것 같다면 반대매매를 당할 수 있는 것**{: style="color: #4682B4;"}입니다. 


또한 **담보제공 주식수의 비율**{: style="color: #4682B4;"}을 통해서 "만약에 반대매매가 되었다면" **주가에 미칠 영향의 크기를 가늠**{: style="color: #4682B4;"}할 수 있습니다. 만약 최대주주가 매우 적은 지분을 들고 있었다면, 그 물량이 시장에 쏟아져 나온다고 해도 주가에는 큰 영향을 미치기 어렵습니다. 따라서 **담보로 제공한 주식의 숫자가 전체 발행주식 수 대비 비율이 클 수록, 반대매매로 인한 주가하락이 클 것**{: style="color: #4682B4;"}임을 알 수 있습니다.




아래는 데이터가이드의 '25.4.11 기준 데이터를 불러왔을 때 확인할 수 있는 모습입니다.

<pre>
행의 개수: 479
상위 10개 행만 확인해보기
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>기준일</th>
      <th>코드</th>
      <th>종목명</th>
      <th>담보주식수</th>
      <th>공시일가치_종가</th>
      <th>공시일가치_수정주가</th>
      <th>기준일가치_수정주가</th>
      <th>지수산정주식수_대비_담보비율</th>
      <th>이벤트</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A000020</td>
      <td>동화약품</td>
      <td>528054.0</td>
      <td>3.231690e+09</td>
      <td>3.231690e+09</td>
      <td>3.136641e+09</td>
      <td>0.018905</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A000050</td>
      <td>경방</td>
      <td>5143684.0</td>
      <td>3.117073e+10</td>
      <td>3.117073e+10</td>
      <td>3.405119e+10</td>
      <td>0.187621</td>
      <td>무상증자 주식발행초과금 자본전입[2012/12/27], 무상증자 주식발행초과금 자본전입[2013/12/27]</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A000070</td>
      <td>삼양홀딩스</td>
      <td>253395.0</td>
      <td>1.426614e+10</td>
      <td>1.426614e+10</td>
      <td>1.419012e+10</td>
      <td>0.029587</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A000150</td>
      <td>두산</td>
      <td>501754.0</td>
      <td>1.615648e+11</td>
      <td>1.615648e+11</td>
      <td>1.440034e+11</td>
      <td>0.030365</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A000180</td>
      <td>성창기업지주</td>
      <td>2435700.0</td>
      <td>3.867892e+09</td>
      <td>3.867892e+09</td>
      <td>2.893612e+09</td>
      <td>0.034919</td>
      <td>유상증자 주주우선배정[2015/10/15]</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A000220</td>
      <td>유유제약</td>
      <td>1025305.0</td>
      <td>4.629252e+09</td>
      <td>4.629252e+09</td>
      <td>1.994982e+09</td>
      <td>0.060197</td>
      <td>무상증자 주식발행초과금 자본전입[2021/03/30], 무상증자 주식발행초과금 자본전입[2021/03/30], 무상증자 주식발행초과금 자본전입[2021/03/30]</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A000230</td>
      <td>일동홀딩스</td>
      <td>1843007.0</td>
      <td>1.192426e+10</td>
      <td>1.192426e+10</td>
      <td>1.127920e+10</td>
      <td>0.159700</td>
      <td>무상증자 주식발행초과금 자본전입[2020/03/05], 주식배당[2018/12/27]</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A000240</td>
      <td>한국앤컴퍼니</td>
      <td>23497119.0</td>
      <td>3.785386e+11</td>
      <td>3.785386e+11</td>
      <td>3.270799e+11</td>
      <td>0.247506</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A000270</td>
      <td>기아</td>
      <td>2650000.0</td>
      <td>1.529050e+11</td>
      <td>1.529050e+11</td>
      <td>2.173000e+11</td>
      <td>0.006537</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A000300</td>
      <td>DH오토넥스</td>
      <td>4347246.0</td>
      <td>1.047686e+09</td>
      <td>8.624920e+09</td>
      <td>1.166091e+08</td>
      <td>0.034377</td>
      <td>유상증자 주주배정[2012/06/26], 유상증자 주주우선배정[2009/06/18]</td>
    </tr>
  </tbody>
</table>
행의 개수: 857
상위 10개 행만 확인해보기
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>기준일</th>
      <th>코드</th>
      <th>종목명</th>
      <th>담보주식수</th>
      <th>공시일가치_종가</th>
      <th>공시일가치_수정주가</th>
      <th>기준일가치_수정주가</th>
      <th>지수산정주식수_대비_담보비율</th>
      <th>이벤트</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A001540</td>
      <td>안국약품</td>
      <td>2633031.0</td>
      <td>1.740433e+10</td>
      <td>1.740433e+10</td>
      <td>1.722002e+10</td>
      <td>0.201882</td>
      <td>주식배당[2013/12/27], 주식배당[2014/12/29]</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A001810</td>
      <td>무림SP</td>
      <td>4700000.0</td>
      <td>8.539900e+09</td>
      <td>8.539900e+09</td>
      <td>7.007700e+09</td>
      <td>0.212309</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A001840</td>
      <td>이화공영</td>
      <td>5300000.0</td>
      <td>1.515800e+10</td>
      <td>1.515800e+10</td>
      <td>8.564800e+09</td>
      <td>0.267598</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A002680</td>
      <td>한탑</td>
      <td>6100000.0</td>
      <td>5.788900e+09</td>
      <td>5.788900e+09</td>
      <td>4.245600e+09</td>
      <td>0.188756</td>
      <td>유상증자 주주배정[2022/03/30]</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A002800</td>
      <td>신신제약</td>
      <td>650000.0</td>
      <td>4.231500e+09</td>
      <td>4.231500e+09</td>
      <td>4.004000e+09</td>
      <td>0.042846</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A003100</td>
      <td>선광</td>
      <td>1151782.0</td>
      <td>1.871646e+10</td>
      <td>1.871646e+10</td>
      <td>1.776048e+10</td>
      <td>0.174512</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A003380</td>
      <td>하림지주</td>
      <td>7913101.0</td>
      <td>4.138552e+10</td>
      <td>4.138552e+10</td>
      <td>4.352206e+10</td>
      <td>0.070649</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A004590</td>
      <td>한국가구</td>
      <td>225000.0</td>
      <td>1.120500e+09</td>
      <td>1.120500e+09</td>
      <td>9.675000e+08</td>
      <td>0.015000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A004650</td>
      <td>창해에탄올</td>
      <td>1025146.0</td>
      <td>9.093045e+09</td>
      <td>9.093045e+09</td>
      <td>9.123799e+09</td>
      <td>0.111539</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A005160</td>
      <td>동국산업</td>
      <td>2226372.0</td>
      <td>1.834531e+10</td>
      <td>1.834531e+10</td>
      <td>7.859093e+09</td>
      <td>0.041043</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</pre>

데이터 중에 발행주식수 대비 담보주식수의 데이터 누락이 있는지를 확인했는데 없었습니다. 대주주가 주식을 담보로 제공한 기업의 숫자는 코스피가 479사, 코스닥이 857사로 확인되었습니다.

```python
# 지수산정주식수_대비_담보비율 칼럼이 누락된 행은 제거
df_kospi2 = df_kospi[~df_kospi['지수산정주식수_대비_담보비율'].isna()]
df_kosdaq2 = df_kosdaq[~df_kosdaq['지수산정주식수_대비_담보비율'].isna()]
```

<pre>
kospi 행 개수 : 479
kospi 삭제행 개수 : 0
kosdaq 행 개수 : 857
kosdaq 삭제행 개수 : 0
</pre>

## 구간별 분포 시각화
발행주식수 대비 담보로 제공된 주식의 비율을 10% 단위로 구간을 쪼개어 시각화해보도록 하겠습니다. 10% 미만은 5%구간으로도 쪼갰습니다.

![first]({{site.url}}/assets/images/2025-04-14-stockcollateral/first.png)
<br><br>
코스피와 코스닥 시장의 대주주 주식담보비율 분포를 살펴보면, 의외로 코스피 시장이 상대적으로 더 높은 수준의 담보를 갖고 있습니다. 코스피 시장의 평균 담보비율은 0.143으로 코스닥의 0.103보다 높고, 담보비율 5% 이상인 기업 비중도 코스피가 64.7%로 코스닥의 56.5%보다 높습니다. 특히 주목할 점은 코스피 시장에서 담보비율이 높은 구간(0.10 이상)에 분포하는 기업들의 비중이 상대적으로 많다는 것입니다. 이는 코스피 상장기업의 대주주들이 자신의 지분을 더 적극적으로 담보로 활용하고 있어, 시장 하락기에 반대매매 압력이 더 크게 작용할 수 있음을 시사합니다.


### 70% 넘는 게 현실적으로 가능한가?

근데 눈에 띄는 점이 있습니다. **발행주식수의 70% 이상을 담보로 잡은 기업들이 있다?**{: style="color: #4682B4;"} 상장사라면 어느정도 주식분산이 이뤄져있어야 하는 점은 차치하고서라도 저정도 수량이 담보로 잡혀있는것은 어떤 케이스일까요? 한번 개별적으로 케이스를 확인해보겠습니다. 

```python
df_outlier = df_all[df_all['지수산정주식수_대비_담보비율'] >= 0.7]
```

<pre>
행의 개수: 11
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>기준일</th>
      <th>코드</th>
      <th>종목명</th>
      <th>구간</th>
      <th>지수산정주식수_대비_담보비율</th>
      <th>공시일가치_수정주가</th>
      <th>기준일가치_수정주가</th>
      <th>이벤트</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2025-04-11</td>
      <td>A000400</td>
      <td>롯데손해보험</td>
      <td>0.70~0.80</td>
      <td>0.77</td>
      <td>486,532,454,045</td>
      <td>386,835,140,366</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11</td>
      <td>A000650</td>
      <td>천일고속</td>
      <td>0.70~0.80</td>
      <td>0.79</td>
      <td>42,808,386,600</td>
      <td>44,620,381,800</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11</td>
      <td>A002990</td>
      <td>금호건설</td>
      <td>0.80~0.90</td>
      <td>0.89</td>
      <td>328,139,072,700</td>
      <td>84,401,940,590</td>
      <td>유상증자 주주우선배정[2012/04/17]</td>
    </tr>
    <tr>
      <td>2025-04-11</td>
      <td>A003280</td>
      <td>흥아해운</td>
      <td>0.70~0.80</td>
      <td>0.75</td>
      <td>510,300,000,000</td>
      <td>281,880,000,000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11</td>
      <td>A003410</td>
      <td>쌍용C&E</td>
      <td>0.90~1.00</td>
      <td>0.98</td>
      <td>3,054,128,070,000</td>
      <td>nan</td>
      <td>유상증자 주주배정[2016/05/25]</td>
    </tr>
    <tr>
      <td>2025-04-11</td>
      <td>A029960</td>
      <td>코엔텍</td>
      <td>0.80~0.90</td>
      <td>0.84</td>
      <td>373,964,407,920</td>
      <td>374,806,670,100</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11</td>
      <td>A048260</td>
      <td>오스템임플란트(주)</td>
      <td>0.80~0.90</td>
      <td>0.82</td>
      <td>2,436,839,300,000</td>
      <td>nan</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11</td>
      <td>A085370</td>
      <td>(주)루트로닉</td>
      <td>0.90~1.00</td>
      <td>0.98</td>
      <td>933,029,935,300</td>
      <td>nan</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11</td>
      <td>A138580</td>
      <td>비즈니스온</td>
      <td>0.90~1.00</td>
      <td>0.99</td>
      <td>353,902,952,700</td>
      <td>nan</td>
      <td>무상증자 주식발행초과금 자본전입[2021/11/16]</td>
    </tr>
    <tr>
      <td>2025-04-11</td>
      <td>A194510</td>
      <td>(주)넥스쳐</td>
      <td>0.90~1.00</td>
      <td>0.99</td>
      <td>167,612,677,400</td>
      <td>nan</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11</td>
      <td>A220630</td>
      <td>(주)맘스터치앤컴퍼니</td>
      <td>NaN</td>
      <td>1.55</td>
      <td>10,693,087,724,000</td>
      <td>nan</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</pre>

일부는 진짜 현재 그러하고, 일부는 이미 상장폐지된 종목인데 데이터가이드의 데이터에 포함되어 있었던 회사들입니다. 먼저, 진짜로 대주주 주식담보비율이 높은 회사들을 몇 개 보겠습니다.

> **롯데손해보험**<br>사업보고서에서 확인되는 발행주식총수가 약 3.1억주인데, 최근 대량보유보고에서는 담보주식수가 2.4억주입니다. 정말로 발행주식의 상당부분이 담보로 제공되어있는게 맞았습니다.


![lotte]({{site.url}}/assets/images/2025-04-14-stockcollateral/lotte.png)
<br><br>

> **천일고속**<br>사업보고서에서 확인되는 발행주식총수가 약 140만주인데, 최근 대량보유보고에서는 담보주식수가110만주입니다. 정말로 발행주식의 상당부분이 담보로 제공되어있는게 맞았습니다.


![chunil]({{site.url}}/assets/images/2025-04-14-stockcollateral/chunil.png)
<br><br>

다음으로 상자폐지된 케이스들입니다. 위의 표에서 확인한 종목들이 다수 확인되는 것을 알 수 있습니다.
![news]({{site.url}}/assets/images/2025-04-14-stockcollateral/news.png)
<br><br>

### 현재 상장된 종목으로만 한정해서 보기
그렇다면 왜곡을 방지하기 위해 상장폐지된 종목은 제외하고 다시 분포를 살펴보도록 하겠습니다. 거래소에서 현재 상장된 기업목록만 불러와서 데이터가이드 데이터 행을 아래와 같이 삭제했습니다.

<pre>
kospi 상폐되어 제거한 기업 수 : 11
제거 후 kospi 기업 수 : 468
kosdaq 상폐되어 제거한 기업 수 : 69
제거 후 kosdaq 기업 수 : 788
</pre>

제거된 기업의 목록은 아래와 같습니다.
<pre>
행의 개수: 80
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>기준일</th>
      <th>코드</th>
      <th>종목명</th>
      <th>담보주식수</th>
      <th>공시일가치_종가</th>
      <th>공시일가치_수정주가</th>
      <th>기준일가치_수정주가</th>
      <th>지수산정주식수_대비_담보비율</th>
      <th>이벤트</th>
      <th>구간</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A001880</td>
      <td>디엘건설(주)</td>
      <td>69736.0</td>
      <td>2.423326e+09</td>
      <td>2.423326e+09</td>
      <td>NaN</td>
      <td>0.003162</td>
      <td>NaN</td>
      <td>0.00~0.05</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A003410</td>
      <td>쌍용C&E</td>
      <td>436304010.0</td>
      <td>3.054128e+12</td>
      <td>3.054128e+12</td>
      <td>NaN</td>
      <td>0.983138</td>
      <td>유상증자 주주배정[2016/05/25]</td>
      <td>0.90~1.00</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A004200</td>
      <td>고려개발</td>
      <td>9484275.0</td>
      <td>3.983396e+10</td>
      <td>7.966791e+10</td>
      <td>NaN</td>
      <td>0.311584</td>
      <td>NaN</td>
      <td>0.30~0.40</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A007630</td>
      <td>(주)폴루스바이오팜</td>
      <td>3117506.0</td>
      <td>8.386091e+09</td>
      <td>8.386091e+09</td>
      <td>NaN</td>
      <td>0.081128</td>
      <td>NaN</td>
      <td>0.05~0.10</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A010050</td>
      <td>우리종합금융(주)</td>
      <td>20000000.0</td>
      <td>7.200000e+09</td>
      <td>1.261103e+10</td>
      <td>NaN</td>
      <td>0.111171</td>
      <td>NaN</td>
      <td>0.10~0.20</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A015540</td>
      <td>(주)에코바이브</td>
      <td>1000000.0</td>
      <td>2.420000e+09</td>
      <td>2.420000e+10</td>
      <td>NaN</td>
      <td>0.034510</td>
      <td>NaN</td>
      <td>0.00~0.05</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A030790</td>
      <td>비케이탑스</td>
      <td>2724795.0</td>
      <td>2.182561e+10</td>
      <td>2.182561e+10</td>
      <td>NaN</td>
      <td>0.207558</td>
      <td>유상증자 주주우선배정[2015/11/03]</td>
      <td>0.20~0.30</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A115390</td>
      <td>락앤락</td>
      <td>30173960.0</td>
      <td>2.640222e+11</td>
      <td>2.640222e+11</td>
      <td>NaN</td>
      <td>0.696433</td>
      <td>유상증자 주주우선배정[2011/09/16]</td>
      <td>0.60~0.70</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A138250</td>
      <td>(주)엔에스쇼핑</td>
      <td>2870490.0</td>
      <td>3.717285e+10</td>
      <td>3.717285e+10</td>
      <td>NaN</td>
      <td>0.085187</td>
      <td>NaN</td>
      <td>0.05~0.10</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A152330</td>
      <td>코리아오토글라스(주)</td>
      <td>1247208.0</td>
      <td>2.269919e+10</td>
      <td>2.269919e+10</td>
      <td>NaN</td>
      <td>0.062360</td>
      <td>NaN</td>
      <td>0.05~0.10</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A282690</td>
      <td>동아타이어</td>
      <td>2618946.0</td>
      <td>3.302491e+10</td>
      <td>3.302491e+10</td>
      <td>NaN</td>
      <td>0.190704</td>
      <td>NaN</td>
      <td>0.10~0.20</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A008800</td>
      <td>(주)행남사</td>
      <td>10551049.0</td>
      <td>1.867536e+10</td>
      <td>1.867536e+10</td>
      <td>NaN</td>
      <td>0.231238</td>
      <td>NaN</td>
      <td>0.20~0.30</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A028040</td>
      <td>미래SCI</td>
      <td>1211117.0</td>
      <td>6.927589e+09</td>
      <td>6.927589e+09</td>
      <td>NaN</td>
      <td>0.040611</td>
      <td>유상증자 주주우선배정[2014/09/30], 무상증자 제적립금자본전입[2014/11/14]</td>
      <td>0.00~0.05</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A028150</td>
      <td>GS홈쇼핑</td>
      <td>445370.0</td>
      <td>6.515763e+10</td>
      <td>6.515763e+10</td>
      <td>NaN</td>
      <td>0.067865</td>
      <td>NaN</td>
      <td>0.05~0.10</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A033430</td>
      <td>디에스티(주)</td>
      <td>4883930.0</td>
      <td>3.882724e+09</td>
      <td>3.882724e+09</td>
      <td>NaN</td>
      <td>0.087205</td>
      <td>NaN</td>
      <td>0.05~0.10</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A033600</td>
      <td>럭슬</td>
      <td>2053809.0</td>
      <td>1.435612e+10</td>
      <td>1.435612e+10</td>
      <td>NaN</td>
      <td>0.172773</td>
      <td>NaN</td>
      <td>0.10~0.20</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A036260</td>
      <td>(주)이매진아시아</td>
      <td>2000000.0</td>
      <td>4.680000e+09</td>
      <td>4.680000e+09</td>
      <td>NaN</td>
      <td>0.056055</td>
      <td>NaN</td>
      <td>0.05~0.10</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A038160</td>
      <td>(주)팍스넷</td>
      <td>1696068.0</td>
      <td>5.368055e+09</td>
      <td>5.368055e+09</td>
      <td>NaN</td>
      <td>0.147948</td>
      <td>NaN</td>
      <td>0.10~0.20</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A038340</td>
      <td>MIT</td>
      <td>3900000.0</td>
      <td>4.309500e+09</td>
      <td>9.878057e+10</td>
      <td>NaN</td>
      <td>0.087078</td>
      <td>NaN</td>
      <td>0.05~0.10</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A039230</td>
      <td>제이앤케이인더스트리(주)</td>
      <td>5626332.0</td>
      <td>1.519110e+10</td>
      <td>4.240128e+10</td>
      <td>NaN</td>
      <td>0.234859</td>
      <td>NaN</td>
      <td>0.20~0.30</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A043290</td>
      <td>케이맥(주)</td>
      <td>6500000.0</td>
      <td>2.314000e+10</td>
      <td>2.314000e+10</td>
      <td>NaN</td>
      <td>0.168815</td>
      <td>NaN</td>
      <td>0.10~0.20</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A045890</td>
      <td>(주)금빛</td>
      <td>2880000.0</td>
      <td>7.977600e+09</td>
      <td>7.977600e+09</td>
      <td>NaN</td>
      <td>0.108326</td>
      <td>무상증자 주식발행초과금 자본전입[2010/02/09], 주식배당[2009/12/29]</td>
      <td>0.10~0.20</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A048260</td>
      <td>오스템임플란트(주)</td>
      <td>1282547.0</td>
      <td>2.436839e+12</td>
      <td>2.436839e+12</td>
      <td>NaN</td>
      <td>0.823386</td>
      <td>NaN</td>
      <td>0.80~0.90</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A050320</td>
      <td>에스에이치엔엘(주)</td>
      <td>1200000.0</td>
      <td>4.980000e+10</td>
      <td>4.980000e+10</td>
      <td>NaN</td>
      <td>0.158246</td>
      <td>NaN</td>
      <td>0.10~0.20</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A050540</td>
      <td>(주)엠피씨플러스</td>
      <td>5170000.0</td>
      <td>4.704700e+09</td>
      <td>4.704700e+10</td>
      <td>NaN</td>
      <td>0.133296</td>
      <td>유상증자 주주우선배정[2010/05/13], 무상증자 제적립금자본전입[2010/06/24]</td>
      <td>0.10~0.20</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A052190</td>
      <td>(주)세영디앤씨</td>
      <td>4500000.0</td>
      <td>1.912500e+10</td>
      <td>5.737557e+11</td>
      <td>NaN</td>
      <td>0.098726</td>
      <td>NaN</td>
      <td>0.05~0.10</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A053110</td>
      <td>(주)소리바다</td>
      <td>2000000.0</td>
      <td>8.020000e+08</td>
      <td>1.604000e+10</td>
      <td>NaN</td>
      <td>0.020844</td>
      <td>NaN</td>
      <td>0.00~0.05</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A053590</td>
      <td>한국테크놀로지</td>
      <td>17400000.0</td>
      <td>1.024860e+10</td>
      <td>1.024860e+10</td>
      <td>NaN</td>
      <td>0.110729</td>
      <td>유상증자 주주우선배정[2018/05/14]</td>
      <td>0.10~0.20</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A053660</td>
      <td>현진소재(주)</td>
      <td>915822.0</td>
      <td>3.425174e+09</td>
      <td>3.425174e+09</td>
      <td>NaN</td>
      <td>0.088667</td>
      <td>유상증자 주주우선배정[2015/04/17], 주식배당[2010/12/29]</td>
      <td>0.05~0.10</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A056000</td>
      <td>(주)코원플레이</td>
      <td>690000.0</td>
      <td>2.760000e+09</td>
      <td>2.760000e+09</td>
      <td>NaN</td>
      <td>0.048809</td>
      <td>NaN</td>
      <td>0.00~0.05</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A058220</td>
      <td>(주)아리온테크놀로지</td>
      <td>1115537.0</td>
      <td>1.617529e+09</td>
      <td>1.617529e+09</td>
      <td>NaN</td>
      <td>0.030791</td>
      <td>무상증자 주식발행초과금 자본전입[2013/10/16], 무상증자 주식발행초과금 자본전입[2016/10/26]</td>
      <td>0.00~0.05</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A058420</td>
      <td>(주)제이웨이</td>
      <td>4158826.0</td>
      <td>2.349737e+09</td>
      <td>1.385131e+11</td>
      <td>NaN</td>
      <td>0.147073</td>
      <td>NaN</td>
      <td>0.10~0.20</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A060300</td>
      <td>(주)레드로버</td>
      <td>1332050.0</td>
      <td>4.042772e+09</td>
      <td>1.212833e+10</td>
      <td>NaN</td>
      <td>0.029772</td>
      <td>유상증자 주주우선배정[2016/07/07], 무상증자 주식발행초과금 자본전입[2012/07/17], 무상증자 주식발행초과금 자본전입[2015/01/15]</td>
      <td>0.00~0.05</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A062860</td>
      <td>티엘아이</td>
      <td>1000000.0</td>
      <td>5.800000e+09</td>
      <td>5.800000e+09</td>
      <td>NaN</td>
      <td>0.101289</td>
      <td>NaN</td>
      <td>0.10~0.20</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A065560</td>
      <td>(주)선도소프트</td>
      <td>2083488.0</td>
      <td>1.145918e+10</td>
      <td>2.291837e+10</td>
      <td>NaN</td>
      <td>0.122912</td>
      <td>무상증자 주식발행초과금 자본전입[2011/03/03]</td>
      <td>0.10~0.20</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A065620</td>
      <td>(주)제낙스</td>
      <td>442000.0</td>
      <td>2.488460e+09</td>
      <td>2.488460e+09</td>
      <td>NaN</td>
      <td>0.019656</td>
      <td>NaN</td>
      <td>0.00~0.05</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A065940</td>
      <td>(주)바이오빌</td>
      <td>1421748.0</td>
      <td>3.213150e+09</td>
      <td>3.213150e+09</td>
      <td>NaN</td>
      <td>0.041714</td>
      <td>무상증자 주식발행초과금 자본전입[2011/10/07]</td>
      <td>0.00~0.05</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A066110</td>
      <td>(주)한프</td>
      <td>8102017.0</td>
      <td>3.807948e+09</td>
      <td>8.964539e+09</td>
      <td>NaN</td>
      <td>0.153448</td>
      <td>유상증자 주주우선배정[2016/04/20], 무상증자 주식발행초과금 자본전입[2016/09/29]</td>
      <td>0.10~0.20</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A069110</td>
      <td>(주)코스온</td>
      <td>1125085.0</td>
      <td>7.470564e+09</td>
      <td>7.470564e+09</td>
      <td>NaN</td>
      <td>0.060174</td>
      <td>NaN</td>
      <td>0.05~0.10</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A073070</td>
      <td>에이팸(주)</td>
      <td>1413255.0</td>
      <td>3.179824e+09</td>
      <td>1.589912e+10</td>
      <td>NaN</td>
      <td>0.016075</td>
      <td>NaN</td>
      <td>0.00~0.05</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A078940</td>
      <td>퀀타피아</td>
      <td>1719602.0</td>
      <td>2.115110e+09</td>
      <td>2.115110e+09</td>
      <td>NaN</td>
      <td>0.043631</td>
      <td>NaN</td>
      <td>0.00~0.05</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A080000</td>
      <td>에스엔유</td>
      <td>0.0</td>
      <td>0.000000e+00</td>
      <td>0.000000e+00</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>유상증자 주주우선배정[2010/06/29], 유상증자 주주우선배정[2015/12/29], 무상증자 주식발행초과금 자본전입[2010/08/16]</td>
      <td>0.00~0.05</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A085370</td>
      <td>(주)루트로닉</td>
      <td>25423159.0</td>
      <td>9.330299e+11</td>
      <td>9.330299e+11</td>
      <td>NaN</td>
      <td>0.982663</td>
      <td>NaN</td>
      <td>0.90~1.00</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A086250</td>
      <td>(주)화신테크</td>
      <td>1022221.0</td>
      <td>5.652882e+09</td>
      <td>5.652882e+09</td>
      <td>NaN</td>
      <td>0.105383</td>
      <td>NaN</td>
      <td>0.10~0.20</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A087730</td>
      <td>(주)이엠네트웍스</td>
      <td>3278685.0</td>
      <td>5.491797e+09</td>
      <td>8.237655e+10</td>
      <td>NaN</td>
      <td>0.176966</td>
      <td>NaN</td>
      <td>0.10~0.20</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A089530</td>
      <td>에이티세미콘</td>
      <td>5167345.0</td>
      <td>5.063998e+09</td>
      <td>5.063998e+09</td>
      <td>NaN</td>
      <td>0.071492</td>
      <td>유상증자 주주우선배정[2021/08/17]</td>
      <td>0.05~0.10</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A090740</td>
      <td>(주)와이앤넥스트</td>
      <td>406000.0</td>
      <td>2.135560e+09</td>
      <td>2.135560e+09</td>
      <td>NaN</td>
      <td>0.021227</td>
      <td>NaN</td>
      <td>0.00~0.05</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A096640</td>
      <td>(주)멜파스</td>
      <td>600000.0</td>
      <td>1.362000e+09</td>
      <td>1.362000e+09</td>
      <td>NaN</td>
      <td>0.016035</td>
      <td>NaN</td>
      <td>0.00~0.05</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A102210</td>
      <td>(주)트레스</td>
      <td>2341881.0</td>
      <td>6.065472e+09</td>
      <td>6.065472e+09</td>
      <td>NaN</td>
      <td>0.031777</td>
      <td>NaN</td>
      <td>0.00~0.05</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A108790</td>
      <td>(주)인터파크</td>
      <td>6500000.0</td>
      <td>2.700750e+10</td>
      <td>2.700750e+10</td>
      <td>NaN</td>
      <td>0.196046</td>
      <td>NaN</td>
      <td>0.10~0.20</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A111820</td>
      <td>(주)지유온</td>
      <td>2300000.0</td>
      <td>1.150000e+10</td>
      <td>1.259889e+10</td>
      <td>NaN</td>
      <td>0.119244</td>
      <td>무상증자 주식발행초과금 자본전입[2016/10/24], 주식배당[2014/12/29]</td>
      <td>0.10~0.20</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A114570</td>
      <td>지스마트글로벌(주)</td>
      <td>1206193.0</td>
      <td>3.286876e+09</td>
      <td>3.098429e+10</td>
      <td>NaN</td>
      <td>0.013855</td>
      <td>유상증자 주주배정[2015/09/10], 무상증자 주식발행초과금 자본전입[2018/11/08]</td>
      <td>0.00~0.05</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A119860</td>
      <td>커넥트웨이브</td>
      <td>18199803.0</td>
      <td>3.275965e+11</td>
      <td>3.275965e+11</td>
      <td>NaN</td>
      <td>0.403848</td>
      <td>NaN</td>
      <td>0.40~0.50</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A126870</td>
      <td>(주)뉴로스</td>
      <td>608119.0</td>
      <td>1.839560e+09</td>
      <td>1.839560e+09</td>
      <td>NaN</td>
      <td>0.020628</td>
      <td>NaN</td>
      <td>0.00~0.05</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A127160</td>
      <td>(주)매직마이크로</td>
      <td>2696814.0</td>
      <td>3.829476e+09</td>
      <td>3.829476e+09</td>
      <td>NaN</td>
      <td>0.045846</td>
      <td>NaN</td>
      <td>0.00~0.05</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A131390</td>
      <td>(주)원익피앤이</td>
      <td>5206506.0</td>
      <td>8.044052e+10</td>
      <td>8.044052e+10</td>
      <td>NaN</td>
      <td>0.351342</td>
      <td>NaN</td>
      <td>0.30~0.40</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A138580</td>
      <td>비즈니스온</td>
      <td>22328262.0</td>
      <td>3.539030e+11</td>
      <td>3.539030e+11</td>
      <td>NaN</td>
      <td>0.993990</td>
      <td>무상증자 주식발행초과금 자본전입[2021/11/16]</td>
      <td>0.90~1.00</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A138690</td>
      <td>(주)엘아이에스</td>
      <td>313031.0</td>
      <td>4.366782e+09</td>
      <td>1.222877e+10</td>
      <td>NaN</td>
      <td>0.019531</td>
      <td>NaN</td>
      <td>0.00~0.05</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A141020</td>
      <td>(주)디에스앤엘</td>
      <td>4600000.0</td>
      <td>4.968000e+08</td>
      <td>1.723265e+10</td>
      <td>NaN</td>
      <td>0.026370</td>
      <td>무상증자 주식발행초과금 자본전입[2014/11/07]</td>
      <td>0.00~0.05</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A141070</td>
      <td>(주)맥스로텍</td>
      <td>2371542.0</td>
      <td>5.181819e+09</td>
      <td>5.181819e+09</td>
      <td>NaN</td>
      <td>0.067680</td>
      <td>NaN</td>
      <td>0.05~0.10</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A148140</td>
      <td>비디아이(주)</td>
      <td>2860000.0</td>
      <td>1.830400e+09</td>
      <td>1.756032e+10</td>
      <td>NaN</td>
      <td>0.066190</td>
      <td>무상증자 주식발행초과금 자본전입[2018/10/25], 무상증자 주식발행초과금 자본전입[2020/05/29]</td>
      <td>0.05~0.10</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A160600</td>
      <td>이큐셀</td>
      <td>1618614.0</td>
      <td>1.484269e+10</td>
      <td>7.523438e+10</td>
      <td>NaN</td>
      <td>0.135652</td>
      <td>NaN</td>
      <td>0.10~0.20</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A161570</td>
      <td>(주)미동전자통신</td>
      <td>2590000.0</td>
      <td>5.788650e+09</td>
      <td>5.788650e+09</td>
      <td>NaN</td>
      <td>0.166208</td>
      <td>NaN</td>
      <td>0.10~0.20</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A176440</td>
      <td>(주)미래오토스</td>
      <td>11494350.0</td>
      <td>2.339100e+10</td>
      <td>2.339100e+10</td>
      <td>NaN</td>
      <td>0.134061</td>
      <td>NaN</td>
      <td>0.10~0.20</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A181340</td>
      <td>(주)이즈미디어</td>
      <td>913062.0</td>
      <td>1.803297e+10</td>
      <td>9.216852e+09</td>
      <td>NaN</td>
      <td>0.128237</td>
      <td>NaN</td>
      <td>0.10~0.20</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A182690</td>
      <td>테라셈(주)</td>
      <td>2000000.0</td>
      <td>5.560000e+09</td>
      <td>5.560000e+09</td>
      <td>NaN</td>
      <td>0.131047</td>
      <td>NaN</td>
      <td>0.10~0.20</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A194510</td>
      <td>(주)넥스쳐</td>
      <td>12058466.0</td>
      <td>1.676127e+11</td>
      <td>1.676127e+11</td>
      <td>NaN</td>
      <td>0.992965</td>
      <td>NaN</td>
      <td>0.90~1.00</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A195440</td>
      <td>(주)퓨전</td>
      <td>732010.0</td>
      <td>5.716998e+09</td>
      <td>4.772397e+10</td>
      <td>NaN</td>
      <td>0.087058</td>
      <td>무상증자 주식발행초과금 자본전입[2017/10/31]</td>
      <td>0.05~0.10</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A204990</td>
      <td>(주)코썬바이오</td>
      <td>1100000.0</td>
      <td>1.413500e+09</td>
      <td>1.413500e+09</td>
      <td>NaN</td>
      <td>0.034436</td>
      <td>NaN</td>
      <td>0.00~0.05</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A213090</td>
      <td>(주)미래테크놀로지</td>
      <td>6000.0</td>
      <td>4.854000e+07</td>
      <td>4.854000e+07</td>
      <td>NaN</td>
      <td>0.000980</td>
      <td>NaN</td>
      <td>0.00~0.05</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A214310</td>
      <td>에스엘에너지</td>
      <td>11348550.0</td>
      <td>3.472656e+09</td>
      <td>6.945313e+10</td>
      <td>NaN</td>
      <td>0.154228</td>
      <td>유상증자 주주우선배정[2021/12/03], 무상증자 주식발행초과금 자본전입[2016/09/12]</td>
      <td>0.10~0.20</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A214870</td>
      <td>한울BnC</td>
      <td>104340.0</td>
      <td>1.132089e+09</td>
      <td>5.664552e+09</td>
      <td>NaN</td>
      <td>0.003489</td>
      <td>무상증자 주식발행초과금 자본전입[2018/01/24]</td>
      <td>0.00~0.05</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A220630</td>
      <td>(주)맘스터치앤컴퍼니</td>
      <td>157948120.0</td>
      <td>1.069309e+12</td>
      <td>1.069309e+13</td>
      <td>NaN</td>
      <td>1.551286</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A221610</td>
      <td>자안바이오(주)</td>
      <td>1955262.0</td>
      <td>2.453854e+10</td>
      <td>2.453854e+10</td>
      <td>NaN</td>
      <td>0.301035</td>
      <td>유상증자 주주우선배정[2020/10/12], 무상증자 주식발행초과금 자본전입[2020/04/29]</td>
      <td>0.30~0.40</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A225330</td>
      <td>(주)씨엠에스에듀</td>
      <td>1644843.0</td>
      <td>1.133297e+10</td>
      <td>1.133297e+10</td>
      <td>NaN</td>
      <td>0.088268</td>
      <td>무상증자 주식발행초과금 자본전입[2017/07/28]</td>
      <td>0.05~0.10</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A226350</td>
      <td>(주)아이엠텍</td>
      <td>909090.0</td>
      <td>9.090900e+08</td>
      <td>2.272725e+10</td>
      <td>NaN</td>
      <td>0.036885</td>
      <td>NaN</td>
      <td>0.00~0.05</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A263540</td>
      <td>어스앤에어로스페이스</td>
      <td>1020000.0</td>
      <td>7.599000e+09</td>
      <td>8.311367e+10</td>
      <td>NaN</td>
      <td>0.127155</td>
      <td>NaN</td>
      <td>0.10~0.20</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A268600</td>
      <td>셀리버리</td>
      <td>452869.0</td>
      <td>3.025165e+09</td>
      <td>3.025165e+09</td>
      <td>NaN</td>
      <td>0.012385</td>
      <td>무상증자 주식발행초과금 자본전입[2021/02/01], 무상증자 주식발행초과금 자본전입[2022/07/25]</td>
      <td>0.00~0.05</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A287410</td>
      <td>제이시스메디칼</td>
      <td>7613030.0</td>
      <td>9.820809e+10</td>
      <td>9.820809e+10</td>
      <td>NaN</td>
      <td>0.100578</td>
      <td>NaN</td>
      <td>0.10~0.20</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A290510</td>
      <td>(주)코리아센터</td>
      <td>29440593.0</td>
      <td>1.408732e+11</td>
      <td>1.408732e+11</td>
      <td>NaN</td>
      <td>0.257045</td>
      <td>NaN</td>
      <td>0.20~0.30</td>
    </tr>
  </tbody>
</table>
</pre>

### 상폐종목 제외하고 구간별 분포 시각화
상장폐지 종목들을 제외한 코스피와 코스닥 시장의 대주주 주식담보비율 분포를 분석해보면, 여전히 코스피 시장에서 더 높은 주식담보제공 수준이 관찰됩니다. 코스피 시장의 평균 담보비율은 0.141(14.1%)로 코스닥의 0.097(9.7%)보다 높습니다. 담보비율이 5% 이상인 기업 비중도 코스피가 64.3%(301개사)로 코스닥의 55.6%(436개사)보다 높은 상황입니다. 특히 코스피 시장에서는 담보비율 0.10 이상 구간에 위치한 기업 수가 상대적으로 많고, 0.30 이상 비율을 보이는 기업들도 상당수 존재합니다. 이는 코스피 상장기업의 대주주들이 자신의 지분을 더 적극적으로 담보로 활용하고 있어, 시장 하락기에 반대매매 위험에 더 취약할 수 있음을 시사합니다.


분포 형태를 살펴보면, 두 시장 모두 오른쪽으로 치우친 분포를 보이고 있으나 코스닥 시장은 낮은담보 구간(0.00-0.05)에 352개사가 집중되어 있는 반면, 코스피는 상대적으로 고르게 분포되어 있습니다. 코스피 시장의 표준편차(0.083)가 코스닥(0.060)보다 높다는 점도 코스피 내 기업들의 담보비율 편차가 더 크다는 것을 보여줍니다. 상장폐지 종목을 제외했음에도 불구하고 이러한 경향이 유지된다는 것은 코스피 시장에서 대주주의 지분 담보 관행이 더 일반화되어 있으며, 이는 시장 충격 발생 시 대형주 중심의 코스피 시장에서도 반대매매로 인한 추가적인 주가 하락 압력이 존재할 수 있음을 시사합니다.
![second]({{site.url}}/assets/images/2025-04-14-stockcollateral/second.png)
<br><br>

## 주주별 주식수 대비 담보비율 분포 파악하기
여태까지의 분석은 다음의 기준이었습니다.

> 회사별 기준<br>대주주등의 담보제공주식 수 ÷ 발행주식 총수

이 기준으로는 반대매매 실행시 초래될 파급효과를 짐작해볼 수 있지만 **반대매매의 가능성**{: style="color: #4682B4;"}에 대해서는 설명이 취약한 점도 있습니다. 다음의 예를 한번 보겠습니다.
> A회사 발행주식총수는 100주<br>대주주B씨는 주식 50주 보유(지분율 50%)<br>대주주B씨의 주식담보대출은 30주에 대해서만 잡혀있음


이경우 발행주식총수 대비 담보비율이 30%이므로 상당히 높은 수준이고, 반대매매가 실행되었을 때 주가가 큰 폭으로 하락할 수 있습니다. 하지만 반대매매가 실행될 가능성은 어떨까요? 대주주B씨는 50주 중에 30주만 담보로 잡았고 아직 20주는 담보로 잡지 않았습니다. 주가가 하락하여 반대매매가 실행되려 하면, **대주주B씨는 나머지 20주를 추가로 담보로 제공**{: style="color: #4682B4;"}할 수 있습니다. 이 경우 반대매매는 이뤄지지 않을 수 있을 것입니다. 따라서 **"주주별" 주식 담보비율의 분포를 확인해볼 필요성**{: style="color: #4682B4;"}도 있습니다.

### 데이터 확인해보기
데이터사업자인 에프엔가이드의 “DataGuide” 서비스에서는 이 비율도 제공하고 있습니다. 어떤 데이터들이 있는지 대략적으로 확인해보니 다음과 같습니다.

* 주주, 보고자, 주주와 보고자와의 관계
* **주주별** 담보로 제공된 주식수
* 발행주식수 대비 **주주별** 담보제공 주식수의 비율
* 발행주식수 대비 **주주별** 보유주식 비율
* 담보로 제공한 날의 주가
* 조회 기준일 주가


<pre>
담보제공 주주 수: 874
상위 10개 행만 확인해보기
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>기준일</th>
      <th>코드</th>
      <th>종목명</th>
      <th>주주</th>
      <th>보고자</th>
      <th>보고자와_관계</th>
      <th>담보주식수</th>
      <th>공시일가치_종가</th>
      <th>공시일가치_수정주가</th>
      <th>기준일가치_수정주가</th>
      <th>주주주식수_대비_담보비율</th>
      <th>지수산정주식수_대비_담보비율</th>
      <th>지수산정주식수_대비_보유비율</th>
      <th>이벤트</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A000020</td>
      <td>동화약품</td>
      <td>윤인호</td>
      <td>윤도준</td>
      <td>특수관계인</td>
      <td>528054.0</td>
      <td>3.231690e+09</td>
      <td>3.231690e+09</td>
      <td>3.136641e+09</td>
      <td>0.293925</td>
      <td>0.018905</td>
      <td>0.064320</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A000050</td>
      <td>경방</td>
      <td>경방어패럴</td>
      <td>김담</td>
      <td>특수관계인</td>
      <td>741403.0</td>
      <td>4.492902e+09</td>
      <td>4.492902e+09</td>
      <td>4.908088e+09</td>
      <td>1.000000</td>
      <td>0.027043</td>
      <td>0.027043</td>
      <td>무상증자 주식발행초과금 자본전입[2012/12/27], 무상증자 주식발행초과금 자본전입[2013/12/27]</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A000050</td>
      <td>경방</td>
      <td>김담</td>
      <td>김담</td>
      <td>특수관계인</td>
      <td>1562281.0</td>
      <td>9.467423e+09</td>
      <td>9.467423e+09</td>
      <td>1.034230e+10</td>
      <td>0.271566</td>
      <td>0.056985</td>
      <td>0.209841</td>
      <td>무상증자 주식발행초과금 자본전입[2012/12/27], 무상증자 주식발행초과금 자본전입[2013/12/27]</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A000050</td>
      <td>경방</td>
      <td>김준</td>
      <td>김담</td>
      <td>특수관계인</td>
      <td>2840000.0</td>
      <td>1.721040e+10</td>
      <td>1.721040e+10</td>
      <td>1.880080e+10</td>
      <td>0.770572</td>
      <td>0.103591</td>
      <td>0.134435</td>
      <td>무상증자 주식발행초과금 자본전입[2012/12/27], 무상증자 주식발행초과금 자본전입[2013/12/27]</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A000070</td>
      <td>삼양홀딩스</td>
      <td>김건호</td>
      <td>김윤</td>
      <td>특수관계인</td>
      <td>98395.0</td>
      <td>5.539638e+09</td>
      <td>5.539638e+09</td>
      <td>5.510120e+09</td>
      <td>0.393139</td>
      <td>0.011489</td>
      <td>0.029224</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A000070</td>
      <td>삼양홀딩스</td>
      <td>김남호</td>
      <td>김윤</td>
      <td>특수관계인</td>
      <td>67000.0</td>
      <td>3.772100e+09</td>
      <td>3.772100e+09</td>
      <td>3.752000e+09</td>
      <td>0.493616</td>
      <td>0.007823</td>
      <td>0.015849</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A000070</td>
      <td>삼양홀딩스</td>
      <td>김윤</td>
      <td>김윤</td>
      <td>본인</td>
      <td>88000.0</td>
      <td>4.954400e+09</td>
      <td>4.954400e+09</td>
      <td>4.928000e+09</td>
      <td>0.254782</td>
      <td>0.010275</td>
      <td>0.040329</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A000150</td>
      <td>두산</td>
      <td>박상수</td>
      <td>박정원</td>
      <td>특수관계인</td>
      <td>76000.0</td>
      <td>2.447200e+10</td>
      <td>2.447200e+10</td>
      <td>2.181200e+10</td>
      <td>0.562508</td>
      <td>0.004599</td>
      <td>0.008177</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A000150</td>
      <td>두산</td>
      <td>박석원</td>
      <td>박정원</td>
      <td>특수관계인</td>
      <td>56200.0</td>
      <td>1.809640e+10</td>
      <td>1.809640e+10</td>
      <td>1.612940e+10</td>
      <td>0.113894</td>
      <td>0.003401</td>
      <td>0.029862</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A000150</td>
      <td>두산</td>
      <td>박인원</td>
      <td>박정원</td>
      <td>특수관계인</td>
      <td>37500.0</td>
      <td>1.207500e+10</td>
      <td>1.207500e+10</td>
      <td>1.076250e+10</td>
      <td>0.114162</td>
      <td>0.002269</td>
      <td>0.019879</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
담보제공 주주 수: 1,213
상위 10개 행만 확인해보기
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>기준일</th>
      <th>코드</th>
      <th>종목명</th>
      <th>주주</th>
      <th>보고자</th>
      <th>보고자와_관계</th>
      <th>담보주식수</th>
      <th>공시일가치_종가</th>
      <th>공시일가치_수정주가</th>
      <th>기준일가치_수정주가</th>
      <th>주주주식수_대비_담보비율</th>
      <th>지수산정주식수_대비_담보비율</th>
      <th>지수산정주식수_대비_보유비율</th>
      <th>이벤트</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A001540</td>
      <td>안국약품</td>
      <td>어진</td>
      <td>어진</td>
      <td>본인</td>
      <td>2633031.0</td>
      <td>1.740433e+10</td>
      <td>1.740433e+10</td>
      <td>1.722002e+10</td>
      <td>0.467157</td>
      <td>0.201882</td>
      <td>0.432150</td>
      <td>주식배당[2013/12/27], 주식배당[2014/12/29]</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A001810</td>
      <td>무림SP</td>
      <td>이도균</td>
      <td>이동욱</td>
      <td>특수관계인</td>
      <td>4700000.0</td>
      <td>8.539900e+09</td>
      <td>8.539900e+09</td>
      <td>7.007700e+09</td>
      <td>0.993663</td>
      <td>0.212309</td>
      <td>0.213663</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A001840</td>
      <td>이화공영</td>
      <td>최삼규</td>
      <td>최삼규</td>
      <td>본인</td>
      <td>5300000.0</td>
      <td>1.515800e+10</td>
      <td>1.515800e+10</td>
      <td>8.564800e+09</td>
      <td>0.753490</td>
      <td>0.267598</td>
      <td>0.355146</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A002680</td>
      <td>한탑</td>
      <td>류지훈</td>
      <td>류원기</td>
      <td>특수관계인</td>
      <td>6100000.0</td>
      <td>5.788900e+09</td>
      <td>5.788900e+09</td>
      <td>4.245600e+09</td>
      <td>0.503500</td>
      <td>0.188756</td>
      <td>0.374888</td>
      <td>유상증자 주주배정[2022/03/30]</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A002800</td>
      <td>신신제약</td>
      <td>이병기</td>
      <td>이병기</td>
      <td>본인</td>
      <td>650000.0</td>
      <td>4.231500e+09</td>
      <td>4.231500e+09</td>
      <td>4.004000e+09</td>
      <td>0.162550</td>
      <td>0.042846</td>
      <td>0.263588</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A003100</td>
      <td>선광</td>
      <td>심우겸</td>
      <td>심충식</td>
      <td>특수관계인</td>
      <td>175000.0</td>
      <td>2.843750e+09</td>
      <td>2.843750e+09</td>
      <td>2.698500e+09</td>
      <td>1.000000</td>
      <td>0.026515</td>
      <td>0.026515</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A003100</td>
      <td>선광</td>
      <td>심우인</td>
      <td>심충식</td>
      <td>특수관계인</td>
      <td>125000.0</td>
      <td>2.031250e+09</td>
      <td>2.031250e+09</td>
      <td>1.927500e+09</td>
      <td>1.000000</td>
      <td>0.018939</td>
      <td>0.018939</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A003100</td>
      <td>선광</td>
      <td>심우진</td>
      <td>심충식</td>
      <td>특수관계인</td>
      <td>126399.0</td>
      <td>2.053984e+09</td>
      <td>2.053984e+09</td>
      <td>1.949073e+09</td>
      <td>1.000000</td>
      <td>0.019151</td>
      <td>0.019151</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A003100</td>
      <td>선광</td>
      <td>심우철</td>
      <td>심충식</td>
      <td>특수관계인</td>
      <td>175000.0</td>
      <td>2.843750e+09</td>
      <td>2.843750e+09</td>
      <td>2.698500e+09</td>
      <td>1.000000</td>
      <td>0.026515</td>
      <td>0.026515</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11 00:00:00</td>
      <td>A003100</td>
      <td>선광</td>
      <td>심장식</td>
      <td>심충식</td>
      <td>특수관계인</td>
      <td>550383.0</td>
      <td>8.943724e+09</td>
      <td>8.943724e+09</td>
      <td>8.486906e+09</td>
      <td>0.998880</td>
      <td>0.083391</td>
      <td>0.083485</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</pre>


한편 주주별 데이터를 대상으로 하다보니 일부 데이터는 null 값이 존재합니다. 해당 데이터를 삭제해주었습니다. 코스피는 30행, 코스닥은 73행을 삭제했습니다.
```python
# 지수산정주식수_대비_담보비율 칼럼이 누락된 행은 제거
df_kospi2 = df_kospi[~df_kospi['주주주식수_대비_담보비율'].isna()]
df_kosdaq2 = df_kosdaq[~df_kosdaq['주주주식수_대비_담보비율'].isna()]
```

<pre>
kospi 행 개수 : 874
kospi 삭제행 개수 : 30
kosdaq 행 개수 : 1213
kosdaq 삭제행 개수 : 73
</pre>
## 주주별 담보비율 구간별 분포 시각화

![third]({{site.url}}/assets/images/2025-04-14-stockcollateral/third.png)
<br><br>

이번 그래프는 주주 개인 단위에서의 담보주식 비율 분포를 보여줍니다. **코스피와 코스닥 시장 모두에서 주목할 만한 특징은 담보비율 0.90-1.00 구간에 상당수의 주주가 집중되어 있다는 점**{: style="color: #4682B4;"}입니다. 코스피에서는 214명(25.4%), 코스닥에서는 248명(21.8%)의 주주가 자신의 보유주식 대부분을 담보로 제공하고 있습니다. 이는 시장 하락 시 반대매매 위험이 특정 주주들에게 집중되어 있음을 의미합니다. 


한편 코스피 시장의 담보비율 평균(0.568)이 코스닥(0.520)보다 높게 설정되어 있습니다. 담보제공비율 50% 이상인 주주의 비중도 코스피가 55.7%로 코스닥의 41.3%보다 높습니다. 이는 이전 기업 수준 분석에서도 확인되었던 **"코스피 시장의 주식담보 수준이 더 높다"는 내용을 개인 주주 수준에서도 재확인**{: style="color: #4682B4;"}시켜 줍니다. 주주 개인의 담보비율이 90% 이상인 경우가 많다는 것으로, 이들은 주가 하락 시 거의 모든 보유 주식이 반대매매될 위험에 처해 있다는 것을 의미합니다. 


## 아웃라이어 확인
그래프에서는 1이상의 수치는 표현되지 않았습니다. **'담보주식수량을 본인이 보유한 수량으로 나눈 값'이 1이상이라는 것은 자신이 보유한 수량 이상으로 담보를 제공하였다는 의미**{: style="color: #4682B4;"}입니다. 언뜻 와닿지는 않지만 데이터가이드의 데이터에는 상당수 존재하고 있었습니다. 코스닥부터 케이스를 몇개 보도록 하겠습니다.

<pre>
코스닥 상위 10개 행만 확인해보기
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>기준일</th>
      <th>코드</th>
      <th>종목명</th>
      <th>주주</th>
      <th>구간</th>
      <th>주주주식수_대비_담보비율</th>
      <th>지수산정주식수_대비_보유비율</th>
      <th>공시일가치_수정주가</th>
      <th>기준일가치_수정주가</th>
      <th>이벤트</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2025-04-11</td>
      <td>A032860</td>
      <td>더라미</td>
      <td>코니퍼1호투자조합</td>
      <td>NaN</td>
      <td>564971.67</td>
      <td>0.00</td>
      <td>11,050,845,800</td>
      <td>2,403,389,470</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11</td>
      <td>A019550</td>
      <td>SBI인베스트먼트</td>
      <td>케이티아이씨홀딩스</td>
      <td>NaN</td>
      <td>5.84</td>
      <td>0.00</td>
      <td>295,501,629</td>
      <td>260,845,577</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11</td>
      <td>A052900</td>
      <td>KX하이텍</td>
      <td>지프라자</td>
      <td>NaN</td>
      <td>4.25</td>
      <td>0.02</td>
      <td>5,484,785,670</td>
      <td>2,457,843,804</td>
      <td>유상증자 주주우선배정[2014/09/04]</td>
    </tr>
    <tr>
      <td>2025-04-11</td>
      <td>A043590</td>
      <td>웰킵스하이텍</td>
      <td>파워리퍼블릭얼라이언스</td>
      <td>NaN</td>
      <td>4.01</td>
      <td>0.04</td>
      <td>16,561,806,117</td>
      <td>1,119,853,270</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11</td>
      <td>A066410</td>
      <td>버킷스튜디오</td>
      <td>이니셜 1호투자조합</td>
      <td>NaN</td>
      <td>3.44</td>
      <td>0.09</td>
      <td>30,659,640,917</td>
      <td>30,659,640,917</td>
      <td>유상증자 주주우선배정[2019/01/31]</td>
    </tr>
    <tr>
      <td>2025-04-11</td>
      <td>A036090</td>
      <td>위지트</td>
      <td>제이더블유인베스트먼트</td>
      <td>NaN</td>
      <td>3.27</td>
      <td>0.12</td>
      <td>20,004,253,396</td>
      <td>11,049,690,525</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11</td>
      <td>A053590</td>
      <td>한국테크놀로지</td>
      <td>한국이노베이션</td>
      <td>NaN</td>
      <td>3.00</td>
      <td>0.04</td>
      <td>10,248,600,000</td>
      <td>nan</td>
      <td>유상증자 주주우선배정[2018/05/14]</td>
    </tr>
    <tr>
      <td>2025-04-11</td>
      <td>A148150</td>
      <td>세경하이테크</td>
      <td>에스지에이치홀딩스</td>
      <td>NaN</td>
      <td>2.90</td>
      <td>0.20</td>
      <td>139,327,512,000</td>
      <td>136,991,227,500</td>
      <td>무상증자 주식발행초과금 자본전입[2023/11/29]</td>
    </tr>
    <tr>
      <td>2025-04-11</td>
      <td>A038340</td>
      <td>MIT</td>
      <td>김우정</td>
      <td>NaN</td>
      <td>2.73</td>
      <td>0.03</td>
      <td>98,780,571,664</td>
      <td>nan</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11</td>
      <td>A086450</td>
      <td>동국제약</td>
      <td>권재범</td>
      <td>NaN</td>
      <td>2.73</td>
      <td>0.05</td>
      <td>35,918,434,300</td>
      <td>17,769,046,750</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</pre>

표에서 확인된 더라미, KX하이텍 두 회사의 대량보유보고 본문을 직접 확인해보니... 오타가 아니었습니다. 비율이 정말 그러하네요...!
![thelami]({{site.url}}/assets/images/2025-04-14-stockcollateral/thelami.png)
<br><br>

![kxhitech]({{site.url}}/assets/images/2025-04-14-stockcollateral/kxhitech.png)
<br><br>


이번엔 코스피 시장의 경우를 보겠습니다.

<pre>
상위 10개 행만 확인해보기
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>기준일</th>
      <th>코드</th>
      <th>종목명</th>
      <th>주주</th>
      <th>구간</th>
      <th>주주주식수_대비_담보비율</th>
      <th>지수산정주식수_대비_보유비율</th>
      <th>공시일가치_수정주가</th>
      <th>기준일가치_수정주가</th>
      <th>이벤트</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2025-04-11</td>
      <td>A034730</td>
      <td>SK</td>
      <td>최영진</td>
      <td>NaN</td>
      <td>77.81</td>
      <td>0.00</td>
      <td>1,856,665,900</td>
      <td>1,876,897,800</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11</td>
      <td>A009240</td>
      <td>한샘</td>
      <td>하임1호유한회사</td>
      <td>NaN</td>
      <td>12.70</td>
      <td>0.01</td>
      <td>181,407,157,250</td>
      <td>153,274,496,500</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11</td>
      <td>A117580</td>
      <td>대성에너지</td>
      <td>알앤알</td>
      <td>NaN</td>
      <td>5.00</td>
      <td>0.01</td>
      <td>12,420,000,000</td>
      <td>15,060,000,000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11</td>
      <td>A002140</td>
      <td>고려산업</td>
      <td>전상익</td>
      <td>NaN</td>
      <td>4.72</td>
      <td>0.00</td>
      <td>1,668,000,000</td>
      <td>844,500,000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11</td>
      <td>A001080</td>
      <td>만호제강</td>
      <td>엠케이에셋</td>
      <td>NaN</td>
      <td>4.38</td>
      <td>0.04</td>
      <td>23,354,960,400</td>
      <td>17,012,039,400</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11</td>
      <td>A014680</td>
      <td>한솔케미칼</td>
      <td>조연주</td>
      <td>NaN</td>
      <td>3.02</td>
      <td>0.01</td>
      <td>53,481,384,000</td>
      <td>52,994,304,000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11</td>
      <td>A028100</td>
      <td>동아지질</td>
      <td>이정우</td>
      <td>NaN</td>
      <td>2.61</td>
      <td>0.13</td>
      <td>60,539,924,060</td>
      <td>64,160,404,000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2025-04-11</td>
      <td>A058730</td>
      <td>다스코</td>
      <td>한시인</td>
      <td>NaN</td>
      <td>2.18</td>
      <td>0.01</td>
      <td>1,692,600,000</td>
      <td>1,632,540,000</td>
      <td>유상증자 주주우선배정[2016/03/03]</td>
    </tr>
    <tr>
      <td>2025-04-11</td>
      <td>A002990</td>
      <td>금호건설</td>
      <td>금호고속</td>
      <td>NaN</td>
      <td>2.00</td>
      <td>0.45</td>
      <td>328,139,072,700</td>
      <td>84,401,940,590</td>
      <td>유상증자 주주우선배정[2012/04/17]</td>
    </tr>
    <tr>
      <td>2025-04-11</td>
      <td>A020120</td>
      <td>키다리스튜디오</td>
      <td>진도투자목적유한회사</td>
      <td>NaN</td>
      <td>2.00</td>
      <td>0.06</td>
      <td>15,933,604,890</td>
      <td>16,261,710,010</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</pre>

SK의 예시를 보았는데.. 어떤 식으로 데이터가이드에 반영되었는지 쉽사리 짐작이 가지는 않습니다. 대략적인 추세를 확인하였다는 시사점을 끝으로 이번 포스팅을 마치겠습니다...

![sk]({{site.url}}/assets/images/2025-04-14-stockcollateral/sk.png)
<br><br>
