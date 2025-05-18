---
layout: single
title:  "의결권 원기옥을 모으기 위해서는 대리인이 필요하다?"
categories: 한국시장
tag: [data background, 주주총회]
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


## 티끌모아 태산!

의결권 원기옥을 모으기 위해서는 의결권을 가진 주주를 **하나하나 찾아가서 설득할 대리인**{: style="color: #4682B4;"}이 필요합니다. 주주 한 명의 의결권은 작은 에너지에 불과합니다. 이를 한데 모아 '원기옥'급의 막강한 의결권 파워를 만들려면, 권유업무 대리인과 의결권 행사 대리인의 촘촘한 네트워크가 필수적입니다. <br>
![12dragonball]({{site.url}}/assets/images/2025-05-15-proxy/12dragonball.png)<br><br>

손오공이 마인부우와 최후의 전투를 벌일때가 기억나시나요? 손오공이 원기옥을 모으기 위해 손을 들어달라고 지구인들에게 부탁했지만, 지구인들은 무서워서 손을 들지 않았습니다. 그러다가 **지구인의 히어로 미스터사탄이 모두 손을 들어달라**{: style="color: #4682B4;"}고 한마디 하자, 모두가 손을 들었고 바로 거대한 원기옥이 완성되었습니다. **미스터사탄은 원기옥의 훌륭한 권유 대리인**{: style="color: #4682B4;"}이었던 것입니다.<br><br>

![11process]({{site.url}}/assets/images/2025-05-15-proxy/11process.png)<br><br>
위의 프로세스 도식을 보면, 대리인이 없이는 수많은 주주의 의결권을 효과적으로 연결·관리할 수 없다는 사실이 한눈에 들어옵니다.

* **피권유자(주주)**{: style="color: #4682B4;"}<br>
개별 주주는 스스로 주총장에 가지 않고, 위임장에 서명·날인해 권유업무 대리인에게 전달합니다. 전자적인 방식으로 한다면 더욱 간편하게 위임할 수 있을 것입니다.

* **권유업무 대리인**{: style="color: #4682B4;"}<br>
주주로부터 위임장을 수집해 권유자에게 회수하고, 추가 안내나 질문 대응도 담당합니다. 발로 뛰며 위임장을 받아와야 하는 특성상 많은 부담이 생길 수 밖에 없습니다. 따라서 권유업무 대리를 사업으로 하는 다수의 사업체가 존재합니다. 사업체의 사례는 추후 살펴보도록 하겠습니다.

* **권유자(공시제출인)**{: style="color: #4682B4;"}<br>
모인 위임장을 바탕으로 '의결권'을 완성하였습니다. 손오공은 직접 원기옥을 날릴 수도 있고, 의결권 행사 대리인에게 위임권을 배분할 수도 있습니다. 

* **의결권 행사 대리인(수임인)**{: style="color: #4682B4;"}<br>
손오공이 원기옥을 모으더라도 직접 원기옥을 날리지 않은 사례도 있습니다. 베지터와의 전투에서 손오반이 원기옥을 쳐내서 베지터에게 원기옥으로 일격을 가한적도 있고, 손오공이 초사이어인으로 변신하기 전에 고전하던 손오공을 대신하여 크리링이 손오공이 모은 원기옥을 날린 적도 있습니다.<br>
의결권 행사 대리인은 이렇듯 권유자로부터 위임받은 의결권을 실제 주총장에서 행사해, 최종 의결권 에너지를 발산합니다.<br><br>

이 과정을 다시 드래곤볼로 비유하자면,
"수백 명이 모여 각자 작은 에너지를 불어넣고, 최종 한 사람에게 모두 집중시켜 '원기옥'을 발사한다"는 느낌입니다. 대리인이 없다면 각 주주의 의결권은 흩어질 뿐이고, 권유자가 원하는 방향으로 힘을 모으는 것은 불가능합니다. 권유업무 대리인이 주주와 권유자 사이를 잇고, 의결권 행사 대리인이 그 에너지를 최종 발산하는 구조가 '의결권 원기옥'을 완성하는 핵심 동력입니다.


