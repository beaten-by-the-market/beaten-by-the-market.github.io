---
layout: single
title:  "2024 사업연도 정기주주총회 이모저모"
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

## 상장법인의 정기주주총회 개최현황

### 정기주주총회란?
정기주주총회는 주식회사가 법적 의무에 따라 **매년 1회 개최**{: style="color: #4682B4;"}하는 최고 의사결정기관의 회의입니다. 상법 제365조에 따라 모든 주식회사는 매년 일정한 시기에 정기주주총회를 개최해야 하며, 결산기 종료일로부터 3개월 이내(일반적으로 12월 결산법인은 다음 해 3월 말까지)에 개최해야 합니다. 이 자리에서는 **지난 1년간의 영업실적 보고, 재무제표 승인, 이사 및 감사 선임, 이익배당 결정, 임원 보수 책정 등 회사의 중요 사안들이 논의되고 결정**{: style="color: #4682B4;"}됩니다. 정기주주총회는 회사의 주인인 주주들이 경영진의 활동을 평가하고, 회사의 방향성을 결정하는 핵심 절차로, 주주가 1인뿐인 회사라도 반드시 개최해야 하는 법적 의무사항입니다.

> **상법 제365조(총회의 소집)** ①정기총회는 매년 1회 일정한 시기에 이를 소집하여야 한다.

> **상법 제354조(주주명부의 폐쇄, 기준일)** ①회사는 의결권을 행사하거나 배당을 받을 자 기타 주주 또는 질권자로서 권리를 행사할 자를 정하기 위하여 일정한 기간을 정하여 주주명부의 기재변경을 정지하거나 일정한 날에 주주명부에 기재된 주주 또는 질권자를 그 권리를 행사할 주주 또는 질권자로 볼 수 있다. <br>
  ②**제1항의 기간은 3월을 초과하지 못한다.**<br>
  ③제1항의 날은 주주 또는 질권자로서 권리를 행사할 날에 앞선 3월내의 날로 정하여야 한다.<br>
  ④회사가 제1항의 기간 또는 날을 정한 때에는 그 기간 또는 날의 2주간전에 이를 공고하여야 한다. 그러나 정관으로 그 기간 또는 날을 지정한 때에는 그러하지 아니하다.


### 2024사업연도 정기주주총회 날짜별 개최현황
2024년 1월 1일 ~ 12월 31일을 사업연도로 하는 상장법인은 위에 따라서 2025년 3월 31일까지 정기주주총회를 개최하였을 것이라고 볼 수 있습니다. 

![1_calendar]({{site.url}}/assets/images/2025-05-01-shmeeting/1_calendar.png)<br><br>

예탁결제원의 SEIBRO에서 공개하는 코스피 및 코스닥 상장법인의 정기주주총회 개최결과를 통해 확인해본 내용은 위와 같습니다. 정기주주총회 개최는 압도적으로 3월 셋째 주(3/17~3/21)와 넷째 주(3/24~3/28)에 집중되어 있었습니다. 특히 3월 넷째 주에는 무려 1,662건의 주주총회가 개최되었으며, 금요일(569건)에 가장 많이 몰려있는 것을 확인할 수 있습니다. 이러한 현상은 회사들이 결산 마감 후 재무제표 작성과 외부감사 완료 시점을 고려하여 3월 말에 맞춰 일정을 잡는 경향이 있기 때문입니다.


