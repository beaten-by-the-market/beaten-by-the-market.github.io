---
layout: single
title:  "기술성장 특례로 상장한 기업들은 어디일까?"
categories: 한국시장
tag: [krx, data background, insight, 상장]
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

## 기술성장 특례로 상장한 기업들은?

투자를 할 때 우리는 보통 기업의 가치를 평가하여 투자 대상을 선정합니다. 이 과정에서 재무정보는 가장 중요한 기준으로 작용합니다. <br>하지만 코스닥 시장에서 '기술성장기업'으로 특례상장된 기업들은 조금 다른 모습을 보입니다. 이들은 재무실적이 좋지 않더라도 기술력과 성장성을 인정받아 상장된 경우가 많습니다. 따라서 전통적인 재무분석 방식으로는 이 기업들의 매력을 제대로 평가하기 어려울 수 있습니다.<br><br>

이런 이유로 투자자 입장에서는 기술성장기업들을 별도의 투자 유니버스로 관리하고 싶어질 것입니다. 만약 기존의 재무기준 필터만을 사용한다면, 기술적으로 유망한 기업들을 놓칠 가능성이 높기 때문입니다.<br><br>

따라서 이들 기업에 대해서는 다른 평가기준이 필요합니다. 기술평가 특례와 성장성 특례와 같은 제도를 통해 상장된 기업들은 전문평가기관에서 기술력과 시장성을 인정받은 만큼, 투자자는 이를 중심으로 새로운 분석 프레임워크를 만들어야 합니다.<br><br>

분석을 논하기 전에... 일단 **"기술성장 특례로 상장한 기업은 어디일까?"**{: style="color: #4682B4;"}라는 질문으로 시작해보겠습니다. 언뜻 간단한 궁금증 같아 보이지만... 매우 기나긴 여정을 거쳐야 합니다.


## 정보데이터시스템에서 상장트랙별 회사 불러오기

특례상장기업 목록 찾기.. 홈페이지 하나에 다 나와있지 않을까? 라는 가벼운 마음으로 시작해봅니다. 이전에도 봤었던 한국거래소의 [정보데이터시스템(링크)](http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0202)에 있을 것 같아서 한번 가보겠습니다.<br><br>

![datakrx]({{site.url}}/assets/images/2025-03-01-listing/datakrx.png)<br><br>

바로 눈에 띄진 않지만 그래도 'IPO' 관련 내용이니깐 관련 메뉴를 클릭하다보면 **"[20043] 공모가 대비 주가수익률"**{: style="color: #4682B4;"}이란 화면이 나옵니다. 쉽게 찾았네요!<br><br>

![datakrx2]({{site.url}}/assets/images/2025-03-01-listing/datakrx2.png)<br><br>

...가 아니라 저 화면은 **최근 5년 상장법인까지만**{: style="color: #4682B4;"} 보여줍니다. 기술성장기업에 대한 특례기간은 보통 5년 정도입니다. 예를들면, 관리종목 지정사유가 발생해도 봐주는 기간이 5년 정도입니다. 이런 점을 고려하면 합리적인 수준의 표출인 것 같기도 합니다만... **혁신기술이나 성장성을 인정받아 상장한 회사 전체를 별도 투자유니버스로 구성하여 확인하고싶다는 궁금증에는 턱없이 부족한 정보입니다.**{: style="color: #4682B4;"}

<br><br>

그리고 하나더. **저 화면에는 종목코드가 없습니다.**{: style="color: #4682B4;"} 엑셀로 다운받아 보아도 없습니다. 종목코드가 없이는 다른 데이터소스와 연계하여 분석을 하기가 힘듭니다. 지난번 사례에서 보았듯, KIND에서의 회사명과 정보데이터시스템에서의 회사명이 다른 경우가 있습니다.

> 회사명으로는 식별되지 않는 경우가 많기 때문에 반드시 종목코드가 필요합니다.


<pre>
종목개수 : 151

<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>회사명</th>
      <th>상장트랙</th>
      <th>주관사</th>
      <th>상장일</th>
      <th>공모가</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>오름테라퓨틱</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2025/02/14</td>
      <td>20000</td>
    </tr>
    <tr>
      <td>아이에스티이</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>KB증권</td>
      <td>2025/02/12</td>
      <td>11400</td>
    </tr>
    <tr>
      <td>아이지넷</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>한국증권</td>
      <td>2025/02/04</td>
      <td>7000</td>
    </tr>
    <tr>
      <td>와이즈넛</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>삼성증권</td>
      <td>2025/01/24</td>
      <td>17000</td>
    </tr>
    <tr>
      <td>파인메딕스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2024/12/26</td>
      <td>10000</td>
    </tr>
    <tr>
      <td>쓰리에이로직스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>신한증권,미래에셋증권</td>
      <td>2024/12/24</td>
      <td>11000</td>
    </tr>
    <tr>
      <td>온코닉테라퓨틱스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2024/12/19</td>
      <td>13000</td>
    </tr>
    <tr>
      <td>온코크로스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권</td>
      <td>2024/12/18</td>
      <td>7300</td>
    </tr>
    <tr>
      <td>쓰리빌리언</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2024/11/14</td>
      <td>4500</td>
    </tr>
    <tr>
      <td>에어레인</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>신영증권</td>
      <td>2024/11/08</td>
      <td>23000</td>
    </tr>
    <tr>
      <td>토모큐브</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2024/11/07</td>
      <td>16000</td>
    </tr>
    <tr>
      <td>에이치이엠파마</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>신한증권</td>
      <td>2024/11/05</td>
      <td>23000</td>
    </tr>
    <tr>
      <td>클로봇</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권</td>
      <td>2024/10/28</td>
      <td>13000</td>
    </tr>
    <tr>
      <td>웨이비스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2024/10/25</td>
      <td>15000</td>
    </tr>
    <tr>
      <td>씨메스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>유진증권,삼성증권</td>
      <td>2024/10/24</td>
      <td>30000</td>
    </tr>
    <tr>
      <td>루미르</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2024/10/21</td>
      <td>12000</td>
    </tr>
    <tr>
      <td>셀비온</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2024/10/16</td>
      <td>15000</td>
    </tr>
    <tr>
      <td>아이언디바이스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2024/09/23</td>
      <td>7000</td>
    </tr>
    <tr>
      <td>이엔셀</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2024/08/23</td>
      <td>15300</td>
    </tr>
    <tr>
      <td>케이쓰리아이</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>하나증권</td>
      <td>2024/08/20</td>
      <td>15500</td>
    </tr>
    <tr>
      <td>넥스트바이오메디컬</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2024/08/20</td>
      <td>29000</td>
    </tr>
    <tr>
      <td>뱅크웨어글로벌</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권</td>
      <td>2024/08/12</td>
      <td>16000</td>
    </tr>
    <tr>
      <td>아이빔테크놀로지</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>삼성증권</td>
      <td>2024/08/06</td>
      <td>10000</td>
    </tr>
    <tr>
      <td>피앤에스미캐닉스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>키움증권</td>
      <td>2024/07/31</td>
      <td>22000</td>
    </tr>
    <tr>
      <td>엑셀세라퓨틱스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2024/07/15</td>
      <td>10000</td>
    </tr>
    <tr>
      <td>하스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>삼성증권</td>
      <td>2024/07/03</td>
      <td>16000</td>
    </tr>
    <tr>
      <td>이노스페이스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권</td>
      <td>2024/07/02</td>
      <td>43300</td>
    </tr>
    <tr>
      <td>에이치브이엠</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2024/06/28</td>
      <td>18000</td>
    </tr>
    <tr>
      <td>에스오에스랩</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2024/06/25</td>
      <td>11500</td>
    </tr>
    <tr>
      <td>한중엔시에스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>IBK증권</td>
      <td>2024/06/24</td>
      <td>30000</td>
    </tr>
    <tr>
      <td>씨어스테크놀로지</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2024/06/19</td>
      <td>17000</td>
    </tr>
    <tr>
      <td>라메디텍</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2024/06/17</td>
      <td>16000</td>
    </tr>
    <tr>
      <td>아이씨티케이</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2024/05/17</td>
      <td>20000</td>
    </tr>
    <tr>
      <td>민테크</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>KB증권</td>
      <td>2024/05/03</td>
      <td>10500</td>
    </tr>
    <tr>
      <td>디앤디파마텍</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2024/05/02</td>
      <td>33000</td>
    </tr>
    <tr>
      <td>아이엠비디엑스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권</td>
      <td>2024/04/03</td>
      <td>13000</td>
    </tr>
    <tr>
      <td>엔젤로보틱스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2024/03/26</td>
      <td>20000</td>
    </tr>
    <tr>
      <td>삼현</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2024/03/21</td>
      <td>30000</td>
    </tr>
    <tr>
      <td>케이엔알시스템</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권,DB금투</td>
      <td>2024/03/07</td>
      <td>13500</td>
    </tr>
    <tr>
      <td>코셈</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>키움증권</td>
      <td>2024/02/23</td>
      <td>16000</td>
    </tr>
    <tr>
      <td>이에이트</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한화투자</td>
      <td>2024/02/23</td>
      <td>20000</td>
    </tr>
    <tr>
      <td>케이웨더</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2024/02/22</td>
      <td>7000</td>
    </tr>
    <tr>
      <td>와이바이오로직스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>유안타증권</td>
      <td>2023/12/05</td>
      <td>9000</td>
    </tr>
    <tr>
      <td>에이텀</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>하나증권</td>
      <td>2023/12/01</td>
      <td>18000</td>
    </tr>
    <tr>
      <td>그린리소스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2023/11/24</td>
      <td>17000</td>
    </tr>
    <tr>
      <td>큐로셀</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권,삼성증권</td>
      <td>2023/11/09</td>
      <td>20000</td>
    </tr>
    <tr>
      <td>컨텍</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2023/11/09</td>
      <td>22500</td>
    </tr>
    <tr>
      <td>쏘닉스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>KB증권</td>
      <td>2023/11/07</td>
      <td>7500</td>
    </tr>
    <tr>
      <td>퀄리타스반도체</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2023/10/27</td>
      <td>17000</td>
    </tr>
    <tr>
      <td>아이엠티</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>유안타증권</td>
      <td>2023/10/10</td>
      <td>14000</td>
    </tr>
    <tr>
      <td>스마트레이더시스템</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2023/08/22</td>
      <td>8000</td>
    </tr>
    <tr>
      <td>큐리옥스바이오시스템즈</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>키움증권</td>
      <td>2023/08/10</td>
      <td>13000</td>
    </tr>
    <tr>
      <td>파두</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권,NH투자증권</td>
      <td>2023/08/07</td>
      <td>31000</td>
    </tr>
    <tr>
      <td>시지트로닉스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>유안타증권</td>
      <td>2023/08/03</td>
      <td>25000</td>
    </tr>
    <tr>
      <td>파로스아이바이오</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2023/07/27</td>
      <td>14000</td>
    </tr>
    <tr>
      <td>버넥트</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2023/07/26</td>
      <td>16000</td>
    </tr>
    <tr>
      <td>와이랩</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>한국증권</td>
      <td>2023/07/20</td>
      <td>9000</td>
    </tr>
    <tr>
      <td>센서뷰</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>삼성증권</td>
      <td>2023/07/19</td>
      <td>4500</td>
    </tr>
    <tr>
      <td>이노시뮬레이션</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>하나증권</td>
      <td>2023/07/06</td>
      <td>15000</td>
    </tr>
    <tr>
      <td>오픈놀</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>하나증권</td>
      <td>2023/06/30</td>
      <td>10000</td>
    </tr>
    <tr>
      <td>프로티아</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>키움증권</td>
      <td>2023/06/16</td>
      <td>4500</td>
    </tr>
    <tr>
      <td>큐라티스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권,신영증권</td>
      <td>2023/06/15</td>
      <td>4000</td>
    </tr>
    <tr>
      <td>모니터랩</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권</td>
      <td>2023/05/19</td>
      <td>9800</td>
    </tr>
    <tr>
      <td>씨유박스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>신한증권,SK증권</td>
      <td>2023/05/19</td>
      <td>15000</td>
    </tr>
    <tr>
      <td>에스바이오메딕스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권</td>
      <td>2023/05/04</td>
      <td>18000</td>
    </tr>
    <tr>
      <td>마이크로투나노</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2023/04/26</td>
      <td>15500</td>
    </tr>
    <tr>
      <td>지아이이노베이션</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권,하나증권,삼성증권</td>
      <td>2023/03/30</td>
      <td>13000</td>
    </tr>
    <tr>
      <td>자람테크놀로지</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>신영증권</td>
      <td>2023/03/07</td>
      <td>22000</td>
    </tr>
    <tr>
      <td>제이오</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2023/02/16</td>
      <td>13000</td>
    </tr>
    <tr>
      <td>샌즈랩</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>키움증권</td>
      <td>2023/02/15</td>
      <td>10500</td>
    </tr>
    <tr>
      <td>오브젠</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2023/01/30</td>
      <td>18000</td>
    </tr>
    <tr>
      <td>티이엠씨</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한화투자</td>
      <td>2023/01/19</td>
      <td>28000</td>
    </tr>
    <tr>
      <td>SAMG엔터</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2022/12/06</td>
      <td>17000</td>
    </tr>
    <tr>
      <td>인벤티지랩</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2022/11/22</td>
      <td>12000</td>
    </tr>
    <tr>
      <td>엔젯</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권</td>
      <td>2022/11/18</td>
      <td>10000</td>
    </tr>
    <tr>
      <td>뉴로메카</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2022/11/04</td>
      <td>16900</td>
    </tr>
    <tr>
      <td>플라즈맵</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권</td>
      <td>2022/10/21</td>
      <td>7000</td>
    </tr>
    <tr>
      <td>핀텔</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2022/10/20</td>
      <td>8900</td>
    </tr>
    <tr>
      <td>샤페론</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2022/10/19</td>
      <td>5000</td>
    </tr>
    <tr>
      <td>에스비비테크</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권</td>
      <td>2022/10/17</td>
      <td>12400</td>
    </tr>
    <tr>
      <td>선바이오</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>하나증권</td>
      <td>2022/10/05</td>
      <td>11000</td>
    </tr>
    <tr>
      <td>아이씨에이치</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>삼성증권</td>
      <td>2022/07/29</td>
      <td>34000</td>
    </tr>
    <tr>
      <td>에이프릴바이오</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2022/07/28</td>
      <td>16000</td>
    </tr>
    <tr>
      <td>루닛</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2022/07/21</td>
      <td>30000</td>
    </tr>
    <tr>
      <td>와이씨켐</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>하나증권</td>
      <td>2022/07/14</td>
      <td>18600</td>
    </tr>
    <tr>
      <td>코난테크놀로지</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2022/07/07</td>
      <td>25000</td>
    </tr>
    <tr>
      <td>넥스트칩</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2022/07/01</td>
      <td>13000</td>
    </tr>
    <tr>
      <td>레이저쎌</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>삼성증권</td>
      <td>2022/06/24</td>
      <td>16000</td>
    </tr>
    <tr>
      <td>보로노이</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권,미래에셋증권</td>
      <td>2022/06/24</td>
      <td>40000</td>
    </tr>
    <tr>
      <td>비큐AI</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>IBK증권</td>
      <td>2022/06/20</td>
      <td>10000</td>
    </tr>
    <tr>
      <td>모아데이타</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>하나증권</td>
      <td>2022/03/10</td>
      <td>20000</td>
    </tr>
    <tr>
      <td>노을</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권,삼성증권</td>
      <td>2022/03/03</td>
      <td>10000</td>
    </tr>
    <tr>
      <td>풍원정밀</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2022/02/28</td>
      <td>15200</td>
    </tr>
    <tr>
      <td>퓨런티어</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>신한증권,유안타증권</td>
      <td>2022/02/23</td>
      <td>15000</td>
    </tr>
    <tr>
      <td>바이오에프디엔씨</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>DB금투</td>
      <td>2022/02/21</td>
      <td>28000</td>
    </tr>
    <tr>
      <td>이지트로닉스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2022/02/04</td>
      <td>22000</td>
    </tr>
    <tr>
      <td>스코넥</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>신영증권</td>
      <td>2022/02/04</td>
      <td>13000</td>
    </tr>
    <tr>
      <td>애드바이오텍</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2022/01/24</td>
      <td>7000</td>
    </tr>
    <tr>
      <td>툴젠</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2021/12/10</td>
      <td>70000</td>
    </tr>
    <tr>
      <td>마음AI</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권,하나증권</td>
      <td>2021/11/23</td>
      <td>30000</td>
    </tr>
    <tr>
      <td>지오엘리먼트</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2021/11/11</td>
      <td>10000</td>
    </tr>
    <tr>
      <td>스카이월드와이드</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>하나증권</td>
      <td>2021/11/10</td>
      <td>11000</td>
    </tr>
    <tr>
      <td>지니너스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2021/11/08</td>
      <td>20000</td>
    </tr>
    <tr>
      <td>차백신연구소</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>삼성증권</td>
      <td>2021/10/22</td>
      <td>11000</td>
    </tr>
    <tr>
      <td>에이비온</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권,한화투자</td>
      <td>2021/09/08</td>
      <td>17000</td>
    </tr>
    <tr>
      <td>바이젠셀</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권,KB증권</td>
      <td>2021/08/25</td>
      <td>52700</td>
    </tr>
    <tr>
      <td>딥노이드</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>KB증권</td>
      <td>2021/08/17</td>
      <td>42000</td>
    </tr>
    <tr>
      <td>원티드랩</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>한국증권</td>
      <td>2021/08/11</td>
      <td>35000</td>
    </tr>
    <tr>
      <td>비트맥스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>하나증권</td>
      <td>2021/07/27</td>
      <td>15000</td>
    </tr>
    <tr>
      <td>큐라클</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>삼성증권</td>
      <td>2021/07/22</td>
      <td>25000</td>
    </tr>
    <tr>
      <td>오비고</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2021/07/13</td>
      <td>14300</td>
    </tr>
    <tr>
      <td>아모센스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>신한증권</td>
      <td>2021/06/25</td>
      <td>12400</td>
    </tr>
    <tr>
      <td>라온테크</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>KB증권</td>
      <td>2021/06/17</td>
      <td>18000</td>
    </tr>
    <tr>
      <td>진시스템</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>삼성증권</td>
      <td>2021/05/26</td>
      <td>20000</td>
    </tr>
    <tr>
      <td>삼영에스앤씨</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>미래에셋증권</td>
      <td>2021/05/21</td>
      <td>11000</td>
    </tr>
    <tr>
      <td>샘씨엔에스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2021/05/20</td>
      <td>6500</td>
    </tr>
    <tr>
      <td>해성에어로보틱스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2021/04/21</td>
      <td>13000</td>
    </tr>
    <tr>
      <td>제노코</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>DB금투</td>
      <td>2021/03/24</td>
      <td>36000</td>
    </tr>
    <tr>
      <td>자이언트스텝</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2021/03/24</td>
      <td>11000</td>
    </tr>
    <tr>
      <td>라이프시맨틱스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2021/03/23</td>
      <td>12500</td>
    </tr>
    <tr>
      <td>네오이뮨텍</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권,하나증권</td>
      <td>2021/03/16</td>
      <td>7500</td>
    </tr>
    <tr>
      <td>프레스티지바이오로직스</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>미래에셋증권,유안타증권</td>
      <td>2021/03/11</td>
      <td>12400</td>
    </tr>
    <tr>
      <td>나노씨엠에스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>키움증권</td>
      <td>2021/03/09</td>
      <td>20000</td>
    </tr>
    <tr>
      <td>뷰노</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권,삼성증권</td>
      <td>2021/02/26</td>
      <td>21000</td>
    </tr>
    <tr>
      <td>씨이랩</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>IBK증권</td>
      <td>2021/02/24</td>
      <td>35000</td>
    </tr>
    <tr>
      <td>피엔에이치테크</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2021/02/16</td>
      <td>18000</td>
    </tr>
    <tr>
      <td>레인보우로보틱스</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>대신증권,미래에셋증권</td>
      <td>2021/02/03</td>
      <td>10000</td>
    </tr>
    <tr>
      <td>아티스트유나이티드</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2021/02/03</td>
      <td>16000</td>
    </tr>
    <tr>
      <td>엔비티</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권</td>
      <td>2021/01/21</td>
      <td>19000</td>
    </tr>
    <tr>
      <td>지놈앤컴퍼니</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2020/12/23</td>
      <td>40000</td>
    </tr>
    <tr>
      <td>석경에이티</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2020/12/23</td>
      <td>10000</td>
    </tr>
    <tr>
      <td>프리시젼바이오</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2020/12/22</td>
      <td>12500</td>
    </tr>
    <tr>
      <td>알체라</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>신영증권</td>
      <td>2020/12/21</td>
      <td>10000</td>
    </tr>
    <tr>
      <td>엔젠바이오</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>삼성증권</td>
      <td>2020/12/10</td>
      <td>14000</td>
    </tr>
    <tr>
      <td>퀀타매트릭스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권</td>
      <td>2020/12/09</td>
      <td>25500</td>
    </tr>
    <tr>
      <td>클리노믹스</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>대신증권</td>
      <td>2020/12/04</td>
      <td>13900</td>
    </tr>
    <tr>
      <td>고바이오랩</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>대신증권,삼성증권</td>
      <td>2020/11/18</td>
      <td>15000</td>
    </tr>
    <tr>
      <td>센코</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2020/10/29</td>
      <td>13000</td>
    </tr>
    <tr>
      <td>바이브컴퍼니</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2020/10/28</td>
      <td>28000</td>
    </tr>
    <tr>
      <td>미코바이오메드</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>KB증권</td>
      <td>2020/10/22</td>
      <td>15000</td>
    </tr>
    <tr>
      <td>피플바이오</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>키움증권</td>
      <td>2020/10/19</td>
      <td>20000</td>
    </tr>
    <tr>
      <td>넥스틴</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>KB증권</td>
      <td>2020/10/08</td>
      <td>75400</td>
    </tr>
    <tr>
      <td>박셀바이오</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>하나증권</td>
      <td>2020/09/22</td>
      <td>30000</td>
    </tr>
    <tr>
      <td>압타머사이언스</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>키움증권</td>
      <td>2020/09/16</td>
      <td>25000</td>
    </tr>
    <tr>
      <td>이오플로우</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>하나증권</td>
      <td>2020/09/14</td>
      <td>19000</td>
    </tr>
    <tr>
      <td>셀레믹스</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>대신증권</td>
      <td>2020/08/21</td>
      <td>20000</td>
    </tr>
    <tr>
      <td>제놀루션</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>신영증권</td>
      <td>2020/07/24</td>
      <td>14000</td>
    </tr>
    <tr>
      <td>솔트룩스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2020/07/23</td>
      <td>25000</td>
    </tr>
    <tr>
      <td>소마젠</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>신한증권</td>
      <td>2020/07/13</td>
      <td>11000</td>
    </tr>
    <tr>
      <td>젠큐릭스</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권</td>
      <td>2020/06/25</td>
      <td>22700</td>
    </tr>
    <tr>
      <td>에스씨엠생명과학</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2020/06/17</td>
      <td>17000</td>
    </tr>
  </tbody>
</table>
</pre>

### 종목코드가 없어서.. 따로 불러오기

그래도 한 회사에서 운영하는 같은 시스템이니, 종목코드를 vlookup거는 것은 어렵지는 않았습니다. 정보데이터시스템의 다른 화면 12005(전종목기본정보)에서 추가로 자료를 받아서 종목코드를 맵핑하는 것으로 해결은 가능합니다. 단지 조금 번거로울 뿐이죠.


<br>회사명을 기준으로 종목코드를 맵핑하여 보겠습니다. 다행히 화면간***([20043] 공모가 대비 주가수익률, [12005]전종목기본정보)***{: style="color: #4682B4;"}에 회사명이 다른 경우는 없었습니다. (휴)

<br>맵핑한 결과는 아래와 같습니다.


<pre>
종목코드 전부 매칭됨
</pre>


<pre>
종목개수 : 151

