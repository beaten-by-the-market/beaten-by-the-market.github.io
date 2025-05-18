---
layout: single
title:  "니가 그렇게 의결권이 많아? 주총장으로 따라와"
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
**[관련 포스팅]** [의결권 원기옥을 모으기 위해서는 대리인이 필요하다?](https://beaten-by-the-market.github.io/%ED%95%9C%EA%B5%AD%EC%8B%9C%EC%9E%A5/proxy1/)<br>
{:.notice--success}


## 너가 그렇게 의결권이 많아? 주총장으로 따라와
![21maljuk]({{site.url}}/assets/images/2025-05-15-proxy/21maljuk.png)<br><br>

영화 말죽거리 잔혹사에서는 주인공이 "너가 그렇게 싸움을 잘해? 옥상으로 따라와"라고 대결을 신청하는 장면이 있습니다. 나쁜 학교 짱이 교실에서 행패를 부리자 보다못한 주인공이 그동안 갈고닦은 격투기 실력을 바탕으로 도전한 것입니다.<br>
이는 마치 대주주의 의사결정에 반발하여 의결권을 모아온 소액주주들이 **"너가 그렇게 의결권이 많아? 주총장으로 따라와"**{: style="color: #4682B4;"}라며 대결을 신청하는 것과 비슷한 면이 있는 것 같습니다.


## 재밌는 싸움구경, 어디어디 싸움났나?
분석대상인 2023~2025년(글 작성시점 5월)에 Proxy Fight가 발생했을 가능성이 있는 사례들을 확인해보겠습니다.. 싸움의 가능성은 다음의 기준으로 하였습니다.
1. **'같은 주주총회일 & 같은 회사'**{: style="color: #4682B4;"} 이면서, 
2. '의결권 대리행사 권유 참고서류' **공시를 제출한 주체가 2곳 이상**{: style="color: #4682B4;"}인 경우


동일한 주주총회에 대해서 '의결권 대리행사 권유 참고서류' 공시를 2곳 이상이 제출했다는 것은 **해당 주총에 의결권을 모으고 있는 주체가 2곳 이상**{: style="color: #4682B4;"}이라는 의미입니다. 따라서 Proxy Fight 발생의 단서로 삼았습니다.


공시를 분석한 결과, **총 185건의 주주총회**{: style="color: #4682B4;"}에서 Proxy Fight의 단서를 찾을 수 있었습니다.<br>
* **코스피(총 90건)**{: style="color: #4682B4;"} : 2023년 20건 / 2024년 35건 / 2025년 35건
* **코스닥(총 95건)**{: style="color: #4682B4;"} : 2023년 39건 / 2024년 38건 / 2025년 18건


## 시시한 싸움, 재밌는 싸움
모든 싸움이 재미있는 것은 아닐 것입니다. 시시한 싸움도 있고, 치열해서 흥미로운 싸움도 있을 것입니다. 주주총회에서 벌어지는 의결권 대리행사 싸움도 마찬가지입니다. 데이터를 분석해보니 다양한 유형의 '싸움'이 존재했는데요, 이를 7가지 카테고리로 분류해보았습니다.<br>

* **Case 1: 싸움처럼 보이지만 싸움이 아닌 경우**{: style="color: #4682B4;"}<br>
**여러 주체가 의결권 대리행사 권유 참고서류를 제출했지만, 실제로 법인이나 개인 대리인을 선임하지 않은 경우**입니다. 마치 싸움을 걸어놓고 실제 결전장에는 아무도 나타나지 않은 상황과 비슷합니다. 이런 경우는 진정한 의미의 Proxy Fight라고 보기 어렵습니다.

* **Case 2: 무리한 도전, 무시하는 회사**{: style="color: #4682B4;"}<br>
**주주가 개인 대리인을 통해 의결권을 모아 회사 측에 도전장을 내밀었지만, 회사는 이에 대응하지 않는 경우**입니다. 아무래도 개인이 의결권을 모으기에는 역량이 부족하겠지요. 이에 **회사 측은 대리인을 선임하지 않고 무시 전략**을 취합니다. 마치 학교 짱에게 도전했지만 상대가 "너랑 싸울 가치도 없어"라며 무시하는 상황과 비슷합니다.

* **Case 3: 권유대리 법인을 선임한 주주의 도전, 회사의 무시**{: style="color: #4682B4;"}<br>
**이번에는 권유 대리인으로 전문법인을 선임하여 회사에 도전했지만, 역시 회사는 대리인을 선임하지 않고 무시**합니다. 더 전문적으로 의결권을 모아서 도전했음에도 회사가 대응하지 않는 것은 자신감의 표현일 수도 있고, 아니면 이미 승부가 결정났다고 판단했기 때문일 수도 있습니다.

* **Case 4: 무리한 도전, 형식적인 대응**{: style="color: #4682B4;"}<br>
주주가 개인 대리인을 통하여 도전했을 때, **회사는 대리법인을 선임하지 않고, 내부 직원을 내세워 대응하는 경우**입니다. 회사 입장에서는 "굳이 의결권 대리행사 권유 대리법인을 고용할 필요 없이, 우리 직원으로도 충분히 대응 가능하다"는 판단을 한 것으로 볼 수 있습니다.

* **Case 5: 권유대리 법인을 선임한 주주의 도전, 회사의 직원 대응**{: style="color: #4682B4;"}<br>
**권유 대리인으로 전문법인을 선임하여 도전했을 때도 회사는 직원을 내세워 대응하는 경우**입니다. 법인을 통해 의결권을 모았음에도 회사가 외부 법인을 고용하지 않고 직원으로 대응하는 것은 여전히 위협을 크게 느끼지 않는다는 신호일 수 있습니다.

* **Case 6: 본격적인 전쟁**{: style="color: #4682B4;"}<br>
이제야 진정한 의미의 Proxy Fight라고 할 수 있는 경우입니다. **회사와 도전자 모두 법인 대리인을 선임하여 본격적인 의결권 전쟁**을 벌입니다. 가장 흥미진진하게 관전할 수 있는 케이스입니다.

* **Case 7: 비대칭 대결**{: style="color: #4682B4;"}<br>
회사는 법인 대리인을 선임했지만, 도전자 측은 개인 대리인만 내세운 경우입니다. 회사가 전문 법인의 도움을 받는 반면, 도전자는 개인의 힘으로 맞서는 다소 비대칭적인 구도입니다. **Proxy Fight를 염두에 두었다기 보다는 의결정족수 확보를 위해 선임한 경우일 가능성**이 높아 보입니다.

### 케이스별 빈도

<pre>
<table border="1" class="dataframe dataframe">  
  <thead>  
    <tr style="text-align: right;">  
      <th>case</th>  
      <th>count</th>  
    </tr>  
  </thead>  
  <tbody>  
    <tr>  
      <td>case1</td>  
      <td>33</td>  
    </tr>  
    <tr>  
      <td>case2</td>  
      <td>2</td>  
    </tr>  
    <tr>  
      <td>case3</td>  
      <td>15</td>  
    </tr>  
    <tr>  
      <td>case5</td>  
      <td>1</td>  
    </tr>  
    <tr>  
      <td>case6</td>  
      <td>98</td>  
    </tr>  
    <tr>  
      <td>case7</td>  
      <td>29</td>  
    </tr>  
  </tbody>  
</table>
</pre>


다음 포스팅에서는 케이스별 어떤 기업들이 있었는지를 보도록 하겠습니다.