> [**SEIBRO(링크)**{: style="color: #4682B4;"}](https://seibro.or.kr/)는 증권의 정보에 대한 정보를 제공하는 포털로 한국예탁결제원에서 운영하고 있습니다. 한국예탁결제원은 증권의 권리와 발행에 관한 실무를 수행합니다. 예를 들어, 배당금을 주주들의 계좌에 넣어주는 절차, 상장되는 증권을 주주들의 계좌에 넣어주는 절차 등에는 한국예탁결제원이 관여되어 있습니다. 따라서 **증권의 권리와 발행에 대한 정보는 SEIBRO에서 매우 유용하게 사용**{: style="color: #4682B4;"}할 수 있습니다.


그런데 특이하게도 4월에도 소수의 주주총회가 개최된 것으로 나타납니다. 앞서 상법에서 확인했던 것과는 다른데요.. 무슨 케이스일까요?

![1_postponed_all]({{site.url}}/assets/images/2025-05-01-shmeeting/1_postponed_all.png)<br><br>

**코스닥상장사 큐라티스**{: style="color: #4682B4;"}의 사례를 보면, 3월 31일 소집되었던 정기주주총회가 회사의 형편상 회의의 목적사항을 다루지 못하여 상법 제372조에 의거 연기회가 결정되었습니다. 이로 인해 4월 7일에 연기 개최된 것을 확인할 수 있습니다. **코스피상장사 이엔플러스**{: style="color: #4682B4;"}의 경우, "감사보고서 지연제출에 따른 주주총회 연기회" 즉, 외부감사인의 감사보고서 지연으로 인해 주주총회가 연기된 사례도 확인됩니다. **KIB플러그에너지**{: style="color: #4682B4;"}는 일부 의안에 대해서는 정기주주총회 연기회를 개최하여 심의하기로 하였습니다. 이에 대한 근거는 아래 상법 조항으로 확인됩니다.

> **상법 제372조(총회의 연기, 속행의 결의)** ①총회에서는 회의의 속행 또는 연기의 결의를 할 수 있다.


한편, 한국에 상장된 외국법인의 경우에도 3월이 지나서 개최되었습니다. 이는 외국법인에 상법에 따른 주주총회 3개월 내 개최가 적용되지는 않지만 자본시장법 시행령에 그 근거가 있습니다.

> **자본시장법 시행령 제176조(사업보고서 등의 제출에 관한 특례)** ② 외국법인등(제1항 각 호의 어느 하나에 해당하는 외국법인등은 제외한다. 이하 이 조에서 같다)은 사업보고서를 법 제159조제1항 본문에서 정하는 기간이 지난 후 30일 이내에 제출할 수 있고, 반기보고서 및 분기보고서를 법 제160조제1항 전단에서 정하는 기간이 지난 후 15일 이내에 제출할 수 있다.


## 어떤 안건들이 논의되었을까?

![2_agenda_freq_all]({{site.url}}/assets/images/2025-05-01-shmeeting/2_agenda_freq_all.png)<br><br>

마찬가지로 SEIBRO에서 자료를 수집하여 간단한 시각화를 Streamlit으로 해보았습니다. 참고로 SEIBRO에 기재된 중분류 안건명을 그대로 사용하였으므로, 일부 커스텀화된 안건은 전수조사의 대세에는 지장을 미치지 않는 것으로 간주하였습니다. <br>
**재무제표 승인**{: style="color: #4682B4;"}은 통상 정기주주총회 안건으로 다뤄지기 때문에, 재무제표 승인을 기준으로 더 많은 안건을 보도록 하겠습니다. 2024년 정기주주총회 안건을 분석한 결과, **코스피 상장사에서는 '사내이사 선임'(829건), '이사 보수한도액 승인'(789건)이 '재무제표승인'(780건) 보다 많았습니다.**{: style="color: #4682B4;"} 반면 **코스닥 상장사에서는 '재무제표승인'(1,706건)이 가장 많았고**{: style="color: #4682B4;"}, '이사 보수한도액 승인'(1,694건), '사내이사 선임'(1,688건) 순이었습니다.<br>
이는 **코스피 상장사들이 재무제표 승인 안건을 주총 결의사항이 아닌 보고안건으로 올려서 그런것일 수도 있겠고, 기업규모가 크기 때문에 이사의 수도 그만큼 많고 따라서 그만큼 안건도 많았을 수도**{: style="color: #4682B4;"} 있겠습니다.


> **상법 제449조의2(재무제표 등의 승인에 대한 특칙)** ① 제449조에도 불구하고 회사는 정관으로 정하는 바에 따라 제447조의 각 서류를 이사회의 결의로 승인할 수 있다. 다만, 이 경우에는 다음 각 호의 요건을 모두 충족하여야 한다.<br>
1.제447조의 각 서류가 법령 및 정관에 따라 회사의 재무상태 및 경영성과를 적정하게 표시하고 있다는 외부감사인의 의견이 있을 것<br>
2.감사(감사위원회 설치회사의 경우에는 감사위원을 말한다) 전원의 동의가 있을 것<br>
② 제1항에 따라 이사회가 승인한 경우에는 이사는 제447조의 각 서류의 내용을 주주총회에 보고하여야 한다.


## 안건이 영문으로 제공된 현황은?

![3_english_all]({{site.url}}/assets/images/2025-05-01-shmeeting/3_english_all.png)<br><br>

바야흐로 기업가치 제고를 위한 밸류업 시대가 도래했습니다. 외국인 투자자들의 한국 시장 관심도 증가에 발맞춰 기업들의 영문 공시도 점차 확대되는 추세입니다. 특히 주주총회 안건의 영문 제공은 글로벌 투자자들이 한국 기업의 주요 의사결정에 참여하는 데 필수적인 요소가 되고 있습니다. 2024년 정기주주총회 시즌을 맞아 안건의 영문 제공 현황을 살펴보겠습니다. 
> 참고로 안건의 영문제공은 **안건의 중분류까지만 대상**{: style="color: #4682B4;"}으로 합니다. "(중분류) 이사의 선임 (소분류) 이사후보 : 홍길동"이라면, "이 안건은 이사의 선임과 관련된 것이다"까지라도 알 수 있게 하는 영문정보가 제공되었느냐를 보는 것입니다.



**영문 안건 제공 비율**{: style="color: #4682B4;"}<br>
**안건별 비율**{: style="color: #4682B4;"} : 코스피와 코스닥 시장 모두에서 영문으로 안건을 제공하는 비율이 상당히 높게 나타났습니다.
* 코스피 : 전체 안건 중 4,856건(94.27%) / 코스닥 : 전체 안건 중 9,427건(95.88%)
<br>

**전체 안건을 영문으로 제공한 법인 비율**{: style="color: #4682B4;"} : 법인 기준으로도 대다수의 기업이 영문 안건을 제공하고 있습니다.
* 코스피 : 총 684개 법인(전체의 85.07%) / 코스닥 : 총 1,470개 법인(전체의 85.32%)



**영문 미제공 안건 유형**{: style="color: #4682B4;"}<br>
두 시장 모두에서 영문 미제공 안건은 대체로 '주주제안' 관련 사항에 집중되어 있습니다. 이는 회사가 아닌 주주 측에서 제안한 안건이라는 특성에 기인한 것으로 추측됩니다.

* 코스피 시장 영문 미제공 주요 안건:
  * 사외이사 선임(주주제안): 45 / 정관변경(주주제안): 24건 / 비상임이사 선임(주주제안): 12건
* 코스닥 시장 영문 미제공 주요 안건:
  * 정관변경(주주제안): 약 20건 / 사외이사 선임(주주제안): 약 19건 / 사내이사 선임(주주제안): 약 17건



## 결과는? 승인? 부결?
2024년 정기주주총회 시즌이 마무리되면서 주요 안건들의 의결 결과를 분석해봤습니다. 코스피와 코스닥 시장 전체적으로 대부분의 안건은 승인되었으나, 일부 안건은 승인되지 않았습니다. 

![4_result_all]({{site.url}}/assets/images/2025-05-01-shmeeting/4_result_all.png)<br><br>


두 시장 모두 95% 내외의 높은 승인률을 보이고 있어 대부분의 안건이 주주총회에서 무난히 통과되고 있음을 알 수 있으며, 코스닥 시장의 승인률이 코스피 시장보다 약 1.34%p 더 높게 나타났습니다. 한편, 주목할 만한 안건별 의결 결과를 확인해보았습니다. **빈도가 높았던 상위 10개 안건 중 승인률이 95% 미만인 안건은 두 가지가 있었습니다.**{: style="color: #4682B4;"}

![5_resultbyagenda_all]({{site.url}}/assets/images/2025-05-01-shmeeting/5_resultbyagenda_all.png)<br><br>
![5_resultbyagenda_all2]({{site.url}}/assets/images/2025-05-01-shmeeting/5_resultbyagenda_all2.png)<br><br>

1. **재무제표 승인**{: style="color: #4682B4;"} : 승인 94.93% / 철회: 4.26%

재무제표 승인 안건의 철회 비율이 4.26%로 상당히 높게 나타났습니다. 일부 사례를 확인해보니 기업들이 처음에는 재무제표 승인을 의결 안건으로 상정했다가 나중에 단순 보고사항으로 변경한 경우가 있었습니다. 최근 일부 기업들은 정관 변경을 통해 재무제표 승인을 이사회 결의사항으로 전환하고 주주총회에서는 단순 보고만 하고 있습니다.
![fs_approval_ex_all]({{site.url}}/assets/images/2025-05-01-shmeeting/fs_approval_ex_all.png)<br><br>


2. **감사 선임**{: style="color: #4682B4;"} : 선임 91.05% / 미선임 7.16%
감사 선임 안건은 미승인 비율이 7.16%로 다른 안건에 비해 상당히 높게 나타났습니다. 이는 상법상 감사 선임을 위한 득표 조항이 까다롭기 때문입니다. 상법에 따르면 감사 선임을 위해서는 출석한 주주 의결권의 과반수와 함께 발행주식 총수의 4분의 1 이상의 찬성이 필요하며, 최대주주와 특수관계인의 의결권은 합산하여 3%로 제한됩니다. 이러한 엄격한 요건으로 인해 다른 안건에 비해 승인률이 낮게 나타나는 것이 아닐지 추정됩니다.

![auditor_deny_ex_all]({{site.url}}/assets/images/2025-05-01-shmeeting/auditor_deny_ex_all.png)<br><br>

> **상법 제409조(선임)** ①감사는 주주총회에서 선임한다.<br>
②의결권없는 주식을 제외한 **발행주식의 총수의 100분의 3**(정관에서 더 낮은 주식 보유비율을 정할 수 있으며, 정관에서 더 낮은 주식 보유비율을 정한 경우에는 그 비율로 한다)**을 초과하는 수의 주식을 가진 주주는 그 초과하는 주식에 관하여 제1항의 감사의 선임에 있어서는 의결권을 행사하지 못한다.**

구체적인 사례로 A기업의 경우를 살펴보겠습니다:

* A기업 발행주식 총수 :  1,000,000주
  - 대주주 및 특수관계인 보유: 600,000주(60%)
  - 일반 주주 보유: 400,000주(40%)


* 주주총회 당일 참석 현황:
  - 대주주 및 특수관계인: 600,000주(60%) 참석
  - 일반 주주: 100,000주(10%) 참석
  - 총 참석률: 700,000주(70%)

* 그러나 감사 선임 안건에 대해서는 3% 의결권 제한이 적용됩니다:
  - 대주주와 특수관계인은 전체 발행주식의 3%인 30,000주만 의결권 행사 가능
  - 일반 주주는 100,000주 모두 의결권 행사 가능
  - 따라서 실제 의결권 행사 가능 주식은 총 130,000주

* 이 상황에서 감사 선임에 대한 찬성표가 다음과 같이 나왔다고 가정:
  - 대주주 측: 30,000주(모두 찬성)
  - 일반 주주: 40,000주(일부만 찬성)
  - **총 찬성표: 70,000주**

* 감사 선임을 위한 정족수 요건:
  - ①**출석한 주주 의결권의 과반수**: 130,000주의 과반수인 65,001주 이상 필요
  - ②**발행주식 총수의 4분의 1**: 1,000,000주의 25%인 250,000주 이상 필요
  - 이 경우 첫 번째 요건은 충족(70,000주 > 65,001주)
  - **두 번째 요건인 발행주식 총수의 4분의 1(250,000주)에는 미달**


다음 포스팅에서는 '주주제안' 안건들의 현황을 살펴보도록 하겠습니다.