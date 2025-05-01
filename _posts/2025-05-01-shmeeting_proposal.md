---
layout: single
title:  "2024 주주총회 언더독의 반란, 성공or실패?"
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


## 주주제안의 법적 근거
올해 주주총회 시즌이 마무리되면서 주주제안 안건 현황을 살펴보는 것은 한국 자본시장의 주주행동주의 트렌드를 파악하는 데 중요한 지표가 됩니다. 주주제안은 소액주주들의 목소리를 반영할 수 있는 중요한 수단입니다. 상법은 아래와 같이 주주제안 내용을 포함하고 있습니다.


> **상법 제363조의2(주주제안권)** ①의결권없는 주식을 제외한 발행주식총수의 100분의 3 이상에 해당하는 주식을 가진 주주는 이사에게 주주총회일(정기주주총회의 경우 직전 연도의 정기주주총회일에 해당하는 그 해의 해당일. 이하 이 조에서 같다)의 6주 전에 서면 또는 전자문서로 일정한 사항을 주주총회의 목적사항으로 할 것을 제안(이하 '株主提案'이라 한다)할 수 있다.<br>
②제1항의 주주는 이사에게 주주총회일의 6주 전에 서면 또는 전자문서로 회의의 목적으로 할 사항에 추가하여 당해 주주가 제출하는 의안의 요령을 제363조에서 정하는 통지에 기재할 것을 청구할 수 있다.<br>
③이사는 제1항에 의한 주주제안이 있는 경우에는 이를 이사회에 보고하고, 이사회는 주주제안의 내용이 법령 또는 정관을 위반하는 경우와 그 밖에 대통령령으로 정하는 경우를 제외하고는 이를 주주총회의 목적사항으로 하여야 한다. 이 경우 주주제안을 한 자의 청구가 있는 때에는 주주총회에서 당해 의안을 설명할 기회를 주어야 한다. 

> **상법 제542조의6(소수주주권)** ② 6개월 전부터 계속하여 상장회사의 의결권 없는 주식을 제외한 발행주식총수의 1천분의 10(대통령령으로 정하는 상장회사의 경우에는 1천분의 5) 이상에 해당하는 주식을 보유한 자는 **제363조의2**(제542조에서 준용하는 경우를 포함한다)에 따른 주주의 권리를 행사할 수 있다.

에 따르면, 의결권 있는 주식의 1% 이상을 보유한 주주는 이사에게 주주총회 목적사항에 추가할 의안을 서면으로 제안할 수 있습니다. 또한 상법 제542조의6에서는 상장회사의 경우 6개월 이상 계속하여 의결권 있는 주식의 0.5%(자본금 1,000억원 이상인 회사는 0.25%) 이상을 보유한 주주에게 제안권을 부여하고 있습니다. 이러한 조항은 소액주주들의 경영참여 기회를 확대하고 주주 권리를 보호하기 위한 제도적 장치입니다.