<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>회사명</th>
      <th>stock_code</th>
      <th>상장트랙</th>
      <th>주관사</th>
      <th>상장일</th>
      <th>공모가</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>오름테라퓨틱</td>
      <td>475830</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2025/02/14</td>
      <td>20000</td>
    </tr>
    <tr>
      <td>아이에스티이</td>
      <td>212710</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>KB증권</td>
      <td>2025/02/12</td>
      <td>11400</td>
    </tr>
    <tr>
      <td>아이지넷</td>
      <td>462980</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>한국증권</td>
      <td>2025/02/04</td>
      <td>7000</td>
    </tr>
    <tr>
      <td>와이즈넛</td>
      <td>096250</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>삼성증권</td>
      <td>2025/01/24</td>
      <td>17000</td>
    </tr>
    <tr>
      <td>파인메딕스</td>
      <td>387570</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2024/12/26</td>
      <td>10000</td>
    </tr>
    <tr>
      <td>쓰리에이로직스</td>
      <td>177900</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>신한증권,미래에셋증권</td>
      <td>2024/12/24</td>
      <td>11000</td>
    </tr>
    <tr>
      <td>온코닉테라퓨틱스</td>
      <td>476060</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2024/12/19</td>
      <td>13000</td>
    </tr>
    <tr>
      <td>온코크로스</td>
      <td>382150</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권</td>
      <td>2024/12/18</td>
      <td>7300</td>
    </tr>
    <tr>
      <td>쓰리빌리언</td>
      <td>394800</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2024/11/14</td>
      <td>4500</td>
    </tr>
    <tr>
      <td>에어레인</td>
      <td>163280</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>신영증권</td>
      <td>2024/11/08</td>
      <td>23000</td>
    </tr>
    <tr>
      <td>토모큐브</td>
      <td>475960</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2024/11/07</td>
      <td>16000</td>
    </tr>
    <tr>
      <td>에이치이엠파마</td>
      <td>376270</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>신한증권</td>
      <td>2024/11/05</td>
      <td>23000</td>
    </tr>
    <tr>
      <td>클로봇</td>
      <td>466100</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권</td>
      <td>2024/10/28</td>
      <td>13000</td>
    </tr>
    <tr>
      <td>웨이비스</td>
      <td>289930</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2024/10/25</td>
      <td>15000</td>
    </tr>
    <tr>
      <td>씨메스</td>
      <td>475400</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>유진증권,삼성증권</td>
      <td>2024/10/24</td>
      <td>30000</td>
    </tr>
    <tr>
      <td>루미르</td>
      <td>474170</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2024/10/21</td>
      <td>12000</td>
    </tr>
    <tr>
      <td>셀비온</td>
      <td>308430</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2024/10/16</td>
      <td>15000</td>
    </tr>
    <tr>
      <td>아이언디바이스</td>
      <td>464500</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2024/09/23</td>
      <td>7000</td>
    </tr>
    <tr>
      <td>이엔셀</td>
      <td>456070</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2024/08/23</td>
      <td>15300</td>
    </tr>
    <tr>
      <td>케이쓰리아이</td>
      <td>431190</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>하나증권</td>
      <td>2024/08/20</td>
      <td>15500</td>
    </tr>
    <tr>
      <td>넥스트바이오메디컬</td>
      <td>389650</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2024/08/20</td>
      <td>29000</td>
    </tr>
    <tr>
      <td>뱅크웨어글로벌</td>
      <td>199480</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권</td>
      <td>2024/08/12</td>
      <td>16000</td>
    </tr>
    <tr>
      <td>아이빔테크놀로지</td>
      <td>460470</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>삼성증권</td>
      <td>2024/08/06</td>
      <td>10000</td>
    </tr>
    <tr>
      <td>피앤에스미캐닉스</td>
      <td>460940</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>키움증권</td>
      <td>2024/07/31</td>
      <td>22000</td>
    </tr>
    <tr>
      <td>엑셀세라퓨틱스</td>
      <td>373110</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2024/07/15</td>
      <td>10000</td>
    </tr>
    <tr>
      <td>하스</td>
      <td>450330</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>삼성증권</td>
      <td>2024/07/03</td>
      <td>16000</td>
    </tr>
    <tr>
      <td>이노스페이스</td>
      <td>462350</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권</td>
      <td>2024/07/02</td>
      <td>43300</td>
    </tr>
    <tr>
      <td>에이치브이엠</td>
      <td>295310</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2024/06/28</td>
      <td>18000</td>
    </tr>
    <tr>
      <td>에스오에스랩</td>
      <td>464080</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2024/06/25</td>
      <td>11500</td>
    </tr>
    <tr>
      <td>한중엔시에스</td>
      <td>107640</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>IBK증권</td>
      <td>2024/06/24</td>
      <td>30000</td>
    </tr>
    <tr>
      <td>씨어스테크놀로지</td>
      <td>458870</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2024/06/19</td>
      <td>17000</td>
    </tr>
    <tr>
      <td>라메디텍</td>
      <td>462510</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2024/06/17</td>
      <td>16000</td>
    </tr>
    <tr>
      <td>아이씨티케이</td>
      <td>456010</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2024/05/17</td>
      <td>20000</td>
    </tr>
    <tr>
      <td>민테크</td>
      <td>452200</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>KB증권</td>
      <td>2024/05/03</td>
      <td>10500</td>
    </tr>
    <tr>
      <td>디앤디파마텍</td>
      <td>347850</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2024/05/02</td>
      <td>33000</td>
    </tr>
    <tr>
      <td>아이엠비디엑스</td>
      <td>461030</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권</td>
      <td>2024/04/03</td>
      <td>13000</td>
    </tr>
    <tr>
      <td>엔젤로보틱스</td>
      <td>455900</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2024/03/26</td>
      <td>20000</td>
    </tr>
    <tr>
      <td>삼현</td>
      <td>437730</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2024/03/21</td>
      <td>30000</td>
    </tr>
    <tr>
      <td>케이엔알시스템</td>
      <td>199430</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권,DB금투</td>
      <td>2024/03/07</td>
      <td>13500</td>
    </tr>
    <tr>
      <td>코셈</td>
      <td>360350</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>키움증권</td>
      <td>2024/02/23</td>
      <td>16000</td>
    </tr>
    <tr>
      <td>이에이트</td>
      <td>418620</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한화투자</td>
      <td>2024/02/23</td>
      <td>20000</td>
    </tr>
    <tr>
      <td>케이웨더</td>
      <td>068100</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2024/02/22</td>
      <td>7000</td>
    </tr>
    <tr>
      <td>와이바이오로직스</td>
      <td>338840</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>유안타증권</td>
      <td>2023/12/05</td>
      <td>9000</td>
    </tr>
    <tr>
      <td>에이텀</td>
      <td>355690</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>하나증권</td>
      <td>2023/12/01</td>
      <td>18000</td>
    </tr>
    <tr>
      <td>그린리소스</td>
      <td>402490</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2023/11/24</td>
      <td>17000</td>
    </tr>
    <tr>
      <td>큐로셀</td>
      <td>372320</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권,삼성증권</td>
      <td>2023/11/09</td>
      <td>20000</td>
    </tr>
    <tr>
      <td>컨텍</td>
      <td>451760</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2023/11/09</td>
      <td>22500</td>
    </tr>
    <tr>
      <td>쏘닉스</td>
      <td>088280</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>KB증권</td>
      <td>2023/11/07</td>
      <td>7500</td>
    </tr>
    <tr>
      <td>퀄리타스반도체</td>
      <td>432720</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2023/10/27</td>
      <td>17000</td>
    </tr>
    <tr>
      <td>아이엠티</td>
      <td>451220</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>유안타증권</td>
      <td>2023/10/10</td>
      <td>14000</td>
    </tr>
    <tr>
      <td>스마트레이더시스템</td>
      <td>424960</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2023/08/22</td>
      <td>8000</td>
    </tr>
    <tr>
      <td>큐리옥스바이오시스템즈</td>
      <td>445680</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>키움증권</td>
      <td>2023/08/10</td>
      <td>13000</td>
    </tr>
    <tr>
      <td>파두</td>
      <td>440110</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권,NH투자증권</td>
      <td>2023/08/07</td>
      <td>31000</td>
    </tr>
    <tr>
      <td>시지트로닉스</td>
      <td>429270</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>유안타증권</td>
      <td>2023/08/03</td>
      <td>25000</td>
    </tr>
    <tr>
      <td>파로스아이바이오</td>
      <td>388870</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2023/07/27</td>
      <td>14000</td>
    </tr>
    <tr>
      <td>버넥트</td>
      <td>438700</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2023/07/26</td>
      <td>16000</td>
    </tr>
    <tr>
      <td>와이랩</td>
      <td>432430</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>한국증권</td>
      <td>2023/07/20</td>
      <td>9000</td>
    </tr>
    <tr>
      <td>센서뷰</td>
      <td>321370</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>삼성증권</td>
      <td>2023/07/19</td>
      <td>4500</td>
    </tr>
    <tr>
      <td>이노시뮬레이션</td>
      <td>274400</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>하나증권</td>
      <td>2023/07/06</td>
      <td>15000</td>
    </tr>
    <tr>
      <td>오픈놀</td>
      <td>440320</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>하나증권</td>
      <td>2023/06/30</td>
      <td>10000</td>
    </tr>
    <tr>
      <td>프로티아</td>
      <td>303360</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>키움증권</td>
      <td>2023/06/16</td>
      <td>4500</td>
    </tr>
    <tr>
      <td>큐라티스</td>
      <td>348080</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권,신영증권</td>
      <td>2023/06/15</td>
      <td>4000</td>
    </tr>
    <tr>
      <td>모니터랩</td>
      <td>434480</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권</td>
      <td>2023/05/19</td>
      <td>9800</td>
    </tr>
    <tr>
      <td>씨유박스</td>
      <td>340810</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>신한증권,SK증권</td>
      <td>2023/05/19</td>
      <td>15000</td>
    </tr>
    <tr>
      <td>에스바이오메딕스</td>
      <td>304360</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권</td>
      <td>2023/05/04</td>
      <td>18000</td>
    </tr>
    <tr>
      <td>마이크로투나노</td>
      <td>424980</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2023/04/26</td>
      <td>15500</td>
    </tr>
    <tr>
      <td>지아이이노베이션</td>
      <td>358570</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권,하나증권,삼성증권</td>
      <td>2023/03/30</td>
      <td>13000</td>
    </tr>
    <tr>
      <td>자람테크놀로지</td>
      <td>389020</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>신영증권</td>
      <td>2023/03/07</td>
      <td>22000</td>
    </tr>
    <tr>
      <td>제이오</td>
      <td>418550</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2023/02/16</td>
      <td>13000</td>
    </tr>
    <tr>
      <td>샌즈랩</td>
      <td>411080</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>키움증권</td>
      <td>2023/02/15</td>
      <td>10500</td>
    </tr>
    <tr>
      <td>오브젠</td>
      <td>417860</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2023/01/30</td>
      <td>18000</td>
    </tr>
    <tr>
      <td>티이엠씨</td>
      <td>425040</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한화투자</td>
      <td>2023/01/19</td>
      <td>28000</td>
    </tr>
    <tr>
      <td>SAMG엔터</td>
      <td>419530</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2022/12/06</td>
      <td>17000</td>
    </tr>
    <tr>
      <td>인벤티지랩</td>
      <td>389470</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2022/11/22</td>
      <td>12000</td>
    </tr>
    <tr>
      <td>엔젯</td>
      <td>419080</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권</td>
      <td>2022/11/18</td>
      <td>10000</td>
    </tr>
    <tr>
      <td>뉴로메카</td>
      <td>348340</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2022/11/04</td>
      <td>16900</td>
    </tr>
    <tr>
      <td>플라즈맵</td>
      <td>405000</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권</td>
      <td>2022/10/21</td>
      <td>7000</td>
    </tr>
    <tr>
      <td>핀텔</td>
      <td>291810</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2022/10/20</td>
      <td>8900</td>
    </tr>
    <tr>
      <td>샤페론</td>
      <td>378800</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2022/10/19</td>
      <td>5000</td>
    </tr>
    <tr>
      <td>에스비비테크</td>
      <td>389500</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권</td>
      <td>2022/10/17</td>
      <td>12400</td>
    </tr>
    <tr>
      <td>선바이오</td>
      <td>067370</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>하나증권</td>
      <td>2022/10/05</td>
      <td>11000</td>
    </tr>
    <tr>
      <td>아이씨에이치</td>
      <td>368600</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>삼성증권</td>
      <td>2022/07/29</td>
      <td>34000</td>
    </tr>
    <tr>
      <td>에이프릴바이오</td>
      <td>397030</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2022/07/28</td>
      <td>16000</td>
    </tr>
    <tr>
      <td>루닛</td>
      <td>328130</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2022/07/21</td>
      <td>30000</td>
    </tr>
    <tr>
      <td>와이씨켐</td>
      <td>112290</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>하나증권</td>
      <td>2022/07/14</td>
      <td>18600</td>
    </tr>
    <tr>
      <td>코난테크놀로지</td>
      <td>402030</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2022/07/07</td>
      <td>25000</td>
    </tr>
    <tr>
      <td>넥스트칩</td>
      <td>396270</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2022/07/01</td>
      <td>13000</td>
    </tr>
    <tr>
      <td>레이저쎌</td>
      <td>412350</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>삼성증권</td>
      <td>2022/06/24</td>
      <td>16000</td>
    </tr>
    <tr>
      <td>보로노이</td>
      <td>310210</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권,미래에셋증권</td>
      <td>2022/06/24</td>
      <td>40000</td>
    </tr>
    <tr>
      <td>비큐AI</td>
      <td>148780</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>IBK증권</td>
      <td>2022/06/20</td>
      <td>10000</td>
    </tr>
    <tr>
      <td>모아데이타</td>
      <td>288980</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>하나증권</td>
      <td>2022/03/10</td>
      <td>20000</td>
    </tr>
    <tr>
      <td>노을</td>
      <td>376930</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권,삼성증권</td>
      <td>2022/03/03</td>
      <td>10000</td>
    </tr>
    <tr>
      <td>풍원정밀</td>
      <td>371950</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2022/02/28</td>
      <td>15200</td>
    </tr>
    <tr>
      <td>퓨런티어</td>
      <td>370090</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>신한증권,유안타증권</td>
      <td>2022/02/23</td>
      <td>15000</td>
    </tr>
    <tr>
      <td>바이오에프디엔씨</td>
      <td>251120</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>DB금투</td>
      <td>2022/02/21</td>
      <td>28000</td>
    </tr>
    <tr>
      <td>이지트로닉스</td>
      <td>377330</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2022/02/04</td>
      <td>22000</td>
    </tr>
    <tr>
      <td>스코넥</td>
      <td>276040</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>신영증권</td>
      <td>2022/02/04</td>
      <td>13000</td>
    </tr>
    <tr>
      <td>애드바이오텍</td>
      <td>179530</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2022/01/24</td>
      <td>7000</td>
    </tr>
    <tr>
      <td>툴젠</td>
      <td>199800</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2021/12/10</td>
      <td>70000</td>
    </tr>
    <tr>
      <td>마음AI</td>
      <td>377480</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권,하나증권</td>
      <td>2021/11/23</td>
      <td>30000</td>
    </tr>
    <tr>
      <td>지오엘리먼트</td>
      <td>311320</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2021/11/11</td>
      <td>10000</td>
    </tr>
    <tr>
      <td>스카이월드와이드</td>
      <td>357880</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>하나증권</td>
      <td>2021/11/10</td>
      <td>11000</td>
    </tr>
    <tr>
      <td>지니너스</td>
      <td>389030</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2021/11/08</td>
      <td>20000</td>
    </tr>
    <tr>
      <td>차백신연구소</td>
      <td>261780</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>삼성증권</td>
      <td>2021/10/22</td>
      <td>11000</td>
    </tr>
    <tr>
      <td>에이비온</td>
      <td>203400</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권,한화투자</td>
      <td>2021/09/08</td>
      <td>17000</td>
    </tr>
    <tr>
      <td>바이젠셀</td>
      <td>308080</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권,KB증권</td>
      <td>2021/08/25</td>
      <td>52700</td>
    </tr>
    <tr>
      <td>딥노이드</td>
      <td>315640</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>KB증권</td>
      <td>2021/08/17</td>
      <td>42000</td>
    </tr>
    <tr>
      <td>원티드랩</td>
      <td>376980</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>한국증권</td>
      <td>2021/08/11</td>
      <td>35000</td>
    </tr>
    <tr>
      <td>비트맥스</td>
      <td>377030</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>하나증권</td>
      <td>2021/07/27</td>
      <td>15000</td>
    </tr>
    <tr>
      <td>큐라클</td>
      <td>365270</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>삼성증권</td>
      <td>2021/07/22</td>
      <td>25000</td>
    </tr>
    <tr>
      <td>오비고</td>
      <td>352910</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>NH투자증권</td>
      <td>2021/07/13</td>
      <td>14300</td>
    </tr>
    <tr>
      <td>아모센스</td>
      <td>357580</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>신한증권</td>
      <td>2021/06/25</td>
      <td>12400</td>
    </tr>
    <tr>
      <td>라온테크</td>
      <td>232680</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>KB증권</td>
      <td>2021/06/17</td>
      <td>18000</td>
    </tr>
    <tr>
      <td>진시스템</td>
      <td>363250</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>삼성증권</td>
      <td>2021/05/26</td>
      <td>20000</td>
    </tr>
    <tr>
      <td>삼영에스앤씨</td>
      <td>361670</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>미래에셋증권</td>
      <td>2021/05/21</td>
      <td>11000</td>
    </tr>
    <tr>
      <td>샘씨엔에스</td>
      <td>252990</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>대신증권</td>
      <td>2021/05/20</td>
      <td>6500</td>
    </tr>
    <tr>
      <td>해성에어로보틱스</td>
      <td>059270</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2021/04/21</td>
      <td>13000</td>
    </tr>
    <tr>
      <td>제노코</td>
      <td>361390</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>DB금투</td>
      <td>2021/03/24</td>
      <td>36000</td>
    </tr>
    <tr>
      <td>자이언트스텝</td>
      <td>289220</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2021/03/24</td>
      <td>11000</td>
    </tr>
    <tr>
      <td>라이프시맨틱스</td>
      <td>347700</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2021/03/23</td>
      <td>12500</td>
    </tr>
    <tr>
      <td>네오이뮨텍</td>
      <td>950220</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권,하나증권</td>
      <td>2021/03/16</td>
      <td>7500</td>
    </tr>
    <tr>
      <td>프레스티지바이오로직스</td>
      <td>334970</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>미래에셋증권,유안타증권</td>
      <td>2021/03/11</td>
      <td>12400</td>
    </tr>
    <tr>
      <td>나노씨엠에스</td>
      <td>247660</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>키움증권</td>
      <td>2021/03/09</td>
      <td>20000</td>
    </tr>
    <tr>
      <td>뷰노</td>
      <td>338220</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권,삼성증권</td>
      <td>2021/02/26</td>
      <td>21000</td>
    </tr>
    <tr>
      <td>씨이랩</td>
      <td>189330</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>IBK증권</td>
      <td>2021/02/24</td>
      <td>35000</td>
    </tr>
    <tr>
      <td>피엔에이치테크</td>
      <td>239890</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2021/02/16</td>
      <td>18000</td>
    </tr>
    <tr>
      <td>레인보우로보틱스</td>
      <td>277810</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>대신증권,미래에셋증권</td>
      <td>2021/02/03</td>
      <td>10000</td>
    </tr>
    <tr>
      <td>아티스트유나이티드</td>
      <td>321820</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2021/02/03</td>
      <td>16000</td>
    </tr>
    <tr>
      <td>엔비티</td>
      <td>236810</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권</td>
      <td>2021/01/21</td>
      <td>19000</td>
    </tr>
    <tr>
      <td>지놈앤컴퍼니</td>
      <td>314130</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2020/12/23</td>
      <td>40000</td>
    </tr>
    <tr>
      <td>석경에이티</td>
      <td>357550</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2020/12/23</td>
      <td>10000</td>
    </tr>
    <tr>
      <td>프리시젼바이오</td>
      <td>335810</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2020/12/22</td>
      <td>12500</td>
    </tr>
    <tr>
      <td>알체라</td>
      <td>347860</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>신영증권</td>
      <td>2020/12/21</td>
      <td>10000</td>
    </tr>
    <tr>
      <td>엔젠바이오</td>
      <td>354200</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>삼성증권</td>
      <td>2020/12/10</td>
      <td>14000</td>
    </tr>
    <tr>
      <td>퀀타매트릭스</td>
      <td>317690</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권</td>
      <td>2020/12/09</td>
      <td>25500</td>
    </tr>
    <tr>
      <td>클리노믹스</td>
      <td>352770</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>대신증권</td>
      <td>2020/12/04</td>
      <td>13900</td>
    </tr>
    <tr>
      <td>고바이오랩</td>
      <td>348150</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>대신증권,삼성증권</td>
      <td>2020/11/18</td>
      <td>15000</td>
    </tr>
    <tr>
      <td>센코</td>
      <td>347000</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2020/10/29</td>
      <td>13000</td>
    </tr>
    <tr>
      <td>바이브컴퍼니</td>
      <td>301300</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2020/10/28</td>
      <td>28000</td>
    </tr>
    <tr>
      <td>미코바이오메드</td>
      <td>214610</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>KB증권</td>
      <td>2020/10/22</td>
      <td>15000</td>
    </tr>
    <tr>
      <td>피플바이오</td>
      <td>304840</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>키움증권</td>
      <td>2020/10/19</td>
      <td>20000</td>
    </tr>
    <tr>
      <td>넥스틴</td>
      <td>348210</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>KB증권</td>
      <td>2020/10/08</td>
      <td>75400</td>
    </tr>
    <tr>
      <td>박셀바이오</td>
      <td>323990</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>하나증권</td>
      <td>2020/09/22</td>
      <td>30000</td>
    </tr>
    <tr>
      <td>압타머사이언스</td>
      <td>291650</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>키움증권</td>
      <td>2020/09/16</td>
      <td>25000</td>
    </tr>
    <tr>
      <td>이오플로우</td>
      <td>294090</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>하나증권</td>
      <td>2020/09/14</td>
      <td>19000</td>
    </tr>
    <tr>
      <td>셀레믹스</td>
      <td>331920</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>대신증권</td>
      <td>2020/08/21</td>
      <td>20000</td>
    </tr>
    <tr>
      <td>제놀루션</td>
      <td>225220</td>
      <td>기술성장기업(사업모델기업)</td>
      <td>신영증권</td>
      <td>2020/07/24</td>
      <td>14000</td>
    </tr>
    <tr>
      <td>솔트룩스</td>
      <td>304100</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2020/07/23</td>
      <td>25000</td>
    </tr>
    <tr>
      <td>소마젠</td>
      <td>950200</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>신한증권</td>
      <td>2020/07/13</td>
      <td>11000</td>
    </tr>
    <tr>
      <td>젠큐릭스</td>
      <td>229000</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>미래에셋증권</td>
      <td>2020/06/25</td>
      <td>22700</td>
    </tr>
    <tr>
      <td>에스씨엠생명과학</td>
      <td>298060</td>
      <td>기술성장기업(혁신기술기업)</td>
      <td>한국증권</td>
      <td>2020/06/17</td>
      <td>17000</td>
    </tr>
  </tbody>
</table>
</pre>

## KIND에서 기술성장기업 불러오기

한국거래소의 정보데이터시스템에는 없었지만, 한국거래소가 운영하는 **상장공시 배포시스템인 KIND**{: style="color: #4682B4;"}에는 혹시 있지 않을까? 라는 생각이 들어서 방문해보았습니다.


### KIND 속에 꽁꽁 숨어있는 기술성장기업 리스트

![kind1]({{site.url}}/assets/images/2025-03-01-listing/kind1.png)<br><br>

여기에도 IPO 관련 메뉴가 있습니다. 여기에 가보면 있겠군요!<br><br>

![kind2]({{site.url}}/assets/images/2025-03-01-listing/kind2.png)<br><br>

상장통계로 들어왔는데 유형별상장 통계만 있고 특례상장내용은 안보입니다. 실망하려던 찰나, **'기타상장통계' 메뉴**를 발견했습니다. 메인화면에서는 보이지 않고, ***'전체메뉴보기' - 'IPO현황' - '신규상장통계' - '상장통계' - '유형별상장통계'*** 경로로 접속하고 나면 보이는 메뉴입니다. <br><br>

![kind3]({{site.url}}/assets/images/2025-03-01-listing/kind3.png)<br><br>

연도별로 특례상장 기업 숫자가 나온 표가 있고, 숫자를 클릭하면 목록을 보여줍니다. **하지만 이번에도 종목코드는 없습니다.**{: style="color: #4682B4;"} <br><br>

![kind4]({{site.url}}/assets/images/2025-03-01-listing/kind4.png)<br><br>

그래도 정보데이터시스템은 5년치만 보여주는 반면, KIND에서는 좀 더 예전 기업까지 볼 수 있습니다. 현재 글을 작성중인 2025년 기준으로, 콤보박스에서 2018년까지 선택이 가능합니다. 그리고 2018년 화면으로 넘어가면 2014년까지 조회가 가능합니다. **어랏...? 기술특례 상장제도는 2005년에 처음 시작되었는데?** <br>

> **한국거래소 정보데이터시스템에서도, KIND에서도 기술성장기업 전체 리스트를 얻을 수는 없습니다.**{: style="color: #4682B4;"}

가용한 2014년 데이터부터라도 수집한 결과는 다음과 같습니다.
<br>

<pre>
2005년 데이터를 찾을 수 없습니다.
2006년 데이터를 찾을 수 없습니다.
2007년 데이터를 찾을 수 없습니다.
2008년 데이터를 찾을 수 없습니다.
2009년 데이터를 찾을 수 없습니다.
2010년 데이터를 찾을 수 없습니다.
2011년 데이터를 찾을 수 없습니다.
2012년 데이터를 찾을 수 없습니다.
2013년 데이터를 찾을 수 없습니다.
</pre>

<pre>
종목개수 : 221