## 가장 많은 대리인이 있었던 곳은 어디일까?
![13histo]({{site.url}}/assets/images/2025-05-15-proxy/13histo.png)<br><br>
2023~2025년5월까지의 주주총회 개최 건수 중 의결권 대리행사 권유를 위해 대리인을 선임한 경우는 공시기준으로 109건이 확인되었습니다. 약 2,500사의 상장사가 3년치 개최한 주주총회에 비하면 대리행사 권유를 위해 대리인을 선임하는 건수는 매우 적음을 알 수 있습니다. <br>
정족수 확보 또는 Proxy Fight의 승리가 절실한 회사일 수록 돈이 들더라도 대리인을 많이 선임하여 표를 확보하려 했을 텐데요, 전체 분포는 위의 그림과 같습니다. 2인(또는 2사)이상의 대리인을 선임한 경우는 39건이 있었습니다.

### 권유에 진심이었을까?
미스터 사탄이 지구인들에게 원기옥을 위해 손을 들라고 하기 바로 직전, 베지터가 지구인들에게 윽박지르며 손을 들라고 한적이 있습니다. 결과는 모두의 외면이었지요. 의결권 대리행사 권유도 마찬가지입니다. **의결권을 갖고 있는 주주에게 얼마나 그 목적을 잘 설명하느냐, 얼마나 노력을 들이느냐, 얼마나 전문적으로 수행하느냐가 권유의 성공으로 이어지는 핵심사항**{: style="color: #4682B4;"}일 것입니다. 아래의 사항은 권유가 실제 위임으로 이어지기까지 어떤 요소가 필요한지에 대해서 세워본 가정입니다.
* 아무래도 대리행사 **권유 대리인의 수가 많을 수록** 접점이 넓어지므로 권유가 더 잘 될 것이라는 가정
* 아무래도 대리행사 **권유를 사업으로 하는 회사**가 개인이 직접 발로 뛰며 권유하는 것보다는 잘 할 것이라는 가정
* 아무래도 대리행사 **권유를 하는 취지를 구구절절 설명**해놓을 수록 좀 더 진정성 있어 보일 것이라는 가정
* **전자위임 등 위임을 위한 절차를 편하게 해놓을 수록** 권유절차가 더 수월할 것이라는 가정

### 대리인이 많을 수록 좋은 것일까?
위의 가정들을 한번 확인해보도록 하겠습니다. 숫자 기준으로 가장 많은 대리인을 선임한 주주총회를 기준으로 10개의 주주총회를 내림차순으로 보았습니다. 결론부터 보자면, **대리인이 많은 곳은 전문 업체보다는 지분이 없는 직원들이 권유업무를 하는 경우**{: style="color: #4682B4;"}들이었습니다. <br>
가장 많은 대리인의 숫자를 기록한 코스닥 상장사 아이에이의 경우, 직원이 21명 동원되었으며, 권유하는 취지를 설명한 내용은 26자에 불과하였습니다. 그러나 전자위임장이 가능하게 하여 편의성을 고려한 측면은 있었습니다.<br>
또한 눈에 띄는 점은 삼성전기가 3번의 주주총회에 걸쳐 등장한다는 점이었습니다. 상당한 규모의 대기업인데 대리 업체를 이용하지 않고 직원들이 발로 뛴다니 조금 의아하기도 합니다. 내용을 살펴보니 정기주총때마다 정예 7인의 직원이 의결권 대리행사 권유를 수행하고 있습니다. 또한 전자위임도 불가능하고, 권유의 취지도 30자 미만으로 빈약하였습니다.

