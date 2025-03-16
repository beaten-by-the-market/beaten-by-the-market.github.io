---
layout: single
title:  "자기주식.. 직접? 신탁?"
categories: 한국시장
tag: [자기주식, insight, krx]
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
**[관련 포스팅]** [10년간 코스피 자사주 직접'처분' 현황(시사점)](https://beaten-by-the-market.github.io/%ED%95%9C%EA%B5%AD%EC%8B%9C%EC%9E%A5/kospi_dart_buyback_resale/)<br>
{:.notice--success}

## 지난 포스팅에선...
지난 포스팅에서는 금융감독원에 제출된 '자기주식 취득/처분 결정'공시를 살펴보았습니다. 10년치 데이터를 전수조사한 결과 다음과 같은 점을 확인할 수 있었습니다.
* 금감원에 제출된 주요사항보고서(자기주식 취득/처분) 공시는 **'결정'을 한 사항이지 확정된 사항이 아니다.**{: style="color: #4682B4;"}<br>
  ⇒ 따라서 실제로 취득/처분한 금액은 '결정'한 금액과 다를 수 있다.<br>
* **'장외' 취득금액은 얼마 되지 않는다.**{: style="color: #4682B4;"}<br>
  ⇒ 따라서 '장내'인 거래소의 데이터로 분석을 해도 시사점 도출에는 무리가 없을 수 있다.

## 직접취득과 신탁취득이란?
회사가 자기 주식을 사들이는 방법에는 두 가지가 있습니다. **'직접 취득 방식'**{: style="color: #4682B4;"}은 회사가 직접 자사 주식을 매입하는 것으로, 회사가 매입 시기와 가격을 직접 결정하므로 통제력이 높습니다. 반면, **'신탁 취득 방식'**{: style="color: #4682B4;"}은 일종의 특별한 펀드에 가입하는 것과 유사합니다. 회사가 자금을 신탁회사에 맡기면, 신탁회사는 오직 그 회사의 자기주식만 매입할 수 있는 제한된 펀드처럼 운용합니다. 이 신탁 안에는 현금과 매입한 자기주식 두 종류의 자산만 존재하죠. 회사는 미리 정한 조건 안에서 전문가에게 주식 매입을 위임함으로써, 시장 교란 우려를 줄이고 객관적인 매입 기준을 적용할 수 있다는 장점이 있습니다. 


## 거래소의 자사주 취득/처분 데이터 불러오기
이전 포스팅 [**'자사주 매매 데이터출처'(링크)**{: style="color: #4682B4;"}](https://beaten-by-the-market.github.io/%ED%95%9C%EA%B5%AD%EC%8B%9C%EC%9E%A5/buybackexplanation2/)에서는 [**KRX 정보데이터시스템(링크)**{: style="color: #4682B4;"}](http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0202)의 "이슈통계 - 자사주취득/처분"메뉴에서는 전체 상장사의 자사주 관련 누적 매매실적을 확인할 수 있음을 소개한 적 있습니다. 거래소 데이터이니 당연히 장내 수량이고 장외 수량은 카운트되어 있지 않습니다.<br><br>

![krxresult]({{site.url}}/assets/images/2025-01-22-buybackexpl2/krxresult.png)
<br><br>

2015~2024년의 데이터를 다운받아 보았습니다. 상위 10개 행을 한번 확인해보겠습니다. 
<pre>
행의 개수: 4,738
상위 10개 행만 확인해보기
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>공시일</th>
      <th>종목코드</th>
      <th>종목명</th>
      <th>시장구분</th>
      <th>직접/신탁</th>
      <th>취득/처분</th>
      <th>취득(처분)예정기간_시작일</th>
      <th>취득(처분)예정기간_종료일</th>
      <th>신고내역_수량</th>
      <th>신고내역_금액</th>
      <th>체결내역(누계)_수량</th>
      <th>체결내역(누계)_체결수량비율</th>
      <th>체결내역(누계)_금액</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2024/12/24</td>
      <td>197140</td>
      <td>디지캡</td>
      <td>KOSDAQ</td>
      <td>직접</td>
      <td>처분</td>
      <td>2024/12/26</td>
      <td>2024/12/26</td>
      <td>324480</td>
      <td>764150400</td>
      <td>324480.0</td>
      <td>100.0</td>
      <td>764150400.0</td>
    </tr>
    <tr>
      <td>2024/12/24</td>
      <td>078350</td>
      <td>한양디지텍</td>
      <td>KOSDAQ</td>
      <td>신탁</td>
      <td>취득</td>
      <td>2024/12/24</td>
      <td>2025/12/23</td>
      <td>0</td>
      <td>2500000000</td>
      <td>240000.0</td>
      <td>0.0</td>
      <td>2340710565.0</td>
    </tr>
    <tr>
      <td>2024/12/23</td>
      <td>162300</td>
      <td>신스틸</td>
      <td>KOSDAQ</td>
      <td>신탁</td>
      <td>취득</td>
      <td>2024/12/23</td>
      <td>2025/06/23</td>
      <td>0</td>
      <td>1000000000</td>
      <td>281580.0</td>
      <td>0.0</td>
      <td>726538210.0</td>
    </tr>
    <tr>
      <td>2024/12/23</td>
      <td>290560</td>
      <td>신시웨이</td>
      <td>KOSDAQ</td>
      <td>신탁</td>
      <td>취득</td>
      <td>2024/12/23</td>
      <td>2025/06/23</td>
      <td>0</td>
      <td>1000000000</td>
      <td>75387.0</td>
      <td>0.0</td>
      <td>483953550.0</td>
    </tr>
    <tr>
      <td>2024/12/20</td>
      <td>092070</td>
      <td>디엔에프</td>
      <td>KOSDAQ</td>
      <td>신탁</td>
      <td>취득</td>
      <td>2024/12/20</td>
      <td>2025/06/19</td>
      <td>0</td>
      <td>2000000000</td>
      <td>187780.0</td>
      <td>0.0</td>
      <td>1998213120.0</td>
    </tr>
    <tr>
      <td>2024/12/20</td>
      <td>006730</td>
      <td>서부T&D</td>
      <td>KOSDAQ</td>
      <td>직접</td>
      <td>취득</td>
      <td>2024/12/21</td>
      <td>2025/03/20</td>
      <td>1000000</td>
      <td>5310000000</td>
      <td>612000.0</td>
      <td>61.2</td>
      <td>3384222620.0</td>
    </tr>
    <tr>
      <td>2024/12/20</td>
      <td>085310</td>
      <td>엔케이</td>
      <td>KOSPI</td>
      <td>신탁</td>
      <td>취득</td>
      <td>2024/12/20</td>
      <td>2025/06/19</td>
      <td>0</td>
      <td>3000000000</td>
      <td>3201817.0</td>
      <td>0.0</td>
      <td>2996999405.0</td>
    </tr>
    <tr>
      <td>2024/12/20</td>
      <td>081150</td>
      <td>티플랙스</td>
      <td>KOSDAQ</td>
      <td>신탁</td>
      <td>취득</td>
      <td>2024/12/23</td>
      <td>2025/06/22</td>
      <td>0</td>
      <td>2000000000</td>
      <td>80757.0</td>
      <td>0.0</td>
      <td>246555065.0</td>
    </tr>
    <tr>
      <td>2024/12/19</td>
      <td>169670</td>
      <td>코스텍시스템</td>
      <td>KONEX</td>
      <td>신탁</td>
      <td>취득</td>
      <td>2025/02/04</td>
      <td>2026/02/03</td>
      <td>0</td>
      <td>2000000000</td>
      <td>32716.0</td>
      <td>0.0</td>
      <td>394072800.0</td>
    </tr>
    <tr>
      <td>2024/12/19</td>
      <td>007280</td>
      <td>한국특강</td>
      <td>KOSPI</td>
      <td>신탁</td>
      <td>취득</td>
      <td>2024/12/19</td>
      <td>2025/06/18</td>
      <td>0</td>
      <td>6000000000</td>
      <td>2155171.0</td>
      <td>0.0</td>
      <td>3568368129.0</td>
    </tr>
  </tbody>
</table>
</pre>

시장(코스피/코스닥), 취득/처분, 방식(직접/신탁)에 걸쳐 10년간 총 4,738건의 기록이 있습니다. 매매건수가 아니라, 상장법인이 자기주식을 취득하겠다고 신고하고 이행한 건수가 4,738건이라는 것입니다. 직접취득, 직접처분, 신탁계약 공시 건수라고 보셔도 좋을 것 같습니다.

## 코스피 법인 추이보기
이제 전체 데이터를 시장별로, 취득/처분별로 쪼개어 보도록 하겠습니다. 먼저 **'코스피' 시장의 '취득'**{: style="color: #4682B4;"}입니다.

### (취득) 연도별 유형별 취득수량/취득금액 구하기




<pre>
행의 개수: 22
확인해보기
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>시장구분</th>
      <th>year</th>
      <th>직접/신탁</th>
      <th>취득/처분</th>
      <th>신고내역_수량</th>
      <th>체결내역(누계)_수량</th>
      <th>신고내역_금액(억원)</th>
      <th>체결내역(누계)_금액(억원)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>KOSPI</td>
      <td>2015</td>
      <td>신탁</td>
      <td>취득</td>
      <td>0</td>
      <td>17,704,884</td>
      <td>3,623</td>
      <td>2,334</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2015</td>
      <td>직접</td>
      <td>취득</td>
      <td>137,975,612</td>
      <td>137,410,358</td>
      <td>97,324</td>
      <td>97,283</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2016</td>
      <td>신탁</td>
      <td>취득</td>
      <td>0</td>
      <td>70,358,259</td>
      <td>17,044</td>
      <td>13,523</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2016</td>
      <td>직접</td>
      <td>취득</td>
      <td>43,658,944</td>
      <td>39,048,576</td>
      <td>87,817</td>
      <td>91,598</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2017</td>
      <td>신탁</td>
      <td>취득</td>
      <td>0</td>
      <td>36,554,913</td>
      <td>8,460</td>
      <td>7,053</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2017</td>
      <td>직접</td>
      <td>취득</td>
      <td>36,564,065</td>
      <td>35,798,399</td>
      <td>94,789</td>
      <td>97,787</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2018</td>
      <td>신탁</td>
      <td>취득</td>
      <td>0</td>
      <td>43,154,691</td>
      <td>9,551</td>
      <td>7,930</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2018</td>
      <td>직접</td>
      <td>취득</td>
      <td>71,057,392</td>
      <td>69,153,688</td>
      <td>46,784</td>
      <td>46,567</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2019</td>
      <td>신탁</td>
      <td>취득</td>
      <td>0</td>
      <td>55,048,998</td>
      <td>11,957</td>
      <td>10,282</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2019</td>
      <td>직접</td>
      <td>취득</td>
      <td>33,896,491</td>
      <td>33,255,244</td>
      <td>22,947</td>
      <td>24,936</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2020</td>
      <td>신탁</td>
      <td>취득</td>
      <td>0</td>
      <td>91,519,157</td>
      <td>28,776</td>
      <td>24,804</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2020</td>
      <td>직접</td>
      <td>취득</td>
      <td>196,677,711</td>
      <td>187,033,380</td>
      <td>27,691</td>
      <td>27,639</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2021</td>
      <td>신탁</td>
      <td>취득</td>
      <td>0</td>
      <td>108,978,602</td>
      <td>12,655</td>
      <td>12,090</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2021</td>
      <td>직접</td>
      <td>취득</td>
      <td>75,018,607</td>
      <td>74,750,544</td>
      <td>21,387</td>
      <td>21,068</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2022</td>
      <td>신탁</td>
      <td>취득</td>
      <td>0</td>
      <td>95,708,100</td>
      <td>24,945</td>
      <td>21,908</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2022</td>
      <td>직접</td>
      <td>취득</td>
      <td>79,342,560</td>
      <td>70,531,297</td>
      <td>24,516</td>
      <td>25,017</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2023</td>
      <td>스톡옵션</td>
      <td>취득</td>
      <td>85,471</td>
      <td>85,471</td>
      <td>100</td>
      <td>112</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2023</td>
      <td>신탁</td>
      <td>취득</td>
      <td>0</td>
      <td>142,548,037</td>
      <td>36,391</td>
      <td>34,638</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2023</td>
      <td>직접</td>
      <td>취득</td>
      <td>77,204,876</td>
      <td>74,650,467</td>
      <td>31,722</td>
      <td>31,970</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2024</td>
      <td>스톡옵션</td>
      <td>취득</td>
      <td>151,000</td>
      <td>151,000</td>
      <td>267</td>
      <td>261</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2024</td>
      <td>신탁</td>
      <td>취득</td>
      <td>0</td>
      <td>115,411,059</td>
      <td>51,076</td>
      <td>46,511</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2024</td>
      <td>직접</td>
      <td>취득</td>
      <td>162,209,113</td>
      <td>157,393,132</td>
      <td>75,549</td>
      <td>76,740</td>
    </tr>
  </tbody>
</table>
</pre>

표로 보니깐 쉽지 않네요... 바로 시각화하여 보도록 하겠습니다.

### (취득) 직접취득 vs 신탁취득 비중확인하기

![2kospi_summary]({{site.url}}/assets/images/2025-03-16-buybackmkt/2kospi_summary.png)
<br><br>
**먼저 전체 수량과 전체 금액을 보겠습니다.**{: style="color: #4682B4;"} 직접취득과 신탁취득을 합쳐서 **취득수량(그림 왼편)은 코스피시장에서 점진적으로 증가한 추세**{: style="color: #4682B4;"}를 확인할 수 있습니다. 2020년에는 코로나 사태로 주가가 급락하자 취득 수량이 급증한 것도 보이네요. 한편, **취득금액(그림 오른편)도 최근에 지속적으로 증가**{: style="color: #4682B4;"}해 온것을 확인할 수 있습니다. <br>

이번엔 **직접취득 vs 신탁취득** 비중을 보겠습니다. 금액만 놓고 보면, 2019년까지는 기업들이 직접 취득한 비중이 확연히 높았는데, **2020년부터는 신탁방식을 통한 취득이 거의 절반수준**{: style="color: #4682B4;"}까지 올라왔습니다.


### (취득) 자사주 취득 신고대비 실제 취득 확인하기(장내취득限)
'직접vs신탁' 비교를 잠시 떠나서, 마침 수집한 데이터에 있으니 신고대비 실제취득을 볼까요? 참고로 여기서 '신고'데이터는 금감원 공시기준은 아니고, 거래소에 신고한 기준입니다. 한편 취득방법에는 '직접/신탁/스톡옵션'이 있는데, 거래소에 사전신고하는 것은 '직접'에만 해당합니다. 전반적으로 크게 갭이 벌어지는 데이터는 없는 것으로 보입니다. <br>

![1kospi_reportreal]({{site.url}}/assets/images/2025-03-16-buybackmkt/1kospi_reportreal.png)
<br><br>


### (처분) 연도별 유형별 처분수량/처분금액 구하기
이번엔 코스피 시장에서 직접/신탁 방식별로 처분 수량과 처분 금액을 살펴보도록 하겠습니다.

<pre>
행의 개수: 16
확인해보기
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>시장구분</th>
      <th>year</th>
      <th>직접/신탁</th>
      <th>취득/처분</th>
      <th>신고내역_수량</th>
      <th>체결내역(누계)_수량</th>
      <th>신고내역_금액(억원)</th>
      <th>체결내역(누계)_금액(억원)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>KOSPI</td>
      <td>2015</td>
      <td>신탁</td>
      <td>처분</td>
      <td>0</td>
      <td>26,158</td>
      <td>10</td>
      <td>4</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2015</td>
      <td>직접</td>
      <td>처분</td>
      <td>24,586,221</td>
      <td>24,518,342</td>
      <td>4,622</td>
      <td>4,566</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2016</td>
      <td>직접</td>
      <td>처분</td>
      <td>42,187,315</td>
      <td>42,184,600</td>
      <td>3,863</td>
      <td>3,780</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2017</td>
      <td>신탁</td>
      <td>처분</td>
      <td>0</td>
      <td>612,645</td>
      <td>220</td>
      <td>33</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2017</td>
      <td>직접</td>
      <td>처분</td>
      <td>54,697,984</td>
      <td>53,336,381</td>
      <td>10,701</td>
      <td>10,561</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2018</td>
      <td>신탁</td>
      <td>처분</td>
      <td>0</td>
      <td>345,019</td>
      <td>45</td>
      <td>13</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2018</td>
      <td>직접</td>
      <td>처분</td>
      <td>31,002,560</td>
      <td>31,000,504</td>
      <td>1,629</td>
      <td>1,605</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2019</td>
      <td>신탁</td>
      <td>처분</td>
      <td>0</td>
      <td>200,000</td>
      <td>20</td>
      <td>14</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2019</td>
      <td>직접</td>
      <td>처분</td>
      <td>23,049,059</td>
      <td>22,764,264</td>
      <td>1,157</td>
      <td>1,132</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2020</td>
      <td>신탁</td>
      <td>처분</td>
      <td>0</td>
      <td>1,276,626</td>
      <td>70</td>
      <td>107</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2020</td>
      <td>직접</td>
      <td>처분</td>
      <td>16,247,856</td>
      <td>16,247,856</td>
      <td>6,206</td>
      <td>6,199</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2021</td>
      <td>직접</td>
      <td>처분</td>
      <td>11,829,905</td>
      <td>11,822,905</td>
      <td>7,462</td>
      <td>7,448</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2022</td>
      <td>신탁</td>
      <td>처분</td>
      <td>0</td>
      <td>1,014,980</td>
      <td>50</td>
      <td>88</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2022</td>
      <td>직접</td>
      <td>처분</td>
      <td>20,421,792</td>
      <td>20,421,792</td>
      <td>15,429</td>
      <td>9,893</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2023</td>
      <td>직접</td>
      <td>처분</td>
      <td>9,293,850</td>
      <td>8,857,547</td>
      <td>3,499</td>
      <td>3,480</td>
    </tr>
    <tr>
      <td>KOSPI</td>
      <td>2024</td>
      <td>직접</td>
      <td>처분</td>
      <td>12,618,600</td>
      <td>11,618,600</td>
      <td>1,522</td>
      <td>1,272</td>
    </tr>
  </tbody>
</table>
</pre>

역시나 표로는 한눈에 안들어옵니다. 바로 시각화 해보도록 하겠습니다.

### (처분) 직접처분 vs 신탁처분 비중확인하기

<br>

![4kospi_summary_resale]({{site.url}}/assets/images/2025-03-16-buybackmkt/4kospi_summary_resale.png)
<br><br>

**먼저 전체 수량과 전체 금액을 보겠습니다.**{: style="color: #4682B4;"} 직접처분과 신탁처분을 합쳐서 **처분수량(그림 왼편)은 코스피시장에서 점진적으로 감소한 추세**{: style="color: #4682B4;"}를 확인할 수 있습니다. 한편, **처분금액(그림 오른편)은 2020~2022년에 높았음**{: style="color: #4682B4;"}을 확인할 수 있습니다. 2020년부터 2022년 중반까지는 주가지수가 상승하거나 높았던 시기입니다. 주가가 높을 때 아무래도 자기주식을 처분하여 현금을 확보하려는 경향이 있었을 것이라 유추해볼 수 있습니다.<br>

![kospichart]({{site.url}}/assets/images/2025-01-23-buyback-resaleinsight/kospichart.png)<br><br>

이번엔 **직접처분 vs 신탁처분** 비중을 보겠습니다. **수량과 금액 모두 신탁을 통한 처분은 없다시피 합니다.**{: style="color: #4682B4;"}


### (처분) 자사주 처분 신고대비 실제 처분 확인하기(장내처분限)
'직접vs신탁' 비교를 잠시 떠나서, 신고대비 실제처분을 볼까요? 2022년에 신고한 처분금액 대비 실제 체결금액이 크게 벌어져 있는 것을 확인할 수 있습니다. 왜 일까요?
<br>

![3kospi_reportreal_resale]({{site.url}}/assets/images/2025-03-16-buybackmkt/3kospi_reportreal_resale.png)
<br><br>
한번 어떤 사유였는지 확인해보겠습니다. 2022년 신고금액과 체결금액의 차이가 큰 순으로 5개를 정렬해보면 다음과 같습니다. 
<pre>
상위 5개 행을 확인해보기
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>공시일</th>
      <th>종목코드</th>
      <th>종목명</th>
      <th>시장구분</th>
      <th>직접/신탁</th>
      <th>취득/처분</th>
      <th>취득(처분)예정기간_시작일</th>
      <th>취득(처분)예정기간_종료일</th>
      <th>신고내역_수량</th>
      <th>체결내역(누계)_수량</th>
      <th>체결내역(누계)_체결수량비율</th>
      <th>신고내역_금액(억원)</th>
      <th>체결내역(누계)_금액(억원)</th>
      <th>차이(억원)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2022-11-23</td>
      <td>010130</td>
      <td>고려아연</td>
      <td>KOSPI</td>
      <td>직접</td>
      <td>처분</td>
      <td>2022/11/24</td>
      <td>2023/02/23</td>
      <td>406,994</td>
      <td>406,994</td>
      <td>100.0</td>
      <td>7,868</td>
      <td>2,633</td>
      <td>5,235</td>
    </tr>
    <tr>
      <td>2022-05-24</td>
      <td>066970</td>
      <td>엘앤에프</td>
      <td>KOSPI</td>
      <td>직접</td>
      <td>처분</td>
      <td>2022/05/24</td>
      <td>2022/08/23</td>
      <td>1,000,000</td>
      <td>1,000,000</td>
      <td>100.0</td>
      <td>2,766</td>
      <td>2,456</td>
      <td>310</td>
    </tr>
    <tr>
      <td>2022-04-08</td>
      <td>011700</td>
      <td>한신기계</td>
      <td>KOSPI</td>
      <td>직접</td>
      <td>처분</td>
      <td>2022/04/12</td>
      <td>2022/07/07</td>
      <td>1,660,200</td>
      <td>1,660,200</td>
      <td>100.0</td>
      <td>188</td>
      <td>155</td>
      <td>33</td>
    </tr>
    <tr>
      <td>2022-04-22</td>
      <td>008040</td>
      <td>사조동아원</td>
      <td>KOSPI</td>
      <td>직접</td>
      <td>처분</td>
      <td>2022/04/25</td>
      <td>2022/07/22</td>
      <td>5,000,000</td>
      <td>5,000,000</td>
      <td>100.0</td>
      <td>106</td>
      <td>101</td>
      <td>5</td>
    </tr>
    <tr>
      <td>2022-04-18</td>
      <td>008040</td>
      <td>사조동아원</td>
      <td>KOSPI</td>
      <td>직접</td>
      <td>처분</td>
      <td>2022/04/19</td>
      <td>2022/07/18</td>
      <td>5,000,000</td>
      <td>5,000,000</td>
      <td>100.0</td>
      <td>94</td>
      <td>89</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</pre> 

**고려아연에서 신고금액과 체결금액의 차이가 약 5,200억 차이**{: style="color: #4682B4;"}가 납니다... 위 그래프의 차이 상당부분에 해당하는 값입니다. 추측해볼 수 있는 사유로는 신고당시보다 처분시에 가격이 엄청나게 하락하거나 했을 수 있습니다. 근데 7,800억을 신고했는데 2,600억이 된다..? 67% 수준의 주가하락인데..
<br>

![chart_010130]({{site.url}}/assets/images/2025-03-16-buybackmkt/chart_010130.png)
<br><br>
확인해보니 많이 하락한게 맞습니다. 그런데 최고가 685천에서 최저가 505천은 약 26%하락인데요..? 공시도 한번 확인해보겠습니다. 

<br>

![disclosure_010130]({{site.url}}/assets/images/2025-03-16-buybackmkt/disclosure_010130.png)
<br><br>

전체 처분수량은 1,195,760주이고, **이중 406,994주가 시간외대량매매**{: style="color: #4682B4;"}였습니다. **거래소에 신고된 수량과 정확히 일치**{: style="color: #4682B4;"}하네요. 시간외대량매매는 거래상대방이 정해져 있어서 흔히 받아들이는 '장내'의 개념과는 살짝 차이가 있지만, 거래소를 통해서 이뤄지기 때문에 장내로 분류합니다. 한편, 전략적 제휴를 위해서 시간외대량매매로 처분을 한 것이기 때문에 가격은 두 파트너간 적절하다고 생각한 수준으로 이뤄졌을 것입니다.

※ 관련 포스팅 : 
* [자사주 매입: 시간외대량매매의 비중은 얼마일까?](https://beaten-by-the-market.github.io/%ED%95%9C%EA%B5%AD%EC%8B%9C%EC%9E%A5/buyback_blockdeal/)
* [자사주 처분: 시간외대량매매의 비중은 얼마일까?](https://beaten-by-the-market.github.io/%ED%95%9C%EA%B5%AD%EC%8B%9C%EC%9E%A5/buyback_resale_blockdeal/)

**그런데 조금 이상합니다.**{: style="color: #4682B4;"} 신고일 종가는 658,000원이었고, 수량이 406,994주면 **신고금액은 267,802,052,000원이 되어야 할 것**{: style="color: #4682B4;"} 같은데요...<br>
거래소 데이터에 기록된 786,810,080,000원은 신고수량인 406,994주로 나눠주면 **처분가격이 주당 1,933,223원**{: style="color: #4682B4;"}입니다. 너무 심각한 차이네요.. 아마 오타가 아닐까요..? 네.. 오타입니다. **금감원 공시를 다시 보시면 786,810,080,000원이 있습니다.****{: style="color: #4682B4;"} 이금액은 **시간외대량매매와 장외처분을 합친 금액****{: style="color: #4682B4;"}입니다. 상장법인이 거래소 시스템에 입력할 때 장내매매(시간외대량매매)에 해당하는 금액만 입력해야 하는데 **실수로 장외매매 금액까지 다 입력해버려서 생긴 일****{: style="color: #4682B4;"}로 보입니다.

<br>

![data010130]({{site.url}}/assets/images/2025-03-16-buybackmkt/data010130.png)
<br><br>


## 코스닥 법인 추이보기

지금까지 코스피 법인을 대상으로 했으니, 이번에는 코스닥 법인도 한번 살펴보겠습니다.

### (취득) 연도별 유형별 취득수량/취득금액 구하기

이미 불러온 거래소 데이터를 코스닥을 기준으로 필터를 걸어서 확인해보겠습니다. 코스닥의 자기지숙 **'취득'**{: style="color: #4682B4;"}입니다.

<pre>
행의 개수: 23
확인해보기
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>시장구분</th>
      <th>year</th>
      <th>직접/신탁</th>
      <th>취득/처분</th>
      <th>신고내역_수량</th>
      <th>체결내역(누계)_수량</th>
      <th>신고내역_금액(억원)</th>
      <th>체결내역(누계)_금액(억원)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>KOSDAQ</td>
      <td>2015</td>
      <td>신탁</td>
      <td>취득</td>
      <td>0</td>
      <td>21,547,130</td>
      <td>2,780</td>
      <td>1,941</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2015</td>
      <td>직접</td>
      <td>취득</td>
      <td>20,295,537</td>
      <td>18,810,977</td>
      <td>2,022</td>
      <td>1,970</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2016</td>
      <td>신탁</td>
      <td>취득</td>
      <td>0</td>
      <td>21,567,869</td>
      <td>4,776</td>
      <td>3,332</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2016</td>
      <td>직접</td>
      <td>취득</td>
      <td>20,102,025</td>
      <td>19,096,771</td>
      <td>3,192</td>
      <td>3,257</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2017</td>
      <td>신탁</td>
      <td>취득</td>
      <td>0</td>
      <td>31,954,656</td>
      <td>4,189</td>
      <td>3,127</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2017</td>
      <td>직접</td>
      <td>취득</td>
      <td>17,147,195</td>
      <td>14,472,834</td>
      <td>1,253</td>
      <td>1,252</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2018</td>
      <td>신탁</td>
      <td>취득</td>
      <td>0</td>
      <td>59,004,459</td>
      <td>8,009</td>
      <td>6,073</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2018</td>
      <td>직접</td>
      <td>취득</td>
      <td>36,423,571</td>
      <td>33,486,621</td>
      <td>4,870</td>
      <td>4,888</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2019</td>
      <td>스톡옵션</td>
      <td>취득</td>
      <td>323,000</td>
      <td>35,018</td>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2019</td>
      <td>신탁</td>
      <td>취득</td>
      <td>0</td>
      <td>37,416,422</td>
      <td>4,237</td>
      <td>2,961</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2019</td>
      <td>직접</td>
      <td>취득</td>
      <td>20,878,760</td>
      <td>19,609,276</td>
      <td>2,128</td>
      <td>2,143</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2020</td>
      <td>스톡옵션</td>
      <td>취득</td>
      <td>21,692</td>
      <td>21,692</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2020</td>
      <td>신탁</td>
      <td>취득</td>
      <td>0</td>
      <td>92,269,431</td>
      <td>9,234</td>
      <td>6,395</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2020</td>
      <td>직접</td>
      <td>취득</td>
      <td>51,064,858</td>
      <td>40,434,511</td>
      <td>3,591</td>
      <td>3,515</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2021</td>
      <td>신탁</td>
      <td>취득</td>
      <td>0</td>
      <td>33,377,359</td>
      <td>6,823</td>
      <td>5,233</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2021</td>
      <td>직접</td>
      <td>취득</td>
      <td>24,575,330</td>
      <td>23,786,489</td>
      <td>2,187</td>
      <td>2,202</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2022</td>
      <td>신탁</td>
      <td>취득</td>
      <td>0</td>
      <td>86,419,965</td>
      <td>14,292</td>
      <td>11,500</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2022</td>
      <td>직접</td>
      <td>취득</td>
      <td>71,582,673</td>
      <td>52,933,651</td>
      <td>4,264</td>
      <td>4,209</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2023</td>
      <td>스톡옵션</td>
      <td>취득</td>
      <td>113,000</td>
      <td>113,000</td>
      <td>9</td>
      <td>9</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2023</td>
      <td>신탁</td>
      <td>취득</td>
      <td>0</td>
      <td>99,127,024</td>
      <td>10,894</td>
      <td>8,548</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2023</td>
      <td>직접</td>
      <td>취득</td>
      <td>45,306,568</td>
      <td>41,644,965</td>
      <td>5,466</td>
      <td>5,428</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2024</td>
      <td>신탁</td>
      <td>취득</td>
      <td>0</td>
      <td>146,037,710</td>
      <td>13,065</td>
      <td>11,863</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2024</td>
      <td>직접</td>
      <td>취득</td>
      <td>75,209,065</td>
      <td>68,642,045</td>
      <td>3,673</td>
      <td>3,757</td>
    </tr>
  </tbody>
</table>
</pre>

표로 보기 힘드니 바로 시각화를 해보겠습니다.


### (취득) 직접취득 vs 신탁취득 비중확인하기
<br>

![6kosdaq_summary]({{site.url}}/assets/images/2025-03-16-buybackmkt/6kosdaq_summary.png)
<br><br>

수량 및 금액 모두 최근에는 증가하는 추이를 보이고 있습니다. 코스피와 다른 점이라면, **코스닥은 신탁을 통한 취득 비중이 직접 취득 보다 더 높네요.**{: style="color: #4682B4;"}


### (취득) 자사주 취득 신고대비 실제 취득 확인하기(장내취득限)
신고대비 취득도 한번 훑어보고 가겠습니다. 신고수량 대비 체결수량이 차이가 나는 경우는 몇 케이스 보이지만 금액은 신고금액과 거의 비슷합니다.
<br>

![5kosdaq_reportreal]({{site.url}}/assets/images/2025-03-16-buybackmkt/5kosdaq_reportreal.png)
<br><br>


### (처분) 연도별 유형별 처분수량/처분금액 구하기
이번에는 코스닥 시장의 자기주식 **'처분'**{: style="color: #4682B4;"}입니다. 표로 보기 힘드니 바로 시각화를 해보겠습니다.


<pre>
행의 개수: 20
확인해보기
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>시장구분</th>
      <th>year</th>
      <th>직접/신탁</th>
      <th>취득/처분</th>
      <th>신고내역_수량</th>
      <th>체결내역(누계)_수량</th>
      <th>신고내역_금액(억원)</th>
      <th>체결내역(누계)_금액(억원)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>KOSDAQ</td>
      <td>2015</td>
      <td>신탁</td>
      <td>처분</td>
      <td>0</td>
      <td>1,815,928</td>
      <td>110</td>
      <td>132</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2015</td>
      <td>직접</td>
      <td>처분</td>
      <td>64,644,329</td>
      <td>63,747,106</td>
      <td>4,317</td>
      <td>4,158</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2016</td>
      <td>신탁</td>
      <td>처분</td>
      <td>0</td>
      <td>512,849</td>
      <td>60</td>
      <td>52</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2016</td>
      <td>직접</td>
      <td>처분</td>
      <td>20,313,993</td>
      <td>17,685,768</td>
      <td>1,607</td>
      <td>1,504</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2017</td>
      <td>신탁</td>
      <td>처분</td>
      <td>0</td>
      <td>1,000,537</td>
      <td>50</td>
      <td>60</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2017</td>
      <td>직접</td>
      <td>처분</td>
      <td>17,317,269</td>
      <td>16,769,277</td>
      <td>2,142</td>
      <td>2,070</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2018</td>
      <td>신탁</td>
      <td>처분</td>
      <td>0</td>
      <td>1,565,486</td>
      <td>120</td>
      <td>71</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2018</td>
      <td>직접</td>
      <td>처분</td>
      <td>11,061,481</td>
      <td>10,609,169</td>
      <td>1,991</td>
      <td>1,944</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2019</td>
      <td>신탁</td>
      <td>처분</td>
      <td>0</td>
      <td>544,819</td>
      <td>35</td>
      <td>35</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2019</td>
      <td>직접</td>
      <td>처분</td>
      <td>6,404,550</td>
      <td>6,404,550</td>
      <td>815</td>
      <td>799</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2020</td>
      <td>신탁</td>
      <td>처분</td>
      <td>0</td>
      <td>2,958,693</td>
      <td>358</td>
      <td>380</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2020</td>
      <td>직접</td>
      <td>처분</td>
      <td>28,217,605</td>
      <td>25,916,199</td>
      <td>3,193</td>
      <td>2,728</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2021</td>
      <td>신탁</td>
      <td>처분</td>
      <td>0</td>
      <td>240,754</td>
      <td>30</td>
      <td>18</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2021</td>
      <td>직접</td>
      <td>처분</td>
      <td>34,663,852</td>
      <td>29,296,638</td>
      <td>3,705</td>
      <td>3,259</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2022</td>
      <td>신탁</td>
      <td>처분</td>
      <td>0</td>
      <td>107,441</td>
      <td>30</td>
      <td>9</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2022</td>
      <td>직접</td>
      <td>처분</td>
      <td>5,927,453</td>
      <td>5,704,905</td>
      <td>1,073</td>
      <td>1,019</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2023</td>
      <td>신탁</td>
      <td>처분</td>
      <td>0</td>
      <td>237,500</td>
      <td>30</td>
      <td>20</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2023</td>
      <td>직접</td>
      <td>처분</td>
      <td>7,839,882</td>
      <td>7,551,882</td>
      <td>1,523</td>
      <td>1,490</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2024</td>
      <td>신탁</td>
      <td>처분</td>
      <td>0</td>
      <td>500,966</td>
      <td>50</td>
      <td>17</td>
    </tr>
    <tr>
      <td>KOSDAQ</td>
      <td>2024</td>
      <td>직접</td>
      <td>처분</td>
      <td>11,316,672</td>
      <td>11,316,672</td>
      <td>1,462</td>
      <td>1,560</td>
    </tr>
  </tbody>
</table>
</pre>


### (처분) 직접처분 vs 신탁처분 비중확인하기
코스피와 비슷하게 **코로나 시국이후 주가가 회복하던 2020년, 2021년에 자기주식 처분이 많았습니다.**{: style="color: #4682B4;"} 자기주식 처분의 방법도 비슷합니다. 2020년에 12.2%를 제외하고는 코스닥시장도 **자기주식을 처분할 때 신탁 방식은 사용하지 않는 것**{: style="color: #4682B4;"}으로 나타났습니다.

![8kosdaq_summary_resale]({{site.url}}/assets/images/2025-03-16-buybackmkt/8kosdaq_summary_resale.png)
<br><br>



### (처분) 자사주 처분 신고대비 실제 처분 확인하기(장내처분限)
신고대비 처분도 한번 훑어보고 가겠습니다. 특이사항은 없습니다.
<br>

![7kosdaq_reportreal_resale]({{site.url}}/assets/images/2025-03-16-buybackmkt/7kosdaq_reportreal_resale.png)
<br><br>

## 눈에 띄는 규제
작년 말에 신탁을 통한 자사주 처분시 공시규제가 대폭 강화되었습니다. 그러나 앞서 10년치의 코스피, 코스닥의 사례를 본 결과, 신탁을 통한 자기주식 처분은 없다시피 합니다. 어차피 하고 있지 않으니 규제에 적용될 상장법인도 없겠지만 그래도 선제적으로 규제를 강화한 게 눈에 띄었습니다. 
<br>

![press]({{site.url}}/assets/images/2025-03-16-buybackmkt/press.png)
<br><br>