## 2024 사업연도 정기주총 주주제안 현황
먼저 자료의 출처는 증권의 권리와 발행에 관한 정보를 제공하는 [**SEIBRO(링크)**{: style="color: #4682B4;"}](https://seibro.or.kr/)입니다. SEIBRO에서는 주주총회의 안건별로 "주주제안"이라고 식별하여 표시하고 있습니다.
<br>

![11_prop_stat]({{site.url}}/assets/images/2025-05-01-shmeeting/11_prop_stat.png)<br><br>


**코스피 시장 주주제안 현황**{: style="color: #4682B4;"}<br>
2024년 코스피 시장에서는 **총 110건의 주주제안 안건이 상정(전체 안건의 2.14%)**{: style="color: #4682B4;"}되었습니다. 주주제안이 있었던 **기업 수는 15개사**{: style="color: #4682B4;"}로, 전체 코스피 상장사 대비 1.87%였습니다. 주주제안 안건 비중(2.14%)이 주주제안 있는 기업 비중(1.87%)보다 다소 높다는 점은 주주제안이 있는 기업들에서 평균적으로 복수의 안건이 제안되었음을 시사합니다.

**코스닥 시장 주주제안 현황**{: style="color: #4682B4;"}<br><br>
코스닥 시장의 경우, 주주제안 안건 수는 **96건으로 집계(전체 안건의 0.98%)**{: style="color: #4682B4;"}되었습니다. 주주제안이 있었던 **기업 수는 21개사**{: style="color: #4682B4;"}로, 전체 코스닥 상장사 중 1.22%에 해당합니다. 코스피와 마찬가지로 소수 기업에 주주제안이 집중되는 경향을 보였습니다.


## 주주제안 안건의 결과는?
![12_prop_result]({{site.url}}/assets/images/2025-05-01-shmeeting/12_prop_result.png)<br><br>


코스피 시장에서는 총 110건의 주주제안 안건이 15개 기업에서 제출되었으나, **실제 승인된 것은 9건(8.18%)**{: style="color: #4682B4;"}이었습니다. 코스닥 시장은 21개 기업에서 96건의 주주제안이 있었지만, **통과된 안건은 6건(6.25%)**{: style="color: #4682B4;"}으로 더욱 낮은 승인율을 보였습니다. 

## 언더독의 반란이 성공한 케이스는 어떤 안건이었을까?
그래도 시장별로 승인된 안건이 코스피 9건, 코스닥 6건이 있었습니다. 승인된 안건 어떤 것들이었을까요?<br>
코스피에서는 디아이동일과 고려아연이 각각 3건씩의 주주제안을 수용했으며, **이사·감사 선임 관련 안건이 5건**{: style="color: #4682B4;"}으로 가장 많았습니다. **정관변경(2건)과 현금배당(1건)**{: style="color: #4682B4;"} 관련 안건도 통과됐습니다.<br>
코스닥 시장에서는 **승인된 안건 유형은 이사·감사 선임(4건), 정관변경(1건), 현금배당(1건)**{: style="color: #4682B4;"}이었습니다.<br>

![13_prop_agendas]({{site.url}}/assets/images/2025-05-01-shmeeting/13_prop_agendas.png)<br><br>


## 정말 배당을 주주제안으로 통과했다고?
코스피와 코스닥 각각 1건씩 주주배당 안건이 주주제안으로 승인이 되었다는 사실이 놀랍습니다. 현대차증권과 케이프인데, 각 공시를 열어보았습니다. 
![15_prop_div_error]({{site.url}}/assets/images/2025-05-01-shmeeting/15_prop_div_error.png)<br><br>
주주제안 배당 안건이 승인된 게 사실이었다면 참 흥미로웠겠지만, 공시를 확인해보니 아쉽게도 사실이 아니었습니다. 현대차증권과 케이프 모두 주주제안 배당안건은 부결되었고, 오히려 회사측이 제안한 원안이 승인된 것으로 확인되었습니다. 현대차증권의 경우 원래 보통주 500원 배당이 회사안이었으나, 주주제안은 보통주 주당 180원, 우선주 주당 418원(현대자동차그룹 제71기 이익배당 비율과 동일)을 요구했고, 케이프 역시 회사안인 보통주 1주당 300원 대신 주주제안은 보통주 1주당 400원을 주장했습니다. 둘 다 주주제안 안건은 부결로 처리되었지만 SEIBRO에서는 승인으로 잘못 표시된 것이었습니다.


## 그래도 주주행동주의의 희망을 보다
배당을 제외한 주주제안 안건들 중 승인된 안건들을 보면 그래도 희망은 있습니다.


![16_prop_misc_ex]({{site.url}}/assets/images/2025-05-01-shmeeting/16_prop_misc_ex.png)<br><br>
주주제안을 통한 감사 선임 사례는 국내 주주행동주의의 뚜렷한 성과를 보여줍니다. 와이엔티, 코스닥시장, 다이아몬일, 강남제비스코 등 기업에서 **주주들이 제안한 감사 후보가 실제로 선임**{: style="color: #4682B4;"}되었습니다. 특히 국내 상법상 감사 선임 시 발행주식 총수의 3%를 초과하는 주식을 가진 주주는 그 초과분에 대해 의결권을 행사할 수 없는 **'3%룰'**{: style="color: #4682B4;"}이 적용되어, 대주주나 경영진이 단독으로 감사를 선임하기 어려운 구조입니다. 이런 상황에서 **주주들이 적극적으로 감사 후보를 제안하고 실제 선임까지 이어진 것은 매우 의미 있는 변화**{: style="color: #4682B4;"}입니다.<br><br>

![14_prop_result_ex]({{site.url}}/assets/images/2025-05-01-shmeeting/14_prop_result_ex.png)<br><br>
주주가치 제고를 위한 안건들이 승인된 사례도 주목할 만합니다. 오스코텍의 경우 경영 투명성과 주주가치 제고를 위한 여러 주주제안이 승인되었으며, 특히 **IR활동 강화 관련 안건이 통과**{: style="color: #4682B4;"}된 점이 흥미롭습니다. 고려제강에서도 주주제안으로 경영 변경의 건과 주주가치 제고를 위한 여러 안건이 승인되었습니다. 특히 IR활동 강화는 기업과 주주 간 소통 채널을 확대하는 중요한 조치인데, 어떤 구체적인 IR 활동이 요구되었는지 궁금합니다. 분기별 IR 미팅 의무화, 기관투자자와의 정기적 대화 채널 구축, 영문 공시 확대 등이 떠오르는데... 어떤 것들이었을까요?
<br><br>
비록 많은 사례는 아니었지만 그래도 주주제안 안건이 승인된 사례들은 한국 자본시장에서 주주행동주의가 단순한 '소리 내기'를 넘어 실질적인 기업 지배구조와 경영 방식 변화로 이어질 수 있다는 희망을 보여줍니다.