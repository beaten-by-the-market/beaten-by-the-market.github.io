---
layout: single
title:  "10년간 코스피 자사주 직접취득 현황(시사점)"
categories: 한국시장
tag: [python, opendart, insight, 자기주식]
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
**[관련 포스팅]** [자사주 매매 데이터출처](https://beaten-by-the-market.github.io/%ED%95%9C%EA%B5%AD%EC%8B%9C%EC%9E%A5/buybackexplanation2/)
{:.notice--success}



## 데이터 수집 및 시각화 방향

**1. OpenDART를 통해 자기주식 관련 금감원 공시 내용 수집하기**{: style="color: #4682B4;"}

* 전체 자사주 **"직접"**{: style="color: #4682B4;"} 취득/처분하기로 **결정한**{: style="color: #4682B4;"} 수량의 추이를 확인
<br>
<br>

**2. 금감원 공시에서 자사주 매매의 장내/장외를 구분하기**{: style="color: #4682B4;"}

* 장내 수량이 얼마나 많을까? 만약 생각보다 장외수량이 미미하다면 거래소 데이터만으로도 활용이 가능할 것이다!
<br><br>


## 금감원 공시를 통해 자사주 **직접 취득** 통계 불러오기
이 데이터는 주요사항보고서(자사주취득) 공시기준 데이터이기 때문에, 실제 취득수량과는 차이가 있습니다.<br>


### 검색기준

데이터의 기준은 "코스피상장법인", "2015~2024"년으로 하였습니다. 참고로 **OpenDart는 2015년부터 데이터를 제공**{: style="color: #4682B4;"}합니다.<br>

### 총 몇 649건 확인

위의 검색기준으로 조회한 결과, 코스피 상장사들이 자사주를 직접취득한다고 제출한 공시건수는 총 649건이 있었습니다.<br>

### 데이터 수집하기


### 수집된 데이터프레임 형태 확인

OpenDart 페이지에서 받아온 데이터프레임이 어떤 형태인지 한번 확인해 보겠습니다. ***(상위 5개 행만 확인)***

<pre>
<table border="1" class="dataframe dataframe">
  <thead>
    <tr>
      <th>회사명</th>
      <th>접수일</th>
      <th colspan="2" halign="left">취득예정주식(주)</th>
      <th colspan="2" halign="left">취득예정금액(원)</th>
      <th colspan="2" halign="left">취득예상기간</th>
      <th colspan="2" halign="left">보유예상기간</th>
      <th>취득목적</th>
      <th>취득방법</th>
      <th>위탁투자중개업자</th>
      <th colspan="8" halign="left">취득 전 자기주식 보유현황</th>
      <th>취득결정일</th>
      <th colspan="2" halign="left">사외이사참석여부</th>
      <th>감사 (사외이사가 아닌 감사위원) 참석여부</th>
      <th colspan="2" halign="left">1일 매수 주문수량 한도</th>
      <th>비고</th>
    </tr>
    <tr>
      <th>회사명</th>
      <th>접수일</th>
      <th colspan="2" halign="left">취득예정주식(주)</th>
      <th colspan="2" halign="left">취득예정금액(원)</th>
      <th colspan="2" halign="left">취득예상기간</th>
      <th colspan="2" halign="left">보유예상기간</th>
      <th>취득목적</th>
      <th>취득방법</th>
      <th>위탁투자중개업자</th>
      <th colspan="4" halign="left">배당가능이익 범위 내 취득(주)</th>
      <th colspan="4" halign="left">기타취득(주)</th>
      <th>취득결정일</th>
      <th colspan="2" halign="left">사외이사참석여부</th>
      <th>감사 (사외이사가 아닌 감사위원) 참석여부</th>
      <th colspan="2" halign="left">1일 매수 주문수량 한도</th>
      <th>비고</th>
    </tr>
    <tr>
      <th>회사명</th>
      <th>접수일</th>
      <th>보통주식</th>
      <th>기타주식</th>
      <th>보통주식</th>
      <th>기타주식</th>
      <th>시작일</th>
      <th>종료일</th>
      <th>시작일</th>
      <th>종료일</th>
      <th>취득목적</th>
      <th>취득방법</th>
      <th>위탁투자중개업자</th>
      <th>보통주식</th>
      <th>비율(%)</th>
      <th>기타주식</th>
      <th>비율(%).1</th>
      <th>보통주식</th>
      <th>비율(%)</th>
      <th>기타주식</th>
      <th>비율(%).1</th>
      <th>취득결정일</th>
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
      <td>2021-06-09</td>
      <td>468222</td>
      <td>-</td>
      <td>2565856560</td>
      <td>-</td>
      <td>2021년 06월 09일</td>
      <td>2021년 06월 09일</td>
      <td>2021년 06월 09일</td>
      <td>-</td>
      <td>주식매수선택권 행사 재원 마련</td>
      <td>무상수증</td>
      <td>-</td>
      <td>1586257</td>
      <td>3.4</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>2021년 06월 09일</td>
      <td>2</td>
      <td>-</td>
      <td>참석</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>유CJ</td>
      <td>2018-07-05</td>
      <td>287770</td>
      <td>-</td>
      <td>40000030000</td>
      <td>-</td>
      <td>2018년 07월 06일</td>
      <td>2018년 10월 05일</td>
      <td>-</td>
      <td>-</td>
      <td>주가 안정을 통한 주주가치 제고</td>
      <td>유가증권 시장을 통한 직접 취득</td>
      <td>NH투자증권  (NH INVESTMENT & SECURITIES CO.,LTD.)</td>
      <td>1134000</td>
      <td>3.9</td>
      <td>-</td>
      <td>-</td>
      <td>1837572</td>
      <td>6.3</td>
      <td>1120</td>
      <td>0.0</td>
      <td>2018년 07월 05일</td>
      <td>3</td>
      <td>-</td>
      <td>-</td>
      <td>28777</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>유DB금융투자</td>
      <td>2022-03-08</td>
      <td>650000</td>
      <td>-</td>
      <td>3971500000</td>
      <td>-</td>
      <td>2022년 03월 10일</td>
      <td>2022년 06월 08일</td>
      <td>-</td>
      <td>-</td>
      <td>주가안정 및 주주가치 제고</td>
      <td>장내 매수</td>
      <td>DB금융투자(주)</td>
      <td>1017500</td>
      <td>2.4</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>2022년 03월 08일</td>
      <td>3</td>
      <td>0</td>
      <td>-</td>
      <td>65000</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>유DB금융투자</td>
      <td>2024-09-10</td>
      <td>650000</td>
      <td>-</td>
      <td>3854500000</td>
      <td>-</td>
      <td>2024년 09월 11일</td>
      <td>2024년 12월 10일</td>
      <td>-</td>
      <td>-</td>
      <td>기업가치제고 계획상 주주환원정책 이행</td>
      <td>장내 매수</td>
      <td>DB금융투자(주) (DB Financial Investment Co.,LTD.)</td>
      <td>1667500</td>
      <td>3.9</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>2024년 09월 10일</td>
      <td>3</td>
      <td>0</td>
      <td>-</td>
      <td>150745</td>
      <td>-</td>
      <td>2024년 09월 10일 최종보고서</td>
    </tr>
    <tr>
      <td>유DB손해보험</td>
      <td>2020-01-30</td>
      <td>708000</td>
      <td>-</td>
      <td>30585600000</td>
      <td>-</td>
      <td>2020년 01월 31일</td>
      <td>2020년 04월 30일</td>
      <td>-</td>
      <td>-</td>
      <td>주가안정을 통한 주주가치 제고</td>
      <td>유가증권시장을 통한 장내매수(직접취득)</td>
      <td>한국투자증권(Korea Investment & Securities Co., Ltd), 하나금융투자(Hana Financial Investment Co., Ltd), NH투자증권(NH Investment & Securities Co., Ltd.), 흥국증권(Heungkuk Securities Co. Ltd.), DB금융투자(DB Financial Investment Co., Ltd.)</td>
      <td>7500000</td>
      <td>10.6</td>
      <td>-</td>
      <td>-</td>
      <td>1660</td>
      <td>0.0</td>
      <td>-</td>
      <td>-</td>
      <td>2020년 01월 30일</td>
      <td>3</td>
      <td>0</td>
      <td>-</td>
      <td>70800</td>
      <td>-</td>
      <td>-</td>
    </tr>
  </tbody>
</table>
</pre>

칼럼이 불필요하게 길어서 위아래로 너무 넓어졌네요. 게다가 칼럼이 3층으로 되어 있습니다. 따라서 분석을 위해 필요한 칼럼을 남기고 칼럼명을 변환하였습니다.
<br><br>

### 데이터프레임 전처리

데이터프레임에 몇가지의 전처리를 더 하였습니다.
<br><br>
**1. 분석에 필요한 칼럼만 남깁니다.**{: style="color: #4682B4;"} <br>

해당 공시에는 우선주에 대한 부분도 있습니다. 물론 우선주 데이터도 가치가 있는 데이터이지만, 우선주가 상장되지 않은 경우가 더 많기 때문에 보통주에 관한 것으로 한정합니다.
<br><br>

**2. 단위를 조정합니다.**{: style="color: #4682B4;"}<br>

칼럼이 현재는 일괄로 str타입으로 되어있습니다. 따라서 분석을 위해 날짜, 숫자 형태 등으로 변경합니다. 또한 주단위(주 → 백만주), 원단위(원 → 억원)를 변환합니다.
<br><br>

**3. 회사명을 조정합니다.**{: style="color: #4682B4;"}<br>

OpenDart API가 아닌 웹페이지에서 크롤링해오다보니, 회사명에 다음과 같은 수식어들이 붙어있습니다. 이러한 수식어들을 제거하는 절차를 수행합니다. <br>
참고로 OpenDart API를 통해 데이터를 수집하는 경우, 이런 구분자가 불필요하게 붙지 않고, 종목코드가 딸려오기 때문에 더 정확하게 회사를 식별할 수 있는 장점이 있습니다.<br>

  * 시장구분자(***유, 코, 넥, 기***)가 회사명의 앞부분에 있습니다.

  * IR홈페이지가 있는 경우, 회사명 뒷부분에 ***'IR'***이 붙어있습니다.

<br>

### 전처리한 데이터프레임 확인

***(상위 5개 행만 확인)***

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
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AJ네트웍스</td>
      <td>2021-06-09</td>
      <td>468222.0</td>
      <td>25.658566</td>
      <td>2021년 06월 09일</td>
      <td>2021년 06월 09일</td>
      <td>2021년 06월 09일</td>
      <td>-</td>
      <td>주식매수선택권 행사 재원 마련</td>
      <td>무상수증</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>CJ</td>
      <td>2018-07-05</td>
      <td>287770.0</td>
      <td>400.000300</td>
      <td>2018년 07월 06일</td>
      <td>2018년 10월 05일</td>
      <td>-</td>
      <td>-</td>
      <td>주가 안정을 통한 주주가치 제고</td>
      <td>유가증권 시장을 통한 직접 취득</td>
      <td>2018</td>
    </tr>
    <tr>
      <td>DB금융투자</td>
      <td>2022-03-08</td>
      <td>650000.0</td>
      <td>39.715000</td>
      <td>2022년 03월 10일</td>
      <td>2022년 06월 08일</td>
      <td>-</td>
      <td>-</td>
      <td>주가안정 및 주주가치 제고</td>
      <td>장내 매수</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>DB금융투자</td>
      <td>2024-09-10</td>
      <td>650000.0</td>
      <td>38.545000</td>
      <td>2024년 09월 11일</td>
      <td>2024년 12월 10일</td>
      <td>-</td>
      <td>-</td>
      <td>기업가치제고 계획상 주주환원정책 이행</td>
      <td>장내 매수</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>DB손해보험</td>
      <td>2020-01-30</td>
      <td>708000.0</td>
      <td>305.856000</td>
      <td>2020년 01월 31일</td>
      <td>2020년 04월 30일</td>
      <td>-</td>
      <td>-</td>
      <td>주가안정을 통한 주주가치 제고</td>
      <td>유가증권시장을 통한 장내매수(직접취득)</td>
      <td>2020</td>
    </tr>
  </tbody>
</table>
</pre>

<br>
이제 보기 편한 데이터프레임이 되었습니다!
<br><br>

## 자사주 직접취득 데이터 시각화

<br>

![all_buyback]({{site.url}}/assets/images/2025-01-22-buybackinsight/all_buyback.png)<br><br>

그래프를 보니 우선 **코로나 시국이었던 2020년**{: style="color: #4682B4;"}이 눈에 띕니다. **수량기준으로는 2020년에 자사주 직접취득이 가장 높았으나 금액 기준으로는 낮은 수준**{: style="color: #4682B4;"}이었던 것을 감안하면, **코로나로 주가가 하락하자, 주가하락을 방어하기 위해 자사주 매입을 늘린 것이 영향이 있지 않았을지 유추**{: style="color: #4682B4;"}해볼 수 있습니다.<br>
한편, 2024년에는 주식수량과 금액기준 모두 높은 수치를 나타내었습니다.


## 자사주취득 장내 vs 장외 구분자 달기


'취득방법'은 선택지로 입력하는 방식이 아니라 회사가 free text로 기재하는 방식입니다. 이렇듯 표준화되지 않은 입력값은 분석에 장애물입니다. 하지만 다행히도 칼럼의 내용을 분석해본 결과, 일정 수준의 규칙으로 장내와 장외를 구분할 수 있는 것으로 보여집니다.


### 장내 vs 장외 구분규칙 정하기

다음의 규칙을 적용하였습니다.

1. **'시장, 장내, 시간외, 거래소'**{: style="color: #4682B4;"} 라는 표현을 포함하면 장내로 분류합니다. 띄어쓰기를 고려하여, '시간 외'도 포함합니다.

2. 조건1을 적용한 결과에서 **'시장외'**{: style="color: #4682B4;"}를 제외시킵니다.(띄어쓰기도 고려) 이는 시장외거래 라는 표현이 혹시나 존재할 경우, '시장'이라는 단어때문에 포함되는 것을 막기 위함입니다.


### 장내 vs 장외 자사주 취득 시각화

<br>

![buyback_mkt_otc]({{site.url}}/assets/images/2025-01-22-buybackinsight/buyback_mkt_otc.png)<br><br>

앞서 장내/장외를 구분하지 않고 합쳐서 보았던 것과 추이는 주식 수량 및 금액이 모두 동일하게 나타났습니다.

### 장내 vs 장외 자사주 취득 시사점

전반적으로 **장외취득은 미미한 수준**{: style="color: #4682B4;"}인 것으로 보입니다. 그러나 **2024년에 유의미하게 높은 것을 확인**{: style="color: #4682B4;"} 가능합니다. 왜 일까요?<br><br>

2024년 데이터를 확인해보겠습니다. 필터를 걸고, 취득예정금액을 기준으로 내림차순으로 정렬합니다.



<pre>
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>회사명</th>
      <th>접수일</th>
      <th>취득예정주식</th>
      <th>취득예정금액</th>
      <th>연도</th>
      <th>method</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>고려아연</td>
      <td>2024-10-11</td>
      <td>3623075.0</td>
      <td>32245.367500</td>
      <td>2024</td>
      <td>otc</td>
    </tr>
    <tr>
      <td>삼성전자</td>
      <td>2024-11-18</td>
      <td>50144628.0</td>
      <td>26827.375980</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>현대자동차</td>
      <td>2024-11-27</td>
      <td>3906545.0</td>
      <td>8731.128075</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>기아</td>
      <td>2024-01-25</td>
      <td>5688282.0</td>
      <td>5000.000000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>NAVER</td>
      <td>2024-09-30</td>
      <td>2347500.0</td>
      <td>4011.877500</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>케이티앤지</td>
      <td>2024-08-08</td>
      <td>3610000.0</td>
      <td>3371.740000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>두산밥캣</td>
      <td>2024-12-16</td>
      <td>4662004.0</td>
      <td>2000.000000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>크래프톤</td>
      <td>2024-03-26</td>
      <td>830000.0</td>
      <td>1992.000000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>신한지주</td>
      <td>2024-02-08</td>
      <td>3500583.0</td>
      <td>1500.000000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>현대모비스</td>
      <td>2024-02-16</td>
      <td>660000.0</td>
      <td>1498.200000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>케이티앤지</td>
      <td>2024-11-07</td>
      <td>1350000.0</td>
      <td>1493.100000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>우리금융지주</td>
      <td>2024-03-13</td>
      <td>9357960.0</td>
      <td>1366.262160</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>셀트리온</td>
      <td>2024-11-21</td>
      <td>583431.0</td>
      <td>1000.000734</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>셀트리온</td>
      <td>2024-10-25</td>
      <td>537924.0</td>
      <td>1000.000716</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>POSCO홀딩스</td>
      <td>2024-07-12</td>
      <td>255428.0</td>
      <td>1000.000620</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>셀트리온</td>
      <td>2024-12-27</td>
      <td>546747.0</td>
      <td>1000.000263</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>SK스퀘어</td>
      <td>2024-11-21</td>
      <td>1253132.0</td>
      <td>1000.000000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>엔씨소프트</td>
      <td>2024-05-09</td>
      <td>533417.0</td>
      <td>980.953863</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>셀트리온</td>
      <td>2024-03-05</td>
      <td>425895.0</td>
      <td>750.001095</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>셀트리온</td>
      <td>2024-04-17</td>
      <td>436047.0</td>
      <td>750.000840</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>셀트리온</td>
      <td>2024-06-14</td>
      <td>410734.0</td>
      <td>750.000284</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>미래에셋증권</td>
      <td>2024-08-07</td>
      <td>10000000.0</td>
      <td>687.000000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>미래에셋증권</td>
      <td>2024-01-25</td>
      <td>10000000.0</td>
      <td>679.000000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>NH투자증권</td>
      <td>2024-03-12</td>
      <td>4173622.0</td>
      <td>500.000000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>키움증권</td>
      <td>2024-08-14</td>
      <td>350000.0</td>
      <td>445.900000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>강원랜드</td>
      <td>2024-10-10</td>
      <td>2405292.0</td>
      <td>400.000000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>한솔케미칼</td>
      <td>2024-10-17</td>
      <td>270000.0</td>
      <td>328.050000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>에스디바이오센서</td>
      <td>2024-11-13</td>
      <td>3726709.0</td>
      <td>300.000074</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>케이티</td>
      <td>2024-02-08</td>
      <td>715985.0</td>
      <td>271.000322</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>하이브</td>
      <td>2024-08-27</td>
      <td>150000.0</td>
      <td>265.950000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>엔에이치엔</td>
      <td>2024-02-13</td>
      <td>787500.0</td>
      <td>200.025000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>신세계인터내셔날</td>
      <td>2024-03-20</td>
      <td>1071000.0</td>
      <td>170.289000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>HDC</td>
      <td>2024-02-01</td>
      <td>2000000.0</td>
      <td>146.400000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>엔에이치엔</td>
      <td>2024-08-05</td>
      <td>524000.0</td>
      <td>100.084000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>엔에이치엔</td>
      <td>2024-11-11</td>
      <td>615400.0</td>
      <td>100.002500</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>롯데렌탈</td>
      <td>2024-07-23</td>
      <td>324675.0</td>
      <td>100.000000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>방림</td>
      <td>2024-12-16</td>
      <td>2111932.0</td>
      <td>100.000000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>현대그린푸드</td>
      <td>2024-11-07</td>
      <td>745374.0</td>
      <td>91.755539</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>엠씨넥스</td>
      <td>2024-11-04</td>
      <td>400000.0</td>
      <td>68.400000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>TYM</td>
      <td>2024-11-12</td>
      <td>1820940.0</td>
      <td>59.999973</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>백산</td>
      <td>2024-03-08</td>
      <td>515000.0</td>
      <td>56.650000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>삼익악기</td>
      <td>2024-02-22</td>
      <td>5000000.0</td>
      <td>52.500000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>JW중외제약</td>
      <td>2024-12-17</td>
      <td>213676.0</td>
      <td>50.000184</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>JW홀딩스</td>
      <td>2024-06-10</td>
      <td>1718214.0</td>
      <td>50.000027</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>LF</td>
      <td>2024-03-20</td>
      <td>351123.0</td>
      <td>50.000000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>대한화섬</td>
      <td>2024-09-12</td>
      <td>50000.0</td>
      <td>49.600000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>미원상사</td>
      <td>2024-08-26</td>
      <td>25000.0</td>
      <td>49.475000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>미원상사</td>
      <td>2024-05-29</td>
      <td>25000.0</td>
      <td>49.250000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>엔피씨</td>
      <td>2024-04-02</td>
      <td>1000000.0</td>
      <td>48.850000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>엔피씨</td>
      <td>2024-09-23</td>
      <td>1000000.0</td>
      <td>45.250000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>광동제약</td>
      <td>2024-11-12</td>
      <td>800000.0</td>
      <td>44.880000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>대동전자</td>
      <td>2024-04-12</td>
      <td>650000.0</td>
      <td>44.330000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>엠씨넥스</td>
      <td>2024-07-08</td>
      <td>200000.0</td>
      <td>43.700000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>미원상사</td>
      <td>2024-03-06</td>
      <td>25000.0</td>
      <td>42.625000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>한화손해보험</td>
      <td>2024-04-18</td>
      <td>1000000.0</td>
      <td>42.000000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>HDC현대EP</td>
      <td>2024-07-25</td>
      <td>1000000.0</td>
      <td>40.500000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>백산</td>
      <td>2024-06-17</td>
      <td>300000.0</td>
      <td>40.500000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>DB금융투자</td>
      <td>2024-09-10</td>
      <td>650000.0</td>
      <td>38.545000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>엠씨넥스</td>
      <td>2024-03-14</td>
      <td>150000.0</td>
      <td>36.525000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>엔피씨</td>
      <td>2024-08-06</td>
      <td>1000000.0</td>
      <td>36.150000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>백산</td>
      <td>2024-07-19</td>
      <td>260000.0</td>
      <td>35.594000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>LF</td>
      <td>2024-10-02</td>
      <td>235057.0</td>
      <td>35.000000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>지누스</td>
      <td>2024-02-06</td>
      <td>237972.0</td>
      <td>34.815304</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>백산</td>
      <td>2024-11-13</td>
      <td>250000.0</td>
      <td>31.600000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>두산밥캣</td>
      <td>2024-04-29</td>
      <td>60467.0</td>
      <td>31.442840</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>LF</td>
      <td>2024-08-19</td>
      <td>212765.0</td>
      <td>30.000000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>LF</td>
      <td>2024-09-06</td>
      <td>211416.0</td>
      <td>30.000000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>미원에스씨</td>
      <td>2024-02-15</td>
      <td>20000.0</td>
      <td>27.000000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>미원에스씨</td>
      <td>2024-10-11</td>
      <td>20000.0</td>
      <td>26.320000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>JW홀딩스</td>
      <td>2024-12-17</td>
      <td>851789.0</td>
      <td>25.000007</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>NI스틸</td>
      <td>2024-11-15</td>
      <td>581395.0</td>
      <td>20.000000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>문배철강</td>
      <td>2024-11-15</td>
      <td>930233.0</td>
      <td>20.000000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>신일전자</td>
      <td>2024-11-05</td>
      <td>1390000.0</td>
      <td>19.863100</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>케이탑리츠</td>
      <td>2024-03-07</td>
      <td>2000000.0</td>
      <td>19.700000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>삼영</td>
      <td>2024-11-06</td>
      <td>240000.0</td>
      <td>9.972000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>동남합성</td>
      <td>2024-12-11</td>
      <td>20000.0</td>
      <td>5.980000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>삼화왕관</td>
      <td>2024-12-12</td>
      <td>20000.0</td>
      <td>5.920000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>동남합성</td>
      <td>2024-03-20</td>
      <td>20000.0</td>
      <td>5.740000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>MH에탄올</td>
      <td>2024-08-27</td>
      <td>100000.0</td>
      <td>5.660000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>문배철강</td>
      <td>2024-02-02</td>
      <td>162338.0</td>
      <td>5.000000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>SK아이이테크놀로지</td>
      <td>2024-06-26</td>
      <td>3652.0</td>
      <td>1.599576</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>SK아이이테크놀로지</td>
      <td>2024-02-02</td>
      <td>1718.0</td>
      <td>1.285064</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>이마트</td>
      <td>2024-07-18</td>
      <td>1000.0</td>
      <td>0.576000</td>
      <td>2024</td>
      <td>mkt</td>
    </tr>
    <tr>
      <td>금양</td>
      <td>2024-10-31</td>
      <td>10000000.0</td>
      <td>0.000000</td>
      <td>2024</td>
      <td>otc</td>
    </tr>
    <tr>
      <td>한화</td>
      <td>2024-07-05</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>2024</td>
      <td>otc</td>
    </tr>
    <tr>
      <td>핸즈코퍼레이션</td>
      <td>2024-07-03</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>2024</td>
      <td>otc</td>
    </tr>
  </tbody>
</table>
</pre>


**고려아연에서 발생한 경영권분쟁 관련 공개매수에 의한 것**{: style="color: #4682B4;"}이었습니다. 이러한 특수한 경우를 제외하고는 "이사회 결정기준" 장외 취득의 비중은 대세에는 영향을 미치지 않는 것으로 보입니다. KRX의 장내 자사주 데이터만으로도 충분히 좋은 시사점을 도출할 수 있겠다는 생각도 이어서 드는 부분입니다.