<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>회사명</th>
      <th>업종</th>
      <th>주요제품</th>
      <th>상장일(스팩합병일)</th>
      <th>결산기</th>
      <th>대표자명</th>
      <th>홈페이지</th>
      <th>지역</th>
      <th>연도</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>아스트</td>
      <td>항공기,우주선 및 부품 제조업</td>
      <td>항공기용 부품 제조 및 동체 조립</td>
      <td>2014-12-24</td>
      <td>12월</td>
      <td>김두일</td>
      <td>홈페이지 보기</td>
      <td>경상남도</td>
      <td>2014</td>
    </tr>
    <tr>
      <td>알테오젠</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>바이오시밀러 및 바이오베터</td>
      <td>2014-12-12</td>
      <td>12월</td>
      <td>박순재</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2014</td>
    </tr>
    <tr>
      <td>덱스터</td>
      <td>영화, 비디오물, 방송프로그램 제작 및 배급업</td>
      <td>시각효과(Visual Effect, VFX)</td>
      <td>2015-12-22</td>
      <td>12월</td>
      <td>김욱, 강종익</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2015</td>
    </tr>
    <tr>
      <td>HLB제약</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>씨트리시메티딘정, 로자틴정</td>
      <td>2015-12-21</td>
      <td>12월31일</td>
      <td>박재형</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2015</td>
    </tr>
    <tr>
      <td>강스템바이오텍</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>줄기세포치료제</td>
      <td>2015-12-21</td>
      <td>12월</td>
      <td>나종천</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2015</td>
    </tr>
    <tr>
      <td>파크시스템스</td>
      <td>측정, 시험, 항해, 제어 및 기타 정밀기기 제조업; 광학기기 제외</td>
      <td>연구용 및 산업용 원자현미경</td>
      <td>2015-12-17</td>
      <td>12월</td>
      <td>박상일</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2015</td>
    </tr>
    <tr>
      <td>멕아이씨에스</td>
      <td>의료용 기기 제조업</td>
      <td>인공호흡기</td>
      <td>2015-12-14</td>
      <td>12월31일</td>
      <td>김종철</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2015</td>
    </tr>
    <tr>
      <td>DXVX</td>
      <td>의료용 기기 제조업</td>
      <td>BAC DNA CHIP</td>
      <td>2015-11-20</td>
      <td>12월</td>
      <td>이용구, 권규찬 (각자 대표이사)</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2015</td>
    </tr>
    <tr>
      <td>아이진</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>당뇨성망막병증 치료제, 욕창치료제, 자궁경부암 예방 백신 등</td>
      <td>2015-11-16</td>
      <td>12월</td>
      <td>최석근</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2015</td>
    </tr>
    <tr>
      <td>시지메드텍</td>
      <td>의료용 기기 제조업</td>
      <td>정형외과용 신체보정용 의료기기</td>
      <td>2015-11-12</td>
      <td>12월</td>
      <td>정주미</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2015</td>
    </tr>
    <tr>
      <td>엔케이맥스</td>
      <td>기초 의약물질 제조업</td>
      <td>연구용 시약, NK Vue KIT</td>
      <td>2015-10-23</td>
      <td>12월31일</td>
      <td>박상우</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2015</td>
    </tr>
    <tr>
      <td>펩트론</td>
      <td>기초 의약물질 제조업</td>
      <td>약효지속성 의약품 및 펩타이드 소재</td>
      <td>2015-07-22</td>
      <td>12월</td>
      <td>최호일</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2015</td>
    </tr>
    <tr>
      <td>코아스템켐온</td>
      <td>의약품 제조업</td>
      <td>줄기세포 치료제</td>
      <td>2015-06-26</td>
      <td>12월</td>
      <td>양길안</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2015</td>
    </tr>
    <tr>
      <td>HLB제넥스</td>
      <td>기초 의약물질 제조업</td>
      <td>산업용 효소</td>
      <td>2015-05-29</td>
      <td>12월31일</td>
      <td>김의중, 김도연 (각자 대표이사)</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2015</td>
    </tr>
    <tr>
      <td>애니젠</td>
      <td>기초 의약물질 제조업</td>
      <td>펩타이드 바이오소재 및 아미노산 펩타이드 신약</td>
      <td>2016-12-07</td>
      <td>12월</td>
      <td>김재일</td>
      <td>홈페이지 보기</td>
      <td>광주광역시</td>
      <td>2016</td>
    </tr>
    <tr>
      <td>신라젠</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>펙사벡(바이러스 항암면역치료제)</td>
      <td>2016-12-06</td>
      <td>12월</td>
      <td>김재경</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2016</td>
    </tr>
    <tr>
      <td>퓨쳐켐</td>
      <td>의약품 제조업</td>
      <td>PET 방사성의약품, 자동합성장치, 합성시약 및 전구체</td>
      <td>2016-12-01</td>
      <td>12월</td>
      <td>지대윤</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2016</td>
    </tr>
    <tr>
      <td>얼라인드</td>
      <td>사진장비 및 광학기기 제조업</td>
      <td>자동세포카운팅시스템, 생체조직투명화시스템, 디지털세포이미징시스템</td>
      <td>2016-11-03</td>
      <td>12월</td>
      <td>정연철</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2016</td>
    </tr>
    <tr>
      <td>지엘팜텍</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>지소렌정</td>
      <td>2016-10-05</td>
      <td>12월31일</td>
      <td>김용일, 진성필</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2016</td>
    </tr>
    <tr>
      <td>아이윈플러스</td>
      <td>전자부품 제조업</td>
      <td>이미지센서 패키징</td>
      <td>2016-07-20</td>
      <td>12월</td>
      <td>이준식</td>
      <td>홈페이지 보기</td>
      <td>충청북도</td>
      <td>2016</td>
    </tr>
    <tr>
      <td>모아라이프플러스</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>자궁경부상피이형증 치료제, 자궁경부전암 치료백신</td>
      <td>2016-07-07</td>
      <td>12월</td>
      <td>한상진</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2016</td>
    </tr>
    <tr>
      <td>팬젠</td>
      <td>의약품 제조업</td>
      <td>바이오시밀러 제품, 바이오의약품 개발 기술이전 서비스 등</td>
      <td>2016-03-11</td>
      <td>12월31일</td>
      <td>윤재승</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2016</td>
    </tr>
    <tr>
      <td>큐리언트</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>저분자 혁신신약</td>
      <td>2016-02-29</td>
      <td>12월</td>
      <td>남기연</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2016</td>
    </tr>
    <tr>
      <td>안트로젠</td>
      <td>기초 의약물질 제조업</td>
      <td>줄기세포치료제</td>
      <td>2016-02-15</td>
      <td>12월</td>
      <td>이성구, 김미형(각자대표)</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2016</td>
    </tr>
    <tr>
      <td>휴마시스</td>
      <td>의료용 기기 제조업</td>
      <td>임신진단키트</td>
      <td>2017-10-17</td>
      <td>12월31일</td>
      <td>김성곤</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2017</td>
    </tr>
    <tr>
      <td>앱클론</td>
      <td>의료용품 및 기타 의약 관련제품 제조업</td>
      <td>항체의약품</td>
      <td>2017-09-18</td>
      <td>12월31일</td>
      <td>이종서</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2017</td>
    </tr>
    <tr>
      <td>어스앤에어로스페이스</td>
      <td>항공기,우주선 및 부품 제조업</td>
      <td>도어시스템</td>
      <td>2017-09-15</td>
      <td>12월31일</td>
      <td>조동우</td>
      <td>홈페이지 보기</td>
      <td>경상남도</td>
      <td>2017</td>
    </tr>
    <tr>
      <td>모비스</td>
      <td>컴퓨터 프로그래밍, 시스템 통합 및 관리업</td>
      <td>핵융합 제어시스템설계, 가속기 제어시스템설계</td>
      <td>2017-03-21</td>
      <td>12월31일</td>
      <td>김지헌</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2017</td>
    </tr>
    <tr>
      <td>아스타</td>
      <td>의료용품 및 기타 의약 관련제품 제조업</td>
      <td>MALDI-TOF 질량분석기 기반 진단시스템</td>
      <td>2017-03-20</td>
      <td>12월31일</td>
      <td>조응준, 김양선 (각자대표이사)</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2017</td>
    </tr>
    <tr>
      <td>피씨엘</td>
      <td>의료용품 및 기타 의약 관련제품 제조업</td>
      <td>다중 체외진단 제품, 플랫폼서비스</td>
      <td>2017-02-23</td>
      <td>12월</td>
      <td>김소연</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2017</td>
    </tr>
    <tr>
      <td>유바이오로직스</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>경구용 콜레라 백신, 바이오의약품 수탁 연구 및 제조</td>
      <td>2017-01-24</td>
      <td>12월</td>
      <td>백영옥</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2017</td>
    </tr>
    <tr>
      <td>비피도</td>
      <td>도시락 및 식사용 조리식품 제조업</td>
      <td>프로바이오틱스 관련 완제품 및 균주 원말 등</td>
      <td>2018-12-26</td>
      <td>12월</td>
      <td>이원범, 박명수(각자대표)</td>
      <td>홈페이지 보기</td>
      <td>강원특별자치도</td>
      <td>2018</td>
    </tr>
    <tr>
      <td>유틸렉스</td>
      <td>기초 의약물질 제조업</td>
      <td>면역항암 세포치료제, 면역항암 항체치료제</td>
      <td>2018-12-24</td>
      <td>12월31일</td>
      <td>권병세, 유연호 (공동대표이사)</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2018</td>
    </tr>
    <tr>
      <td>에이비엘바이오</td>
      <td>기초 의약물질 제조업</td>
      <td>항체의약품 연구개발</td>
      <td>2018-12-19</td>
      <td>12월</td>
      <td>이상훈</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2018</td>
    </tr>
    <tr>
      <td>전진바이오팜</td>
      <td>기타 화학제품 제조업</td>
      <td>방충방향제, 유해동물피해감소제, 기생충피해감소제</td>
      <td>2018-12-14</td>
      <td>12월31일</td>
      <td>이태훈</td>
      <td>홈페이지 보기</td>
      <td>대구광역시</td>
      <td>2018</td>
    </tr>
    <tr>
      <td>나무기술</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>가상화 및 클라우드 솔루션</td>
      <td>2018-12-11</td>
      <td>12월31일</td>
      <td>정철</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2018</td>
    </tr>
    <tr>
      <td>티앤알바이오팹</td>
      <td>기초 의약물질 제조업</td>
      <td>생분해성 의료기기, 3D 바이오프린팅 시스템, 바이오잉크, 3D 오가노이드, 3D 세포치료제</td>
      <td>2018-11-28</td>
      <td>12월</td>
      <td>윤원수</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2018</td>
    </tr>
    <tr>
      <td>네오펙트</td>
      <td>의료용 기기 제조업</td>
      <td>라파엘스마트글러브 외</td>
      <td>2018-11-28</td>
      <td>12월</td>
      <td>반호영</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2018</td>
    </tr>
    <tr>
      <td>싸이토젠</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>CTC 기반 Liquid Biopsy 응용사업 및 플랫폼</td>
      <td>2018-11-22</td>
      <td>12월</td>
      <td>전병희, 안지훈 (각자대표)</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2018</td>
    </tr>
    <tr>
      <td>파멥신</td>
      <td>의약품 제조업</td>
      <td>항체치료제</td>
      <td>2018-11-21</td>
      <td>12월31일</td>
      <td>심주엽</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2018</td>
    </tr>
    <tr>
      <td>셀리버리</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>바이오의약품[iCP-Parkin(파킨슨병 치료제)]및 연구용 시약</td>
      <td>2018-11-09</td>
      <td>12월31일</td>
      <td>조대웅</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2018</td>
    </tr>
    <tr>
      <td>로보티즈</td>
      <td>특수 목적용 기계 제조업</td>
      <td>솔루션(로봇 엑츄에이터 모듈과 구동 소프트웨어), 에듀테인먼트 로봇, 로봇 플랫폼</td>
      <td>2018-10-26</td>
      <td>12월</td>
      <td>김병수</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2018</td>
    </tr>
    <tr>
      <td>옵티팜</td>
      <td>의료용품 및 기타 의약 관련제품 제조업</td>
      <td>옵티케어, 메디피그 등</td>
      <td>2018-10-26</td>
      <td>12월</td>
      <td>김현일</td>
      <td>홈페이지 보기</td>
      <td>충청북도</td>
      <td>2018</td>
    </tr>
    <tr>
      <td>바이오솔루션</td>
      <td>기초 의약물질 제조업</td>
      <td>세포치료제, 인체조직모델 등</td>
      <td>2018-08-20</td>
      <td>12월</td>
      <td>이정선</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2018</td>
    </tr>
    <tr>
      <td>올릭스</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>siRNA 신약 개발</td>
      <td>2018-07-18</td>
      <td>12월</td>
      <td>이동기</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2018</td>
    </tr>
    <tr>
      <td>아이큐어</td>
      <td>의약품 제조업</td>
      <td>플라스타, 의약 및 의약외품 패취등, 마스크팩, 화장품 기초라인</td>
      <td>2018-07-12</td>
      <td>12월</td>
      <td>이영석</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2018</td>
    </tr>
    <tr>
      <td>EDGC</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>유전체 분석 진단 서비스</td>
      <td>2018-06-26</td>
      <td>12월</td>
      <td>대표이사 이민섭</td>
      <td>홈페이지 보기</td>
      <td>인천광역시</td>
      <td>2018</td>
    </tr>
    <tr>
      <td>유네코</td>
      <td>특수 목적용 기계 제조업</td>
      <td>SAP</td>
      <td>2018-03-15</td>
      <td>12월</td>
      <td>박동필, 김종원(각자대표)</td>
      <td>홈페이지 보기</td>
      <td>인천광역시</td>
      <td>2018</td>
    </tr>
    <tr>
      <td>오스테오닉</td>
      <td>의료용 기기 제조업</td>
      <td>골접합 및 재건용 금속소재 및 생분해성 복합소재 기반 임플란트</td>
      <td>2018-02-22</td>
      <td>12월</td>
      <td>이동원</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2018</td>
    </tr>
    <tr>
      <td>엔지켐생명과학</td>
      <td>기초 의약물질 제조업</td>
      <td>EC-18(신약), 원료의약품</td>
      <td>2018-02-21</td>
      <td>12월</td>
      <td>손기영</td>
      <td>홈페이지 보기</td>
      <td>충청북도</td>
      <td>2018</td>
    </tr>
    <tr>
      <td>아시아종묘</td>
      <td>작물 재배업</td>
      <td>종자</td>
      <td>2018-02-12</td>
      <td>09월</td>
      <td>류경오</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2018</td>
    </tr>
    <tr>
      <td>링크제니시스</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>반도체, 디스플레이, 자동화 S/W 및 시스템 테스트 자동화 솔루션 개발(XCOMPRO, XGEM, MAT)</td>
      <td>2018-02-05</td>
      <td>12월</td>
      <td>정성우</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2018</td>
    </tr>
    <tr>
      <td>CJ 바이오사이언스</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>생명정보 플랫폼, 마이크로바이옴 분석 서비스</td>
      <td>2019-12-26</td>
      <td>12월31일</td>
      <td>천종식</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2019</td>
    </tr>
    <tr>
      <td>브릿지바이오</td>
      <td>기초 의약물질 제조업</td>
      <td>펠리노-1 단백질 저해제, 오토택신 저해제</td>
      <td>2019-12-20</td>
      <td>12월</td>
      <td>이정규</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2019</td>
    </tr>
    <tr>
      <td>메드팩토</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>항암제 신약개발</td>
      <td>2019-12-19</td>
      <td>12월31일</td>
      <td>김성진</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2019</td>
    </tr>
    <tr>
      <td>신테카바이오</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>유전체 빅데이터 기반의 AI신약개발 및 정밀의료서비스</td>
      <td>2019-12-17</td>
      <td>12월</td>
      <td>정종선</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2019</td>
    </tr>
    <tr>
      <td>제이엘케이</td>
      <td>컴퓨터 프로그래밍, 시스템 통합 및 관리업</td>
      <td>인공지능 기반 의료영상 진단 플랫폼, 인공지능 기반 산업용 X-ray 판독시스템</td>
      <td>2019-12-11</td>
      <td>12월</td>
      <td>김동민</td>
      <td>홈페이지 보기</td>
      <td>충청북도</td>
      <td>2019</td>
    </tr>
    <tr>
      <td>티움바이오</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>특발성폐섬유증 치료제, 면역항암제, 자궁내막증치료제, 혈우병치료제</td>
      <td>2019-11-22</td>
      <td>12월31일</td>
      <td>김훈택</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2019</td>
    </tr>
    <tr>
      <td>자비스</td>
      <td>특수 목적용 기계 제조업</td>
      <td>산업용 X-ray 검사장비(Xscan) 및 식품이물검사장비(Fscan)</td>
      <td>2019-11-15</td>
      <td>12월31일</td>
      <td>김형철</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2019</td>
    </tr>
    <tr>
      <td>라파스</td>
      <td>기타 화학제품 제조업</td>
      <td>마이크로니들 패치 제품(의약품패치, 의료기기패치, 미용패치 등)</td>
      <td>2019-11-11</td>
      <td>12월</td>
      <td>정도현</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2019</td>
    </tr>
    <tr>
      <td>미디어젠</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>음성인식 소프트웨어 기술개발</td>
      <td>2019-11-05</td>
      <td>12월</td>
      <td>송민규</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2019</td>
    </tr>
    <tr>
      <td>캐리소프트</td>
      <td>영화, 비디오물, 방송프로그램 제작 및 배급업</td>
      <td>영상 콘텐츠(30.05%), 공연(29.76%), 키즈카페(17.38%), 커머스(12.77%), 라이선스 및 기타(10.04%)</td>
      <td>2019-10-29</td>
      <td>12월</td>
      <td>박창신</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2019</td>
    </tr>
    <tr>
      <td>엔바이오니아</td>
      <td>그외 기타 제품 제조업</td>
      <td>양전하필터(정수기)</td>
      <td>2019-10-24</td>
      <td>12월</td>
      <td>한정철</td>
      <td>홈페이지 보기</td>
      <td>충청북도</td>
      <td>2019</td>
    </tr>
    <tr>
      <td>올리패스</td>
      <td>기초 의약물질 제조업</td>
      <td>인공유전자 플랫폼(OliPass PNA) 기술을 활용한 RNA치료제 신약개발</td>
      <td>2019-09-20</td>
      <td>12월</td>
      <td>손형석, 이진한 (각자 대표이사)</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2019</td>
    </tr>
    <tr>
      <td>라닉스</td>
      <td>반도체 제조업</td>
      <td>자동차 및 IoT 통신,보안 솔루션</td>
      <td>2019-09-18</td>
      <td>12월</td>
      <td>최승욱</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2019</td>
    </tr>
    <tr>
      <td>나노브릭</td>
      <td>기초 화학물질 제조업</td>
      <td>보안응용제품(M-tag 및 M-pac), 보안소재제품(M-secuprint)</td>
      <td>2019-08-19</td>
      <td>12월</td>
      <td>임용택</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2019</td>
    </tr>
    <tr>
      <td>플리토</td>
      <td>자료처리, 호스팅, 포털 및 기타 인터넷 정보매개 서비스업</td>
      <td>언어 데이터 구축 및 판매</td>
      <td>2019-07-17</td>
      <td>12월31일</td>
      <td>이정수</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2019</td>
    </tr>
    <tr>
      <td>압타바이오</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>용역매출(50.7%), 유전자전달체(32.7%), 압타머 연구용 시약(16.6%)</td>
      <td>2019-06-12</td>
      <td>12월</td>
      <td>이수진</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2019</td>
    </tr>
    <tr>
      <td>마이크로디지탈</td>
      <td>의료용 기기 제조업</td>
      <td>바이오 분석 시스템, 메디칼 자동화 시스템</td>
      <td>2019-06-05</td>
      <td>12월31일</td>
      <td>김경남</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2019</td>
    </tr>
    <tr>
      <td>수젠텍</td>
      <td>의료용품 및 기타 의약 관련제품 제조업</td>
      <td>체외진단 기기 및 시약</td>
      <td>2019-05-28</td>
      <td>12월31일</td>
      <td>손미진</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2019</td>
    </tr>
    <tr>
      <td>아모그린텍</td>
      <td>전자부품 제조업</td>
      <td>비정질 및 나노결정립을 이용한 자성부품 및 전류센서</td>
      <td>2019-03-29</td>
      <td>12월31일</td>
      <td>양성철, 김병규(각자대표)</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2019</td>
    </tr>
    <tr>
      <td>지노믹트리</td>
      <td>의료용품 및 기타 의약 관련제품 제조업</td>
      <td>암 조기진단 제품</td>
      <td>2019-03-27</td>
      <td>12월</td>
      <td>안성환</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2019</td>
    </tr>
    <tr>
      <td>셀리드</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>항암면역치료백신</td>
      <td>2019-02-20</td>
      <td>12월</td>
      <td>강창율</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2019</td>
    </tr>
    <tr>
      <td>SCL사이언스</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>의료용지혈제, 밀폐제 및 접착제</td>
      <td>2019-02-01</td>
      <td>12월31일</td>
      <td>이경률, 백세연 (각자대표)</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2019</td>
    </tr>
    <tr>
      <td>지놈앤컴퍼니</td>
      <td>기초 의약물질 제조업</td>
      <td>마이크로바이옴 기반 치료제, 화장품, 건강기능식품</td>
      <td>2020-12-23</td>
      <td>12월</td>
      <td>홍유석, 배지수, 박한수 (각자 대표이사)</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>석경에이티</td>
      <td>기초 화학물질 제조업</td>
      <td>바이오 및 전기전자 나노 소재</td>
      <td>2020-12-23</td>
      <td>12월</td>
      <td>임형섭</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>프리시젼바이오</td>
      <td>의료용 기기 제조업</td>
      <td>체외진단 기기 및 시약</td>
      <td>2020-12-22</td>
      <td>12월</td>
      <td>김한신</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>알체라</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>얼굴인식 AI, 이상상황 감지 AI 등</td>
      <td>2020-12-21</td>
      <td>12월31일</td>
      <td>황영규</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>엔젠바이오</td>
      <td>그외 기타 전문, 과학 및 기술 서비스업</td>
      <td>유전체 분야 진단시약 제조 및 유전체 분야 소프트웨어 연구,개발,판매</td>
      <td>2020-12-10</td>
      <td>12월31일</td>
      <td>최대출</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>퀀타매트릭스</td>
      <td>의료용 기기 제조업</td>
      <td>신속항균제검사 장비 및 키트</td>
      <td>2020-12-09</td>
      <td>12월</td>
      <td>권성훈</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>클리노믹스</td>
      <td>의료용품 및 기타 의약 관련제품 제조업</td>
      <td>Geno Series, CD-PRIME, Cancer Prime</td>
      <td>2020-12-04</td>
      <td>12월31일</td>
      <td>백서현</td>
      <td>홈페이지 보기</td>
      <td>울산광역시</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>고바이오랩</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>마이크로바이옴 치료제 및 건강기능식품</td>
      <td>2020-11-18</td>
      <td>12월</td>
      <td>고광표</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>센코</td>
      <td>전자부품 제조업</td>
      <td>가스센서 및 모듈, 휴대용 및 고정형 가스검지기, 악취 & 미세먼지 모니터링 시스템</td>
      <td>2020-10-29</td>
      <td>12월</td>
      <td>하승철</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>바이브컴퍼니</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>소셜 빅데이터 기반 인공지능 서비스 (소셜메트릭스), 문제 해결 솔루션 (AI Solver)</td>
      <td>2020-10-28</td>
      <td>12월</td>
      <td>김경서</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>미코바이오메드</td>
      <td>의료용 기기 제조업</td>
      <td>체외진단용 의료기기</td>
      <td>2020-10-22</td>
      <td>12월</td>
      <td>정민영</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>피플바이오</td>
      <td>의료용품 및 기타 의약 관련제품 제조업</td>
      <td>올리고머화 베타-아밀로이드 검사제품(알츠하이머병 진단)</td>
      <td>2020-10-19</td>
      <td>12월31일</td>
      <td>강성민</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>넥스틴</td>
      <td>특수 목적용 기계 제조업</td>
      <td>반도체 전공정용 패턴결함 검사장비(AEGIS 등)</td>
      <td>2020-10-08</td>
      <td>12월</td>
      <td>박태훈</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>박셀바이오</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>항암면역세포치료제(자연살해세포, 수지상세포, CAR-T 및 인터루킨 기반 항암제)</td>
      <td>2020-09-22</td>
      <td>12월31일</td>
      <td>이제중 (단독 대표이사)</td>
      <td>홈페이지 보기</td>
      <td>전라남도</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>압타머사이언스</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>압타머기반 신약개발 및 진단제품 개발</td>
      <td>2020-09-16</td>
      <td>12월</td>
      <td>한동일</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>이오플로우</td>
      <td>의료용 기기 제조업</td>
      <td>웨어러블 인슐린펌프</td>
      <td>2020-09-14</td>
      <td>12월</td>
      <td>김재진</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>셀레믹스</td>
      <td>기초 의약물질 제조업</td>
      <td>타겟캡처키트</td>
      <td>2020-08-21</td>
      <td>12월</td>
      <td>김효기, 이용훈</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>제놀루션</td>
      <td>기초 의약물질 제조업</td>
      <td>핵산추출기기 및 시약, RNAi 사업 등</td>
      <td>2020-07-24</td>
      <td>12월</td>
      <td>김기옥</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>솔트룩스</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>인공지능 및 빅데이터 소프트웨어</td>
      <td>2020-07-23</td>
      <td>12월</td>
      <td>이경일</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>소마젠</td>
      <td>그외 기타 전문, 과학 및 기술 서비스업</td>
      <td>유전체 분석 서비스 (NGS, CES 등)</td>
      <td>2020-07-13</td>
      <td>12월31일</td>
      <td>홍수</td>
      <td>홈페이지 보기</td>
      <td>미국</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>젠큐릭스</td>
      <td>의료용품 및 기타 의약 관련제품 제조업</td>
      <td>유방암 예후진단 및 폐암/대장암 동반진단 제품/검사서비스</td>
      <td>2020-06-25</td>
      <td>12월31일</td>
      <td>조상래</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>에스씨엠생명과학</td>
      <td>의약품 제조업</td>
      <td>세포치료제</td>
      <td>2020-06-17</td>
      <td>12월</td>
      <td>송기령</td>
      <td>홈페이지 보기</td>
      <td>인천광역시</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>카이노스메드</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>뇌질환치료제, 항암제, 항바이러스제 등</td>
      <td>2020-06-08</td>
      <td>12월31일</td>
      <td>이기섭</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>레몬</td>
      <td>화학섬유 제조업</td>
      <td>EMI Shield Can, 나노멤브레인 등</td>
      <td>2020-02-28</td>
      <td>12월</td>
      <td>김광진</td>
      <td>홈페이지 보기</td>
      <td>경상북도</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>서남</td>
      <td>기타 전기장비 제조업</td>
      <td>고온초전도선재</td>
      <td>2020-02-20</td>
      <td>12월</td>
      <td>문승현</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>툴젠</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>유전자교정 플랫폼 관련 제품</td>
      <td>2021-12-10</td>
      <td>12월</td>
      <td>이병화</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>마음AI</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>종합 인공지능 엔진 및 플랫폼</td>
      <td>2021-11-23</td>
      <td>12월</td>
      <td>유태준</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>지오엘리먼트</td>
      <td>전자부품 제조업</td>
      <td>센서, 캐니스터</td>
      <td>2021-11-11</td>
      <td>12월</td>
      <td>신현국</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>스카이월드와이드</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>그래프데이터베이스, 그래프분석서비스</td>
      <td>2021-11-10</td>
      <td>12월</td>
      <td>신재혁</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>지니너스</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>NGS기반 조직생검 암유전체 동반진단(CancerSCAN), 액체생검 암유전체 동반진단(LiquidSCAN), 단일세포분석(Celinus) 등</td>
      <td>2021-11-08</td>
      <td>12월</td>
      <td>박웅양</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>차백신연구소</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>백신 및 면역증강제 등</td>
      <td>2021-10-22</td>
      <td>12월</td>
      <td>염정선</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>에이비온</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>표적 항암제, 바이오 베터 신약</td>
      <td>2021-09-08</td>
      <td>12월</td>
      <td>신영기</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>바이젠셀</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>면역세포치료제 (면역항암제, 면역조절치료제 등)</td>
      <td>2021-08-25</td>
      <td>12월</td>
      <td>김태규</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>딥노이드</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>의료 인공지능플랫폼, 인공지능 임상의사결정 시스템</td>
      <td>2021-08-17</td>
      <td>12월31일</td>
      <td>최우식</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>원티드랩</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>채용 플랫폼</td>
      <td>2021-08-11</td>
      <td>12월</td>
      <td>이복기</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>비트맥스</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>AR 개발 플랫폼/AR솔루션</td>
      <td>2021-07-27</td>
      <td>12월31일</td>
      <td>홍상혁</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>큐라클</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>혈관질환치료제 등</td>
      <td>2021-07-22</td>
      <td>12월</td>
      <td>유재현</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>오비고</td>
      <td>컴퓨터 프로그래밍, 시스템 통합 및 관리업</td>
      <td>스마트카 소프트웨어 플랫폼</td>
      <td>2021-07-13</td>
      <td>12월</td>
      <td>황도연</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>아모센스</td>
      <td>전자부품 제조업</td>
      <td>무선충전 차폐시트</td>
      <td>2021-06-25</td>
      <td>12월31일</td>
      <td>김인응</td>
      <td>홈페이지 보기</td>
      <td>충청남도</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>라온테크</td>
      <td>특수 목적용 기계 제조업</td>
      <td>반도체 및 FPD용 로봇시스템</td>
      <td>2021-06-17</td>
      <td>12월</td>
      <td>김원경</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>진시스템</td>
      <td>의료용 기기 제조업</td>
      <td>분자진단기반 플랫폼 개발 및 제조·판매</td>
      <td>2021-05-26</td>
      <td>12월</td>
      <td>서유진</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>삼영에스앤씨</td>
      <td>전자부품 제조업</td>
      <td>칩형 온습도센서, 상대습도센서, 미세먼지센서, 공기질 통합센서 노드 및 트랜스미터</td>
      <td>2021-05-21</td>
      <td>12월</td>
      <td>박상익</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>샘씨엔에스</td>
      <td>전자부품 제조업</td>
      <td>세라믹 STF(다층 세라믹 기판)</td>
      <td>2021-05-20</td>
      <td>12월</td>
      <td>최정혁(단독 대표이사)</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>해성에어로보틱스</td>
      <td>기타 금속 가공제품 제조업</td>
      <td>기어 및 동력전달장치</td>
      <td>2021-04-21</td>
      <td>12월</td>
      <td>이건복,이정훈(각자 대표)</td>
      <td>홈페이지 보기</td>
      <td>인천광역시</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>자이언트스텝</td>
      <td>영화, 비디오물, 방송프로그램 제작 및 배급업</td>
      <td>광고VFX, 영상VFX 및 리얼타임 콘텐츠 제작</td>
      <td>2021-03-24</td>
      <td>12월</td>
      <td>하승봉, 이지철</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>제노코</td>
      <td>통신 및 방송 장비 제조업</td>
      <td>위성탑재체, 위성운용국, 항공전자 등</td>
      <td>2021-03-24</td>
      <td>12월</td>
      <td>유태삼</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>라이프시맨틱스</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>소프트웨어(개인건강기록 플랫폼,진료기록번역플랫폼,질병분류기호 검색) 개발,공급/의료기기 도매/자문,컨설팅/전자상거래,통신판매</td>
      <td>2021-03-23</td>
      <td>12월</td>
      <td>최광수</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>네오이뮨텍</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>면역항암제</td>
      <td>2021-03-16</td>
      <td>12월</td>
      <td>Luke Yun Suk Oh</td>
      <td>홈페이지 보기</td>
      <td>미국</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>프레스티지바이오로직스</td>
      <td>의약품 제조업</td>
      <td>바이오시밀러 제조</td>
      <td>2021-03-11</td>
      <td>12월31일</td>
      <td>현덕훈</td>
      <td>홈페이지 보기</td>
      <td>충청북도</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>나노씨엠에스</td>
      <td>전자부품 제조업</td>
      <td>근적외선 흡수/반사 안료, 자외선 유기형광 안료, 적외선 발광체</td>
      <td>2021-03-09</td>
      <td>12월31일</td>
      <td>신동근</td>
      <td>홈페이지 보기</td>
      <td>충청남도</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>뷰노</td>
      <td>자료처리, 호스팅, 포털 및 기타 인터넷 정보매개 서비스업</td>
      <td>뷰노메드 음성솔루션, 뷰노메드 영상솔루션, 기타 솔루션 등</td>
      <td>2021-02-26</td>
      <td>12월</td>
      <td>이예하</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>씨이랩</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>빅데이터플랫폼</td>
      <td>2021-02-24</td>
      <td>12월31일</td>
      <td>이우영</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>피엔에이치테크</td>
      <td>기초 화학물질 제조업</td>
      <td>OLED 소재</td>
      <td>2021-02-16</td>
      <td>12월</td>
      <td>현서용, 송영권</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>레인보우로보틱스</td>
      <td>특수 목적용 기계 제조업</td>
      <td>협동로봇, 천문마운트시스템, 이족보행로봇 등</td>
      <td>2021-02-03</td>
      <td>12월31일</td>
      <td>이정호</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>아티스트유나이티드</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>빅데이터/인공지능 마케팅플랫폼 및 데이터플랫폼</td>
      <td>2021-02-03</td>
      <td>12월</td>
      <td>황경주</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2021</td>
    </tr>
    <tr>
      <td>SAMG엔터</td>
      <td>영화, 비디오물, 방송프로그램 제작 및 배급업</td>
      <td>애니메이션 IP 기획 및 관련 제품 제작</td>
      <td>2022-12-06</td>
      <td>12월</td>
      <td>김수훈</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>인벤티지랩</td>
      <td>의약품 제조업</td>
      <td>마이크로/나노 입자 기반 약물전달 플랫폼 및 관련 제품</td>
      <td>2022-11-22</td>
      <td>12월</td>
      <td>김주희</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>엔젯</td>
      <td>특수 목적용 기계 제조업</td>
      <td>EHD 잉크젯 프린터, EHD 코터</td>
      <td>2022-11-18</td>
      <td>12월</td>
      <td>변도영</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>뉴로메카</td>
      <td>특수 목적용 기계 제조업</td>
      <td>협동로봇, 협동로봇 자동화 플랫폼, 로봇제어기 등</td>
      <td>2022-11-04</td>
      <td>12월</td>
      <td>박종훈</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>플라즈맵</td>
      <td>의료용 기기 제조업</td>
      <td>플라즈마 멸균기 및 표면처리기기</td>
      <td>2022-10-21</td>
      <td>12월31일</td>
      <td>김형민(단독 대표이사)</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>핀텔</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>AI 영상 분석 솔루션 및 소프트웨어</td>
      <td>2022-10-20</td>
      <td>12월31일</td>
      <td>김동기</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>샤페론</td>
      <td>기초 의약물질 제조업</td>
      <td>합성신약 및 항체치료제신약 기술제품 및 기술이전</td>
      <td>2022-10-19</td>
      <td>12월</td>
      <td>성승용</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>에스비비테크</td>
      <td>일반 목적용 기계 제조업</td>
      <td>베어링, 감속기</td>
      <td>2022-10-17</td>
      <td>12월</td>
      <td>류재완, 송진웅(각자 대표이사)</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>선바이오</td>
      <td>의약품 제조업</td>
      <td>PEG유도체 제품 (62%), 기술료수입 (38%)</td>
      <td>2022-10-05</td>
      <td>12월31일</td>
      <td>노광</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>아이씨에이치</td>
      <td>그외 기타 제품 제조업</td>
      <td>스마트기기용 필름형 안테나</td>
      <td>2022-07-29</td>
      <td>12월</td>
      <td>김영훈</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>에이프릴바이오</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>항체의약품 및 재조합 단백질 의약품</td>
      <td>2022-07-28</td>
      <td>12월31일</td>
      <td>차상훈</td>
      <td>홈페이지 보기</td>
      <td>강원특별자치도</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>루닛</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>Lunit INSIGHT</td>
      <td>2022-07-21</td>
      <td>12월</td>
      <td>서범석</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>와이씨켐</td>
      <td>기타 화학제품 제조업</td>
      <td>반도체 및 디스플레이용 화학소재</td>
      <td>2022-07-14</td>
      <td>12월</td>
      <td>이성일, 이승훈</td>
      <td>홈페이지 보기</td>
      <td>경상북도</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>코난테크놀로지</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>AI 기반 검색엔진(Konan Search), AI기반 영상인식 솔루션(D: Watcher)</td>
      <td>2022-07-07</td>
      <td>12월31일</td>
      <td>김영섬</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>넥스트칩</td>
      <td>반도체 제조업</td>
      <td>차량 및 자율주행차용 비메모리 반도체(ISP, AHD, ADAS/AD)</td>
      <td>2022-07-01</td>
      <td>12월31일</td>
      <td>김경수</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>원텍</td>
      <td>의료용 기기 제조업</td>
      <td>피부, 미용 의료기기 제조 및 판매</td>
      <td>2022-06-30</td>
      <td>12월31일</td>
      <td>김종원, 김정현</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>보로노이</td>
      <td>기초 의약물질 제조업</td>
      <td>표적치료제</td>
      <td>2022-06-24</td>
      <td>12월31일</td>
      <td>김현태</td>
      <td>홈페이지 보기</td>
      <td>인천광역시</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>레이저쎌</td>
      <td>특수 목적용 기계 제조업</td>
      <td>에어리어 레이저솔루션, LSR, LCB, LSB, BSOM 등</td>
      <td>2022-06-24</td>
      <td>12월</td>
      <td>안건준</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>비큐AI</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>아이서퍼, 위고몬 등</td>
      <td>2022-06-20</td>
      <td>12월</td>
      <td>임경환</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>하이딥</td>
      <td>반도체 제조업</td>
      <td>시스템반도체 IC설계</td>
      <td>2022-05-12</td>
      <td>12월31일</td>
      <td>고범규</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>모아데이타</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>인공지능 기반 ICT 시스템 이상탐지 및 예측 솔루션</td>
      <td>2022-03-10</td>
      <td>12월</td>
      <td>한상진</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>노을</td>
      <td>의료용 기기 제조업</td>
      <td>융복합 체외진단 플랫폼</td>
      <td>2022-03-03</td>
      <td>12월</td>
      <td>임찬양(단독 대표이사)</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>풍원정밀</td>
      <td>전자부품 제조업</td>
      <td>OLED 증착용 Metal Mask</td>
      <td>2022-02-28</td>
      <td>12월</td>
      <td>유명훈</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>퓨런티어</td>
      <td>측정, 시험, 항해, 제어 및 기타 정밀기기 제조업; 광학기기 제외</td>
      <td>전장카메라모듈장비, 모바일카메라모듈장비, PC및 광원</td>
      <td>2022-02-23</td>
      <td>12월</td>
      <td>오상근</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>바이오에프디엔씨</td>
      <td>기초 의약물질 제조업</td>
      <td>식물세포 유래 유효물질 및 약리물질</td>
      <td>2022-02-21</td>
      <td>12월</td>
      <td>모상현, 정대현</td>
      <td>홈페이지 보기</td>
      <td>인천광역시</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>스코넥</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>XR 교육/훈련 시스템, VR 게임 콘텐츠 등</td>
      <td>2022-02-04</td>
      <td>12월</td>
      <td>황대실</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>이지트로닉스</td>
      <td>전동기, 발전기 및 전기 변환 · 공급 · 제어 장치 제조업</td>
      <td>전력변환장치</td>
      <td>2022-02-04</td>
      <td>12월31일</td>
      <td>강찬호</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>애드바이오텍</td>
      <td>의약품 제조업</td>
      <td>동물용약품,영양제,단미사료(네오폐녹스),보조사료 제조,도매/식품첨가물,화장품 도소매,무역</td>
      <td>2022-01-24</td>
      <td>12월</td>
      <td>정홍걸</td>
      <td>홈페이지 보기</td>
      <td>강원특별자치도</td>
      <td>2022</td>
    </tr>
    <tr>
      <td>와이바이오로직스</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>항체의약품 및 항체후보물질 연구개발</td>
      <td>2023-12-05</td>
      <td>12월</td>
      <td>박영우, 장우익</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>에이텀</td>
      <td>전자부품 제조업</td>
      <td>평판형 트랜스</td>
      <td>2023-12-01</td>
      <td>06월</td>
      <td>한택수</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>그린리소스</td>
      <td>반도체 제조업</td>
      <td>반도체 및 디스플레이 장비 보호코팅 및 소재</td>
      <td>2023-11-24</td>
      <td>12월</td>
      <td>이종수,이종범(공동대표이사)</td>
      <td>홈페이지 보기</td>
      <td>인천광역시</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>큐로셀</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>CAR-T 세포치료제</td>
      <td>2023-11-09</td>
      <td>12월</td>
      <td>김건수</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>컨텍</td>
      <td>컴퓨터 프로그래밍, 시스템 통합 및 관리업</td>
      <td>지상국 시스템 엔지니어링 솔루션, 위성영상 생성을 위한 데이터처리 솔루션</td>
      <td>2023-11-09</td>
      <td>12월</td>
      <td>이성희</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>쏘닉스</td>
      <td>반도체 제조업</td>
      <td>RF필터 파운드리</td>
      <td>2023-11-07</td>
      <td>12월</td>
      <td>양형국</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>세니젠</td>
      <td>그외 기타 제품 제조업</td>
      <td>Genelix, Genext, Geneka 등</td>
      <td>2023-11-03</td>
      <td>12월</td>
      <td>박정웅</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>퀄리타스반도체</td>
      <td>반도체 제조업</td>
      <td>초고속 통신용 반도체 IP</td>
      <td>2023-10-27</td>
      <td>12월</td>
      <td>김두호</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>아이엠티</td>
      <td>특수 목적용 기계 제조업</td>
      <td>건식세정 장비 및 EUV Mask Baking Laser</td>
      <td>2023-10-10</td>
      <td>12월</td>
      <td>최재성</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>코어라인소프트</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>의료영상 진단보조 솔루션</td>
      <td>2023-09-18</td>
      <td>12월31일</td>
      <td>김진국</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>크라우드웍스</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>인공지능 데이터 구축 서비스</td>
      <td>2023-08-31</td>
      <td>12월</td>
      <td>김우승</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>시큐레터</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>SLE(이메일 보안), SLF(파일 보안)</td>
      <td>2023-08-24</td>
      <td>12월</td>
      <td>임차성</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>스마트레이더시스템</td>
      <td>측정, 시험, 항해, 제어 및 기타 정밀기기 제조업; 광학기기 제외</td>
      <td>모빌리티 및 비모빌리티용 4D이미징레이다</td>
      <td>2023-08-22</td>
      <td>12월31일</td>
      <td>김용환</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>큐리옥스바이오시스템즈</td>
      <td>의료용 기기 제조업</td>
      <td>세포 전처리 자동화기기 등</td>
      <td>2023-08-10</td>
      <td>12월</td>
      <td>김남용</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>파두</td>
      <td>반도체 제조업</td>
      <td>SSD 컨트롤러</td>
      <td>2023-08-07</td>
      <td>12월</td>
      <td>이지효,남이현</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>시지트로닉스</td>
      <td>반도체 제조업</td>
      <td>특화반도체 소자</td>
      <td>2023-08-03</td>
      <td>12월</td>
      <td>심규환 (단독 대표이사)</td>
      <td>홈페이지 보기</td>
      <td>전북특별자치도</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>파로스아이바이오</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>PHI-101 급성골수성백혈병 치료제 및 재발성난소암 치료제</td>
      <td>2023-07-27</td>
      <td>12월31일</td>
      <td>윤정혁</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>버넥트</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>산업용 XR 솔루션</td>
      <td>2023-07-26</td>
      <td>12월</td>
      <td>하태진</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>와이랩</td>
      <td>영화, 비디오물, 방송프로그램 제작 및 배급업</td>
      <td>만화출판물의 제작 및 영상물 제작</td>
      <td>2023-07-20</td>
      <td>12월</td>
      <td>심준경</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>센서뷰</td>
      <td>절연선 및 케이블 제조업</td>
      <td>T&M 케이블, 초소형 전송선로</td>
      <td>2023-07-19</td>
      <td>12월</td>
      <td>김병남</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>이노시뮬레이션</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>스마트 모빌리티 시뮬레이터, XR 가상훈련 시스템 등</td>
      <td>2023-07-06</td>
      <td>12월</td>
      <td>조준희</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>오픈놀</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>미니인턴플랫폼(커리어 및 채용 플랫폼)</td>
      <td>2023-06-30</td>
      <td>12월31일</td>
      <td>권인택</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>프로티아</td>
      <td>의료용 기기 제조업</td>
      <td>알레르기 진단 제품</td>
      <td>2023-06-16</td>
      <td>12월</td>
      <td>임국진</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>큐라티스</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>백신 및 면역증강제 개발제조업, CMO/CDMO</td>
      <td>2023-06-15</td>
      <td>12월</td>
      <td>김성준</td>
      <td>홈페이지 보기</td>
      <td>충청북도</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>씨유박스</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>AI얼굴인식 시스템, AI얼굴인증 솔루션, AI 객체인식 솔루션, AI데이터 플랫폼</td>
      <td>2023-05-19</td>
      <td>12월</td>
      <td>남운성</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>모니터랩</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>웹방화벽,유해사이트솔루션,가시성SSL 솔루션, SASE플랫폼기반 SECaaS</td>
      <td>2023-05-19</td>
      <td>12월</td>
      <td>이광후</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>에스바이오메딕스</td>
      <td>의약품 제조업</td>
      <td>줄기세포 치료제 연구 및 개발</td>
      <td>2023-05-04</td>
      <td>12월</td>
      <td>강세일</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>마이크로투나노</td>
      <td>반도체 제조업</td>
      <td>메모리 테스트용 프로브 카드</td>
      <td>2023-04-26</td>
      <td>12월</td>
      <td>황규호</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>지아이이노베이션</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>면역항암제 및 알레르기 치료제</td>
      <td>2023-03-30</td>
      <td>12월</td>
      <td>이병건, 홍준호(각자대표이사)</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>라온텍</td>
      <td>전자부품 제조업</td>
      <td>마이크로디스플레이, 컨트롤러 IC</td>
      <td>2023-03-09</td>
      <td>12월</td>
      <td>김보은</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2023</td>
    </tr>
    <tr>
      <td>파인메딕스</td>
      <td>의료용 기기 제조업</td>
      <td>인젝터, 스네어, 나이프, 포셉 등 내시경용 시술기구</td>
      <td>2024-12-26</td>
      <td>12월</td>
      <td>전성우, 김성철</td>
      <td>홈페이지 보기</td>
      <td>대구광역시</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>엠에프씨</td>
      <td>기초 의약물질 제조업</td>
      <td>원료의약품(API) 및 핵심소재</td>
      <td>2024-12-26</td>
      <td>12월</td>
      <td>황성관</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>쓰리에이로직스</td>
      <td>반도체 제조업</td>
      <td>NFC/IoT SoC 및 모듈</td>
      <td>2024-12-24</td>
      <td>12월</td>
      <td>박광범, 이평한</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>온코닉테라퓨틱스</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>자큐보정(Zastaprazan, 소화기질환 신약), Nesuparib(표적항암제 신약)</td>
      <td>2024-12-19</td>
      <td>12월</td>
      <td>김존</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>온코크로스</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>AI플랫폼 기반 신약개발 용역서비스</td>
      <td>2024-12-18</td>
      <td>12월</td>
      <td>김이랑</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>유디엠텍</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>PLC eXpert, OPTRA Black-box, OPTRA Tracker</td>
      <td>2024-11-20</td>
      <td>12월</td>
      <td>왕지남</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>쓰리빌리언</td>
      <td>의료용 기기 제조업</td>
      <td>유전체 분석 기반 희귀 유전질환 진단 검사 서비스</td>
      <td>2024-11-14</td>
      <td>12월</td>
      <td>금창원</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>에어레인</td>
      <td>일반 목적용 기계 제조업</td>
      <td>기체분리막 모듈 및 시스템</td>
      <td>2024-11-08</td>
      <td>12월</td>
      <td>하성용</td>
      <td>홈페이지 보기</td>
      <td>충청북도</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>토모큐브</td>
      <td>사진장비 및 광학기기 제조업</td>
      <td>홀로토모그래피 HT-X1, HT-2H</td>
      <td>2024-11-07</td>
      <td>12월</td>
      <td>박용근, 홍기현</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>에이치이엠파마</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>맞춤형 헬스케어, LBP 디스커버리 플랫폼</td>
      <td>2024-11-05</td>
      <td>12월</td>
      <td>지요셉</td>
      <td>홈페이지 보기</td>
      <td>경상북도</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>클로봇</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>로봇 소프트웨어(카멜레온, 크롬스)</td>
      <td>2024-10-28</td>
      <td>12월</td>
      <td>각자 대표이사 김창구, 김경필</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>웨이비스</td>
      <td>반도체 제조업</td>
      <td>GaN RF 칩, 패키지 트랜지스터, 모듈 등</td>
      <td>2024-10-25</td>
      <td>12월31일</td>
      <td>한민석</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>씨메스</td>
      <td>특수 목적용 기계 제조업</td>
      <td>AI 기반 로봇 솔루션 및 3D 비전 솔루션</td>
      <td>2024-10-24</td>
      <td>12월</td>
      <td>이성호</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>루미르</td>
      <td>항공기,우주선 및 부품 제조업</td>
      <td>인공위성 시스템 및 전장품, 위성 영상 및 정보</td>
      <td>2024-10-21</td>
      <td>12월</td>
      <td>남명용</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>셀비온</td>
      <td>의약품 제조업</td>
      <td>셀비온그린주, 셀비온메브로페닌주, 도페정 등</td>
      <td>2024-10-16</td>
      <td>12월31일</td>
      <td>김권</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>아이언디바이스</td>
      <td>반도체 제조업</td>
      <td>스마트폰용 오디오 앰프 반도체 Soc</td>
      <td>2024-09-23</td>
      <td>12월</td>
      <td>박기태</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>이엔셀</td>
      <td>기초 의약물질 제조업</td>
      <td>첨단바이오의약품 위탁개발생산(CDMO) 서비스 / 차세대 세포,유전자 치료제</td>
      <td>2024-08-23</td>
      <td>12월31일</td>
      <td>장종욱</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>넥스트바이오메디컬</td>
      <td>의료용 기기 제조업</td>
      <td>내시경용 지혈재, 혈관색전 미립구</td>
      <td>2024-08-20</td>
      <td>12월31일</td>
      <td>이돈행</td>
      <td>홈페이지 보기</td>
      <td>인천광역시</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>케이쓰리아이</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>XR 실감형콘텐츠</td>
      <td>2024-08-20</td>
      <td>12월</td>
      <td>이재영</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>뱅크웨어글로벌</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>국내외 은행 및 금융기업 대상 코어뱅킹 소프트웨어</td>
      <td>2024-08-12</td>
      <td>12월</td>
      <td>이경조, 이은중</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>아이빔테크놀로지</td>
      <td>사진장비 및 광학기기 제조업</td>
      <td>생체현미경, CRO 서비스</td>
      <td>2024-08-06</td>
      <td>12월</td>
      <td>김필한</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>피앤에스미캐닉스</td>
      <td>의료용 기기 제조업</td>
      <td>보행재활로봇 시스템</td>
      <td>2024-07-31</td>
      <td>12월</td>
      <td>박광훈</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>엑셀세라퓨틱스</td>
      <td>기초 의약물질 제조업</td>
      <td>CellCor SFD/CD(세포배양배지)</td>
      <td>2024-07-15</td>
      <td>12월</td>
      <td>이의일</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>하스</td>
      <td>의료용품 및 기타 의약 관련제품 제조업</td>
      <td>리튬디실리케이트 수복소재(Amber block, Amber Ingot 등), 지르코니아 유치관</td>
      <td>2024-07-03</td>
      <td>12월</td>
      <td>김용수</td>
      <td>홈페이지 보기</td>
      <td>강원특별자치도</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>이노스페이스</td>
      <td>항공기,우주선 및 부품 제조업</td>
      <td>소형발사체, 로켓추진기관, 과학로켓, 시험평가용역</td>
      <td>2024-07-02</td>
      <td>12월</td>
      <td>김수종</td>
      <td>홈페이지 보기</td>
      <td>세종특별자치시</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>에이치브이엠</td>
      <td>1차 비철금속 제조업</td>
      <td>Ni계 합금, Fe계 합금, 스퍼터링타겟, Cu계 합금 등</td>
      <td>2024-06-28</td>
      <td>12월</td>
      <td>문승호</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>에스오에스랩</td>
      <td>측정, 시험, 항해, 제어 및 기타 정밀기기 제조업; 광학기기 제외</td>
      <td>산업용 및 차량용 라이다(LiDAR)</td>
      <td>2024-06-25</td>
      <td>12월</td>
      <td>정지성</td>
      <td>홈페이지 보기</td>
      <td>광주광역시</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>한중엔시에스</td>
      <td>전동기, 발전기 및 전기 변환 · 공급 · 제어 장치 제조업</td>
      <td>수냉식 냉각시스템 ESS Parts, 공랭식 ESS Module Parts, EV Module 및 내연기관 Parts</td>
      <td>2024-06-24</td>
      <td>12월</td>
      <td>김환식</td>
      <td>홈페이지 보기</td>
      <td>경상북도</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>씨어스테크놀로지</td>
      <td>의료용 기기 제조업</td>
      <td>심전도검사솔루션 입원환자모니터링솔루션</td>
      <td>2024-06-19</td>
      <td>12월</td>
      <td>이영신</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>라메디텍</td>
      <td>의료용 기기 제조업</td>
      <td>초소형 레이저 의료기기  및 미용기기</td>
      <td>2024-06-17</td>
      <td>12월</td>
      <td>최종석</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2024</td>
    </tr>
    <tr>
      <td>오름테라퓨틱</td>
      <td>기초 의약물질 제조업</td>
      <td>항체약물접합체(ADC) 단백질 분해제(TPD) 연구 개발</td>
      <td>2025-02-14</td>
      <td>12월</td>
      <td>이승주</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2025</td>
    </tr>
    <tr>
      <td>아이에스티이</td>
      <td>반도체 제조업</td>
      <td>반도체 제조용 장비</td>
      <td>2025-02-12</td>
      <td>12월</td>
      <td>조창현</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2025</td>
    </tr>
    <tr>
      <td>아이지넷</td>
      <td>기타 정보 서비스업</td>
      <td>보험 서비스 어플리케이션, 기업용 보험 솔루션</td>
      <td>2025-02-04</td>
      <td>12월</td>
      <td>김창균, 김지태</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2025</td>
    </tr>
    <tr>
      <td>와이즈넛</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>검색엔진, 챗봇, 클라우드서비스</td>
      <td>2025-01-24</td>
      <td>12월</td>
      <td>강용성</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2025</td>
    </tr>
  </tbody>