---
* 시장: 코스닥, 종목코드: 038880, 상장회사명: 아이에이  
* 주주총회일: 20250328  
* 전체 대리인의 수: 21명, 권유를 대리하는 개인의 수: 21명  
* 전자투표 가능여부: 전자투표 가능, 전자위임 가능여부: 전자위임장 가능  
* 권유문구 글자수: 26  
* URL: [공시원문 링크](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20250312000709)
<pre>
<table border="1" class="dataframe dataframe">  
  <thead>  
    <tr style="text-align: right;">  
      <th>상장회사명</th>  
      <th>권유공시 제출인</th>  
      <th>대리인</th>  
      <th>대리인 회사 관계</th>  
      <th>대리인 권유자 관계</th>  
      <th>대리인 구분</th>  
      <th>대리인 보유 주식종류</th>  
      <th>대리인 보유 주식수</th>  
    </tr>  
  </thead>  
  <tbody>  
    <tr>  
      <td>아이에이</td>  
      <td>아이에이</td>  
      <td>이한국</td>  
      <td>0</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>아이에이</td>  
      <td>아이에이</td>  
      <td>강영범</td>  
      <td>0</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>아이에이</td>  
      <td>아이에이</td>  
      <td>권수영</td>  
      <td>0</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>아이에이</td>  
      <td>아이에이</td>  
      <td>권준영</td>  
      <td>0</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>아이에이</td>  
      <td>아이에이</td>  
      <td>김성기</td>  
      <td>0</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>아이에이</td>  
      <td>아이에이</td>  
      <td>김정태</td>  
      <td>0</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>아이에이</td>  
      <td>아이에이</td>  
      <td>김지애</td>  
      <td>0</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>아이에이</td>  
      <td>아이에이</td>  
      <td>민지영</td>  
      <td>0</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>아이에이</td>  
      <td>아이에이</td>  
      <td>박문순</td>  
      <td>0</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>아이에이</td>  
      <td>아이에이</td>  
      <td>석굴암</td>  
      <td>0</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>아이에이</td>  
      <td>아이에이</td>  
      <td>안용선</td>  
      <td>0</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>아이에이</td>  
      <td>아이에이</td>  
      <td>유지우</td>  
      <td>0</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>아이에이</td>  
      <td>아이에이</td>  
      <td>이창섭</td>  
      <td>0</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>아이에이</td>  
      <td>아이에이</td>  
      <td>임태암</td>  
      <td>0</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>아이에이</td>  
      <td>아이에이</td>  
      <td>임태장</td>  
      <td>0</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>아이에이</td>  
      <td>아이에이</td>  
      <td>장윤정</td>  
      <td>0</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>아이에이</td>  
      <td>아이에이</td>  
      <td>전승준</td>  
      <td>0</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>아이에이</td>  
      <td>아이에이</td>  
      <td>정유훈</td>  
      <td>0</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>아이에이</td>  
      <td>아이에이</td>  
      <td>정은욱</td>  
      <td>0</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>아이에이</td>  
      <td>아이에이</td>  
      <td>최종승</td>  
      <td>0</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>아이에이</td>  
      <td>아이에이</td>  
      <td>홍정기</td>  
      <td>0</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>0</td>  
    </tr>  
  </tbody>  
</table>  
</pre>

---
* 시장: 코스피, 종목코드: 175330, 상장회사명: JB금융지주  
* 주주총회일: 20240328  
* 전체 대리인의 수: 13명, 권유를 대리하는 개인의 수: 11명  
* 전자투표 가능여부: 전자투표 가능, 전자위임 가능여부: 전자위임장 가능  
* 권유문구 글자수: 988  
* URL: [공시원문 링크](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20240305000235)
<pre>
<table border="1" class="dataframe dataframe">  
  <thead>  
    <tr style="text-align: right;">  
      <th>상장회사명</th>  
      <th>권유공시 제출인</th>  
      <th>대리인</th>  
      <th>대리인 회사 관계</th>  
      <th>대리인 권유자 관계</th>  
      <th>대리인 구분</th>  
      <th>대리인 보유 주식종류</th>  
      <th>대리인 보유 주식수</th>  
    </tr>  
  </thead>  
  <tbody>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>머로우소달리코리아 유한회사</td>  
      <td>없음</td>  
      <td>없음</td>  
      <td>법인</td>  
      <td>-</td>  
      <td>-</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>주식회사 로코모티브</td>  
      <td>없음</td>  
      <td>없음</td>  
      <td>법인</td>  
      <td>-</td>  
      <td>-</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>방극봉</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>10,093</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>김영석</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>1,113</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>김태현</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>14,474</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>임양진</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>-</td>  
      <td>-</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>조계준</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>6,250</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>김두봉</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>-</td>  
      <td>-</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>마광수</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>7,142</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>김명진</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>10,509</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>권재웅</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>7,000</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>천민근</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>-</td>  
      <td>-</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>문순환</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>-</td>  
      <td>-</td>  
    </tr>  
  </tbody>  
