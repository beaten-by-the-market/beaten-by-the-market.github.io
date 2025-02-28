---
layout: single
title:  "무상증자의 회계처리와 기업가치"
categories: 한국시장
tag: [data background, 무상증자는 기업가치에 영향을 미칠까?]
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


**'무상증자는 기업가치에 영향을 미칠까?'**주제에 대해 일련의 포스팅을 작성해보고자 합니다. 블로그 상단의 'Tag'를 통해 본 주제와 관련된 포스팅을 모아볼 수 있습니다.
{:.notice--warning}


## 무상증자는 회계적으로 어떤 사건일까?

무상증자가 기업가치에 영향을 미치는지 알기 위해, 먼저 회계적으로 어떤 이벤트가 생기는지 보는 것이 좋을 것 같습니다. **기업가치를 평가할 땐 결국 회계상 숫자를 활용**{: style="color: #4682B4;"}하게 되니까요.

## 무상증자에 앞서 유상증자부터!

무상증자의 회계적 효과를 이해하기 전에, 먼저 유상증자의 회계처리를 보고 오도록 하겠습니다. 유상증자의 개념이 더 직관적이어서 유상증자를 먼저 보고 무상증자를 보는 게 나을 것 같습니다.<br>
> 유상증자란 돈을 받고 주식을 발행해주는 것입니다.

<br>

한 회사가 있습니다. 이 회사의 주식은 액면가 500원입니다. 기업의 가치가 어찌저찌 올라서 이젠 회사의 주식가치는 1,000원이 되었습니다. 그리고 회사는 1주를 추가로 발행하는 유상증자를 결정하였습니다. **그러면 1,000원이 회사에 들어오고, 회사의 주식은 1주 증가하게 됩니다.**{: style="color: #4682B4;"}
<br>

### 유상증자의 회계처리

1,000원의 현금이 회사에 유입되었다면, 회사의 장부에는 현금 +1,000이 될 것입니다. 그리고 주식을 1주 발행했으니 자본금이 +500(액면가액)이 될 것입니다. 그리고 남은 500원은 자본잉여금으로 회계처리합니다.<br>

![1paidincap]({{site.url}}/assets/images/2025-01-27-bonusissue/1paidincap.png)<br><br>


## 무상증자란?

유상증자에서 현금의 유입이 없는 게 무상증자라고 볼 수 있습니다. 즉, 돈을 안받고 주식을 추가로 발행해 주는 것입니다. 1주당 1주 무상증자를 했다고 한다면, 주주 입장에서는 만약 10주를 들고있었으면, 주식 잔고에 10주가 더 생겨서 20주를 보유하게 되는 효과입니다.<br>
한편 주식을 1주 발행하면 액면가만큼 자본금이 증가하는데요, 유상증자와 달리 외부에서 받은 돈이 없으니 내부에 기존에 있던 잉여금에서 끌어다 써야 합니다. **어떤 잉여금(재원)을 사용할 것인가**{: style="color: #4682B4;"}에 따라서 배당소득세를 낼수도 있습니다. 다만 무상증자가 이뤄지는 대다수의 경우, 자본잉여금을 재원으로 하여 배당소득세를 내지 않는 것으로 파악되고 있습니다.
<br>
> 무상증자란 돈을 받지 않고 주식을 발행해주는 것입니다.
<br>

### 무상증자의 회계처리

기존 발행된 주식 1주당 1주를 추가로 발행해주는 무상증자의 예를 보겠습니다. 현금의 유입 없이 주식을 발행한다고 했으니, 자본잉여금 계정(재원)을 차감(△500원)하여 자본금을 증가(+500원)시키는 회계처리를 합니다. 재무상태표상으로는 ***500원 줄고 500원 늘고*** 하는 현상이 동시에 일어나니 변화는 없습니다.<br>


![2bonusissue]({{site.url}}/assets/images/2025-01-27-bonusissue/2bonusissue.png)<br>


## 유상증자와 무상증자의 비교

1주를 추가로 발행하는 유상증자와 무상증자를 비교해 보겠습니다. <br>
* **유상증자**{: style="color: #4682B4;"}의 경우 현금의 유입이 있으니 재무상태표의 자산(차변)도 늘고, 자본(대변)도 늘어나서 결과적으로는 **재무상태표가 기존보다 커졌습니다.**{: style="color: #4682B4;"}
<br>

* **무상증자**{: style="color: #4682B4;"}의 경우 재무상태표의 자본(차변)이 늘었지만, 마찬가지로 자본(차변)이 줄어서 결과적으로는 **재무상태표의 크기가 기존과 동일합니다.**{: style="color: #4682B4;"}
<br>

그렇다면 **회계처리 관점에서 기업의 가치가 증가하는 경우는 유상증자일까요 무상증자일까요?**{: style="color: #4682B4;"} 그림만 본다면 무상증자는 기업가치가 증가할 여지가 없어보이는데... 무상증자가 회계장부가 아닌 주주에게 미치는 영향을 좀 더 둘러봐야겠습니다.
<br>

![3comparison]({{site.url}}/assets/images/2025-01-27-bonusissue/3comparison.png)<br><br>