</table>
</pre>

### 각 기업이 기술성장의 어느 트랙인지 확인하기

문제가 하나 더 있습니다. **KIND의 기타 상장통계화면에서는 혁신기술 트랙인지, 사업모델 트랙인지 구분하여 표시하고 있지 않습니다.**{: style="color: #4682B4;"} 정상적인 통계화면에서는 조회가능하지 않고... 우회적인 방법으로 트랙을 확인해야 합니다.<br><br>

![reportpage]({{site.url}}/assets/images/2025-03-01-listing/reportpage.png)<br><br>

KIND에는 ***'상장법인상세정보'-'기업분석보고서'-'사업모델평가보고서'***메뉴가 있습니다. 한국거래소의 코스닥 상장규정에서는 사업모델 트랙으로 상장한 특례기업의 상장을 주관한 **상장주관사에 성장성보고서(사업모델보고서) 제출을 의무화**{: style="color: #4682B4;"}하고 있습니다. 따라서 이 게시판에서 조회되는 회사는 사업모델 트랙으로 상장했음을 알 수 있습니다. <br>

이 게시판의 제출내역을 한번 봐보겠습니다.


<pre>
개수 : 21

<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>번호</th>
      <th>작성일</th>
      <th>회사명</th>
      <th>작성기관</th>
      <th>첨부</th>
      <th>상장트랙</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>21</td>
      <td>2024-11-06</td>
      <td>아이지넷</td>
      <td>한국투자증권</td>
      <td>상장주선인 추천에 의한 사업모델기업 평가보고서_아이지넷(게시용).pdf</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>20</td>
      <td>2023-07-17</td>
      <td>와이랩</td>
      <td>한국투자증권</td>
      <td>상장주선인 추천에 의한 기술성장기업 성장성 보고서_와이랩_공시.pdf</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>19</td>
      <td>2022-06-17</td>
      <td>선바이오</td>
      <td>하나증권</td>
      <td>기술성장기업 성장성 보고서_선바이오.pdf</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>18</td>
      <td>2021-06-22</td>
      <td>원티드랩</td>
      <td>한국투자증권</td>
      <td>(주)원티드랩_성장성보고서.pdf</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>17</td>
      <td>2021-04-02</td>
      <td>진시스템</td>
      <td>삼성증권</td>
      <td>[삼성증권]진시스템_상장주선인의 성장성보고서.pdf</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>16</td>
      <td>2021-03-23</td>
      <td>삼영에스앤씨</td>
      <td>미래에셋증권</td>
      <td>삼영에스앤씨_상장주선인 추천에 의한 기술성장기업 성장성 보고서.pdf</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>15</td>
      <td>2021-01-15</td>
      <td>레인보우로보틱스</td>
      <td>미래에셋증권</td>
      <td>레인보우로보틱스_상장주선인 추천에 의한 기술성장기업 성장성 보고서_vF.pdf</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>14</td>
      <td>2020-12-23</td>
      <td>프레스티지바이오로직스</td>
      <td>미래에셋증권</td>
      <td>프레스티지바이오로직스_상장주선인 추천에 의한 기술성장기업 성장성 보고서.pdf</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>13</td>
      <td>2020-10-05</td>
      <td>고바이오랩</td>
      <td>삼성증권</td>
      <td>고바이오랩_상장주선인의 성장성보고서.pdf</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>12</td>
      <td>2020-10-05</td>
      <td>클리노믹스</td>
      <td>대신증권</td>
      <td>상장주선인 기술성장기업 성장성보고서_클리노믹스_20201005.pdf</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>11</td>
      <td>2020-09-09</td>
      <td>알체라</td>
      <td>신영증권</td>
      <td>99. 알체라 기술성장기업 성장성 보고서.pdf</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>10</td>
      <td>2020-07-29</td>
      <td>압타머사이언스</td>
      <td>키움증권</td>
      <td>기술성장기업 성장성 보고서_압타머사이언스.pdf</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>9</td>
      <td>2020-07-17</td>
      <td>제놀루션</td>
      <td>신영증권</td>
      <td>제놀루션_기술성장기업 성장성 보고서_신영증권.pdf</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>8</td>
      <td>2020-07-16</td>
      <td>이오플로우</td>
      <td>하나증권</td>
      <td>상장주선인 추천에 의한 기술성장기업 성장성보고서(이오플로우).pdf</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>7</td>
      <td>2020-06-24</td>
      <td>셀레믹스</td>
      <td>대신증권</td>
      <td>01. 셀레믹스 성장성보고서_2020414_수정.pdf</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>6</td>
      <td>2019-11-06</td>
      <td>신테카바이오</td>
      <td>KB증권</td>
      <td>신테카바이오_성장성보고서_KB증권.pdf</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>5</td>
      <td>2019-10-30</td>
      <td>브릿지바이오</td>
      <td>대신증권</td>
      <td>성장성보고서_브릿지바이오테라퓨틱스.pdf</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>4</td>
      <td>2019-10-02</td>
      <td>라파스</td>
      <td>DB금융투자</td>
      <td>DBFI_Raphas_성장성보고서_20190725.pdf</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>3</td>
      <td>2019-07-17</td>
      <td>올리패스</td>
      <td>미래에셋증권</td>
      <td>올리패스_상장주선인 추천에 의한 기술성장기업 성장성 보고서.pdf</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>2</td>
      <td>2019-07-15</td>
      <td>라닉스</td>
      <td>한국투자증권</td>
      <td>라닉스_상장주선인 추천에 의한 기술성장기업 성장성 보고서.pdf</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2018-09-18</td>
      <td>셀리버리</td>
      <td>DB금융투자</td>
      <td>셀리버리_성장성보고서_0918.pdf</td>
      <td>사업모델</td>
    </tr>
  </tbody>
</table>
</pre>

## KIND에서 코스닥 종목코드 불러오기

지금까지 KIND에서 2014년부터 현재까지 기술성장기업 목록과 상장트랙을 확인하였습니다. **그러나 여전히 종목코드가 없습니다.**{: style="color: #4682B4;"} <br>

아쉽게도 KIND에서 회사명과 종목코드를 일람표 형태로 보여주는 곳은 찾지 못했으나, 크롤링을 하는 과정에서 확인해보니 **html 소스에는 회사코드가 포함**{: style="color: #4682B4;"}된 경우가 대부분이었습니다. <br>

> KIND의 HTML 소스를 통해서 회사코드를 확인할 수 있습니다.


> 통상 종목코드는 회사코드 5자리 숫자 + 0입니다.

<br>


### 코스닥 상장법인 현황 불러오기

![kindlisting]({{site.url}}/assets/images/2025-03-01-listing/kindlisting.png)<br><br>

***'상장법인상세정보'-'상장법인목록'***을 들어가면 상장법인 목록이 있고, html소스에서 5자리 회사코드를 확인할 수 있습니다. 이를 활용하여 앞서 수집한 기술성장기업에 vlookup을 걸어보고, 혹시 vlookup이 안걸린 부분이 있는지 확인해보겠습니다.



<pre>
종목코드 전부 매칭됨
</pre>

### 사업모델 보고서에 종목코드 붙이기

앞서 보았던 상장주관사가 제출하는 사업모델보고서(성장성보고서)에도 종목코드를 맵핑시켜 주겠습니다.

<br>

<pre>
종목코드 전부 매칭됨
</pre>

### KIND에서 불러온 내용 전체 합치기

이제 KIND에서 불러온 아래의 정보들을 합쳐보겠습니다.<br>

* **기술성장기업 목록(종목코드 없음)**{: style="color: #4682B4;"}

* **주관사가 제출한 사업모델보고서(성장성보고서)(종목코드 없음)**{: style="color: #4682B4;"}

* **상장된 회사의 회사명과 회사코드**{: style="color: #4682B4;"}

* **상장폐지된 회사의 회사명과 회사코드**{: style="color: #4682B4;"}



<br>