</table>  
</pre>

---
* 시장: 코스피, 종목코드: 175330, 상장회사명: JB금융지주  
* 주주총회일: 20230330  
* 전체 대리인의 수: 13명, 권유를 대리하는 개인의 수: 11명  
* 전자투표 가능여부: 전자투표 가능, 전자위임 가능여부: 전자위임장 가능  
* 권유문구 글자수: 987  
* URL: [공시원문 링크](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20230309000295)
<pre>
<table border="1" class="dataframe dataframe">   
  <thead>  
    <tr style="text-align: right;">  
      <th>상장회사명</th>  
      <th>권유공시 제출인</th>  
      <th>대리인</th>  
      <th>대리인 회사 관계</th>  
      <th>대리인 권유자 관계</th>  
      <th>대리인 구분</th>  
      <th>대리인 보유 주식종류</th>  
      <th>대리인 보유 주식수</th>  
    </tr>  
  </thead>  
  <tbody>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>머로우소달리코리아 유한회사</td>  
      <td>없음</td>  
      <td>없음</td>  
      <td>법인</td>  
      <td>-</td>  
      <td>-</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>유한회사 한국엠앤에이</td>  
      <td>없음</td>  
      <td>없음</td>  
      <td>법인</td>  
      <td>-</td>  
      <td>-</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>권오진</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>15</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>방극봉</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>2,600</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>김태현</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>10,407</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>김인수</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>-</td>  
      <td>-</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>조계준</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>-</td>  
      <td>-</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>정일선</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>-</td>  
      <td>-</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>이준호</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>9,000</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>마광수</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>150</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>김명진</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>3</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>권재웅</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>7,000</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>천민근</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>-</td>  
      <td>-</td>  
    </tr>  
  </tbody>  
</table>  
</pre>

---
* 시장: 코스피, 종목코드: 175330, 상장회사명: JB금융지주  
* 주주총회일: 20250327  
* 전체 대리인의 수: 8명, 권유를 대리하는 개인의 수: 8명  
* 전자투표 가능여부: 전자투표 가능, 전자위임 가능여부: 전자위임장 가능  
* 권유문구 글자수: 30  
* URL: [공시원문 링크](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20250305000336)
<pre>
<table border="1" class="dataframe dataframe">   
  <thead>  
    <tr style="text-align: right;">  
      <th>상장회사명</th>  
      <th>권유공시 제출인</th>  
      <th>대리인</th>  
      <th>대리인 회사 관계</th>  
      <th>대리인 권유자 관계</th>  
      <th>대리인 구분</th>  
      <th>대리인 보유 주식종류</th>  
      <th>대리인 보유 주식수</th>  
    </tr>  
  </thead>  
  <tbody>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>탁형재</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>3,000</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>김승덕</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>-</td>  
      <td>-</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>임양진</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>401</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>김현성</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>-</td>  
      <td>-</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>오기용</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>1,602</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>채희재</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>-</td>  
      <td>-</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>천민근</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>-</td>  
      <td>-</td>  
    </tr>  
    <tr>  
      <td>JB금융지주</td>  
      <td>JB금융지주</td>  
      <td>문순환</td>  
      <td>계열사 임직원</td>  
      <td>계열사 임직원</td>  
      <td>개인</td>  
      <td>-</td>  
      <td>-</td>  
    </tr>  
  </tbody>  
