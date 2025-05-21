---
layout: single
title:  "주총장에서 싸움났다! 걔랑 걔가 싸운대! 구경가자!"
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

**[관련 포스팅]** [의결권 원기옥: 주주들이여, 제게 의결권을 나눠주세요!](https://beaten-by-the-market.github.io/%ED%95%9C%EA%B5%AD%EC%8B%9C%EC%9E%A5/proxy/)<br>
**[관련 포스팅]** [의결권 원기옥을 모으기 위해서는 대리인이 필요하다?](https://beaten-by-the-market.github.io/%ED%95%9C%EA%B5%AD%EC%8B%9C%EC%9E%A5/proxy_agents1/)<br>
**[관련 포스팅]** [니가 그렇게 의결권이 많아? 주총장으로 따라와](https://beaten-by-the-market.github.io/%ED%95%9C%EA%B5%AD%EC%8B%9C%EC%9E%A5/proxy_agents2/)<br>
{:.notice--success}


## Proxy Fight의 유형 복습
지난 포스팅[(니가 그렇게 의결권이 많아? 주총장으로 따라와, 링크)](https://beaten-by-the-market.github.io/%ED%95%9C%EA%B5%AD%EC%8B%9C%EC%9E%A5/proxy_agents2/)에서는 의결권 대리행사 권유를 2개 주체 이상이 하는 경우를 케이스별로 나누어 보았습니다. 

* **Case 1: 싸움처럼 보이지만 싸움이 아닌 경우**{: style="color: #4682B4;"}<br>
* **Case 2: 무리한 도전, 무시하는 회사**{: style="color: #4682B4;"}<br>
* **Case 3: 권유대리 법인을 선임한 주주의 도전, 회사의 무시**{: style="color: #4682B4;"}<br>
* **Case 4: 무리한 도전, 형식적인 대응**{: style="color: #4682B4;"}<br>
* **Case 5: 권유대리 법인을 선임한 주주의 도전, 회사의 직원 대응**{: style="color: #4682B4;"}<br>
* **Case 6: 본격적인 전쟁**{: style="color: #4682B4;"}<br>
* **Case 7: 비대칭 대결**{: style="color: #4682B4;"}<br>

이번 포스팅에서는 진짜 싸움인 Case 6의 사례 몇가지를 살펴보겠습니다.


## 한미약품 : 모회사와 자회사의 대립
먼저 살펴볼 케이스는 **2024년 12월 19일에 있었던 한미약품의 주주총회**{: style="color: #4682B4;"}입니다. 한미사이언스는 한미약품의 지분 41%를 보유한 최대주주임에도 불구하고 자회사인 한미약품과 의결권 싸움을 벌이는 매우 특이한 상황이 발생했습니다. 일반적으로 이렇게 높은 지분을 가진 모회사가 자회사와 대립하는 경우는 드문데, 이번 사례는 그룹 내부의 거버넌스 갈등을 보여줍니다.<br><br>

아래는 **한미사이언스**{: style="color: #4682B4;"}의 의결권 대리행사 권유 취지입니다.
![1_hanmi_science_purpose]({{site.url}}/assets/images/2025-05-21-proxy/1_hanmi_science_purpose.png)<br><br>

다음은 **한미약품**{: style="color: #4682B4;"}의 의결권 대리행사 권유 취지 입니다.
![1_hanmi_pharma_purpose]({{site.url}}/assets/images/2025-05-21-proxy/1_hanmi_pharma_purpose.png)<br><br>



### 주요 쟁점
* **한미사이언스 측 주장**{: style="color: #4682B4;"}: 한미약품이 창립 이후 사상 최대 실적과 신약개발 포트폴리오를 진행 중임에도, 지주회사인 한미사이언스의 영업방해와 경영간섭으로 사업에 차질이 생기고 있다고 주장합니다. 특히 2024년 3월 주주총회 이후 선임된 임종훈 대표이사가 부당한 업무지시와 압력을 행사하고 있다고 지적합니다.

* **한미약품 측 주장**{: style="color: #4682B4;"}: 한미사이언스는 한미그룹의 발전을 위해 노력해왔으나, 최근 한미약품이 그룹의 발전 방향에 역행하는 행보를 보이고 있다고 주 장합니다. 신약 개발이라는 중요한 시점에 불필요한 갈등을 야기하고 있어 새로운 경영진 선임이 필요하다고 강조합니다.


### 의결권 대리행사 권유 대리인 현황
![1_hanmi_agent_number]({{site.url}}/assets/images/2025-05-21-proxy/1_hanmi_agent_number.png)<br><br>

한미사이언스는 3곳의 법인 대리인을 선임했고, 한미약품은 4곳의 대리인을 선임했습니다. 아무래도 한미사이언스가 41%를 확보한 상태로 게임을 시작하니, 한미약품이 대리인을 좀 더 적극적으로 선임했을 유인이 있었을 것 같습니다.


### 결과는?
![1_hanmi_result]({{site.url}}/assets/images/2025-05-21-proxy/1_hanmi_result.png)<br><br>
한미사이언스는 한미약품 지분 41%를 보유한 대주주임에도 불구하고, 특별결의(이사 해임은 특별결의 사항)의 벽을 넘지 못하였습니다. 이에 따라 후속 안건이었던 새로운 이사 선임 건도 자동 폐기되었습니다. 결국 이번 의결권 대리행사 싸움에서는 자회사인 한미약품의 현 경영진이 모회사인 한미사이언스의 도전을 물리치는 승리를 거두었으며, 이는 한미약품의 다른 주주들이 현 경영진을 지지했음을 의미합니다.


## SM엔터테인먼트 : 대형 엔터사 간의 싸움
다음으로 살펴볼 케이스는 2023년 3월 31일에 열린 SM엔터테인먼트의 주주총회입니다. 하이브는 SM엔터테인먼트의 지분 19%를 보유하며 경영권 도전을 시도했습니다. 국내 최대 엔터테인먼트 기업 간의 의결권 대리행사 경쟁이라는 점에서 업계의 많은 관심을 받았습니다.

아래는 **하이브**{: style="color: #4682B4;"}의 의결권 대리행사 권유 취지입니다.
![2_hive]({{site.url}}/assets/images/2025-05-21-proxy/2_hive.png)<br><br>

다음은 **SM**{: style="color: #4682B4;"}의 의결권 대리행사 권유 취지 입니다.
![2_sm]({{site.url}}/assets/images/2025-05-21-proxy/2_sm.png)<br><br>


### 주요 쟁점
* **하이브 측 주장**{: style="color: #4682B4;"}: "현 SM 경영진을 신뢰할 수 없다"며 "문제로 지적돼 왔던 라이크 기획과의 계약을 스스로 집행한 사실에 비추어 볼 때, 현 SM 경영진은 신뢰할 수 없다"고 주장했습니다. 특히 신주 및 전환사채 발행 과정이나 자사주 매입 과정에서의 위법 논란을 제기하며 하이브 추천 이사진에게 의결권을 위임해달라고 요청했습니다.

* **SM 측 주장**{: style="color: #4682B4;"}: SM 현 경영진은 'SM 3.0' 비전을 제시하며 제작 센터와 내·외부 레이블 설립을 통한 체계 개편, 신인 제작과 미주 등 해외 진출 계획을 강조했습니다. 또한 창업자 이수만의 개인회사인 라이크기획과의 계약 관계를 개선하고 독립적인 이사회를 구성하겠다는 의지를 표명했습니다.

### 의결권 대리행사 권유 대리인 현황
![2_sm_agent_number]({{site.url}}/assets/images/2025-05-21-proxy/2_sm_agent_number.png)<br><br>

SM은 소액주주들의 의결권을 모으기 위해 케이디엠메가홀딩스, 비사이드코리아, 머로우소달리코리아 등 3곳을 먼저 공시했고, 이후 씨지트러스트, 제이스에스에스, 리앤모어그룹 등 4곳을 추가로 의결권 대리행사 권유업무 대리인으로 선임했습니다. 총 7개의 대리법인을 통해 의결권을 모으는 적극적인 대응 전략을 취했습니다. 이에 반해 하이브는 2곳의 대리인으로 선임했습니다.

### 결과는?
2023년 3월 31일 개최된 SM엔터테인먼트 정기주주총회에서는 SM 이사회가 제안한 모든 안건이 가결되었습니다. 장철혁 CFO, 김지원 마케팅센터장, 최정민 글로벌 비즈니스 센터장이 사내이사로 선임되었고, 독립적인 사외이사들도 이사회에 합류하게 되었습니다. 반면 하이브가 추천한 이사진은 모두 선임되지 못했습니다.
주목할 만한 점은, 하이브가 이수만 전 총괄프로듀서로부터 매입한 SM 지분 약 14.8%와 더불어 이수만의 잔여 지분(3.65%)에 대한 의결권까지 위임받았음에도 불구하고 주주총회에서 승리하지 못했다는 것입니다. 결국 경영권 분쟁 중이던 하이브는 카카오와 합의하여 보유 지분을 카카오에 매각했고, 카카오가 SM의 새로운 최대주주가 되었습니다.


## 금호석유화학 : 행동주의 펀드의 싸움
다음으로 살펴볼 케이스는 2024년 3월 22일에 열린 금호석유화학의 주주총회입니다. 차파트너스자산운용은 금호석유화학의 지분을 갖고 있지는 않지만,  금호석유화학의 개인 최대주주인 박철완 전 상무로부터 의결권을 위임받아 주주제안을 했습니다. 특별관계인의 지분을 합치면 약 13.32%의 의결권을 확보한 행동주의 펀드의 도전이었습니다. 13%를 확보했고, 의결권 대리행사 권유를 통해 추가로 의결권을 확보하여 금호석유화학과 한판 붙겠다는 것입니다.

아래는 **차파트너스**{: style="color: #4682B4;"}의 의결권 대리행사 권유 취지입니다.
![3_tcha]({{site.url}}/assets/images/2025-05-21-proxy/3_tcha.png)<br><br>

다음은 **금호석유화학**{: style="color: #4682B4;"}의 의결권 대리행사 권유 취지 입니다.
![3_kumho]({{site.url}}/assets/images/2025-05-21-proxy/3_kumho.png)<br><br>


### 주요 쟁점
* **차파트너스 측 주장**{: style="color: #4682B4;"}: 금호석유화학은 2024년 1월 기준 지난 3년간 고성과 대비 약 60% 하락했으며, 총 주주수익률(TSR)은 업계 평균과 국내 상장 화학기업대비 최하위 수준이라고 지적했습니다. 특히 지분의 18.4%에 달하는 자사주를 보유함에도 이를 소각하지 않는 점이 주주가치 저하의 가장 큰 원인으로 꼽았습니다. 자사주를 소각하는 정관 변경과 자사주 50%(약 224만 주) 소각을 주주제안으로 내세웠습니다.

* **금호석유화학 측 주장**{: style="color: #4682B4;"}: 회사는 창립 이후 사상 최대 실적과 주주가치 전략을 수립하고 이를 실행 중이라고 강조했습니다. 제47기 결산 배당금으로 주당 1,765원의 현금배당을 실시했고, 소각특적금 500억원, 소각목적주도 별도 확보했다고 밝혔습니다. 현재 총 자사주의 의결권을 행사할 수 있는 독점적인 권한을 이사회에서 제거하고 주주총회에 분산시키는 것은 오히려 불필요한 경영 간섭과 M&A 위협을 증가시킬 뿐이라고 주장했습니다.


### 의결권 대리행사 권유 대리인 현황
이번 주주총회에서는 차파트너스 측이 머큐리오스컨설팅코리아, Georgeson LLC, (주)앤비파트너스 등 3곳을 의결권 대리행사 권유업무 대리인으로 선임했습니다. 반면 금호석유화학은 메루카소컨설팅코리아, 엘엠피트리뉴스, (주)한국의결권대행, (주)에스오피 등 4곳을 대리인으로 선임하여 보다 적극적인 의결권 확보 전략을 취했습니다.

### 결과는?
2024년 3월 22일 개최된 금호석유화학 제47기 정기주주총회에서는 회사 측 안건이 모두 가결되었습니다. 반면 차파트너스 측이 제안한 정관 일부 변경안과 자사주 소각 안건, 사외이사 선임 안건은 모두 부결되었습니다. 표결 결과를 살펴보면, 정관 변경 건은 사측 74.6% 대 차파트너스 측 25.6%, 사외이사 선임안은 사측 76.1% 대 차파트너스 측 23%로 큰 차이를 보였습니다. 차파트너스와 박철완 전 상무의 지분 약 13%를 제외한 일반주주의 안건 찬성률은 약 10% 정도에 불과했습니다.
이는 박철완 전 상무가 2021년 처음 시도했던 경영권 도전 이후 네 번째 패배로, '조카의 난'으로 불리는 금호그룹 내 경영권 분쟁이 또다시 실패로 돌아간 사례입니다.