<pre>
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>회사명</th>
      <th>업종</th>
      <th>주요제품</th>
      <th>상장일(스팩합병일)</th>
      <th>결산기</th>
      <th>대표자명</th>
      <th>홈페이지</th>
      <th>지역</th>
      <th>연도</th>
      <th>회사코드</th>
      <th>상장트랙</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>아스트</td>
      <td>항공기,우주선 및 부품 제조업</td>
      <td>항공기용 부품 제조 및 동체 조립</td>
      <td>2014-12-24</td>
      <td>12월</td>
      <td>김두일</td>
      <td>홈페이지 보기</td>
      <td>경상남도</td>
      <td>2014</td>
      <td>067390</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>알테오젠</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>바이오시밀러 및 바이오베터</td>
      <td>2014-12-12</td>
      <td>12월</td>
      <td>박순재</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2014</td>
      <td>196170</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>덱스터</td>
      <td>영화, 비디오물, 방송프로그램 제작 및 배급업</td>
      <td>시각효과(Visual Effect, VFX)</td>
      <td>2015-12-22</td>
      <td>12월</td>
      <td>김욱, 강종익</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2015</td>
      <td>206560</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>HLB제약</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>씨트리시메티딘정, 로자틴정</td>
      <td>2015-12-21</td>
      <td>12월31일</td>
      <td>박재형</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2015</td>
      <td>047920</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>강스템바이오텍</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>줄기세포치료제</td>
      <td>2015-12-21</td>
      <td>12월</td>
      <td>나종천</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2015</td>
      <td>217730</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>파크시스템스</td>
      <td>측정, 시험, 항해, 제어 및 기타 정밀기기 제조업; 광학기기 제외</td>
      <td>연구용 및 산업용 원자현미경</td>
      <td>2015-12-17</td>
      <td>12월</td>
      <td>박상일</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2015</td>
      <td>140860</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>멕아이씨에스</td>
      <td>의료용 기기 제조업</td>
      <td>인공호흡기</td>
      <td>2015-12-14</td>
      <td>12월31일</td>
      <td>김종철</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2015</td>
      <td>058110</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>DXVX</td>
      <td>의료용 기기 제조업</td>
      <td>BAC DNA CHIP</td>
      <td>2015-11-20</td>
      <td>12월</td>
      <td>이용구, 권규찬 (각자 대표이사)</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2015</td>
      <td>180400</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>아이진</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>당뇨성망막병증 치료제, 욕창치료제, 자궁경부암 예방 백신 등</td>
      <td>2015-11-16</td>
      <td>12월</td>
      <td>최석근</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2015</td>
      <td>185490</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>시지메드텍</td>
      <td>의료용 기기 제조업</td>
      <td>정형외과용 신체보정용 의료기기</td>
      <td>2015-11-12</td>
      <td>12월</td>
      <td>정주미</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2015</td>
      <td>056090</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>엔케이맥스</td>
      <td>기초 의약물질 제조업</td>
      <td>연구용 시약, NK Vue KIT</td>
      <td>2015-10-23</td>
      <td>12월31일</td>
      <td>박상우</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2015</td>
      <td>182400</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>펩트론</td>
      <td>기초 의약물질 제조업</td>
      <td>약효지속성 의약품 및 펩타이드 소재</td>
      <td>2015-07-22</td>
      <td>12월</td>
      <td>최호일</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2015</td>
      <td>087010</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>코아스템켐온</td>
      <td>의약품 제조업</td>
      <td>줄기세포 치료제</td>
      <td>2015-06-26</td>
      <td>12월</td>
      <td>양길안</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2015</td>
      <td>166480</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>HLB제넥스</td>
      <td>기초 의약물질 제조업</td>
      <td>산업용 효소</td>
      <td>2015-05-29</td>
      <td>12월31일</td>
      <td>김의중, 김도연 (각자 대표이사)</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2015</td>
      <td>187420</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>애니젠</td>
      <td>기초 의약물질 제조업</td>
      <td>펩타이드 바이오소재 및 아미노산 펩타이드 신약</td>
      <td>2016-12-07</td>
      <td>12월</td>
      <td>김재일</td>
      <td>홈페이지 보기</td>
      <td>광주광역시</td>
      <td>2016</td>
      <td>196300</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>신라젠</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>펙사벡(바이러스 항암면역치료제)</td>
      <td>2016-12-06</td>
      <td>12월</td>
      <td>김재경</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2016</td>
      <td>215600</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>퓨쳐켐</td>
      <td>의약품 제조업</td>
      <td>PET 방사성의약품, 자동합성장치, 합성시약 및 전구체</td>
      <td>2016-12-01</td>
      <td>12월</td>
      <td>지대윤</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2016</td>
      <td>220100</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>얼라인드</td>
      <td>사진장비 및 광학기기 제조업</td>
      <td>자동세포카운팅시스템, 생체조직투명화시스템, 디지털세포이미징시스템</td>
      <td>2016-11-03</td>
      <td>12월</td>
      <td>정연철</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2016</td>
      <td>238120</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>지엘팜텍</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>지소렌정</td>
      <td>2016-10-05</td>
      <td>12월31일</td>
      <td>김용일, 진성필</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2016</td>
      <td>204840</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>아이윈플러스</td>
      <td>전자부품 제조업</td>
      <td>이미지센서 패키징</td>
      <td>2016-07-20</td>
      <td>12월</td>
      <td>이준식</td>
      <td>홈페이지 보기</td>
      <td>충청북도</td>
      <td>2016</td>
      <td>123010</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>모아라이프플러스</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>자궁경부상피이형증 치료제, 자궁경부전암 치료백신</td>
      <td>2016-07-07</td>
      <td>12월</td>
      <td>한상진</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2016</td>
      <td>142760</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>팬젠</td>
      <td>의약품 제조업</td>
      <td>바이오시밀러 제품, 바이오의약품 개발 기술이전 서비스 등</td>
      <td>2016-03-11</td>
      <td>12월31일</td>
      <td>윤재승</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2016</td>
      <td>222110</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>큐리언트</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>저분자 혁신신약</td>
      <td>2016-02-29</td>
      <td>12월</td>
      <td>남기연</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2016</td>
      <td>115180</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>안트로젠</td>
      <td>기초 의약물질 제조업</td>
      <td>줄기세포치료제</td>
      <td>2016-02-15</td>
      <td>12월</td>
      <td>이성구, 김미형(각자대표)</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2016</td>
      <td>065660</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>휴마시스</td>
      <td>의료용 기기 제조업</td>
      <td>임신진단키트</td>
      <td>2017-10-17</td>
      <td>12월31일</td>
      <td>김성곤</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2017</td>
      <td>205470</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>앱클론</td>
      <td>의료용품 및 기타 의약 관련제품 제조업</td>
      <td>항체의약품</td>
      <td>2017-09-18</td>
      <td>12월31일</td>
      <td>이종서</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2017</td>
      <td>174900</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>어스앤에어로스페이스</td>
      <td>항공기,우주선 및 부품 제조업</td>
      <td>도어시스템</td>
      <td>2017-09-15</td>
      <td>12월31일</td>
      <td>조동우</td>
      <td>홈페이지 보기</td>
      <td>경상남도</td>
      <td>2017</td>
      <td>263540</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>모비스</td>
      <td>컴퓨터 프로그래밍, 시스템 통합 및 관리업</td>
      <td>핵융합 제어시스템설계, 가속기 제어시스템설계</td>
      <td>2017-03-21</td>
      <td>12월31일</td>
      <td>김지헌</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2017</td>
      <td>250060</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>아스타</td>
      <td>의료용품 및 기타 의약 관련제품 제조업</td>
      <td>MALDI-TOF 질량분석기 기반 진단시스템</td>
      <td>2017-03-20</td>
      <td>12월31일</td>
      <td>조응준, 김양선 (각자대표이사)</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2017</td>
      <td>246720</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>피씨엘</td>
      <td>의료용품 및 기타 의약 관련제품 제조업</td>
      <td>다중 체외진단 제품, 플랫폼서비스</td>
      <td>2017-02-23</td>
      <td>12월</td>
      <td>김소연</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2017</td>
      <td>241820</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>유바이오로직스</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>경구용 콜레라 백신, 바이오의약품 수탁 연구 및 제조</td>
      <td>2017-01-24</td>
      <td>12월</td>
      <td>백영옥</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2017</td>
      <td>206650</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>비피도</td>
      <td>도시락 및 식사용 조리식품 제조업</td>
      <td>프로바이오틱스 관련 완제품 및 균주 원말 등</td>
      <td>2018-12-26</td>
      <td>12월</td>
      <td>이원범, 박명수(각자대표)</td>
      <td>홈페이지 보기</td>
      <td>강원특별자치도</td>
      <td>2018</td>
      <td>238200</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>유틸렉스</td>
      <td>기초 의약물질 제조업</td>
      <td>면역항암 세포치료제, 면역항암 항체치료제</td>
      <td>2018-12-24</td>
      <td>12월31일</td>
      <td>권병세, 유연호 (공동대표이사)</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2018</td>
      <td>263050</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>에이비엘바이오</td>
      <td>기초 의약물질 제조업</td>
      <td>항체의약품 연구개발</td>
      <td>2018-12-19</td>
      <td>12월</td>
      <td>이상훈</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2018</td>
      <td>298380</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>전진바이오팜</td>
      <td>기타 화학제품 제조업</td>
      <td>방충방향제, 유해동물피해감소제, 기생충피해감소제</td>
      <td>2018-12-14</td>
      <td>12월31일</td>
      <td>이태훈</td>
      <td>홈페이지 보기</td>
      <td>대구광역시</td>
      <td>2018</td>
      <td>110020</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>나무기술</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>가상화 및 클라우드 솔루션</td>
      <td>2018-12-11</td>
      <td>12월31일</td>
      <td>정철</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2018</td>
      <td>242040</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>티앤알바이오팹</td>
      <td>기초 의약물질 제조업</td>
      <td>생분해성 의료기기, 3D 바이오프린팅 시스템, 바이오잉크, 3D 오가노이드, 3D 세포치료제</td>
      <td>2018-11-28</td>
      <td>12월</td>
      <td>윤원수</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2018</td>
      <td>246710</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>네오펙트</td>
      <td>의료용 기기 제조업</td>
      <td>라파엘스마트글러브 외</td>
      <td>2018-11-28</td>
      <td>12월</td>
      <td>반호영</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2018</td>
      <td>290660</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>싸이토젠</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>CTC 기반 Liquid Biopsy 응용사업 및 플랫폼</td>
      <td>2018-11-22</td>
      <td>12월</td>
      <td>전병희, 안지훈 (각자대표)</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2018</td>
      <td>217330</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>파멥신</td>
      <td>의약품 제조업</td>
      <td>항체치료제</td>
      <td>2018-11-21</td>
      <td>12월31일</td>
      <td>심주엽</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2018</td>
      <td>208340</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>셀리버리</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>바이오의약품[iCP-Parkin(파킨슨병 치료제)]및 연구용 시약</td>
      <td>2018-11-09</td>
      <td>12월31일</td>
      <td>조대웅</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2018</td>
      <td>268600</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>로보티즈</td>
      <td>특수 목적용 기계 제조업</td>
      <td>솔루션(로봇 엑츄에이터 모듈과 구동 소프트웨어), 에듀테인먼트 로봇, 로봇 플랫폼</td>
      <td>2018-10-26</td>
      <td>12월</td>
      <td>김병수</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2018</td>
      <td>108490</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>옵티팜</td>
      <td>의료용품 및 기타 의약 관련제품 제조업</td>
      <td>옵티케어, 메디피그 등</td>
      <td>2018-10-26</td>
      <td>12월</td>
      <td>김현일</td>
      <td>홈페이지 보기</td>
      <td>충청북도</td>
      <td>2018</td>
      <td>153710</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>바이오솔루션</td>
      <td>기초 의약물질 제조업</td>
      <td>세포치료제, 인체조직모델 등</td>
      <td>2018-08-20</td>
      <td>12월</td>
      <td>이정선</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2018</td>
      <td>086820</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>올릭스</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>siRNA 신약 개발</td>
      <td>2018-07-18</td>
      <td>12월</td>
      <td>이동기</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2018</td>
      <td>226950</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>아이큐어</td>
      <td>의약품 제조업</td>
      <td>플라스타, 의약 및 의약외품 패취등, 마스크팩, 화장품 기초라인</td>
      <td>2018-07-12</td>
      <td>12월</td>
      <td>이영석</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2018</td>
      <td>175250</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>EDGC</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>유전체 분석 진단 서비스</td>
      <td>2018-06-26</td>
      <td>12월</td>
      <td>대표이사 이민섭</td>
      <td>홈페이지 보기</td>
      <td>인천광역시</td>
      <td>2018</td>
      <td>245620</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>유네코</td>
      <td>특수 목적용 기계 제조업</td>
      <td>SAP</td>
      <td>2018-03-15</td>
      <td>12월</td>
      <td>박동필, 김종원(각자대표)</td>
      <td>홈페이지 보기</td>
      <td>인천광역시</td>
      <td>2018</td>
      <td>064510</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>오스테오닉</td>
      <td>의료용 기기 제조업</td>
      <td>골접합 및 재건용 금속소재 및 생분해성 복합소재 기반 임플란트</td>
      <td>2018-02-22</td>
      <td>12월</td>
      <td>이동원</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2018</td>
      <td>226400</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>엔지켐생명과학</td>
      <td>기초 의약물질 제조업</td>
      <td>EC-18(신약), 원료의약품</td>
      <td>2018-02-21</td>
      <td>12월</td>
      <td>손기영</td>
      <td>홈페이지 보기</td>
      <td>충청북도</td>
      <td>2018</td>
      <td>183490</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>아시아종묘</td>
      <td>작물 재배업</td>
      <td>종자</td>
      <td>2018-02-12</td>
      <td>09월</td>
      <td>류경오</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2018</td>
      <td>154030</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>링크제니시스</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>반도체, 디스플레이, 자동화 S/W 및 시스템 테스트 자동화 솔루션 개발(XCOMPRO, XGEM, MAT)</td>
      <td>2018-02-05</td>
      <td>12월</td>
      <td>정성우</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2018</td>
      <td>219420</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>CJ 바이오사이언스</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>생명정보 플랫폼, 마이크로바이옴 분석 서비스</td>
      <td>2019-12-26</td>
      <td>12월31일</td>
      <td>천종식</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2019</td>
      <td>311690</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>브릿지바이오</td>
      <td>기초 의약물질 제조업</td>
      <td>펠리노-1 단백질 저해제, 오토택신 저해제</td>
      <td>2019-12-20</td>
      <td>12월</td>
      <td>이정규</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2019</td>
      <td>288330</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>메드팩토</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>항암제 신약개발</td>
      <td>2019-12-19</td>
      <td>12월31일</td>
      <td>김성진</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2019</td>
      <td>235980</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>신테카바이오</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>유전체 빅데이터 기반의 AI신약개발 및 정밀의료서비스</td>
      <td>2019-12-17</td>
      <td>12월</td>
      <td>정종선</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2019</td>
      <td>226330</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>제이엘케이</td>
      <td>컴퓨터 프로그래밍, 시스템 통합 및 관리업</td>
      <td>인공지능 기반 의료영상 진단 플랫폼, 인공지능 기반 산업용 X-ray 판독시스템</td>
      <td>2019-12-11</td>
      <td>12월</td>
      <td>김동민</td>
      <td>홈페이지 보기</td>
      <td>충청북도</td>
      <td>2019</td>
      <td>322510</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>티움바이오</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>특발성폐섬유증 치료제, 면역항암제, 자궁내막증치료제, 혈우병치료제</td>
      <td>2019-11-22</td>
      <td>12월31일</td>
      <td>김훈택</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2019</td>
      <td>321550</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>자비스</td>
      <td>특수 목적용 기계 제조업</td>
      <td>산업용 X-ray 검사장비(Xscan) 및 식품이물검사장비(Fscan)</td>
      <td>2019-11-15</td>
      <td>12월31일</td>
      <td>김형철</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2019</td>
      <td>254120</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>라파스</td>
      <td>기타 화학제품 제조업</td>
      <td>마이크로니들 패치 제품(의약품패치, 의료기기패치, 미용패치 등)</td>
      <td>2019-11-11</td>
      <td>12월</td>
      <td>정도현</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2019</td>
      <td>214260</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>미디어젠</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>음성인식 소프트웨어 기술개발</td>
      <td>2019-11-05</td>
      <td>12월</td>
      <td>송민규</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2019</td>
      <td>279600</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>캐리소프트</td>
      <td>영화, 비디오물, 방송프로그램 제작 및 배급업</td>
      <td>영상 콘텐츠(30.05%), 공연(29.76%), 키즈카페(17.38%), 커머스(12.77%), 라이선스 및 기타(10.04%)</td>
      <td>2019-10-29</td>
      <td>12월</td>
      <td>박창신</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2019</td>
      <td>317530</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>엔바이오니아</td>
      <td>그외 기타 제품 제조업</td>
      <td>양전하필터(정수기)</td>
      <td>2019-10-24</td>
      <td>12월</td>
      <td>한정철</td>
      <td>홈페이지 보기</td>
      <td>충청북도</td>
      <td>2019</td>
      <td>317870</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>올리패스</td>
      <td>기초 의약물질 제조업</td>
      <td>인공유전자 플랫폼(OliPass PNA) 기술을 활용한 RNA치료제 신약개발</td>
      <td>2019-09-20</td>
      <td>12월</td>
      <td>손형석, 이진한 (각자 대표이사)</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2019</td>
      <td>244460</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>라닉스</td>
      <td>반도체 제조업</td>
      <td>자동차 및 IoT 통신,보안 솔루션</td>
      <td>2019-09-18</td>
      <td>12월</td>
      <td>최승욱</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2019</td>
      <td>317120</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>나노브릭</td>
      <td>기초 화학물질 제조업</td>
      <td>보안응용제품(M-tag 및 M-pac), 보안소재제품(M-secuprint)</td>
      <td>2019-08-19</td>
      <td>12월</td>
      <td>임용택</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2019</td>
      <td>286750</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>플리토</td>
      <td>자료처리, 호스팅, 포털 및 기타 인터넷 정보매개 서비스업</td>
      <td>언어 데이터 구축 및 판매</td>
      <td>2019-07-17</td>
      <td>12월31일</td>
      <td>이정수</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2019</td>
      <td>300080</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>압타바이오</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>용역매출(50.7%), 유전자전달체(32.7%), 압타머 연구용 시약(16.6%)</td>
      <td>2019-06-12</td>
      <td>12월</td>
      <td>이수진</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2019</td>
      <td>293780</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>마이크로디지탈</td>
      <td>의료용 기기 제조업</td>
      <td>바이오 분석 시스템, 메디칼 자동화 시스템</td>
      <td>2019-06-05</td>
      <td>12월31일</td>
      <td>김경남</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2019</td>
      <td>305090</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>수젠텍</td>
      <td>의료용품 및 기타 의약 관련제품 제조업</td>
      <td>체외진단 기기 및 시약</td>
      <td>2019-05-28</td>
      <td>12월31일</td>
      <td>손미진</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2019</td>
      <td>253840</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>아모그린텍</td>
      <td>전자부품 제조업</td>
      <td>비정질 및 나노결정립을 이용한 자성부품 및 전류센서</td>
      <td>2019-03-29</td>
      <td>12월31일</td>
      <td>양성철, 김병규(각자대표)</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2019</td>
      <td>125210</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>지노믹트리</td>
      <td>의료용품 및 기타 의약 관련제품 제조업</td>
      <td>암 조기진단 제품</td>
      <td>2019-03-27</td>
      <td>12월</td>
      <td>안성환</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2019</td>
      <td>228760</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>셀리드</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>항암면역치료백신</td>
      <td>2019-02-20</td>
      <td>12월</td>
      <td>강창율</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2019</td>
      <td>299660</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>SCL사이언스</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>의료용지혈제, 밀폐제 및 접착제</td>
      <td>2019-02-01</td>
      <td>12월31일</td>
      <td>이경률, 백세연 (각자대표)</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2019</td>
      <td>246960</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>지놈앤컴퍼니</td>
      <td>기초 의약물질 제조업</td>
      <td>마이크로바이옴 기반 치료제, 화장품, 건강기능식품</td>
      <td>2020-12-23</td>
      <td>12월</td>
      <td>홍유석, 배지수, 박한수 (각자 대표이사)</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2020</td>
      <td>314130</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>석경에이티</td>
      <td>기초 화학물질 제조업</td>
      <td>바이오 및 전기전자 나노 소재</td>
      <td>2020-12-23</td>
      <td>12월</td>
      <td>임형섭</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2020</td>
      <td>357550</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>프리시젼바이오</td>
      <td>의료용 기기 제조업</td>
      <td>체외진단 기기 및 시약</td>
      <td>2020-12-22</td>
      <td>12월</td>
      <td>김한신</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2020</td>
      <td>335810</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>알체라</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>얼굴인식 AI, 이상상황 감지 AI 등</td>
      <td>2020-12-21</td>
      <td>12월31일</td>
      <td>황영규</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2020</td>
      <td>347860</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>엔젠바이오</td>
      <td>그외 기타 전문, 과학 및 기술 서비스업</td>
      <td>유전체 분야 진단시약 제조 및 유전체 분야 소프트웨어 연구,개발,판매</td>
      <td>2020-12-10</td>
      <td>12월31일</td>
      <td>최대출</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2020</td>
      <td>354200</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>퀀타매트릭스</td>
      <td>의료용 기기 제조업</td>
      <td>신속항균제검사 장비 및 키트</td>
      <td>2020-12-09</td>
      <td>12월</td>
      <td>권성훈</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2020</td>
      <td>317690</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>클리노믹스</td>
      <td>의료용품 및 기타 의약 관련제품 제조업</td>
      <td>Geno Series, CD-PRIME, Cancer Prime</td>
      <td>2020-12-04</td>
      <td>12월31일</td>
      <td>백서현</td>
      <td>홈페이지 보기</td>
      <td>울산광역시</td>
      <td>2020</td>
      <td>352770</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>고바이오랩</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>마이크로바이옴 치료제 및 건강기능식품</td>
      <td>2020-11-18</td>
      <td>12월</td>
      <td>고광표</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2020</td>
      <td>348150</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>센코</td>
      <td>전자부품 제조업</td>
      <td>가스센서 및 모듈, 휴대용 및 고정형 가스검지기, 악취 & 미세먼지 모니터링 시스템</td>
      <td>2020-10-29</td>
      <td>12월</td>
      <td>하승철</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2020</td>
      <td>347000</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>바이브컴퍼니</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>소셜 빅데이터 기반 인공지능 서비스 (소셜메트릭스), 문제 해결 솔루션 (AI Solver)</td>
      <td>2020-10-28</td>
      <td>12월</td>
      <td>김경서</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2020</td>
      <td>301300</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>미코바이오메드</td>
      <td>의료용 기기 제조업</td>
      <td>체외진단용 의료기기</td>
      <td>2020-10-22</td>
      <td>12월</td>
      <td>정민영</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2020</td>
      <td>214610</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>피플바이오</td>
      <td>의료용품 및 기타 의약 관련제품 제조업</td>
      <td>올리고머화 베타-아밀로이드 검사제품(알츠하이머병 진단)</td>
      <td>2020-10-19</td>
      <td>12월31일</td>
      <td>강성민</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2020</td>
      <td>304840</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>넥스틴</td>
      <td>특수 목적용 기계 제조업</td>
      <td>반도체 전공정용 패턴결함 검사장비(AEGIS 등)</td>
      <td>2020-10-08</td>
      <td>12월</td>
      <td>박태훈</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2020</td>
      <td>348210</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>박셀바이오</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>항암면역세포치료제(자연살해세포, 수지상세포, CAR-T 및 인터루킨 기반 항암제)</td>
      <td>2020-09-22</td>
      <td>12월31일</td>
      <td>이제중 (단독 대표이사)</td>
      <td>홈페이지 보기</td>
      <td>전라남도</td>
      <td>2020</td>
      <td>323990</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>압타머사이언스</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>압타머기반 신약개발 및 진단제품 개발</td>
      <td>2020-09-16</td>
      <td>12월</td>
      <td>한동일</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2020</td>
      <td>291650</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>이오플로우</td>
      <td>의료용 기기 제조업</td>
      <td>웨어러블 인슐린펌프</td>
      <td>2020-09-14</td>
      <td>12월</td>
      <td>김재진</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2020</td>
      <td>294090</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>셀레믹스</td>
      <td>기초 의약물질 제조업</td>
      <td>타겟캡처키트</td>
      <td>2020-08-21</td>
      <td>12월</td>
      <td>김효기, 이용훈</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2020</td>
      <td>331920</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>제놀루션</td>
      <td>기초 의약물질 제조업</td>
      <td>핵산추출기기 및 시약, RNAi 사업 등</td>
      <td>2020-07-24</td>
      <td>12월</td>
      <td>김기옥</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2020</td>
      <td>225220</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>솔트룩스</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>인공지능 및 빅데이터 소프트웨어</td>
      <td>2020-07-23</td>
      <td>12월</td>
      <td>이경일</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2020</td>
      <td>304100</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>소마젠</td>
      <td>그외 기타 전문, 과학 및 기술 서비스업</td>
      <td>유전체 분석 서비스 (NGS, CES 등)</td>
      <td>2020-07-13</td>
      <td>12월31일</td>
      <td>홍수</td>
      <td>홈페이지 보기</td>
      <td>미국</td>
      <td>2020</td>
      <td>USA15</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>젠큐릭스</td>
      <td>의료용품 및 기타 의약 관련제품 제조업</td>
      <td>유방암 예후진단 및 폐암/대장암 동반진단 제품/검사서비스</td>
      <td>2020-06-25</td>
      <td>12월31일</td>
      <td>조상래</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2020</td>
      <td>229000</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>에스씨엠생명과학</td>
      <td>의약품 제조업</td>
      <td>세포치료제</td>
      <td>2020-06-17</td>
      <td>12월</td>
      <td>송기령</td>
      <td>홈페이지 보기</td>
      <td>인천광역시</td>
      <td>2020</td>
      <td>298060</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>카이노스메드</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>뇌질환치료제, 항암제, 항바이러스제 등</td>
      <td>2020-06-08</td>
      <td>12월31일</td>
      <td>이기섭</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2020</td>
      <td>284620</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>레몬</td>
      <td>화학섬유 제조업</td>
      <td>EMI Shield Can, 나노멤브레인 등</td>
      <td>2020-02-28</td>
      <td>12월</td>
      <td>김광진</td>
      <td>홈페이지 보기</td>
      <td>경상북도</td>
      <td>2020</td>
      <td>294140</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>서남</td>
      <td>기타 전기장비 제조업</td>
      <td>고온초전도선재</td>
      <td>2020-02-20</td>
      <td>12월</td>
      <td>문승현</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2020</td>
      <td>294630</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>툴젠</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>유전자교정 플랫폼 관련 제품</td>
      <td>2021-12-10</td>
      <td>12월</td>
      <td>이병화</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2021</td>
      <td>199800</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>마음AI</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>종합 인공지능 엔진 및 플랫폼</td>
      <td>2021-11-23</td>
      <td>12월</td>
      <td>유태준</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2021</td>
      <td>377480</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>지오엘리먼트</td>
      <td>전자부품 제조업</td>
      <td>센서, 캐니스터</td>
      <td>2021-11-11</td>
      <td>12월</td>
      <td>신현국</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2021</td>
      <td>311320</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>스카이월드와이드</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>그래프데이터베이스, 그래프분석서비스</td>
      <td>2021-11-10</td>
      <td>12월</td>
      <td>신재혁</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2021</td>
      <td>357880</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>지니너스</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>NGS기반 조직생검 암유전체 동반진단(CancerSCAN), 액체생검 암유전체 동반진단(LiquidSCAN), 단일세포분석(Celinus) 등</td>
      <td>2021-11-08</td>
      <td>12월</td>
      <td>박웅양</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2021</td>
      <td>389030</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>차백신연구소</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>백신 및 면역증강제 등</td>
      <td>2021-10-22</td>
      <td>12월</td>
      <td>염정선</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2021</td>
      <td>261780</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>에이비온</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>표적 항암제, 바이오 베터 신약</td>
      <td>2021-09-08</td>
      <td>12월</td>
      <td>신영기</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2021</td>
      <td>203400</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>바이젠셀</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>면역세포치료제 (면역항암제, 면역조절치료제 등)</td>
      <td>2021-08-25</td>
      <td>12월</td>
      <td>김태규</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2021</td>
      <td>308080</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>딥노이드</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>의료 인공지능플랫폼, 인공지능 임상의사결정 시스템</td>
      <td>2021-08-17</td>
      <td>12월31일</td>
      <td>최우식</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2021</td>
      <td>315640</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>원티드랩</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>채용 플랫폼</td>
      <td>2021-08-11</td>
      <td>12월</td>
      <td>이복기</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2021</td>
      <td>376980</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>비트맥스</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>AR 개발 플랫폼/AR솔루션</td>
      <td>2021-07-27</td>
      <td>12월31일</td>
      <td>홍상혁</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2021</td>
      <td>377030</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>큐라클</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>혈관질환치료제 등</td>
      <td>2021-07-22</td>
      <td>12월</td>
      <td>유재현</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2021</td>
      <td>365270</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>오비고</td>
      <td>컴퓨터 프로그래밍, 시스템 통합 및 관리업</td>
      <td>스마트카 소프트웨어 플랫폼</td>
      <td>2021-07-13</td>
      <td>12월</td>
      <td>황도연</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2021</td>
      <td>352910</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>아모센스</td>
      <td>전자부품 제조업</td>
      <td>무선충전 차폐시트</td>
      <td>2021-06-25</td>
      <td>12월31일</td>
      <td>김인응</td>
      <td>홈페이지 보기</td>
      <td>충청남도</td>
      <td>2021</td>
      <td>357580</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>라온테크</td>
      <td>특수 목적용 기계 제조업</td>
      <td>반도체 및 FPD용 로봇시스템</td>
      <td>2021-06-17</td>
      <td>12월</td>
      <td>김원경</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2021</td>
      <td>232680</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>진시스템</td>
      <td>의료용 기기 제조업</td>
      <td>분자진단기반 플랫폼 개발 및 제조·판매</td>
      <td>2021-05-26</td>
      <td>12월</td>
      <td>서유진</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2021</td>
      <td>363250</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>삼영에스앤씨</td>
      <td>전자부품 제조업</td>
      <td>칩형 온습도센서, 상대습도센서, 미세먼지센서, 공기질 통합센서 노드 및 트랜스미터</td>
      <td>2021-05-21</td>
      <td>12월</td>
      <td>박상익</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2021</td>
      <td>361670</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>샘씨엔에스</td>
      <td>전자부품 제조업</td>
      <td>세라믹 STF(다층 세라믹 기판)</td>
      <td>2021-05-20</td>
      <td>12월</td>
      <td>최정혁(단독 대표이사)</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2021</td>
      <td>252990</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>해성에어로보틱스</td>
      <td>기타 금속 가공제품 제조업</td>
      <td>기어 및 동력전달장치</td>
      <td>2021-04-21</td>
      <td>12월</td>
      <td>이건복,이정훈(각자 대표)</td>
      <td>홈페이지 보기</td>
      <td>인천광역시</td>
      <td>2021</td>
      <td>059270</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>자이언트스텝</td>
      <td>영화, 비디오물, 방송프로그램 제작 및 배급업</td>
      <td>광고VFX, 영상VFX 및 리얼타임 콘텐츠 제작</td>
      <td>2021-03-24</td>
      <td>12월</td>
      <td>하승봉, 이지철</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2021</td>
      <td>289220</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>제노코</td>
      <td>통신 및 방송 장비 제조업</td>
      <td>위성탑재체, 위성운용국, 항공전자 등</td>
      <td>2021-03-24</td>
      <td>12월</td>
      <td>유태삼</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2021</td>
      <td>361390</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>라이프시맨틱스</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>소프트웨어(개인건강기록 플랫폼,진료기록번역플랫폼,질병분류기호 검색) 개발,공급/의료기기 도매/자문,컨설팅/전자상거래,통신판매</td>
      <td>2021-03-23</td>
      <td>12월</td>
      <td>최광수</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2021</td>
      <td>347700</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>네오이뮨텍</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>면역항암제</td>
      <td>2021-03-16</td>
      <td>12월</td>
      <td>Luke Yun Suk Oh</td>
      <td>홈페이지 보기</td>
      <td>미국</td>
      <td>2021</td>
      <td>USA14</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>프레스티지바이오로직스</td>
      <td>의약품 제조업</td>
      <td>바이오시밀러 제조</td>
      <td>2021-03-11</td>
      <td>12월31일</td>
      <td>현덕훈</td>
      <td>홈페이지 보기</td>
      <td>충청북도</td>
      <td>2021</td>
      <td>334970</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>나노씨엠에스</td>
      <td>전자부품 제조업</td>
      <td>근적외선 흡수/반사 안료, 자외선 유기형광 안료, 적외선 발광체</td>
      <td>2021-03-09</td>
      <td>12월31일</td>
      <td>신동근</td>
      <td>홈페이지 보기</td>
      <td>충청남도</td>
      <td>2021</td>
      <td>247660</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>뷰노</td>
      <td>자료처리, 호스팅, 포털 및 기타 인터넷 정보매개 서비스업</td>
      <td>뷰노메드 음성솔루션, 뷰노메드 영상솔루션, 기타 솔루션 등</td>
      <td>2021-02-26</td>
      <td>12월</td>
      <td>이예하</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2021</td>
      <td>338220</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>씨이랩</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>빅데이터플랫폼</td>
      <td>2021-02-24</td>
      <td>12월31일</td>
      <td>이우영</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2021</td>
      <td>189330</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>피엔에이치테크</td>
      <td>기초 화학물질 제조업</td>
      <td>OLED 소재</td>
      <td>2021-02-16</td>
      <td>12월</td>
      <td>현서용, 송영권</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2021</td>
      <td>239890</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>레인보우로보틱스</td>
      <td>특수 목적용 기계 제조업</td>
      <td>협동로봇, 천문마운트시스템, 이족보행로봇 등</td>
      <td>2021-02-03</td>
      <td>12월31일</td>
      <td>이정호</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2021</td>
      <td>277810</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>아티스트유나이티드</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>빅데이터/인공지능 마케팅플랫폼 및 데이터플랫폼</td>
      <td>2021-02-03</td>
      <td>12월</td>
      <td>황경주</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2021</td>
      <td>321820</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>SAMG엔터</td>
      <td>영화, 비디오물, 방송프로그램 제작 및 배급업</td>
      <td>애니메이션 IP 기획 및 관련 제품 제작</td>
      <td>2022-12-06</td>
      <td>12월</td>
      <td>김수훈</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2022</td>
      <td>419530</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>인벤티지랩</td>
      <td>의약품 제조업</td>
      <td>마이크로/나노 입자 기반 약물전달 플랫폼 및 관련 제품</td>
      <td>2022-11-22</td>
      <td>12월</td>
      <td>김주희</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2022</td>
      <td>389470</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>엔젯</td>
      <td>특수 목적용 기계 제조업</td>
      <td>EHD 잉크젯 프린터, EHD 코터</td>
      <td>2022-11-18</td>
      <td>12월</td>
      <td>변도영</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2022</td>
      <td>419080</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>뉴로메카</td>
      <td>특수 목적용 기계 제조업</td>
      <td>협동로봇, 협동로봇 자동화 플랫폼, 로봇제어기 등</td>
      <td>2022-11-04</td>
      <td>12월</td>
      <td>박종훈</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2022</td>
      <td>348340</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>플라즈맵</td>
      <td>의료용 기기 제조업</td>
      <td>플라즈마 멸균기 및 표면처리기기</td>
      <td>2022-10-21</td>
      <td>12월31일</td>
      <td>김형민(단독 대표이사)</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2022</td>
      <td>405000</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>핀텔</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>AI 영상 분석 솔루션 및 소프트웨어</td>
      <td>2022-10-20</td>
      <td>12월31일</td>
      <td>김동기</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2022</td>
      <td>291810</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>샤페론</td>
      <td>기초 의약물질 제조업</td>
      <td>합성신약 및 항체치료제신약 기술제품 및 기술이전</td>
      <td>2022-10-19</td>
      <td>12월</td>
      <td>성승용</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2022</td>
      <td>378800</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>에스비비테크</td>
      <td>일반 목적용 기계 제조업</td>
      <td>베어링, 감속기</td>
      <td>2022-10-17</td>
      <td>12월</td>
      <td>류재완, 송진웅(각자 대표이사)</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2022</td>
      <td>389500</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>선바이오</td>
      <td>의약품 제조업</td>
      <td>PEG유도체 제품 (62%), 기술료수입 (38%)</td>
      <td>2022-10-05</td>
      <td>12월31일</td>
      <td>노광</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2022</td>
      <td>067370</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>아이씨에이치</td>
      <td>그외 기타 제품 제조업</td>
      <td>스마트기기용 필름형 안테나</td>
      <td>2022-07-29</td>
      <td>12월</td>
      <td>김영훈</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2022</td>
      <td>368600</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>에이프릴바이오</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>항체의약품 및 재조합 단백질 의약품</td>
      <td>2022-07-28</td>
      <td>12월31일</td>
      <td>차상훈</td>
      <td>홈페이지 보기</td>
      <td>강원특별자치도</td>
      <td>2022</td>
      <td>397030</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>루닛</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>Lunit INSIGHT</td>
      <td>2022-07-21</td>
      <td>12월</td>
      <td>서범석</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2022</td>
      <td>328130</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>와이씨켐</td>
      <td>기타 화학제품 제조업</td>
      <td>반도체 및 디스플레이용 화학소재</td>
      <td>2022-07-14</td>
      <td>12월</td>
      <td>이성일, 이승훈</td>
      <td>홈페이지 보기</td>
      <td>경상북도</td>
      <td>2022</td>
      <td>112290</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>코난테크놀로지</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>AI 기반 검색엔진(Konan Search), AI기반 영상인식 솔루션(D: Watcher)</td>
      <td>2022-07-07</td>
      <td>12월31일</td>
      <td>김영섬</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2022</td>
      <td>402030</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>넥스트칩</td>
      <td>반도체 제조업</td>
      <td>차량 및 자율주행차용 비메모리 반도체(ISP, AHD, ADAS/AD)</td>
      <td>2022-07-01</td>
      <td>12월31일</td>
      <td>김경수</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2022</td>
      <td>396270</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>원텍</td>
      <td>의료용 기기 제조업</td>
      <td>피부, 미용 의료기기 제조 및 판매</td>
      <td>2022-06-30</td>
      <td>12월31일</td>
      <td>김종원, 김정현</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2022</td>
      <td>336570</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>보로노이</td>
      <td>기초 의약물질 제조업</td>
      <td>표적치료제</td>
      <td>2022-06-24</td>
      <td>12월31일</td>
      <td>김현태</td>
      <td>홈페이지 보기</td>
      <td>인천광역시</td>
      <td>2022</td>
      <td>310210</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>레이저쎌</td>
      <td>특수 목적용 기계 제조업</td>
      <td>에어리어 레이저솔루션, LSR, LCB, LSB, BSOM 등</td>
      <td>2022-06-24</td>
      <td>12월</td>
      <td>안건준</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2022</td>
      <td>412350</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>비큐AI</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>아이서퍼, 위고몬 등</td>
      <td>2022-06-20</td>
      <td>12월</td>
      <td>임경환</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2022</td>
      <td>148780</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>하이딥</td>
      <td>반도체 제조업</td>
      <td>시스템반도체 IC설계</td>
      <td>2022-05-12</td>
      <td>12월31일</td>
      <td>고범규</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2022</td>
      <td>365590</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>모아데이타</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>인공지능 기반 ICT 시스템 이상탐지 및 예측 솔루션</td>
      <td>2022-03-10</td>
      <td>12월</td>
      <td>한상진</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2022</td>
      <td>288980</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>노을</td>
      <td>의료용 기기 제조업</td>
      <td>융복합 체외진단 플랫폼</td>
      <td>2022-03-03</td>
      <td>12월</td>
      <td>임찬양(단독 대표이사)</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2022</td>
      <td>376930</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>풍원정밀</td>
      <td>전자부품 제조업</td>
      <td>OLED 증착용 Metal Mask</td>
      <td>2022-02-28</td>
      <td>12월</td>
      <td>유명훈</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2022</td>
      <td>371950</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>퓨런티어</td>
      <td>측정, 시험, 항해, 제어 및 기타 정밀기기 제조업; 광학기기 제외</td>
      <td>전장카메라모듈장비, 모바일카메라모듈장비, PC및 광원</td>
      <td>2022-02-23</td>
      <td>12월</td>
      <td>오상근</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2022</td>
      <td>370090</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>바이오에프디엔씨</td>
      <td>기초 의약물질 제조업</td>
      <td>식물세포 유래 유효물질 및 약리물질</td>
      <td>2022-02-21</td>
      <td>12월</td>
      <td>모상현, 정대현</td>
      <td>홈페이지 보기</td>
      <td>인천광역시</td>
      <td>2022</td>
      <td>251120</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>스코넥</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>XR 교육/훈련 시스템, VR 게임 콘텐츠 등</td>
      <td>2022-02-04</td>
      <td>12월</td>
      <td>황대실</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2022</td>
      <td>276040</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>이지트로닉스</td>
      <td>전동기, 발전기 및 전기 변환 · 공급 · 제어 장치 제조업</td>
      <td>전력변환장치</td>
      <td>2022-02-04</td>
      <td>12월31일</td>
      <td>강찬호</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2022</td>
      <td>377330</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>애드바이오텍</td>
      <td>의약품 제조업</td>
      <td>동물용약품,영양제,단미사료(네오폐녹스),보조사료 제조,도매/식품첨가물,화장품 도소매,무역</td>
      <td>2022-01-24</td>
      <td>12월</td>
      <td>정홍걸</td>
      <td>홈페이지 보기</td>
      <td>강원특별자치도</td>
      <td>2022</td>
      <td>179530</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>와이바이오로직스</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>항체의약품 및 항체후보물질 연구개발</td>
      <td>2023-12-05</td>
      <td>12월</td>
      <td>박영우, 장우익</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2023</td>
      <td>338840</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>에이텀</td>
      <td>전자부품 제조업</td>
      <td>평판형 트랜스</td>
      <td>2023-12-01</td>
      <td>06월</td>
      <td>한택수</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2023</td>
      <td>355690</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>그린리소스</td>
      <td>반도체 제조업</td>
      <td>반도체 및 디스플레이 장비 보호코팅 및 소재</td>
      <td>2023-11-24</td>
      <td>12월</td>
      <td>이종수,이종범(공동대표이사)</td>
      <td>홈페이지 보기</td>
      <td>인천광역시</td>
      <td>2023</td>
      <td>402490</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>큐로셀</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>CAR-T 세포치료제</td>
      <td>2023-11-09</td>
      <td>12월</td>
      <td>김건수</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2023</td>
      <td>372320</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>컨텍</td>
      <td>컴퓨터 프로그래밍, 시스템 통합 및 관리업</td>
      <td>지상국 시스템 엔지니어링 솔루션, 위성영상 생성을 위한 데이터처리 솔루션</td>
      <td>2023-11-09</td>
      <td>12월</td>
      <td>이성희</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2023</td>
      <td>451760</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>쏘닉스</td>
      <td>반도체 제조업</td>
      <td>RF필터 파운드리</td>
      <td>2023-11-07</td>
      <td>12월</td>
      <td>양형국</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2023</td>
      <td>088280</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>세니젠</td>
      <td>그외 기타 제품 제조업</td>
      <td>Genelix, Genext, Geneka 등</td>
      <td>2023-11-03</td>
      <td>12월</td>
      <td>박정웅</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2023</td>
      <td>188260</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>퀄리타스반도체</td>
      <td>반도체 제조업</td>
      <td>초고속 통신용 반도체 IP</td>
      <td>2023-10-27</td>
      <td>12월</td>
      <td>김두호</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2023</td>
      <td>432720</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>아이엠티</td>
      <td>특수 목적용 기계 제조업</td>
      <td>건식세정 장비 및 EUV Mask Baking Laser</td>
      <td>2023-10-10</td>
      <td>12월</td>
      <td>최재성</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2023</td>
      <td>451220</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>코어라인소프트</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>의료영상 진단보조 솔루션</td>
      <td>2023-09-18</td>
      <td>12월31일</td>
      <td>김진국</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2023</td>
      <td>384470</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>크라우드웍스</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>인공지능 데이터 구축 서비스</td>
      <td>2023-08-31</td>
      <td>12월</td>
      <td>김우승</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2023</td>
      <td>355390</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>시큐레터</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>SLE(이메일 보안), SLF(파일 보안)</td>
      <td>2023-08-24</td>
      <td>12월</td>
      <td>임차성</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2023</td>
      <td>418250</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>스마트레이더시스템</td>
      <td>측정, 시험, 항해, 제어 및 기타 정밀기기 제조업; 광학기기 제외</td>
      <td>모빌리티 및 비모빌리티용 4D이미징레이다</td>
      <td>2023-08-22</td>
      <td>12월31일</td>
      <td>김용환</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2023</td>
      <td>424960</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>큐리옥스바이오시스템즈</td>
      <td>의료용 기기 제조업</td>
      <td>세포 전처리 자동화기기 등</td>
      <td>2023-08-10</td>
      <td>12월</td>
      <td>김남용</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2023</td>
      <td>445680</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>파두</td>
      <td>반도체 제조업</td>
      <td>SSD 컨트롤러</td>
      <td>2023-08-07</td>
      <td>12월</td>
      <td>이지효,남이현</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2023</td>
      <td>440110</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>시지트로닉스</td>
      <td>반도체 제조업</td>
      <td>특화반도체 소자</td>
      <td>2023-08-03</td>
      <td>12월</td>
      <td>심규환 (단독 대표이사)</td>
      <td>홈페이지 보기</td>
      <td>전북특별자치도</td>
      <td>2023</td>
      <td>429270</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>파로스아이바이오</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>PHI-101 급성골수성백혈병 치료제 및 재발성난소암 치료제</td>
      <td>2023-07-27</td>
      <td>12월31일</td>
      <td>윤정혁</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2023</td>
      <td>388870</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>버넥트</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>산업용 XR 솔루션</td>
      <td>2023-07-26</td>
      <td>12월</td>
      <td>하태진</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2023</td>
      <td>438700</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>와이랩</td>
      <td>영화, 비디오물, 방송프로그램 제작 및 배급업</td>
      <td>만화출판물의 제작 및 영상물 제작</td>
      <td>2023-07-20</td>
      <td>12월</td>
      <td>심준경</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2023</td>
      <td>432430</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>센서뷰</td>
      <td>절연선 및 케이블 제조업</td>
      <td>T&M 케이블, 초소형 전송선로</td>
      <td>2023-07-19</td>
      <td>12월</td>
      <td>김병남</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2023</td>
      <td>321370</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>이노시뮬레이션</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>스마트 모빌리티 시뮬레이터, XR 가상훈련 시스템 등</td>
      <td>2023-07-06</td>
      <td>12월</td>
      <td>조준희</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2023</td>
      <td>274400</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>오픈놀</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>미니인턴플랫폼(커리어 및 채용 플랫폼)</td>
      <td>2023-06-30</td>
      <td>12월31일</td>
      <td>권인택</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2023</td>
      <td>440320</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>프로티아</td>
      <td>의료용 기기 제조업</td>
      <td>알레르기 진단 제품</td>
      <td>2023-06-16</td>
      <td>12월</td>
      <td>임국진</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2023</td>
      <td>303360</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>큐라티스</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>백신 및 면역증강제 개발제조업, CMO/CDMO</td>
      <td>2023-06-15</td>
      <td>12월</td>
      <td>김성준</td>
      <td>홈페이지 보기</td>
      <td>충청북도</td>
      <td>2023</td>
      <td>348080</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>씨유박스</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>AI얼굴인식 시스템, AI얼굴인증 솔루션, AI 객체인식 솔루션, AI데이터 플랫폼</td>
      <td>2023-05-19</td>
      <td>12월</td>
      <td>남운성</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2023</td>
      <td>340810</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>모니터랩</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>웹방화벽,유해사이트솔루션,가시성SSL 솔루션, SASE플랫폼기반 SECaaS</td>
      <td>2023-05-19</td>
      <td>12월</td>
      <td>이광후</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2023</td>
      <td>434480</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>에스바이오메딕스</td>
      <td>의약품 제조업</td>
      <td>줄기세포 치료제 연구 및 개발</td>
      <td>2023-05-04</td>
      <td>12월</td>
      <td>강세일</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2023</td>
      <td>304360</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>마이크로투나노</td>
      <td>반도체 제조업</td>
      <td>메모리 테스트용 프로브 카드</td>
      <td>2023-04-26</td>
      <td>12월</td>
      <td>황규호</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2023</td>
      <td>424980</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>지아이이노베이션</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>면역항암제 및 알레르기 치료제</td>
      <td>2023-03-30</td>
      <td>12월</td>
      <td>이병건, 홍준호(각자대표이사)</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2023</td>
      <td>358570</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>라온텍</td>
      <td>전자부품 제조업</td>
      <td>마이크로디스플레이, 컨트롤러 IC</td>
      <td>2023-03-09</td>
      <td>12월</td>
      <td>김보은</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2023</td>
      <td>418420</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>파인메딕스</td>
      <td>의료용 기기 제조업</td>
      <td>인젝터, 스네어, 나이프, 포셉 등 내시경용 시술기구</td>
      <td>2024-12-26</td>
      <td>12월</td>
      <td>전성우, 김성철</td>
      <td>홈페이지 보기</td>
      <td>대구광역시</td>
      <td>2024</td>
      <td>387570</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>엠에프씨</td>
      <td>기초 의약물질 제조업</td>
      <td>원료의약품(API) 및 핵심소재</td>
      <td>2024-12-26</td>
      <td>12월</td>
      <td>황성관</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2024</td>
      <td>432980</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>쓰리에이로직스</td>
      <td>반도체 제조업</td>
      <td>NFC/IoT SoC 및 모듈</td>
      <td>2024-12-24</td>
      <td>12월</td>
      <td>박광범, 이평한</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2024</td>
      <td>177900</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>온코닉테라퓨틱스</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>자큐보정(Zastaprazan, 소화기질환 신약), Nesuparib(표적항암제 신약)</td>
      <td>2024-12-19</td>
      <td>12월</td>
      <td>김존</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2024</td>
      <td>476060</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>온코크로스</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>AI플랫폼 기반 신약개발 용역서비스</td>
      <td>2024-12-18</td>
      <td>12월</td>
      <td>김이랑</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2024</td>
      <td>382150</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>유디엠텍</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>PLC eXpert, OPTRA Black-box, OPTRA Tracker</td>
      <td>2024-11-20</td>
      <td>12월</td>
      <td>왕지남</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2024</td>
      <td>389680</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>쓰리빌리언</td>
      <td>의료용 기기 제조업</td>
      <td>유전체 분석 기반 희귀 유전질환 진단 검사 서비스</td>
      <td>2024-11-14</td>
      <td>12월</td>
      <td>금창원</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2024</td>
      <td>394800</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>에어레인</td>
      <td>일반 목적용 기계 제조업</td>
      <td>기체분리막 모듈 및 시스템</td>
      <td>2024-11-08</td>
      <td>12월</td>
      <td>하성용</td>
      <td>홈페이지 보기</td>
      <td>충청북도</td>
      <td>2024</td>
      <td>163280</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>토모큐브</td>
      <td>사진장비 및 광학기기 제조업</td>
      <td>홀로토모그래피 HT-X1, HT-2H</td>
      <td>2024-11-07</td>
      <td>12월</td>
      <td>박용근, 홍기현</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2024</td>
      <td>475960</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>에이치이엠파마</td>
      <td>자연과학 및 공학 연구개발업</td>
      <td>맞춤형 헬스케어, LBP 디스커버리 플랫폼</td>
      <td>2024-11-05</td>
      <td>12월</td>
      <td>지요셉</td>
      <td>홈페이지 보기</td>
      <td>경상북도</td>
      <td>2024</td>
      <td>376270</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>클로봇</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>로봇 소프트웨어(카멜레온, 크롬스)</td>
      <td>2024-10-28</td>
      <td>12월</td>
      <td>각자 대표이사 김창구, 김경필</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2024</td>
      <td>466100</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>웨이비스</td>
      <td>반도체 제조업</td>
      <td>GaN RF 칩, 패키지 트랜지스터, 모듈 등</td>
      <td>2024-10-25</td>
      <td>12월31일</td>
      <td>한민석</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2024</td>
      <td>289930</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>씨메스</td>
      <td>특수 목적용 기계 제조업</td>
      <td>AI 기반 로봇 솔루션 및 3D 비전 솔루션</td>
      <td>2024-10-24</td>
      <td>12월</td>
      <td>이성호</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2024</td>
      <td>475400</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>루미르</td>
      <td>항공기,우주선 및 부품 제조업</td>
      <td>인공위성 시스템 및 전장품, 위성 영상 및 정보</td>
      <td>2024-10-21</td>
      <td>12월</td>
      <td>남명용</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2024</td>
      <td>474170</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>셀비온</td>
      <td>의약품 제조업</td>
      <td>셀비온그린주, 셀비온메브로페닌주, 도페정 등</td>
      <td>2024-10-16</td>
      <td>12월31일</td>
      <td>김권</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2024</td>
      <td>308430</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>아이언디바이스</td>
      <td>반도체 제조업</td>
      <td>스마트폰용 오디오 앰프 반도체 Soc</td>
      <td>2024-09-23</td>
      <td>12월</td>
      <td>박기태</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2024</td>
      <td>464500</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>이엔셀</td>
      <td>기초 의약물질 제조업</td>
      <td>첨단바이오의약품 위탁개발생산(CDMO) 서비스 / 차세대 세포,유전자 치료제</td>
      <td>2024-08-23</td>
      <td>12월31일</td>
      <td>장종욱</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2024</td>
      <td>456070</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>넥스트바이오메디컬</td>
      <td>의료용 기기 제조업</td>
      <td>내시경용 지혈재, 혈관색전 미립구</td>
      <td>2024-08-20</td>
      <td>12월31일</td>
      <td>이돈행</td>
      <td>홈페이지 보기</td>
      <td>인천광역시</td>
      <td>2024</td>
      <td>389650</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>케이쓰리아이</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>XR 실감형콘텐츠</td>
      <td>2024-08-20</td>
      <td>12월</td>
      <td>이재영</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2024</td>
      <td>431190</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>뱅크웨어글로벌</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>국내외 은행 및 금융기업 대상 코어뱅킹 소프트웨어</td>
      <td>2024-08-12</td>
      <td>12월</td>
      <td>이경조, 이은중</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2024</td>
      <td>199480</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>아이빔테크놀로지</td>
      <td>사진장비 및 광학기기 제조업</td>
      <td>생체현미경, CRO 서비스</td>
      <td>2024-08-06</td>
      <td>12월</td>
      <td>김필한</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2024</td>
      <td>460470</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>피앤에스미캐닉스</td>
      <td>의료용 기기 제조업</td>
      <td>보행재활로봇 시스템</td>
      <td>2024-07-31</td>
      <td>12월</td>
      <td>박광훈</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2024</td>
      <td>460940</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>엑셀세라퓨틱스</td>
      <td>기초 의약물질 제조업</td>
      <td>CellCor SFD/CD(세포배양배지)</td>
      <td>2024-07-15</td>
      <td>12월</td>
      <td>이의일</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2024</td>
      <td>373110</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>하스</td>
      <td>의료용품 및 기타 의약 관련제품 제조업</td>
      <td>리튬디실리케이트 수복소재(Amber block, Amber Ingot 등), 지르코니아 유치관</td>
      <td>2024-07-03</td>
      <td>12월</td>
      <td>김용수</td>
      <td>홈페이지 보기</td>
      <td>강원특별자치도</td>
      <td>2024</td>
      <td>450330</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>이노스페이스</td>
      <td>항공기,우주선 및 부품 제조업</td>
      <td>소형발사체, 로켓추진기관, 과학로켓, 시험평가용역</td>
      <td>2024-07-02</td>
      <td>12월</td>
      <td>김수종</td>
      <td>홈페이지 보기</td>
      <td>세종특별자치시</td>
      <td>2024</td>
      <td>462350</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>에이치브이엠</td>
      <td>1차 비철금속 제조업</td>
      <td>Ni계 합금, Fe계 합금, 스퍼터링타겟, Cu계 합금 등</td>
      <td>2024-06-28</td>
      <td>12월</td>
      <td>문승호</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2024</td>
      <td>295310</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>에스오에스랩</td>
      <td>측정, 시험, 항해, 제어 및 기타 정밀기기 제조업; 광학기기 제외</td>
      <td>산업용 및 차량용 라이다(LiDAR)</td>
      <td>2024-06-25</td>
      <td>12월</td>
      <td>정지성</td>
      <td>홈페이지 보기</td>
      <td>광주광역시</td>
      <td>2024</td>
      <td>464080</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>한중엔시에스</td>
      <td>전동기, 발전기 및 전기 변환 · 공급 · 제어 장치 제조업</td>
      <td>수냉식 냉각시스템 ESS Parts, 공랭식 ESS Module Parts, EV Module 및 내연기관 Parts</td>
      <td>2024-06-24</td>
      <td>12월</td>
      <td>김환식</td>
      <td>홈페이지 보기</td>
      <td>경상북도</td>
      <td>2024</td>
      <td>107640</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>씨어스테크놀로지</td>
      <td>의료용 기기 제조업</td>
      <td>심전도검사솔루션 입원환자모니터링솔루션</td>
      <td>2024-06-19</td>
      <td>12월</td>
      <td>이영신</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2024</td>
      <td>458870</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>라메디텍</td>
      <td>의료용 기기 제조업</td>
      <td>초소형 레이저 의료기기  및 미용기기</td>
      <td>2024-06-17</td>
      <td>12월</td>
      <td>최종석</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2024</td>
      <td>462510</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>오름테라퓨틱</td>
      <td>기초 의약물질 제조업</td>
      <td>항체약물접합체(ADC) 단백질 분해제(TPD) 연구 개발</td>
      <td>2025-02-14</td>
      <td>12월</td>
      <td>이승주</td>
      <td>홈페이지 보기</td>
      <td>대전광역시</td>
      <td>2025</td>
      <td>475830</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>아이에스티이</td>
      <td>반도체 제조업</td>
      <td>반도체 제조용 장비</td>
      <td>2025-02-12</td>
      <td>12월</td>
      <td>조창현</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2025</td>
      <td>212710</td>
      <td>혁신기술</td>
    </tr>
    <tr>
      <td>아이지넷</td>
      <td>기타 정보 서비스업</td>
      <td>보험 서비스 어플리케이션, 기업용 보험 솔루션</td>
      <td>2025-02-04</td>
      <td>12월</td>
      <td>김창균, 김지태</td>
      <td>홈페이지 보기</td>
      <td>서울특별시</td>
      <td>2025</td>
      <td>462980</td>
      <td>사업모델</td>
    </tr>
    <tr>
      <td>와이즈넛</td>
      <td>소프트웨어 개발 및 공급업</td>
      <td>검색엔진, 챗봇, 클라우드서비스</td>
      <td>2025-01-24</td>
      <td>12월</td>
      <td>강용성</td>
      <td>홈페이지 보기</td>
      <td>경기도</td>
      <td>2025</td>
      <td>096250</td>
      <td>혁신기술</td>
    </tr>
  </tbody>