</table>  
</pre> 

---
* 시장: 코스피, 종목코드: 009150, 상장회사명: 삼성전기  
* 주주총회일: 20240320  
* 전체 대리인의 수: 7명, 권유를 대리하는 개인의 수: 7명  
* 전자투표 가능여부: 전자투표 가능, 전자위임 가능여부: 해당사항 없음  
* 권유문구 글자수: 28  
* URL: [공시원문 링크](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20240220001106) 
<pre>
<table border="1" class="dataframe dataframe">   
  <thead>  
    <tr style="text-align: right;">  
      <th>상장회사명</th>  
      <th>권유공시 제출인</th>  
      <th>대리인</th>  
      <th>대리인 회사 관계</th>  
      <th>대리인 권유자 관계</th>  
      <th>대리인 구분</th>  
      <th>대리인 보유 주식종류</th>  
      <th>대리인 보유 주식수</th>  
    </tr>  
  </thead>  
  <tbody>  
    <tr>  
      <td>삼성전기</td>  
      <td>삼성전기</td>  
      <td>김경오</td>  
      <td>직원</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주/우선주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>삼성전기</td>  
      <td>삼성전기</td>  
      <td>김병찬</td>  
      <td>직원</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주/우선주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>삼성전기</td>  
      <td>삼성전기</td>  
      <td>안성섭</td>  
      <td>직원</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주/우선주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>삼성전기</td>  
      <td>삼성전기</td>  
      <td>유수정</td>  
      <td>직원</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주/우선주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>삼성전기</td>  
      <td>삼성전기</td>  
      <td>장민석</td>  
      <td>직원</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주/우선주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>삼성전기</td>  
      <td>삼성전기</td>  
      <td>조준상</td>  
      <td>직원</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주/우선주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>삼성전기</td>  
      <td>삼성전기</td>  
      <td>박지훈</td>  
      <td>직원</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주/우선주</td>  
      <td>0</td>  
    </tr>  
  </tbody>  
</table>  
</pre> 

---
* 시장: 코스피, 종목코드: 009150, 상장회사명: 삼성전기  
* 주주총회일: 20230315  
* 전체 대리인의 수: 7명, 권유를 대리하는 개인의 수: 7명  
* 전자투표 가능여부: 전자투표 가능, 전자위임 가능여부: 해당사항 없음  
* 권유문구 글자수: 28  
* URL: [공시원문 링크](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20230214000824) 
<pre>
<table border="1" class="dataframe dataframe">  
  <thead>  
    <tr style="text-align: right;">  
      <th>상장회사명</th>  
      <th>권유공시 제출인</th>  
      <th>대리인</th>  
      <th>대리인 회사 관계</th>  
      <th>대리인 권유자 관계</th>  
      <th>대리인 구분</th>  
      <th>대리인 보유 주식종류</th>  
      <th>대리인 보유 주식수</th>  
    </tr>  
  </thead>  
  <tbody>  
    <tr>  
      <td>삼성전기</td>  
      <td>삼성전기</td>  
      <td>조준상</td>  
      <td>직원</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주/우선주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>삼성전기</td>  
      <td>삼성전기</td>  
      <td>김경오</td>  
      <td>직원</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주/우선주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>삼성전기</td>  
      <td>삼성전기</td>  
      <td>김병찬</td>  
      <td>직원</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주/우선주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>삼성전기</td>  
      <td>삼성전기</td>  
      <td>안성섭</td>  
      <td>직원</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주/우선주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>삼성전기</td>  
      <td>삼성전기</td>  
      <td>장민석</td>  
      <td>직원</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주/우선주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>삼성전기</td>  
      <td>삼성전기</td>  
      <td>정희원</td>  
      <td>직원</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주/우선주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>삼성전기</td>  
      <td>삼성전기</td>  
      <td>박지훈</td>  
      <td>직원</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주/우선주</td>  
      <td>0</td>  
    </tr>  
  </tbody>  