</table>
</pre>

## 2014년 이전의 기술특례기업 목록은?


KIND에서도 2014년부터 기술성장기업의 목록을 제공합니다. 그이전에 상장한 기술성장기업 목록은 아쉽게도 한국거래소의 웹서비스를 통해서 구하진 못했습니다. <br>

여러경로로 검색하던 결과, 한국거래소와 인터뷰를 토대로 작성된 기사에 기술기업 목록이 기재된 것을 찾았습니다. <br>

[**거래소 기술기업상장부 인터뷰 기사(링크)**](https://www.newspim.com/news/view/20150310000431)

<br>

![listfromnews]({{site.url}}/assets/images/2025-03-01-listing/listfromnews.jpg)<br><br>



총 13개 종목이 확인되었으나, 여기에도 종목코드는 입력이 되어있지 않기 때문에 KIND에서 불러온 정보를 맵핑해보았습니다.

<br>




### 종목코드 매칭해보기

세 개의 기업에 대해 종목코드가 맵핑되지 않았습니다. 셋 다 상장 이후에 회사명을 변경한 사례입니다.. 다행히 KIND에서는 변경전회사명을 입력하더라도 회사 검색이 가능합니다. 이를 활용하여 3개의 회사에 대해서 현재기준 회사명과 코드를 불러와 보았습니다.


<pre>
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>종목코드</th>
      <th>변경후회사명</th>
      <th>회사명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>084990</td>
      <td>헬릭스미스</td>
      <td>바이로메드</td>
    </tr>
    <tr>
      <td>083790</td>
      <td>CG인바이츠</td>
      <td>크리스탈지노믹스</td>
    </tr>
    <tr>
      <td>141080</td>
      <td>리가켐바이오</td>
      <td>레고켐바이오</td>
    </tr>
  </tbody>
</table>
</pre>

### 다시 종목코드 매칭해보기

회사명과 종목코드를 업데이트 하였으니 이제는 2014년 이전에 상장한 기술기업의 목록with 종목코드를 확보하였습니다!

<pre>
개수 : 13

<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>상장일자</th>
      <th>회사코드</th>
      <th>회사명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2005-12-29</td>
      <td>084990</td>
      <td>헬릭스미스</td>
    </tr>
    <tr>
      <td>2005-12-29</td>
      <td>064550</td>
      <td>바이오니아</td>
    </tr>
    <tr>
      <td>2006-01-06</td>
      <td>083790</td>
      <td>CG인바이츠</td>
    </tr>
    <tr>
      <td>2009-02-03</td>
      <td>086890</td>
      <td>이수앱지스</td>
    </tr>
    <tr>
      <td>2009-09-15</td>
      <td>095700</td>
      <td>제넥신</td>
    </tr>
    <tr>
      <td>2009-11-06</td>
      <td>109820</td>
      <td>진매트릭스</td>
    </tr>
    <tr>
      <td>2011-01-26</td>
      <td>048530</td>
      <td>인트론바이오</td>
    </tr>
    <tr>
      <td>2011-07-13</td>
      <td>138610</td>
      <td>나이벡</td>
    </tr>
    <tr>
      <td>2011-12-26</td>
      <td>127120</td>
      <td>디엔에이링크</td>
    </tr>
    <tr>
      <td>2013-03-05</td>
      <td>104540</td>
      <td>코렌텍</td>
    </tr>
    <tr>
      <td>2013-05-10</td>
      <td>141080</td>
      <td>리가켐바이오</td>
    </tr>
    <tr>
      <td>2013-09-12</td>
      <td>092040</td>
      <td>아미코젠</td>
    </tr>
    <tr>
      <td>2013-12-19</td>
      <td>150840</td>
      <td>인트로메딕</td>
    </tr>
  </tbody>
</table>
</pre>

## 정보데이터시스템, KIND, 뉴스 종합하기!

일단 세 가지 소스에서 데이터를 준비해보았습니다. 아래의 도식대로 데이터를 처리하여 다음을 최종적으로 구해보겠습니다.<br><br>

**기술성장기업**

* with 종목코드

* with 상장트랙



<br>



![datacomparison]({{site.url}}/assets/images/2025-03-01-listing/datacomparison.png)<br><br>


### 참고할 상장법인 정보를 가져오기

앞서 상장법인 목록을 통해서 상장사의 상장일 등의 정보를 가져온 적이 있었습니다. 근데 그 목록에는 상장폐지법인이 포함되어 있지 않았습니다. <br>

한편 상장폐지법인 목록에는 상장일 같은 정보는 없었습니다.<br>

그래서 차라리 '신규상장법인'목록을 표출해주는 화면에서 상장사 정보를 가져오기로 했습니다. 해당 화면에는 상장폐지된 법인도 표출이 되어있습니다.<br><br>

![kind6]({{site.url}}/assets/images/2025-03-01-listing/kind6.png)<br><br>

**...?**<br><br>

그렇네요.. 처음부터 '신규상장법인'목록을 통해서 가져왔으면 되는데 말이죠..ㅎㅎ 그랬으면 상장/상장폐지 화면을 돌아다니면서 가져올 필요가 없었습니다. 워낙 참고할 화면이 많다보니 이런 시행착오도 겪은 것이라 생각하겠습니다.


<pre>
총 2237개의 데이터를 찾았습니다.
</pre>

### 스팩합병일 경우는?

스팩합병 상장의 절차는 다음과 같습니다.

1. 먼저 껍데기 회사(스팩)을 상장시킵니다.

2. 상장된 스팩은 합병을 할 회사를 물색합니다.

3. 회사와 스팩이 합병하여 진짜 상장이 이루어집니다.



<br>

위에서 가져온 신규상장법인 현황의 경우, **스팩존속 합병법인에 대해서는 스팩상장일이 기재**{: style="color: #4682B4;"}되어 있습니다. 우리가 궁금한건 '진짜 상장일'이니, 스팩합병상장일을 추가로 구해와야 합니다. KIND에는 아래와 같은 화면에서 이를 확인할 수 있습니다.

<br><br>

![kind7]({{site.url}}/assets/images/2025-03-01-listing/kind7.png)<br><br>



### KIND와 뉴스를 먼저 종합하기

일단 KIND와 뉴스기사를 통해서 제도 도입이래 기술성장기업 목록을 확보합니다.


<pre>
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>회사명</th>
      <th>회사코드</th>
      <th>상장트랙</th>
      <th>상장당시회사명</th>
      <th>상장일</th>
      <th>상장유형</th>
      <th>증권구분</th>
      <th>국적</th>
      <th>상장주선인</th>
      <th>합병상장일</th>
      <th>합병상장유형</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>헬릭스미스</td>
      <td>084990</td>
      <td>혁신기술</td>
      <td>바이로메드</td>
      <td>2005-12-29</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>KB증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>바이오니아</td>
      <td>064550</td>
      <td>혁신기술</td>
      <td>바이오니아</td>
      <td>2005-12-29</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>CG인바이츠</td>
      <td>083790</td>
      <td>혁신기술</td>
      <td>크리스탈지노믹스</td>
      <td>2006-01-06</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>이수앱지스</td>
      <td>086890</td>
      <td>혁신기술</td>
      <td>이수앱지스</td>
      <td>2009-02-03</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>제넥신</td>
      <td>095700</td>
      <td>혁신기술</td>
      <td>제넥신</td>
      <td>2009-09-15</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>교보증권(주),미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>진매트릭스</td>
      <td>109820</td>
      <td>혁신기술</td>
      <td>진매트릭스</td>
      <td>2009-11-06</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>인트론바이오</td>
      <td>048530</td>
      <td>혁신기술</td>
      <td>인트론바이오</td>
      <td>2011-01-26</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>신한투자증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>나이벡</td>
      <td>138610</td>
      <td>혁신기술</td>
      <td>나이벡</td>
      <td>2011-07-13</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>디엔에이링크</td>
      <td>127120</td>
      <td>혁신기술</td>
      <td>디엔에이링크</td>
      <td>2011-12-26</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>코렌텍</td>
      <td>104540</td>
      <td>혁신기술</td>
      <td>코렌텍</td>
      <td>2013-03-05</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>리가켐바이오</td>
      <td>141080</td>
      <td>혁신기술</td>
      <td>레고켐바이오</td>
      <td>2013-05-10</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>아미코젠</td>
      <td>092040</td>
      <td>혁신기술</td>
      <td>아미코젠</td>
      <td>2013-09-12</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>인트로메딕</td>
      <td>150840</td>
      <td>혁신기술</td>
      <td>인트로메딕</td>
      <td>2013-12-19</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>아스트</td>
      <td>067390</td>
      <td>혁신기술</td>
      <td>아스트</td>
      <td>2014-12-24</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>케이비투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>알테오젠</td>
      <td>196170</td>
      <td>혁신기술</td>
      <td>알테오젠</td>
      <td>2014-12-12</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>덱스터</td>
      <td>206560</td>
      <td>혁신기술</td>
      <td>덱스터</td>
      <td>2015-12-22</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>HLB제약</td>
      <td>047920</td>
      <td>혁신기술</td>
      <td>씨트리</td>
      <td>2015-12-21</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>신한투자증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>강스템바이오텍</td>
      <td>217730</td>
      <td>혁신기술</td>
      <td>강스템바이오텍</td>
      <td>2015-12-21</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>파크시스템스</td>
      <td>140860</td>
      <td>혁신기술</td>
      <td>파크시스템스</td>
      <td>2015-12-17</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>케이비투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>멕아이씨에스</td>
      <td>058110</td>
      <td>혁신기술</td>
      <td>멕아이씨에스</td>
      <td>2015-12-14</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>DXVX</td>
      <td>180400</td>
      <td>혁신기술</td>
      <td>엠지메드</td>
      <td>2015-11-20</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>신한투자증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>아이진</td>
      <td>185490</td>
      <td>혁신기술</td>
      <td>아이진</td>
      <td>2015-11-16</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>시지메드텍</td>
      <td>056090</td>
      <td>혁신기술</td>
      <td>유앤아이</td>
      <td>2015-11-12</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>엔케이맥스</td>
      <td>182400</td>
      <td>혁신기술</td>
      <td>에이티젠</td>
      <td>2015-10-23</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>펩트론</td>
      <td>087010</td>
      <td>혁신기술</td>
      <td>펩트론</td>
      <td>2015-07-22</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>코아스템켐온</td>
      <td>166480</td>
      <td>혁신기술</td>
      <td>코아스템</td>
      <td>2015-06-26</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>HLB제넥스</td>
      <td>187420</td>
      <td>혁신기술</td>
      <td>제노포커스</td>
      <td>2015-05-29</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>애니젠</td>
      <td>196300</td>
      <td>혁신기술</td>
      <td>애니젠</td>
      <td>2016-12-07</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>신라젠</td>
      <td>215600</td>
      <td>혁신기술</td>
      <td>신라젠</td>
      <td>2016-12-06</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사,하나증권주식회사,DB금융투자주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>퓨쳐켐</td>
      <td>220100</td>
      <td>혁신기술</td>
      <td>퓨쳐켐</td>
      <td>2016-12-01</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>얼라인드</td>
      <td>238120</td>
      <td>혁신기술</td>
      <td>로고스바이오</td>
      <td>2016-11-03</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>신한투자증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>지엘팜텍</td>
      <td>204840</td>
      <td>혁신기술</td>
      <td>IBKS제2호스팩</td>
      <td>2014-11-20</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>IBK투자증권(주)</td>
      <td>2016-10-05</td>
      <td>SPAC 존속합병</td>
    </tr>
    <tr>
      <td>아이윈플러스</td>
      <td>123010</td>
      <td>혁신기술</td>
      <td>옵토팩</td>
      <td>2016-07-20</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>IBK투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>모아라이프플러스</td>
      <td>142760</td>
      <td>혁신기술</td>
      <td>바이오리더스</td>
      <td>2016-07-07</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>팬젠</td>
      <td>222110</td>
      <td>혁신기술</td>
      <td>팬젠</td>
      <td>2016-03-11</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>큐리언트</td>
      <td>115180</td>
      <td>혁신기술</td>
      <td>큐리언트</td>
      <td>2016-02-29</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>안트로젠</td>
      <td>065660</td>
      <td>혁신기술</td>
      <td>안트로젠</td>
      <td>2016-02-15</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>휴마시스</td>
      <td>205470</td>
      <td>혁신기술</td>
      <td>하이제2호스팩</td>
      <td>2014-12-01</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>iM증권</td>
      <td>2017-10-17</td>
      <td>SPAC 존속합병</td>
    </tr>
    <tr>
      <td>앱클론</td>
      <td>174900</td>
      <td>혁신기술</td>
      <td>앱클론</td>
      <td>2017-09-18</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>어스앤에어로스페이스</td>
      <td>263540</td>
      <td>혁신기술</td>
      <td>샘코</td>
      <td>2017-09-15</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주),대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>모비스</td>
      <td>250060</td>
      <td>혁신기술</td>
      <td>하나금융8호스팩</td>
      <td>2016-09-08</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>2017-03-21</td>
      <td>SPAC 존속합병</td>
    </tr>
    <tr>
      <td>아스타</td>
      <td>246720</td>
      <td>혁신기술</td>
      <td>아스타</td>
      <td>2017-03-20</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>피씨엘</td>
      <td>241820</td>
      <td>혁신기술</td>
      <td>피씨엘</td>
      <td>2017-02-23</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>유바이오로직스</td>
      <td>206650</td>
      <td>혁신기술</td>
      <td>유바이오로직스</td>
      <td>2017-01-24</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>비피도</td>
      <td>238200</td>
      <td>혁신기술</td>
      <td>비피도</td>
      <td>2018-12-26</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>유틸렉스</td>
      <td>263050</td>
      <td>혁신기술</td>
      <td>유틸렉스</td>
      <td>2018-12-24</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>에이비엘바이오</td>
      <td>298380</td>
      <td>혁신기술</td>
      <td>에이비엘바이오</td>
      <td>2018-12-19</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>전진바이오팜</td>
      <td>110020</td>
      <td>혁신기술</td>
      <td>전진바이오팜</td>
      <td>2018-12-14</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>나무기술</td>
      <td>242040</td>
      <td>혁신기술</td>
      <td>교보비엔케이스팩</td>
      <td>2016-09-07</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>교보증권(주),(주)비엔케이투자증권</td>
      <td>2018-12-11</td>
      <td>SPAC 존속합병</td>
    </tr>
    <tr>
      <td>티앤알바이오팹</td>
      <td>246710</td>
      <td>혁신기술</td>
      <td>티앤알바이오팹</td>
      <td>2018-11-28</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>네오펙트</td>
      <td>290660</td>
      <td>혁신기술</td>
      <td>네오펙트</td>
      <td>2018-11-28</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>싸이토젠</td>
      <td>217330</td>
      <td>혁신기술</td>
      <td>싸이토젠</td>
      <td>2018-11-22</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>파멥신</td>
      <td>208340</td>
      <td>혁신기술</td>
      <td>파멥신</td>
      <td>2018-11-21</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>KB증권(주),삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>셀리버리</td>
      <td>268600</td>
      <td>사업모델</td>
      <td>셀리버리</td>
      <td>2018-11-09</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>DB금융투자주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>로보티즈</td>
      <td>108490</td>
      <td>혁신기술</td>
      <td>로보티즈</td>
      <td>2018-10-26</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>옵티팜</td>
      <td>153710</td>
      <td>혁신기술</td>
      <td>옵티팜</td>
      <td>2018-10-26</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>바이오솔루션</td>
      <td>086820</td>
      <td>혁신기술</td>
      <td>바이오솔루션</td>
      <td>2018-08-20</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>올릭스</td>
      <td>226950</td>
      <td>혁신기술</td>
      <td>올릭스</td>
      <td>2018-07-18</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>아이큐어</td>
      <td>175250</td>
      <td>혁신기술</td>
      <td>아이큐어</td>
      <td>2018-07-12</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>EDGC</td>
      <td>245620</td>
      <td>혁신기술</td>
      <td>EDGC</td>
      <td>2018-06-26</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>SK증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>유네코</td>
      <td>064510</td>
      <td>혁신기술</td>
      <td>에코마이스터</td>
      <td>2018-03-15</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주),한화투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>오스테오닉</td>
      <td>226400</td>
      <td>혁신기술</td>
      <td>오스테오닉</td>
      <td>2018-02-22</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>엔지켐생명과학</td>
      <td>183490</td>
      <td>혁신기술</td>
      <td>엔지켐생명과학</td>
      <td>2018-02-21</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>아시아종묘</td>
      <td>154030</td>
      <td>혁신기술</td>
      <td>아시아종묘</td>
      <td>2018-02-12</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>링크제니시스</td>
      <td>219420</td>
      <td>혁신기술</td>
      <td>링크제니시스</td>
      <td>2018-02-05</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>CJ 바이오사이언스</td>
      <td>311690</td>
      <td>혁신기술</td>
      <td>천랩</td>
      <td>2019-12-26</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>브릿지바이오</td>
      <td>288330</td>
      <td>사업모델</td>
      <td>브릿지바이오</td>
      <td>2019-12-20</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주),KB증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>메드팩토</td>
      <td>235980</td>
      <td>혁신기술</td>
      <td>메드팩토</td>
      <td>2019-12-19</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>신테카바이오</td>
      <td>226330</td>
      <td>사업모델</td>
      <td>신테카바이오</td>
      <td>2019-12-17</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>KB증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>제이엘케이</td>
      <td>322510</td>
      <td>혁신기술</td>
      <td>제이엘케이인스펙션</td>
      <td>2019-12-11</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>티움바이오</td>
      <td>321550</td>
      <td>혁신기술</td>
      <td>티움바이오</td>
      <td>2019-11-22</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>자비스</td>
      <td>254120</td>
      <td>혁신기술</td>
      <td>IBKS제5호스팩</td>
      <td>2016-12-02</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>IBK투자증권(주)</td>
      <td>2019-11-15</td>
      <td>SPAC 존속합병</td>
    </tr>
    <tr>
      <td>라파스</td>
      <td>214260</td>
      <td>사업모델</td>
      <td>라파스</td>
      <td>2019-11-11</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>DB금융투자주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>미디어젠</td>
      <td>279600</td>
      <td>혁신기술</td>
      <td>미디어젠</td>
      <td>2019-11-05</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>교보증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>캐리소프트</td>
      <td>317530</td>
      <td>혁신기술</td>
      <td>캐리소프트</td>
      <td>2019-10-29</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>엔바이오니아</td>
      <td>317870</td>
      <td>혁신기술</td>
      <td>엔바이오니아</td>
      <td>2019-10-24</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>올리패스</td>
      <td>244460</td>
      <td>사업모델</td>
      <td>올리패스</td>
      <td>2019-09-20</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사,키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>라닉스</td>
      <td>317120</td>
      <td>사업모델</td>
      <td>라닉스</td>
      <td>2019-09-18</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>나노브릭</td>
      <td>286750</td>
      <td>혁신기술</td>
      <td>나노브릭</td>
      <td>2019-08-19</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>KB증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>플리토</td>
      <td>300080</td>
      <td>혁신기술</td>
      <td>플리토</td>
      <td>2019-07-17</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>압타바이오</td>
      <td>293780</td>
      <td>혁신기술</td>
      <td>압타바이오</td>
      <td>2019-06-12</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사,삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>마이크로디지탈</td>
      <td>305090</td>
      <td>혁신기술</td>
      <td>마이크로디지탈</td>
      <td>2019-06-05</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>수젠텍</td>
      <td>253840</td>
      <td>혁신기술</td>
      <td>수젠텍</td>
      <td>2019-05-28</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>아모그린텍</td>
      <td>125210</td>
      <td>혁신기술</td>
      <td>아모그린텍</td>
      <td>2019-03-29</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>지노믹트리</td>
      <td>228760</td>
      <td>혁신기술</td>
      <td>지노믹트리</td>
      <td>2019-03-27</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>셀리드</td>
      <td>299660</td>
      <td>혁신기술</td>
      <td>셀리드</td>
      <td>2019-02-20</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>SCL사이언스</td>
      <td>246960</td>
      <td>혁신기술</td>
      <td>이노테라피</td>
      <td>2019-02-01</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>지놈앤컴퍼니</td>
      <td>314130</td>
      <td>혁신기술</td>
      <td>지놈앤컴퍼니</td>
      <td>2020-12-23</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>석경에이티</td>
      <td>357550</td>
      <td>혁신기술</td>
      <td>석경에이티</td>
      <td>2020-12-23</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>프리시젼바이오</td>
      <td>335810</td>
      <td>혁신기술</td>
      <td>프리시젼바이오</td>
      <td>2020-12-22</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>알체라</td>
      <td>347860</td>
      <td>사업모델</td>
      <td>알체라</td>
      <td>2020-12-21</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>신영증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>엔젠바이오</td>
      <td>354200</td>
      <td>혁신기술</td>
      <td>엔젠바이오</td>
      <td>2020-12-10</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>퀀타매트릭스</td>
      <td>317690</td>
      <td>혁신기술</td>
      <td>퀀타매트릭스</td>
      <td>2020-12-09</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>클리노믹스</td>
      <td>352770</td>
      <td>사업모델</td>
      <td>클리노믹스</td>
      <td>2020-12-04</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>고바이오랩</td>
      <td>348150</td>
      <td>사업모델</td>
      <td>고바이오랩</td>
      <td>2020-11-18</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주),삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>센코</td>
      <td>347000</td>
      <td>혁신기술</td>
      <td>센코</td>
      <td>2020-10-29</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>바이브컴퍼니</td>
      <td>301300</td>
      <td>혁신기술</td>
      <td>바이브컴퍼니</td>
      <td>2020-10-28</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>미코바이오메드</td>
      <td>214610</td>
      <td>혁신기술</td>
      <td>미코바이오메드</td>
      <td>2020-10-22</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>KB증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>피플바이오</td>
      <td>304840</td>
      <td>혁신기술</td>
      <td>피플바이오</td>
      <td>2020-10-19</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>넥스틴</td>
      <td>348210</td>
      <td>혁신기술</td>
      <td>넥스틴</td>
      <td>2020-10-08</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>KB증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>박셀바이오</td>
      <td>323990</td>
      <td>혁신기술</td>
      <td>박셀바이오</td>
      <td>2020-09-22</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>압타머사이언스</td>
      <td>291650</td>
      <td>사업모델</td>
      <td>압타머사이언스</td>
      <td>2020-09-16</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>이오플로우</td>
      <td>294090</td>
      <td>사업모델</td>
      <td>이오플로우</td>
      <td>2020-09-14</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>셀레믹스</td>
      <td>331920</td>
      <td>사업모델</td>
      <td>셀레믹스</td>
      <td>2020-08-21</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>제놀루션</td>
      <td>225220</td>
      <td>사업모델</td>
      <td>제놀루션</td>
      <td>2020-07-24</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>신영증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>솔트룩스</td>
      <td>304100</td>
      <td>혁신기술</td>
      <td>솔트룩스</td>
      <td>2020-07-23</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>소마젠</td>
      <td>USA15</td>
      <td>혁신기술</td>
      <td>소마젠</td>
      <td>2020-07-13</td>
      <td>신규상장</td>
      <td>주식예탁증권</td>
      <td>미국</td>
      <td>신한투자증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>젠큐릭스</td>
      <td>229000</td>
      <td>혁신기술</td>
      <td>젠큐릭스</td>
      <td>2020-06-25</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>에스씨엠생명과학</td>
      <td>298060</td>
      <td>혁신기술</td>
      <td>에스씨엠생명과학</td>
      <td>2020-06-17</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>카이노스메드</td>
      <td>284620</td>
      <td>혁신기술</td>
      <td>하나금융11호스팩</td>
      <td>2018-06-08</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>2020-06-08</td>
      <td>SPAC 존속합병</td>
    </tr>
    <tr>
      <td>레몬</td>
      <td>294140</td>
      <td>혁신기술</td>
      <td>레몬</td>
      <td>2020-02-28</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>서남</td>
      <td>294630</td>
      <td>혁신기술</td>
      <td>서남</td>
      <td>2020-02-20</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>툴젠</td>
      <td>199800</td>
      <td>혁신기술</td>
      <td>툴젠</td>
      <td>2021-12-10</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>마음AI</td>
      <td>377480</td>
      <td>혁신기술</td>
      <td>마인즈랩</td>
      <td>2021-11-23</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사,하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>지오엘리먼트</td>
      <td>311320</td>
      <td>혁신기술</td>
      <td>지오엘리먼트</td>
      <td>2021-11-11</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>스카이월드와이드</td>
      <td>357880</td>
      <td>혁신기술</td>
      <td>비트나인</td>
      <td>2021-11-10</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>지니너스</td>
      <td>389030</td>
      <td>혁신기술</td>
      <td>지니너스</td>
      <td>2021-11-08</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>차백신연구소</td>
      <td>261780</td>
      <td>혁신기술</td>
      <td>차백신연구소</td>
      <td>2021-10-22</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>에이비온</td>
      <td>203400</td>
      <td>혁신기술</td>
      <td>에이비온</td>
      <td>2021-09-08</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사,한화투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>바이젠셀</td>
      <td>308080</td>
      <td>혁신기술</td>
      <td>바이젠셀</td>
      <td>2021-08-25</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주),KB증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>딥노이드</td>
      <td>315640</td>
      <td>혁신기술</td>
      <td>딥노이드</td>
      <td>2021-08-17</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>KB증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>원티드랩</td>
      <td>376980</td>
      <td>사업모델</td>
      <td>원티드랩</td>
      <td>2021-08-11</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>비트맥스</td>
      <td>377030</td>
      <td>혁신기술</td>
      <td>맥스트</td>
      <td>2021-07-27</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>큐라클</td>
      <td>365270</td>
      <td>혁신기술</td>
      <td>큐라클</td>
      <td>2021-07-22</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>오비고</td>
      <td>352910</td>
      <td>혁신기술</td>
      <td>오비고</td>
      <td>2021-07-13</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>아모센스</td>
      <td>357580</td>
      <td>혁신기술</td>
      <td>아모센스</td>
      <td>2021-06-25</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>신한투자증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>라온테크</td>
      <td>232680</td>
      <td>혁신기술</td>
      <td>라온테크</td>
      <td>2021-06-17</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>KB증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>진시스템</td>
      <td>363250</td>
      <td>사업모델</td>
      <td>진시스템</td>
      <td>2021-05-26</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>삼영에스앤씨</td>
      <td>361670</td>
      <td>사업모델</td>
      <td>삼영에스앤씨</td>
      <td>2021-05-21</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>샘씨엔에스</td>
      <td>252990</td>
      <td>혁신기술</td>
      <td>샘씨엔에스</td>
      <td>2021-05-20</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>해성에어로보틱스</td>
      <td>059270</td>
      <td>혁신기술</td>
      <td>해성티피씨</td>
      <td>2021-04-21</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>자이언트스텝</td>
      <td>289220</td>
      <td>혁신기술</td>
      <td>자이언트스텝</td>
      <td>2021-03-24</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>제노코</td>
      <td>361390</td>
      <td>혁신기술</td>
      <td>제노코</td>
      <td>2021-03-24</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>DB금융투자주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>라이프시맨틱스</td>
      <td>347700</td>
      <td>혁신기술</td>
      <td>라이프시맨틱스</td>
      <td>2021-03-23</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>네오이뮨텍</td>
      <td>USA14</td>
      <td>혁신기술</td>
      <td>네오이뮨텍</td>
      <td>2021-03-16</td>
      <td>신규상장</td>
      <td>주식예탁증권</td>
      <td>미국</td>
      <td>미래에셋증권 주식회사,하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>프레스티지바이오로직스</td>
      <td>334970</td>
      <td>사업모델</td>
      <td>프레스티지바이오로직스</td>
      <td>2021-03-11</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사,유안타증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>나노씨엠에스</td>
      <td>247660</td>
      <td>혁신기술</td>
      <td>나노씨엠에스</td>
      <td>2021-03-09</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>뷰노</td>
      <td>338220</td>
      <td>혁신기술</td>
      <td>뷰노</td>
      <td>2021-02-26</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사,삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>씨이랩</td>
      <td>189330</td>
      <td>혁신기술</td>
      <td>씨이랩</td>
      <td>2021-02-24</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>IBK투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>피엔에이치테크</td>
      <td>239890</td>
      <td>혁신기술</td>
      <td>피엔에이치테크</td>
      <td>2021-02-16</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>레인보우로보틱스</td>
      <td>277810</td>
      <td>사업모델</td>
      <td>레인보우로보틱스</td>
      <td>2021-02-03</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주),미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>아티스트유나이티드</td>
      <td>321820</td>
      <td>혁신기술</td>
      <td>와이더플래닛</td>
      <td>2021-02-03</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>SAMG엔터</td>
      <td>419530</td>
      <td>혁신기술</td>
      <td>SAMG엔터</td>
      <td>2022-12-06</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>인벤티지랩</td>
      <td>389470</td>
      <td>혁신기술</td>
      <td>인벤티지랩</td>
      <td>2022-11-22</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>엔젯</td>
      <td>419080</td>
      <td>혁신기술</td>
      <td>엔젯</td>
      <td>2022-11-18</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>뉴로메카</td>
      <td>348340</td>
      <td>혁신기술</td>
      <td>뉴로메카</td>
      <td>2022-11-04</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>플라즈맵</td>
      <td>405000</td>
      <td>혁신기술</td>
      <td>플라즈맵</td>
      <td>2022-10-21</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>핀텔</td>
      <td>291810</td>
      <td>혁신기술</td>
      <td>핀텔</td>
      <td>2022-10-20</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>샤페론</td>
      <td>378800</td>
      <td>혁신기술</td>
      <td>샤페론</td>
      <td>2022-10-19</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>에스비비테크</td>
      <td>389500</td>
      <td>혁신기술</td>
      <td>에스비비테크</td>
      <td>2022-10-17</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>선바이오</td>
      <td>067370</td>
      <td>사업모델</td>
      <td>선바이오</td>
      <td>2022-10-05</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>아이씨에이치</td>
      <td>368600</td>
      <td>혁신기술</td>
      <td>아이씨에이치</td>
      <td>2022-07-29</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>에이프릴바이오</td>
      <td>397030</td>
      <td>혁신기술</td>
      <td>에이프릴바이오</td>
      <td>2022-07-28</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>루닛</td>
      <td>328130</td>
      <td>혁신기술</td>
      <td>루닛</td>
      <td>2022-07-21</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>와이씨켐</td>
      <td>112290</td>
      <td>혁신기술</td>
      <td>영창케미칼</td>
      <td>2022-07-14</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>코난테크놀로지</td>
      <td>402030</td>
      <td>혁신기술</td>
      <td>코난테크놀로지</td>
      <td>2022-07-07</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>넥스트칩</td>
      <td>396270</td>
      <td>혁신기술</td>
      <td>넥스트칩</td>
      <td>2022-07-01</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>원텍</td>
      <td>336570</td>
      <td>혁신기술</td>
      <td>대신밸런스제8호스팩</td>
      <td>2019-12-19</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>2022-06-30</td>
      <td>SPAC 존속합병</td>
    </tr>
    <tr>
      <td>보로노이</td>
      <td>310210</td>
      <td>혁신기술</td>
      <td>보로노이</td>
      <td>2022-06-24</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주),미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>레이저쎌</td>
      <td>412350</td>
      <td>혁신기술</td>
      <td>레이저쎌</td>
      <td>2022-06-24</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>비큐AI</td>
      <td>148780</td>
      <td>혁신기술</td>
      <td>비플라이소프트</td>
      <td>2022-06-20</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>IBK투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>하이딥</td>
      <td>365590</td>
      <td>혁신기술</td>
      <td>엔에이치스팩18호</td>
      <td>2020-12-21</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>2022-05-12</td>
      <td>SPAC 존속합병</td>
    </tr>
    <tr>
      <td>모아데이타</td>
      <td>288980</td>
      <td>혁신기술</td>
      <td>모아데이타</td>
      <td>2022-03-10</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>노을</td>
      <td>376930</td>
      <td>혁신기술</td>
      <td>노을</td>
      <td>2022-03-03</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주),삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>풍원정밀</td>
      <td>371950</td>
      <td>혁신기술</td>
      <td>풍원정밀</td>
      <td>2022-02-28</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>퓨런티어</td>
      <td>370090</td>
      <td>혁신기술</td>
      <td>퓨런티어</td>
      <td>2022-02-23</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>신한투자증권 주식회사,유안타증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>바이오에프디엔씨</td>
      <td>251120</td>
      <td>혁신기술</td>
      <td>바이오에프디엔씨</td>
      <td>2022-02-21</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>DB금융투자주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>스코넥</td>
      <td>276040</td>
      <td>혁신기술</td>
      <td>스코넥</td>
      <td>2022-02-04</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>신영증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>이지트로닉스</td>
      <td>377330</td>
      <td>혁신기술</td>
      <td>이지트로닉스</td>
      <td>2022-02-04</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>애드바이오텍</td>
      <td>179530</td>
      <td>혁신기술</td>
      <td>애드바이오텍</td>
      <td>2022-01-24</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>와이바이오로직스</td>
      <td>338840</td>
      <td>혁신기술</td>
      <td>와이바이오로직스</td>
      <td>2023-12-05</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>유안타증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>에이텀</td>
      <td>355690</td>
      <td>혁신기술</td>
      <td>에이텀</td>
      <td>2023-12-01</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>그린리소스</td>
      <td>402490</td>
      <td>혁신기술</td>
      <td>그린리소스</td>
      <td>2023-11-24</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>큐로셀</td>
      <td>372320</td>
      <td>혁신기술</td>
      <td>큐로셀</td>
      <td>2023-11-09</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사,삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>컨텍</td>
      <td>451760</td>
      <td>혁신기술</td>
      <td>컨텍</td>
      <td>2023-11-09</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>쏘닉스</td>
      <td>088280</td>
      <td>혁신기술</td>
      <td>쏘닉스</td>
      <td>2023-11-07</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>KB증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>세니젠</td>
      <td>188260</td>
      <td>혁신기술</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>퀄리타스반도체</td>
      <td>432720</td>
      <td>혁신기술</td>
      <td>퀄리타스반도체</td>
      <td>2023-10-27</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>아이엠티</td>
      <td>451220</td>
      <td>혁신기술</td>
      <td>아이엠티</td>
      <td>2023-10-10</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>유안타증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>코어라인소프트</td>
      <td>384470</td>
      <td>혁신기술</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>크라우드웍스</td>
      <td>355390</td>
      <td>혁신기술</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>시큐레터</td>
      <td>418250</td>
      <td>혁신기술</td>
      <td>시큐레터</td>
      <td>2023-08-24</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>스마트레이더시스템</td>
      <td>424960</td>
      <td>혁신기술</td>
      <td>스마트레이더시스템</td>
      <td>2023-08-22</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>큐리옥스바이오시스템즈</td>
      <td>445680</td>
      <td>혁신기술</td>
      <td>큐리옥스바이오시스템즈</td>
      <td>2023-08-10</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>파두</td>
      <td>440110</td>
      <td>혁신기술</td>
      <td>파두</td>
      <td>2023-08-07</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주),엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>시지트로닉스</td>
      <td>429270</td>
      <td>혁신기술</td>
      <td>시지트로닉스</td>
      <td>2023-08-03</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>유안타증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>파로스아이바이오</td>
      <td>388870</td>
      <td>혁신기술</td>
      <td>파로스아이바이오</td>
      <td>2023-07-27</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>버넥트</td>
      <td>438700</td>
      <td>혁신기술</td>
      <td>버넥트</td>
      <td>2023-07-26</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>와이랩</td>
      <td>432430</td>
      <td>사업모델</td>
      <td>와이랩</td>
      <td>2023-07-20</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>센서뷰</td>
      <td>321370</td>
      <td>혁신기술</td>
      <td>센서뷰</td>
      <td>2023-07-19</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>이노시뮬레이션</td>
      <td>274400</td>
      <td>혁신기술</td>
      <td>이노시뮬레이션</td>
      <td>2023-07-06</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>오픈놀</td>
      <td>440320</td>
      <td>혁신기술</td>
      <td>오픈놀</td>
      <td>2023-06-30</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>프로티아</td>
      <td>303360</td>
      <td>혁신기술</td>
      <td>프로테옴텍</td>
      <td>2023-06-16</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>큐라티스</td>
      <td>348080</td>
      <td>혁신기술</td>
      <td>큐라티스</td>
      <td>2023-06-15</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주),신영증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>씨유박스</td>
      <td>340810</td>
      <td>혁신기술</td>
      <td>씨유박스</td>
      <td>2023-05-19</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>신한투자증권 주식회사,SK증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>모니터랩</td>
      <td>434480</td>
      <td>혁신기술</td>
      <td>모니터랩</td>
      <td>2023-05-19</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>에스바이오메딕스</td>
      <td>304360</td>
      <td>혁신기술</td>
      <td>에스바이오메딕스</td>
      <td>2023-05-04</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>마이크로투나노</td>
      <td>424980</td>
      <td>혁신기술</td>
      <td>마이크로투나노</td>
      <td>2023-04-26</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>지아이이노베이션</td>
      <td>358570</td>
      <td>혁신기술</td>
      <td>지아이이노베이션</td>
      <td>2023-03-30</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사,하나증권주식회사,삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>라온텍</td>
      <td>418420</td>
      <td>혁신기술</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>파인메딕스</td>
      <td>387570</td>
      <td>혁신기술</td>
      <td>파인메딕스</td>
      <td>2024-12-26</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>엠에프씨</td>
      <td>432980</td>
      <td>혁신기술</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>쓰리에이로직스</td>
      <td>177900</td>
      <td>혁신기술</td>
      <td>쓰리에이로직스</td>
      <td>2024-12-24</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>신한투자증권 주식회사,미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>온코닉테라퓨틱스</td>
      <td>476060</td>
      <td>혁신기술</td>
      <td>온코닉테라퓨틱스</td>
      <td>2024-12-19</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>온코크로스</td>
      <td>382150</td>
      <td>혁신기술</td>
      <td>온코크로스</td>
      <td>2024-12-18</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>유디엠텍</td>
      <td>389680</td>
      <td>혁신기술</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>쓰리빌리언</td>
      <td>394800</td>
      <td>혁신기술</td>
      <td>쓰리빌리언</td>
      <td>2024-11-14</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>에어레인</td>
      <td>163280</td>
      <td>혁신기술</td>
      <td>에어레인</td>
      <td>2024-11-08</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>신영증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>토모큐브</td>
      <td>475960</td>
      <td>혁신기술</td>
      <td>토모큐브</td>
      <td>2024-11-07</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>에이치이엠파마</td>
      <td>376270</td>
      <td>혁신기술</td>
      <td>에이치이엠파마</td>
      <td>2024-11-05</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>신한투자증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>클로봇</td>
      <td>466100</td>
      <td>혁신기술</td>
      <td>클로봇</td>
      <td>2024-10-28</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>웨이비스</td>
      <td>289930</td>
      <td>혁신기술</td>
      <td>웨이비스</td>
      <td>2024-10-25</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>씨메스</td>
      <td>475400</td>
      <td>혁신기술</td>
      <td>씨메스</td>
      <td>2024-10-24</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>유진투자증권(주),삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>루미르</td>
      <td>474170</td>
      <td>혁신기술</td>
      <td>루미르</td>
      <td>2024-10-21</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>셀비온</td>
      <td>308430</td>
      <td>혁신기술</td>
      <td>셀비온</td>
      <td>2024-10-16</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>아이언디바이스</td>
      <td>464500</td>
      <td>혁신기술</td>
      <td>아이언디바이스</td>
      <td>2024-09-23</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>이엔셀</td>
      <td>456070</td>
      <td>혁신기술</td>
      <td>이엔셀</td>
      <td>2024-08-23</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>넥스트바이오메디컬</td>
      <td>389650</td>
      <td>혁신기술</td>
      <td>넥스트바이오메디컬</td>
      <td>2024-08-20</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>케이쓰리아이</td>
      <td>431190</td>
      <td>혁신기술</td>
      <td>케이쓰리아이</td>
      <td>2024-08-20</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>뱅크웨어글로벌</td>
      <td>199480</td>
      <td>혁신기술</td>
      <td>뱅크웨어글로벌</td>
      <td>2024-08-12</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>아이빔테크놀로지</td>
      <td>460470</td>
      <td>혁신기술</td>
      <td>아이빔테크놀로지</td>
      <td>2024-08-06</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>피앤에스미캐닉스</td>
      <td>460940</td>
      <td>혁신기술</td>
      <td>피앤에스미캐닉스</td>
      <td>2024-07-31</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>엑셀세라퓨틱스</td>
      <td>373110</td>
      <td>혁신기술</td>
      <td>엑셀세라퓨틱스</td>
      <td>2024-07-15</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>하스</td>
      <td>450330</td>
      <td>혁신기술</td>
      <td>하스</td>
      <td>2024-07-03</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>이노스페이스</td>
      <td>462350</td>
      <td>혁신기술</td>
      <td>이노스페이스</td>
      <td>2024-07-02</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>에이치브이엠</td>
      <td>295310</td>
      <td>혁신기술</td>
      <td>에이치브이엠</td>
      <td>2024-06-28</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>에스오에스랩</td>
      <td>464080</td>
      <td>혁신기술</td>
      <td>에스오에스랩</td>
      <td>2024-06-25</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>한중엔시에스</td>
      <td>107640</td>
      <td>혁신기술</td>
      <td>한중엔시에스</td>
      <td>2024-06-24</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>IBK투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>씨어스테크놀로지</td>
      <td>458870</td>
      <td>혁신기술</td>
      <td>씨어스테크놀로지</td>
      <td>2024-06-19</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>라메디텍</td>
      <td>462510</td>
      <td>혁신기술</td>
      <td>라메디텍</td>
      <td>2024-06-17</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>오름테라퓨틱</td>
      <td>475830</td>
      <td>혁신기술</td>
      <td>오름테라퓨틱</td>
      <td>2025-02-14</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>아이에스티이</td>
      <td>212710</td>
      <td>혁신기술</td>
      <td>아이에스티이</td>
      <td>2025-02-12</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>KB증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>아이지넷</td>
      <td>462980</td>
      <td>사업모델</td>
      <td>아이지넷</td>
      <td>2025-02-04</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>와이즈넛</td>
      <td>096250</td>
      <td>혁신기술</td>
      <td>와이즈넛</td>
      <td>2025-01-24</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</pre>