</table>  
</pre>

---
* 시장: 코스피, 종목코드: 009150, 상장회사명: 삼성전기  
* 주주총회일: 20250319  
* 전체 대리인의 수: 7명, 권유를 대리하는 개인의 수: 7명  
* 전자투표 가능여부: 전자투표 가능, 전자위임 가능여부: 해당사항 없음  
* 권유문구 글자수: 28  
* URL: [공시원문 링크](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20250219001962)
<pre>
<table border="1" class="dataframe dataframe">  
  <thead>  
    <tr style="text-align: right;">  
      <th>상장회사명</th>  
      <th>권유공시 제출인</th>  
      <th>대리인</th>  
      <th>대리인 회사 관계</th>  
      <th>대리인 권유자 관계</th>  
      <th>대리인 구분</th>  
      <th>대리인 보유 주식종류</th>  
      <th>대리인 보유 주식수</th>  
    </tr>  
  </thead>  
  <tbody>  
    <tr>  
      <td>삼성전기</td>  
      <td>삼성전기</td>  
      <td>김경오</td>  
      <td>직원</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주/우선주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>삼성전기</td>  
      <td>삼성전기</td>  
      <td>김병찬</td>  
      <td>직원</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주/우선주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>삼성전기</td>  
      <td>삼성전기</td>  
      <td>안성섭</td>  
      <td>직원</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주/우선주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>삼성전기</td>  
      <td>삼성전기</td>  
      <td>유수정</td>  
      <td>직원</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주/우선주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>삼성전기</td>  
      <td>삼성전기</td>  
      <td>조준상</td>  
      <td>직원</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주/우선주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>삼성전기</td>  
      <td>삼성전기</td>  
      <td>박지훈</td>  
      <td>직원</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주/우선주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>삼성전기</td>  
      <td>삼성전기</td>  
      <td>김지수</td>  
      <td>직원</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주/우선주</td>  
      <td>0</td>  
    </tr>  
  </tbody>  
</table>  
</pre> 

---
* 시장: 코스피, 종목코드: 109070, 상장회사명: 주성코퍼레이션  
* 주주총회일: 20230328  
* 전체 대리인의 수: 5명, 권유를 대리하는 개인의 수: 5명  
* 전자투표 가능여부: 해당사항 없음, 전자위임 가능여부: 해당사항 없음  
* 권유문구 글자수: 23  
* URL: [공시원문 링크](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20230313000500)
<pre>
<table border="1" class="dataframe dataframe">  
  <thead>  
    <tr style="text-align: right;">  
      <th>상장회사명</th>  
      <th>권유공시 제출인</th>  
      <th>대리인</th>  
      <th>대리인 회사 관계</th>  
      <th>대리인 권유자 관계</th>  
      <th>대리인 구분</th>  
      <th>대리인 보유 주식종류</th>  
      <th>대리인 보유 주식수</th>  
    </tr>  
  </thead>  
  <tbody>  
    <tr>  
      <td>주성코퍼레이션</td>  
      <td>주성코퍼레이션</td>  
      <td>강유진</td>  
      <td>임직원</td>  
      <td>임직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>주성코퍼레이션</td>  
      <td>주성코퍼레이션</td>  
      <td>박대원</td>  
      <td>임직원</td>  
      <td>임직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>164,100</td>  
    </tr>  
    <tr>  
      <td>주성코퍼레이션</td>  
      <td>주성코퍼레이션</td>  
      <td>김동우</td>  
      <td>임직원</td>  
      <td>임직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>7,453</td>  
    </tr>  
    <tr>  
      <td>주성코퍼레이션</td>  
      <td>주성코퍼레이션</td>  
      <td>유진우</td>  
      <td>임직원</td>  
      <td>임직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>2,932</td>  
    </tr>  
    <tr>  
      <td>주성코퍼레이션</td>  
      <td>주성코퍼레이션</td>  
      <td>강은우</td>  
      <td>임직원</td>  
      <td>임직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>0</td>  
    </tr>  
  </tbody>  