### 외구주권,DR 종목코드 받아오기

정보데이터시스템과 비교하기 위해선 종목코드는 반드시 필요한데 말이죠...,<br>

> 외국회사와 KDR(주식예탁증권)의 경우, 회사코드에 0을 붙여서 보통주 종목코드가 되는 구조가 아닐 수 있습니다.



<br>

따라서 마지막으로 KIND에서 외국회사, KDR의 종목코드까지만 구하고 다음단계로 진행해보겠습니다. 우선 외국회사와 KDR의 목록을 KIND에서 확인해보겠습니다.



<pre>
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>구분</th>
      <th>회사명</th>
      <th>종목코드</th>
      <th>상장일</th>
      <th>상장주식</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>DR</td>
      <td>네오이뮨텍</td>
      <td>950220</td>
      <td>2021-03-16</td>
      <td>98,867</td>
    </tr>
    <tr>
      <td>DR</td>
      <td>고스트스튜디오</td>
      <td>950190</td>
      <td>2020-08-18</td>
      <td>13,580</td>
    </tr>
    <tr>
      <td>DR</td>
      <td>소마젠</td>
      <td>950200</td>
      <td>2020-07-13</td>
      <td>19,236</td>
    </tr>
    <tr>
      <td>DR</td>
      <td>JTC</td>
      <td>950170</td>
      <td>2018-04-06</td>
      <td>51,746</td>
    </tr>
    <tr>
      <td>DR</td>
      <td>코오롱티슈진</td>
      <td>950160</td>
      <td>2017-11-06</td>
      <td>81,524</td>
    </tr>
    <tr>
      <td>DR</td>
      <td>잉글우드랩</td>
      <td>950140</td>
      <td>2016-10-14</td>
      <td>19,868</td>
    </tr>
    <tr>
      <td>DR</td>
      <td>엑세스바이오</td>
      <td>950130</td>
      <td>2013-05-30</td>
      <td>37,728</td>
    </tr>
    <tr>
      <td>DR</td>
      <td>SBI핀테크솔루션즈</td>
      <td>950110</td>
      <td>2012-12-17</td>
      <td>24,053</td>
    </tr>
    <tr>
      <td>FS</td>
      <td>윙입푸드</td>
      <td>900340</td>
      <td>2018-11-30</td>
      <td>50,331</td>
    </tr>
    <tr>
      <td>FS</td>
      <td>컬러레이</td>
      <td>900310</td>
      <td>2017-08-10</td>
      <td>64,042</td>
    </tr>
    <tr>
      <td>FS</td>
      <td>오가닉티코스메틱</td>
      <td>900300</td>
      <td>2016-11-04</td>
      <td>51,002</td>
    </tr>
    <tr>
      <td>FS</td>
      <td>GRT</td>
      <td>900290</td>
      <td>2016-10-25</td>
      <td>80,850</td>
    </tr>
    <tr>
      <td>FS</td>
      <td>헝셩그룹</td>
      <td>900270</td>
      <td>2016-08-18</td>
      <td>152,282</td>
    </tr>
    <tr>
      <td>FS</td>
      <td>로스웰</td>
      <td>900260</td>
      <td>2016-06-30</td>
      <td>36,031</td>
    </tr>
    <tr>
      <td>FS</td>
      <td>크리스탈신소재</td>
      <td>900250</td>
      <td>2016-01-28</td>
      <td>130,640</td>
    </tr>
    <tr>
      <td>FS</td>
      <td>이스트아시아홀딩스</td>
      <td>900110</td>
      <td>2010-04-23</td>
      <td>542,651</td>
    </tr>
    <tr>
      <td>FS</td>
      <td>애머릿지</td>
      <td>900100</td>
      <td>2010-04-21</td>
      <td>43,539</td>
    </tr>
    <tr>
      <td>FS</td>
      <td>씨엑스아이</td>
      <td>900120</td>
      <td>2010-03-31</td>
      <td>300,578</td>
    </tr>
    <tr>
      <td>FS</td>
      <td>글로벌에스엠</td>
      <td>900070</td>
      <td>2009-12-23</td>
      <td>53,744</td>
    </tr>
  </tbody>
</table>
</pre>

<br>총 19개의 종목이 있습니다. 이제 우리가 앞서 구해보았던 기술성장기업 중에 종목코드가 숫자 6자리가 아닌 것을 찾아서 숫자 6자리로 교체해주도록 하겠습니다.<br>

**네오이뮨텍(USA14), 소마젠(USA15)가 여기에 해당하여 수정해주었습니다.**{: style="color: #4682B4;"}



<pre>
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>회사명</th>
      <th>회사코드</th>
      <th>상장트랙</th>
      <th>상장당시회사명</th>
      <th>상장일</th>
      <th>상장유형</th>
      <th>증권구분</th>
      <th>국적</th>
      <th>상장주선인</th>
      <th>합병상장일</th>
      <th>합병상장유형</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>소마젠</td>
      <td>USA15</td>
      <td>혁신기술</td>
      <td>소마젠</td>
      <td>2020-07-13</td>
      <td>신규상장</td>
      <td>주식예탁증권</td>
      <td>미국</td>
      <td>신한투자증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>네오이뮨텍</td>
      <td>USA14</td>
      <td>혁신기술</td>
      <td>네오이뮨텍</td>
      <td>2021-03-16</td>
      <td>신규상장</td>
      <td>주식예탁증권</td>
      <td>미국</td>
      <td>미래에셋증권 주식회사,하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</pre>

<pre>
소마젠의 회사코드가 950200로 변경되었습니다.
네오이뮨텍의 회사코드가 950220로 변경되었습니다.
</pre>
### 정보데이터시스템과도 합쳐서 정합성 확인하기

정보데이터시스템은 5년치만 있지만 상장트랙(기술/사업모델)을 구분하는 정합성이 높습니다. <br><br>

![listingtrack]({{site.url}}/assets/images/2025-03-01-listing/listingtrack.png)<br><br>



따라서 5년치 데이터에 대해서는 매칭시켜서 혹시 불일치하는 것은 없는지 확인해보겠습니다. 결과적으로 불일치하는 것은 없었습니다!



## 2025년 2월말 기준 기술성장기업 목록 완성

마침내 완성했습니다. KIND, 정보데이터시스템, 기사를 통해 확인된 2025년 2월말 기준 역대 기술성장기업은 234사였습니다.