</table>  
</pre>  

---
* 시장: 코스닥, 종목코드: 196300, 상장회사명: HLB펩  
* 주주총회일: 20240705  
* 전체 대리인의 수: 4명, 권유를 대리하는 개인의 수: 3명  
* 전자투표 가능여부: 해당사항 없음, 전자위임 가능여부: 해당사항 없음  
* 권유문구 글자수: 27  
* URL: [공시원문 링크](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20240619000358)
<pre>
<table border="1" class="dataframe dataframe">  
  <thead>  
    <tr style="text-align: right;">  
      <th>상장회사명</th>  
      <th>권유공시 제출인</th>  
      <th>대리인</th>  
      <th>대리인 회사 관계</th>  
      <th>대리인 권유자 관계</th>  
      <th>대리인 구분</th>  
      <th>대리인 보유 주식종류</th>  
      <th>대리인 보유 주식수</th>  
    </tr>  
  </thead>  
  <tbody>  
    <tr>  
      <td>HLB펩</td>  
      <td>HLB펩</td>  
      <td>정현선</td>  
      <td>직원</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>-</td>  
      <td>-</td>  
    </tr>  
    <tr>  
      <td>HLB펩</td>  
      <td>HLB펩</td>  
      <td>이하나</td>  
      <td>직원</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>-</td>  
      <td>-</td>  
    </tr>  
    <tr>  
      <td>HLB펩</td>  
      <td>HLB펩</td>  
      <td>신한휴</td>  
      <td>직원</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>-</td>  
      <td>-</td>  
    </tr>  
    <tr>  
      <td>HLB펩</td>  
      <td>HLB펩</td>  
      <td>(주)위스컴퍼니윅스</td>  
      <td>-</td>  
      <td>-</td>  
      <td>법인</td>  
      <td>-</td>  
      <td>-</td>  
    </tr>  
  </tbody>  
</table>  
</pre>

---
* 시장: 코스피, 종목코드: 326030, 상장회사명: 에스케이바이오팜  
* 주주총회일: 20240326  
* 전체 대리인의 수: 4명, 권유를 대리하는 개인의 수: 4명  
* 전자투표 가능여부: 전자투표 가능, 전자위임 가능여부: 전자위임장 가능  
* 권유문구 글자수: 28  
* URL: [공시원문 링크](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20240307000351)
<pre>
<table border="1" class="dataframe dataframe">  
  <thead>  
    <tr style="text-align: right;">  
      <th>상장회사명</th>  
      <th>권유공시 제출인</th>  
      <th>대리인</th>  
      <th>대리인 회사 관계</th>  
      <th>대리인 권유자 관계</th>  
      <th>대리인 구분</th>  
      <th>대리인 보유 주식종류</th>  
      <th>대리인 보유 주식수</th>  
    </tr>  
  </thead>  
  <tbody>  
    <tr>  
      <td>에스케이바이오팜</td>  
      <td>에스케이바이오팜</td>  
      <td>송상원</td>  
      <td>직원</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>에스케이바이오팜</td>  
      <td>에스케이바이오팜</td>  
      <td>김재형</td>  
      <td>직원</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>에스케이바이오팜</td>  
      <td>에스케이바이오팜</td>  
      <td>이민선</td>  
      <td>직원</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>0</td>  
    </tr>  
    <tr>  
      <td>에스케이바이오팜</td>  
      <td>에스케이바이오팜</td>  
      <td>김이진</td>  
      <td>직원</td>  
      <td>직원</td>  
      <td>개인</td>  
      <td>보통주</td>  
      <td>0</td>  
    </tr>  
  </tbody>  
</table>  
</pre>