<pre>
기술성장기업 개수234
<table border="1" class="dataframe dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>회사명</th>
      <th>회사코드</th>
      <th>상장트랙</th>
      <th>상장당시회사명</th>
      <th>상장일</th>
      <th>상장유형</th>
      <th>증권구분</th>
      <th>국적</th>
      <th>상장주선인</th>
      <th>합병상장일</th>
      <th>합병상장유형</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>헬릭스미스</td>
      <td>084990</td>
      <td>혁신기술</td>
      <td>바이로메드</td>
      <td>2005-12-29</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>KB증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>바이오니아</td>
      <td>064550</td>
      <td>혁신기술</td>
      <td>바이오니아</td>
      <td>2005-12-29</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>CG인바이츠</td>
      <td>083790</td>
      <td>혁신기술</td>
      <td>크리스탈지노믹스</td>
      <td>2006-01-06</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>이수앱지스</td>
      <td>086890</td>
      <td>혁신기술</td>
      <td>이수앱지스</td>
      <td>2009-02-03</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>제넥신</td>
      <td>095700</td>
      <td>혁신기술</td>
      <td>제넥신</td>
      <td>2009-09-15</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>교보증권(주),미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>진매트릭스</td>
      <td>109820</td>
      <td>혁신기술</td>
      <td>진매트릭스</td>
      <td>2009-11-06</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>인트론바이오</td>
      <td>048530</td>
      <td>혁신기술</td>
      <td>인트론바이오</td>
      <td>2011-01-26</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>신한투자증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>나이벡</td>
      <td>138610</td>
      <td>혁신기술</td>
      <td>나이벡</td>
      <td>2011-07-13</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>디엔에이링크</td>
      <td>127120</td>
      <td>혁신기술</td>
      <td>디엔에이링크</td>
      <td>2011-12-26</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>코렌텍</td>
      <td>104540</td>
      <td>혁신기술</td>
      <td>코렌텍</td>
      <td>2013-03-05</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>리가켐바이오</td>
      <td>141080</td>
      <td>혁신기술</td>
      <td>레고켐바이오</td>
      <td>2013-05-10</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>아미코젠</td>
      <td>092040</td>
      <td>혁신기술</td>
      <td>아미코젠</td>
      <td>2013-09-12</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>인트로메딕</td>
      <td>150840</td>
      <td>혁신기술</td>
      <td>인트로메딕</td>
      <td>2013-12-19</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>아스트</td>
      <td>067390</td>
      <td>혁신기술</td>
      <td>아스트</td>
      <td>2014-12-24</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>케이비투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>알테오젠</td>
      <td>196170</td>
      <td>혁신기술</td>
      <td>알테오젠</td>
      <td>2014-12-12</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>덱스터</td>
      <td>206560</td>
      <td>혁신기술</td>
      <td>덱스터</td>
      <td>2015-12-22</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>HLB제약</td>
      <td>047920</td>
      <td>혁신기술</td>
      <td>씨트리</td>
      <td>2015-12-21</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>신한투자증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>강스템바이오텍</td>
      <td>217730</td>
      <td>혁신기술</td>
      <td>강스템바이오텍</td>
      <td>2015-12-21</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>파크시스템스</td>
      <td>140860</td>
      <td>혁신기술</td>
      <td>파크시스템스</td>
      <td>2015-12-17</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>케이비투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>멕아이씨에스</td>
      <td>058110</td>
      <td>혁신기술</td>
      <td>멕아이씨에스</td>
      <td>2015-12-14</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>DXVX</td>
      <td>180400</td>
      <td>혁신기술</td>
      <td>엠지메드</td>
      <td>2015-11-20</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>신한투자증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>아이진</td>
      <td>185490</td>
      <td>혁신기술</td>
      <td>아이진</td>
      <td>2015-11-16</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>시지메드텍</td>
      <td>056090</td>
      <td>혁신기술</td>
      <td>유앤아이</td>
      <td>2015-11-12</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>엔케이맥스</td>
      <td>182400</td>
      <td>혁신기술</td>
      <td>에이티젠</td>
      <td>2015-10-23</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>펩트론</td>
      <td>087010</td>
      <td>혁신기술</td>
      <td>펩트론</td>
      <td>2015-07-22</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>코아스템켐온</td>
      <td>166480</td>
      <td>혁신기술</td>
      <td>코아스템</td>
      <td>2015-06-26</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>HLB제넥스</td>
      <td>187420</td>
      <td>혁신기술</td>
      <td>제노포커스</td>
      <td>2015-05-29</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>애니젠</td>
      <td>196300</td>
      <td>혁신기술</td>
      <td>애니젠</td>
      <td>2016-12-07</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>신라젠</td>
      <td>215600</td>
      <td>혁신기술</td>
      <td>신라젠</td>
      <td>2016-12-06</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사,하나증권주식회사,DB금융투자주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>퓨쳐켐</td>
      <td>220100</td>
      <td>혁신기술</td>
      <td>퓨쳐켐</td>
      <td>2016-12-01</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>얼라인드</td>
      <td>238120</td>
      <td>혁신기술</td>
      <td>로고스바이오</td>
      <td>2016-11-03</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>신한투자증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>지엘팜텍</td>
      <td>204840</td>
      <td>혁신기술</td>
      <td>IBKS제2호스팩</td>
      <td>2014-11-20</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>IBK투자증권(주)</td>
      <td>2016-10-05</td>
      <td>SPAC 존속합병</td>
    </tr>
    <tr>
      <td>아이윈플러스</td>
      <td>123010</td>
      <td>혁신기술</td>
      <td>옵토팩</td>
      <td>2016-07-20</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>IBK투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>모아라이프플러스</td>
      <td>142760</td>
      <td>혁신기술</td>
      <td>바이오리더스</td>
      <td>2016-07-07</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>팬젠</td>
      <td>222110</td>
      <td>혁신기술</td>
      <td>팬젠</td>
      <td>2016-03-11</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>큐리언트</td>
      <td>115180</td>
      <td>혁신기술</td>
      <td>큐리언트</td>
      <td>2016-02-29</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>안트로젠</td>
      <td>065660</td>
      <td>혁신기술</td>
      <td>안트로젠</td>
      <td>2016-02-15</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>휴마시스</td>
      <td>205470</td>
      <td>혁신기술</td>
      <td>하이제2호스팩</td>
      <td>2014-12-01</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>iM증권</td>
      <td>2017-10-17</td>
      <td>SPAC 존속합병</td>
    </tr>
    <tr>
      <td>앱클론</td>
      <td>174900</td>
      <td>혁신기술</td>
      <td>앱클론</td>
      <td>2017-09-18</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>어스앤에어로스페이스</td>
      <td>263540</td>
      <td>혁신기술</td>
      <td>샘코</td>
      <td>2017-09-15</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주),대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>모비스</td>
      <td>250060</td>
      <td>혁신기술</td>
      <td>하나금융8호스팩</td>
      <td>2016-09-08</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>2017-03-21</td>
      <td>SPAC 존속합병</td>
    </tr>
    <tr>
      <td>아스타</td>
      <td>246720</td>
      <td>혁신기술</td>
      <td>아스타</td>
      <td>2017-03-20</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>피씨엘</td>
      <td>241820</td>
      <td>혁신기술</td>
      <td>피씨엘</td>
      <td>2017-02-23</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>유바이오로직스</td>
      <td>206650</td>
      <td>혁신기술</td>
      <td>유바이오로직스</td>
      <td>2017-01-24</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>비피도</td>
      <td>238200</td>
      <td>혁신기술</td>
      <td>비피도</td>
      <td>2018-12-26</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>유틸렉스</td>
      <td>263050</td>
      <td>혁신기술</td>
      <td>유틸렉스</td>
      <td>2018-12-24</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>에이비엘바이오</td>
      <td>298380</td>
      <td>혁신기술</td>
      <td>에이비엘바이오</td>
      <td>2018-12-19</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>전진바이오팜</td>
      <td>110020</td>
      <td>혁신기술</td>
      <td>전진바이오팜</td>
      <td>2018-12-14</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>나무기술</td>
      <td>242040</td>
      <td>혁신기술</td>
      <td>교보비엔케이스팩</td>
      <td>2016-09-07</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>교보증권(주),(주)비엔케이투자증권</td>
      <td>2018-12-11</td>
      <td>SPAC 존속합병</td>
    </tr>
    <tr>
      <td>티앤알바이오팹</td>
      <td>246710</td>
      <td>혁신기술</td>
      <td>티앤알바이오팹</td>
      <td>2018-11-28</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>네오펙트</td>
      <td>290660</td>
      <td>혁신기술</td>
      <td>네오펙트</td>
      <td>2018-11-28</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>싸이토젠</td>
      <td>217330</td>
      <td>혁신기술</td>
      <td>싸이토젠</td>
      <td>2018-11-22</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>파멥신</td>
      <td>208340</td>
      <td>혁신기술</td>
      <td>파멥신</td>
      <td>2018-11-21</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>KB증권(주),삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>셀리버리</td>
      <td>268600</td>
      <td>사업모델</td>
      <td>셀리버리</td>
      <td>2018-11-09</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>DB금융투자주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>로보티즈</td>
      <td>108490</td>
      <td>혁신기술</td>
      <td>로보티즈</td>
      <td>2018-10-26</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>옵티팜</td>
      <td>153710</td>
      <td>혁신기술</td>
      <td>옵티팜</td>
      <td>2018-10-26</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>바이오솔루션</td>
      <td>086820</td>
      <td>혁신기술</td>
      <td>바이오솔루션</td>
      <td>2018-08-20</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>올릭스</td>
      <td>226950</td>
      <td>혁신기술</td>
      <td>올릭스</td>
      <td>2018-07-18</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>아이큐어</td>
      <td>175250</td>
      <td>혁신기술</td>
      <td>아이큐어</td>
      <td>2018-07-12</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>EDGC</td>
      <td>245620</td>
      <td>혁신기술</td>
      <td>EDGC</td>
      <td>2018-06-26</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>SK증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>유네코</td>
      <td>064510</td>
      <td>혁신기술</td>
      <td>에코마이스터</td>
      <td>2018-03-15</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주),한화투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>오스테오닉</td>
      <td>226400</td>
      <td>혁신기술</td>
      <td>오스테오닉</td>
      <td>2018-02-22</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>엔지켐생명과학</td>
      <td>183490</td>
      <td>혁신기술</td>
      <td>엔지켐생명과학</td>
      <td>2018-02-21</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>아시아종묘</td>
      <td>154030</td>
      <td>혁신기술</td>
      <td>아시아종묘</td>
      <td>2018-02-12</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>링크제니시스</td>
      <td>219420</td>
      <td>혁신기술</td>
      <td>링크제니시스</td>
      <td>2018-02-05</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>CJ 바이오사이언스</td>
      <td>311690</td>
      <td>혁신기술</td>
      <td>천랩</td>
      <td>2019-12-26</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>브릿지바이오</td>
      <td>288330</td>
      <td>사업모델</td>
      <td>브릿지바이오</td>
      <td>2019-12-20</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주),KB증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>메드팩토</td>
      <td>235980</td>
      <td>혁신기술</td>
      <td>메드팩토</td>
      <td>2019-12-19</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>신테카바이오</td>
      <td>226330</td>
      <td>사업모델</td>
      <td>신테카바이오</td>
      <td>2019-12-17</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>KB증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>제이엘케이</td>
      <td>322510</td>
      <td>혁신기술</td>
      <td>제이엘케이인스펙션</td>
      <td>2019-12-11</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>티움바이오</td>
      <td>321550</td>
      <td>혁신기술</td>
      <td>티움바이오</td>
      <td>2019-11-22</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>자비스</td>
      <td>254120</td>
      <td>혁신기술</td>
      <td>IBKS제5호스팩</td>
      <td>2016-12-02</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>IBK투자증권(주)</td>
      <td>2019-11-15</td>
      <td>SPAC 존속합병</td>
    </tr>
    <tr>
      <td>라파스</td>
      <td>214260</td>
      <td>사업모델</td>
      <td>라파스</td>
      <td>2019-11-11</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>DB금융투자주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>미디어젠</td>
      <td>279600</td>
      <td>혁신기술</td>
      <td>미디어젠</td>
      <td>2019-11-05</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>교보증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>캐리소프트</td>
      <td>317530</td>
      <td>혁신기술</td>
      <td>캐리소프트</td>
      <td>2019-10-29</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>엔바이오니아</td>
      <td>317870</td>
      <td>혁신기술</td>
      <td>엔바이오니아</td>
      <td>2019-10-24</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>올리패스</td>
      <td>244460</td>
      <td>사업모델</td>
      <td>올리패스</td>
      <td>2019-09-20</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사,키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>라닉스</td>
      <td>317120</td>
      <td>사업모델</td>
      <td>라닉스</td>
      <td>2019-09-18</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>나노브릭</td>
      <td>286750</td>
      <td>혁신기술</td>
      <td>나노브릭</td>
      <td>2019-08-19</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>KB증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>플리토</td>
      <td>300080</td>
      <td>혁신기술</td>
      <td>플리토</td>
      <td>2019-07-17</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>압타바이오</td>
      <td>293780</td>
      <td>혁신기술</td>
      <td>압타바이오</td>
      <td>2019-06-12</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사,삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>마이크로디지탈</td>
      <td>305090</td>
      <td>혁신기술</td>
      <td>마이크로디지탈</td>
      <td>2019-06-05</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>수젠텍</td>
      <td>253840</td>
      <td>혁신기술</td>
      <td>수젠텍</td>
      <td>2019-05-28</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>아모그린텍</td>
      <td>125210</td>
      <td>혁신기술</td>
      <td>아모그린텍</td>
      <td>2019-03-29</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>지노믹트리</td>
      <td>228760</td>
      <td>혁신기술</td>
      <td>지노믹트리</td>
      <td>2019-03-27</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>셀리드</td>
      <td>299660</td>
      <td>혁신기술</td>
      <td>셀리드</td>
      <td>2019-02-20</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>SCL사이언스</td>
      <td>246960</td>
      <td>혁신기술</td>
      <td>이노테라피</td>
      <td>2019-02-01</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>지놈앤컴퍼니</td>
      <td>314130</td>
      <td>혁신기술</td>
      <td>지놈앤컴퍼니</td>
      <td>2020-12-23</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>석경에이티</td>
      <td>357550</td>
      <td>혁신기술</td>
      <td>석경에이티</td>
      <td>2020-12-23</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>프리시젼바이오</td>
      <td>335810</td>
      <td>혁신기술</td>
      <td>프리시젼바이오</td>
      <td>2020-12-22</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>알체라</td>
      <td>347860</td>
      <td>사업모델</td>
      <td>알체라</td>
      <td>2020-12-21</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>신영증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>엔젠바이오</td>
      <td>354200</td>
      <td>혁신기술</td>
      <td>엔젠바이오</td>
      <td>2020-12-10</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>퀀타매트릭스</td>
      <td>317690</td>
      <td>혁신기술</td>
      <td>퀀타매트릭스</td>
      <td>2020-12-09</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>클리노믹스</td>
      <td>352770</td>
      <td>사업모델</td>
      <td>클리노믹스</td>
      <td>2020-12-04</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>고바이오랩</td>
      <td>348150</td>
      <td>사업모델</td>
      <td>고바이오랩</td>
      <td>2020-11-18</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주),삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>센코</td>
      <td>347000</td>
      <td>혁신기술</td>
      <td>센코</td>
      <td>2020-10-29</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>바이브컴퍼니</td>
      <td>301300</td>
      <td>혁신기술</td>
      <td>바이브컴퍼니</td>
      <td>2020-10-28</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>미코바이오메드</td>
      <td>214610</td>
      <td>혁신기술</td>
      <td>미코바이오메드</td>
      <td>2020-10-22</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>KB증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>피플바이오</td>
      <td>304840</td>
      <td>혁신기술</td>
      <td>피플바이오</td>
      <td>2020-10-19</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>넥스틴</td>
      <td>348210</td>
      <td>혁신기술</td>
      <td>넥스틴</td>
      <td>2020-10-08</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>KB증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>박셀바이오</td>
      <td>323990</td>
      <td>혁신기술</td>
      <td>박셀바이오</td>
      <td>2020-09-22</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>압타머사이언스</td>
      <td>291650</td>
      <td>사업모델</td>
      <td>압타머사이언스</td>
      <td>2020-09-16</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>이오플로우</td>
      <td>294090</td>
      <td>사업모델</td>
      <td>이오플로우</td>
      <td>2020-09-14</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>셀레믹스</td>
      <td>331920</td>
      <td>사업모델</td>
      <td>셀레믹스</td>
      <td>2020-08-21</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>제놀루션</td>
      <td>225220</td>
      <td>사업모델</td>
      <td>제놀루션</td>
      <td>2020-07-24</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>신영증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>솔트룩스</td>
      <td>304100</td>
      <td>혁신기술</td>
      <td>솔트룩스</td>
      <td>2020-07-23</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>소마젠</td>
      <td>950200</td>
      <td>혁신기술</td>
      <td>소마젠</td>
      <td>2020-07-13</td>
      <td>신규상장</td>
      <td>주식예탁증권</td>
      <td>미국</td>
      <td>신한투자증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>젠큐릭스</td>
      <td>229000</td>
      <td>혁신기술</td>
      <td>젠큐릭스</td>
      <td>2020-06-25</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>에스씨엠생명과학</td>
      <td>298060</td>
      <td>혁신기술</td>
      <td>에스씨엠생명과학</td>
      <td>2020-06-17</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>카이노스메드</td>
      <td>284620</td>
      <td>혁신기술</td>
      <td>하나금융11호스팩</td>
      <td>2018-06-08</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>2020-06-08</td>
      <td>SPAC 존속합병</td>
    </tr>
    <tr>
      <td>레몬</td>
      <td>294140</td>
      <td>혁신기술</td>
      <td>레몬</td>
      <td>2020-02-28</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>서남</td>
      <td>294630</td>
      <td>혁신기술</td>
      <td>서남</td>
      <td>2020-02-20</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>툴젠</td>
      <td>199800</td>
      <td>혁신기술</td>
      <td>툴젠</td>
      <td>2021-12-10</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>마음AI</td>
      <td>377480</td>
      <td>혁신기술</td>
      <td>마인즈랩</td>
      <td>2021-11-23</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사,하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>지오엘리먼트</td>
      <td>311320</td>
      <td>혁신기술</td>
      <td>지오엘리먼트</td>
      <td>2021-11-11</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>스카이월드와이드</td>
      <td>357880</td>
      <td>혁신기술</td>
      <td>비트나인</td>
      <td>2021-11-10</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>지니너스</td>
      <td>389030</td>
      <td>혁신기술</td>
      <td>지니너스</td>
      <td>2021-11-08</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>차백신연구소</td>
      <td>261780</td>
      <td>혁신기술</td>
      <td>차백신연구소</td>
      <td>2021-10-22</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>에이비온</td>
      <td>203400</td>
      <td>혁신기술</td>
      <td>에이비온</td>
      <td>2021-09-08</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사,한화투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>바이젠셀</td>
      <td>308080</td>
      <td>혁신기술</td>
      <td>바이젠셀</td>
      <td>2021-08-25</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주),KB증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>딥노이드</td>
      <td>315640</td>
      <td>혁신기술</td>
      <td>딥노이드</td>
      <td>2021-08-17</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>KB증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>원티드랩</td>
      <td>376980</td>
      <td>사업모델</td>
      <td>원티드랩</td>
      <td>2021-08-11</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>비트맥스</td>
      <td>377030</td>
      <td>혁신기술</td>
      <td>맥스트</td>
      <td>2021-07-27</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>큐라클</td>
      <td>365270</td>
      <td>혁신기술</td>
      <td>큐라클</td>
      <td>2021-07-22</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>오비고</td>
      <td>352910</td>
      <td>혁신기술</td>
      <td>오비고</td>
      <td>2021-07-13</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>아모센스</td>
      <td>357580</td>
      <td>혁신기술</td>
      <td>아모센스</td>
      <td>2021-06-25</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>신한투자증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>라온테크</td>
      <td>232680</td>
      <td>혁신기술</td>
      <td>라온테크</td>
      <td>2021-06-17</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>KB증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>진시스템</td>
      <td>363250</td>
      <td>사업모델</td>
      <td>진시스템</td>
      <td>2021-05-26</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>삼영에스앤씨</td>
      <td>361670</td>
      <td>사업모델</td>
      <td>삼영에스앤씨</td>
      <td>2021-05-21</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>샘씨엔에스</td>
      <td>252990</td>
      <td>혁신기술</td>
      <td>샘씨엔에스</td>
      <td>2021-05-20</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>해성에어로보틱스</td>
      <td>059270</td>
      <td>혁신기술</td>
      <td>해성티피씨</td>
      <td>2021-04-21</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>자이언트스텝</td>
      <td>289220</td>
      <td>혁신기술</td>
      <td>자이언트스텝</td>
      <td>2021-03-24</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>제노코</td>
      <td>361390</td>
      <td>혁신기술</td>
      <td>제노코</td>
      <td>2021-03-24</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>DB금융투자주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>라이프시맨틱스</td>
      <td>347700</td>
      <td>혁신기술</td>
      <td>라이프시맨틱스</td>
      <td>2021-03-23</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>네오이뮨텍</td>
      <td>950220</td>
      <td>혁신기술</td>
      <td>네오이뮨텍</td>
      <td>2021-03-16</td>
      <td>신규상장</td>
      <td>주식예탁증권</td>
      <td>미국</td>
      <td>미래에셋증권 주식회사,하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>프레스티지바이오로직스</td>
      <td>334970</td>
      <td>사업모델</td>
      <td>프레스티지바이오로직스</td>
      <td>2021-03-11</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사,유안타증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>나노씨엠에스</td>
      <td>247660</td>
      <td>혁신기술</td>
      <td>나노씨엠에스</td>
      <td>2021-03-09</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>뷰노</td>
      <td>338220</td>
      <td>혁신기술</td>
      <td>뷰노</td>
      <td>2021-02-26</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사,삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>씨이랩</td>
      <td>189330</td>
      <td>혁신기술</td>
      <td>씨이랩</td>
      <td>2021-02-24</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>IBK투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>피엔에이치테크</td>
      <td>239890</td>
      <td>혁신기술</td>
      <td>피엔에이치테크</td>
      <td>2021-02-16</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>레인보우로보틱스</td>
      <td>277810</td>
      <td>사업모델</td>
      <td>레인보우로보틱스</td>
      <td>2021-02-03</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주),미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>아티스트유나이티드</td>
      <td>321820</td>
      <td>혁신기술</td>
      <td>와이더플래닛</td>
      <td>2021-02-03</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>SAMG엔터</td>
      <td>419530</td>
      <td>혁신기술</td>
      <td>SAMG엔터</td>
      <td>2022-12-06</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>인벤티지랩</td>
      <td>389470</td>
      <td>혁신기술</td>
      <td>인벤티지랩</td>
      <td>2022-11-22</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>엔젯</td>
      <td>419080</td>
      <td>혁신기술</td>
      <td>엔젯</td>
      <td>2022-11-18</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>뉴로메카</td>
      <td>348340</td>
      <td>혁신기술</td>
      <td>뉴로메카</td>
      <td>2022-11-04</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>플라즈맵</td>
      <td>405000</td>
      <td>혁신기술</td>
      <td>플라즈맵</td>
      <td>2022-10-21</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>핀텔</td>
      <td>291810</td>
      <td>혁신기술</td>
      <td>핀텔</td>
      <td>2022-10-20</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>샤페론</td>
      <td>378800</td>
      <td>혁신기술</td>
      <td>샤페론</td>
      <td>2022-10-19</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>에스비비테크</td>
      <td>389500</td>
      <td>혁신기술</td>
      <td>에스비비테크</td>
      <td>2022-10-17</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>선바이오</td>
      <td>067370</td>
      <td>사업모델</td>
      <td>선바이오</td>
      <td>2022-10-05</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>아이씨에이치</td>
      <td>368600</td>
      <td>혁신기술</td>
      <td>아이씨에이치</td>
      <td>2022-07-29</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>에이프릴바이오</td>
      <td>397030</td>
      <td>혁신기술</td>
      <td>에이프릴바이오</td>
      <td>2022-07-28</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>루닛</td>
      <td>328130</td>
      <td>혁신기술</td>
      <td>루닛</td>
      <td>2022-07-21</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>와이씨켐</td>
      <td>112290</td>
      <td>혁신기술</td>
      <td>영창케미칼</td>
      <td>2022-07-14</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>코난테크놀로지</td>
      <td>402030</td>
      <td>혁신기술</td>
      <td>코난테크놀로지</td>
      <td>2022-07-07</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>넥스트칩</td>
      <td>396270</td>
      <td>혁신기술</td>
      <td>넥스트칩</td>
      <td>2022-07-01</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>원텍</td>
      <td>336570</td>
      <td>혁신기술</td>
      <td>대신밸런스제8호스팩</td>
      <td>2019-12-19</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>2022-06-30</td>
      <td>SPAC 존속합병</td>
    </tr>
    <tr>
      <td>보로노이</td>
      <td>310210</td>
      <td>혁신기술</td>
      <td>보로노이</td>
      <td>2022-06-24</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주),미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>레이저쎌</td>
      <td>412350</td>
      <td>혁신기술</td>
      <td>레이저쎌</td>
      <td>2022-06-24</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>비큐AI</td>
      <td>148780</td>
      <td>혁신기술</td>
      <td>비플라이소프트</td>
      <td>2022-06-20</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>IBK투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>하이딥</td>
      <td>365590</td>
      <td>혁신기술</td>
      <td>엔에이치스팩18호</td>
      <td>2020-12-21</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>2022-05-12</td>
      <td>SPAC 존속합병</td>
    </tr>
    <tr>
      <td>모아데이타</td>
      <td>288980</td>
      <td>혁신기술</td>
      <td>모아데이타</td>
      <td>2022-03-10</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>노을</td>
      <td>376930</td>
      <td>혁신기술</td>
      <td>노을</td>
      <td>2022-03-03</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주),삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>풍원정밀</td>
      <td>371950</td>
      <td>혁신기술</td>
      <td>풍원정밀</td>
      <td>2022-02-28</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>퓨런티어</td>
      <td>370090</td>
      <td>혁신기술</td>
      <td>퓨런티어</td>
      <td>2022-02-23</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>신한투자증권 주식회사,유안타증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>바이오에프디엔씨</td>
      <td>251120</td>
      <td>혁신기술</td>
      <td>바이오에프디엔씨</td>
      <td>2022-02-21</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>DB금융투자주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>스코넥</td>
      <td>276040</td>
      <td>혁신기술</td>
      <td>스코넥</td>
      <td>2022-02-04</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>신영증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>이지트로닉스</td>
      <td>377330</td>
      <td>혁신기술</td>
      <td>이지트로닉스</td>
      <td>2022-02-04</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>애드바이오텍</td>
      <td>179530</td>
      <td>혁신기술</td>
      <td>애드바이오텍</td>
      <td>2022-01-24</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>와이바이오로직스</td>
      <td>338840</td>
      <td>혁신기술</td>
      <td>와이바이오로직스</td>
      <td>2023-12-05</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>유안타증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>에이텀</td>
      <td>355690</td>
      <td>혁신기술</td>
      <td>에이텀</td>
      <td>2023-12-01</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>그린리소스</td>
      <td>402490</td>
      <td>혁신기술</td>
      <td>그린리소스</td>
      <td>2023-11-24</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>큐로셀</td>
      <td>372320</td>
      <td>혁신기술</td>
      <td>큐로셀</td>
      <td>2023-11-09</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사,삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>컨텍</td>
      <td>451760</td>
      <td>혁신기술</td>
      <td>컨텍</td>
      <td>2023-11-09</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>쏘닉스</td>
      <td>088280</td>
      <td>혁신기술</td>
      <td>쏘닉스</td>
      <td>2023-11-07</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>KB증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>세니젠</td>
      <td>188260</td>
      <td>혁신기술</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>퀄리타스반도체</td>
      <td>432720</td>
      <td>혁신기술</td>
      <td>퀄리타스반도체</td>
      <td>2023-10-27</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>아이엠티</td>
      <td>451220</td>
      <td>혁신기술</td>
      <td>아이엠티</td>
      <td>2023-10-10</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>유안타증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>코어라인소프트</td>
      <td>384470</td>
      <td>혁신기술</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>크라우드웍스</td>
      <td>355390</td>
      <td>혁신기술</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>시큐레터</td>
      <td>418250</td>
      <td>혁신기술</td>
      <td>시큐레터</td>
      <td>2023-08-24</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>스마트레이더시스템</td>
      <td>424960</td>
      <td>혁신기술</td>
      <td>스마트레이더시스템</td>
      <td>2023-08-22</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>큐리옥스바이오시스템즈</td>
      <td>445680</td>
      <td>혁신기술</td>
      <td>큐리옥스바이오시스템즈</td>
      <td>2023-08-10</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>파두</td>
      <td>440110</td>
      <td>혁신기술</td>
      <td>파두</td>
      <td>2023-08-07</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주),엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>시지트로닉스</td>
      <td>429270</td>
      <td>혁신기술</td>
      <td>시지트로닉스</td>
      <td>2023-08-03</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>유안타증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>파로스아이바이오</td>
      <td>388870</td>
      <td>혁신기술</td>
      <td>파로스아이바이오</td>
      <td>2023-07-27</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>버넥트</td>
      <td>438700</td>
      <td>혁신기술</td>
      <td>버넥트</td>
      <td>2023-07-26</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>와이랩</td>
      <td>432430</td>
      <td>사업모델</td>
      <td>와이랩</td>
      <td>2023-07-20</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>센서뷰</td>
      <td>321370</td>
      <td>혁신기술</td>
      <td>센서뷰</td>
      <td>2023-07-19</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>이노시뮬레이션</td>
      <td>274400</td>
      <td>혁신기술</td>
      <td>이노시뮬레이션</td>
      <td>2023-07-06</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>오픈놀</td>
      <td>440320</td>
      <td>혁신기술</td>
      <td>오픈놀</td>
      <td>2023-06-30</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>프로티아</td>
      <td>303360</td>
      <td>혁신기술</td>
      <td>프로테옴텍</td>
      <td>2023-06-16</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>큐라티스</td>
      <td>348080</td>
      <td>혁신기술</td>
      <td>큐라티스</td>
      <td>2023-06-15</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주),신영증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>씨유박스</td>
      <td>340810</td>
      <td>혁신기술</td>
      <td>씨유박스</td>
      <td>2023-05-19</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>신한투자증권 주식회사,SK증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>모니터랩</td>
      <td>434480</td>
      <td>혁신기술</td>
      <td>모니터랩</td>
      <td>2023-05-19</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>에스바이오메딕스</td>
      <td>304360</td>
      <td>혁신기술</td>
      <td>에스바이오메딕스</td>
      <td>2023-05-04</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>마이크로투나노</td>
      <td>424980</td>
      <td>혁신기술</td>
      <td>마이크로투나노</td>
      <td>2023-04-26</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>지아이이노베이션</td>
      <td>358570</td>
      <td>혁신기술</td>
      <td>지아이이노베이션</td>
      <td>2023-03-30</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사,하나증권주식회사,삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>라온텍</td>
      <td>418420</td>
      <td>혁신기술</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>파인메딕스</td>
      <td>387570</td>
      <td>혁신기술</td>
      <td>파인메딕스</td>
      <td>2024-12-26</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>엠에프씨</td>
      <td>432980</td>
      <td>혁신기술</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>쓰리에이로직스</td>
      <td>177900</td>
      <td>혁신기술</td>
      <td>쓰리에이로직스</td>
      <td>2024-12-24</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>신한투자증권 주식회사,미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>온코닉테라퓨틱스</td>
      <td>476060</td>
      <td>혁신기술</td>
      <td>온코닉테라퓨틱스</td>
      <td>2024-12-19</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>온코크로스</td>
      <td>382150</td>
      <td>혁신기술</td>
      <td>온코크로스</td>
      <td>2024-12-18</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>유디엠텍</td>
      <td>389680</td>
      <td>혁신기술</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>쓰리빌리언</td>
      <td>394800</td>
      <td>혁신기술</td>
      <td>쓰리빌리언</td>
      <td>2024-11-14</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>에어레인</td>
      <td>163280</td>
      <td>혁신기술</td>
      <td>에어레인</td>
      <td>2024-11-08</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>신영증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>토모큐브</td>
      <td>475960</td>
      <td>혁신기술</td>
      <td>토모큐브</td>
      <td>2024-11-07</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>에이치이엠파마</td>
      <td>376270</td>
      <td>혁신기술</td>
      <td>에이치이엠파마</td>
      <td>2024-11-05</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>신한투자증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>클로봇</td>
      <td>466100</td>
      <td>혁신기술</td>
      <td>클로봇</td>
      <td>2024-10-28</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>웨이비스</td>
      <td>289930</td>
      <td>혁신기술</td>
      <td>웨이비스</td>
      <td>2024-10-25</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>씨메스</td>
      <td>475400</td>
      <td>혁신기술</td>
      <td>씨메스</td>
      <td>2024-10-24</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>유진투자증권(주),삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>루미르</td>
      <td>474170</td>
      <td>혁신기술</td>
      <td>루미르</td>
      <td>2024-10-21</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>셀비온</td>
      <td>308430</td>
      <td>혁신기술</td>
      <td>셀비온</td>
      <td>2024-10-16</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>아이언디바이스</td>
      <td>464500</td>
      <td>혁신기술</td>
      <td>아이언디바이스</td>
      <td>2024-09-23</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>이엔셀</td>
      <td>456070</td>
      <td>혁신기술</td>
      <td>이엔셀</td>
      <td>2024-08-23</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>넥스트바이오메디컬</td>
      <td>389650</td>
      <td>혁신기술</td>
      <td>넥스트바이오메디컬</td>
      <td>2024-08-20</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>케이쓰리아이</td>
      <td>431190</td>
      <td>혁신기술</td>
      <td>케이쓰리아이</td>
      <td>2024-08-20</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>하나증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>뱅크웨어글로벌</td>
      <td>199480</td>
      <td>혁신기술</td>
      <td>뱅크웨어글로벌</td>
      <td>2024-08-12</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>아이빔테크놀로지</td>
      <td>460470</td>
      <td>혁신기술</td>
      <td>아이빔테크놀로지</td>
      <td>2024-08-06</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>피앤에스미캐닉스</td>
      <td>460940</td>
      <td>혁신기술</td>
      <td>피앤에스미캐닉스</td>
      <td>2024-07-31</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>키움증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>엑셀세라퓨틱스</td>
      <td>373110</td>
      <td>혁신기술</td>
      <td>엑셀세라퓨틱스</td>
      <td>2024-07-15</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>하스</td>
      <td>450330</td>
      <td>혁신기술</td>
      <td>하스</td>
      <td>2024-07-03</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>이노스페이스</td>
      <td>462350</td>
      <td>혁신기술</td>
      <td>이노스페이스</td>
      <td>2024-07-02</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>미래에셋증권 주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>에이치브이엠</td>
      <td>295310</td>
      <td>혁신기술</td>
      <td>에이치브이엠</td>
      <td>2024-06-28</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>엔에이치투자증권주식회사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>에스오에스랩</td>
      <td>464080</td>
      <td>혁신기술</td>
      <td>에스오에스랩</td>
      <td>2024-06-25</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>한중엔시에스</td>
      <td>107640</td>
      <td>혁신기술</td>
      <td>한중엔시에스</td>
      <td>2024-06-24</td>
      <td>이전상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>IBK투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>씨어스테크놀로지</td>
      <td>458870</td>
      <td>혁신기술</td>
      <td>씨어스테크놀로지</td>
      <td>2024-06-19</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>라메디텍</td>
      <td>462510</td>
      <td>혁신기술</td>
      <td>라메디텍</td>
      <td>2024-06-17</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>대신증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>오름테라퓨틱</td>
      <td>475830</td>
      <td>혁신기술</td>
      <td>오름테라퓨틱</td>
      <td>2025-02-14</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>아이에스티이</td>
      <td>212710</td>
      <td>혁신기술</td>
      <td>아이에스티이</td>
      <td>2025-02-12</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>KB증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>아이지넷</td>
      <td>462980</td>
      <td>사업모델</td>
      <td>아이지넷</td>
      <td>2025-02-04</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>한국투자증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>와이즈넛</td>
      <td>096250</td>
      <td>혁신기술</td>
      <td>와이즈넛</td>
      <td>2025-01-24</td>
      <td>신규상장</td>
      <td>주권</td>
      <td>대한민국</td>
      <td>삼성증권(주)</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</pre>


간단할 줄 알알았던 이 과제는 이토록 먼길을 돌아오게 되었습니다. 2014년 전에 상장한 기술기업 목록이 한국거래소에서는 제공되지 않아서 인터넷을 검색하던 중, 기술성장 트랙 상장에 대해 컨설팅을 제공하는 업체의 사이트를 우연히 방문하게 되었습니다. 여기의 Top조회 게시물은 기술성장기업의 목록이었습니다. 투자의 목적이든 상장을 준비하는 회사의 입장이던 시장에서 충분히 궁금해할 만한 수요있는 정보라는 생각이 들었습니다. 앞으로도 시장을 더 알아가는 컨텐츠를 만들어보겠습니다. <br>

![rise]({{site.url}}/assets/images/2025-03-01-listing/rise.png)<br><br>

