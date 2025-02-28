---
layout: single
title:  "자사주 취득의 데이터는 어디서 구할까? (2편)"
categories: 한국시장
tag: [data background, opendart, 자기주식]
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


**[관련 포스팅]** [자사주 매매 프로세스](https://beaten-by-the-market.github.io/%ED%95%9C%EA%B5%AD%EC%8B%9C%EC%9E%A5/buybackexplanation/)
{:.notice--success}

<br>
<br>

## 자사주 매매 프로세스별 데이터를 구하는 곳은?


자사주 매매 프로세스별 데이터를 어디서 구할 수 있을까요? 의사결정에 대한 데이터, 매매체결에 대한 데이터, 결과보고에 대한 데이터 순으로 보겠습니다.<br>
<br>
<br>   
   
## 1. 의사결정에 대한 데이터

   
회사는 자기주식을 취득/처분하기로 이사회에서 결정하면, 당일 금융감독원에 **"주요사항보고서"**{: style="color: #4682B4;"}를 제출한다고 하였습니다. 개별 공시를 하나씩 까봤다면 데이터를 확인할 엄두도 못냈겠지만, 고맙게도 금감원은 [**OpenDart**{: style="color: #4682B4;"}](https://opendart.fss.or.kr/)라는 서비스를 운영중입니다. (OpenDart에서 사용할 수 있는 다양한 데이터들의 활용사례는 향후 포스팅에서 차차 풀어보도록 하겠습니다.) <br>
<br>
자사주 매매 의사결정에 대한 데이터는 OpenDart에 접속하면 보이는 아래의 두 개 메뉴를 통해서 확인이 가능합니다. "개발가이드" 부분은 OpenDart API를 사용하는 방식이고, "공시정보활용마당" 부분은 웹으로 조회하고 엑셀 다운로드가 되는 기능입니다. <br>
OpenDart API의 경우 회사코드가 필수 입력인자라서 상장사 개수만큼 loop을 돌려야 하는 부담이 있습니다. 따라서 "공시정보활용마당"을 이용해보도록 하겠습니다.
<br>

![opendartmenu]({{site.url}}/assets/images/2025-01-22-buybackexpl2/opendartmenu.png)<br>

<br>

"공시정보활용마당-주요사항보고서 주요정보조회"에서 볼 수 있는 화면입니다. 필수로 입력해야 하는 인자가 "기간"뿐이고, 전체 상장사를 대상으로 조회 및 엑셀 다운로드가 가능하도록 되어있습니다. ***(정말 편리하네요!)***<br><br>


![search]({{site.url}}/assets/images/2025-01-22-buybackexpl2/search.png)<br>

<br>

"검색"버튼 클릭만으로 이렇게 시장 전체의 공시이력을 모아볼 수 있습니다. 단, 제공하는 데이터의 범위는 공시의 주요사항이 들어있는 본문의 첫번째 표에 기재된 내용입니다. 
* 취득예정주식수
* 취득예정금액
* 취득예정기간
* 취득목적
* 취득방법
* 위탁중개투자업자
* 취득전 자기주식 보유현황 : 배당가능이익범위 내 주식, 기타취득 주식
* 취득결정일
* 사외이사, 감사 참석여부
* 1일 매수 주문수량 한도(장내에서 취득하는 경우)
* 비고
<br>

![searchresult]({{site.url}}/assets/images/2025-01-22-buybackexpl2/searchresult.png)<br>

한편, 제공되는 데이터는 **회사가 작성한**{: style="color: #4682B4;"} 데이터입니다. 즉, 만약에 회사가 오타를 냈다면... 그부분의 정합성까지는 담보될 수 없습니다. <br>
<br>

   
## 2. 실행단계의 데이터
    
실행단계, 즉 매매를 하는 과정은 크게 **장내취득**{: style="color: #4682B4;"}과 **장외취득**{: style="color: #4682B4;"}으로 이뤄진다고 말씀드린 바 있습니다. **장내취득의 경우 KRX 정보데이터시스템을 통해 확인이 가능**{: style="color: #4682B4;"}하나, **장외의 경우 확인할 수 있는 방법은 없습니다.**{: style="color: #4682B4;"}<br>

### 장내에서 취득하는 경우

<br>
[**KRX 정보데이터시스템**{: style="color: #4682B4;"}](http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0202) 의 의 "이슈통계 - 자사주추득/처분"메뉴에서는 전체 상장사의 자사주 관련 누적 매매실적을 확인할 수 있습니다. <br>

제공되는 데이터중 "공시일"과 "취득(처분)예정기간"은 금감원에 제출된 공시의 내용을 기반으로 합니다. 따라서 자기주식을 취득/처분하겠다는 **각 의사결정별로 실제로 얼마나 이행했는지를 확인**{: style="color: #4682B4;"}해볼 수 있는 부분입니다. 물론 장내에 한정해서요.<br>
<br>

![krxresult]({{site.url}}/assets/images/2025-01-22-buybackexpl2/krxresult.png)


## 3. 결과보고에 대한 데이터


자기주식 취득에 대한 결과는 금융감독원에 제출되는 **1)결과보고서와 2)정기보고서(사업보고서, 분/반기 보고서)**를 통해 확인이 가능하다고 말씀드린 바 있습니다.<br>

### 결과보고서
아쉽게도 자기주식취득/처분 결과보고서는 OpenDart에서 제공하고 있지 않습니다. 표준화된 표 형태로 잘 정리되어 있지만, 일괄로 받을 수 있는 방법은 현재는 없습니다. 그래도 표준화가 되어있으니, OpenAPI로 각 URL을 받은 후 크롤링을 통해 데이터를 수집하는 것은 가능합니다. 추후에 기회가 되면 진행해 보도록 하겠습니다. <br>
<br>

### 정기보고서(사업, 분/반기보고서)
비록 적시성은 떨어지지만(45~90 이후 제출), 개별 정기보고서 화면에서는 이렇게 기재되는 내용이 있습니다. (**"Ⅰ. 회사의 개요 - 4. 주식의 총수 등 - 나. 자기주식 취득 및 처분 현황"**{: style="color: #4682B4;"}) 기초수량과 변동수량(취득, 처분, 소각), 그리고 기말수량이 잘 정리되어 기재되어 있습니다.<br><br>
![annualreportex]({{site.url}}/assets/images/2025-01-22-buybackexpl2/annualreportex.png)

<br><br>

다행히도 OpenDart에서는 사업보고서와 분/반기보고서에 기재된 자기주식 취득/처분 데이터를 일괄로 받아볼 수 있습니다. OpenAPI로도 수집은 가능하지만 회사별로 loop을 돌려야 하는 관계로, **"공시정보활용마당 - 정기보고서 주요정보조회"**{: style="color: #4682B4;"}에서 데이터를 확인해보았습니다. 
<br>
<br>

![annualreportmenu]({{site.url}}/assets/images/2025-01-22-buybackexpl2/annualreportmenu.png)
<br>
<br>
정기보고서에 기재된 내용 전체가 일괄 조회가 되며, 엑셀 형태로도 다운이 가능합니다. ***(정말 편리하네요!)***
<br>

![annualsearchresult]({{site.url}}/assets/images/2025-01-22-buybackexpl2/annualsearchresult.png)
<br>
<br>
하지만 한 가지 아쉬운 점이 있습니다. 통상 상장되어 있는 보통주를 기준으로 데이터를 뽑아보고 싶을텐데, **"주식의 종류" 칼럼을 살펴보면 회사마다 기재하는 방식이 천차만별**{: style="color: #4682B4;"}입니다. 오타와 오기재 사항도 상당수 있습니다. 2023년 사업보고서 코스피, 코스닥 전체를 대상으로 다운받은 엑셀파일에서 "주식의종류"를 확인해보니 아래와 같이 다양한 사례가 존재합니다. ***표현이 통일이 되지 않았으며, 오타도 있고, "기초수량"을 "주식의종류"에 실수로 기재한 경우도 있습니다.*** 오기재된 부분이 엄청난 양은 아니다 보니 어느정도의 수작업 보정을 통해서 처리할 수 있는 수준이긴합니다만... 10년치를 분석하고자 하는 경우, 향후에도 계속 수집하고자 하는 경우에는 상당히 번거로워질 수 있습니다.<br>

![type]({{site.url}}/assets/images/2025-01-22-buybackexpl2/typo.png)
<br><br>


## 4. 각 데이터의 품질
앞에서는 의사결정단계, 실행단계, 결과보고단계별 데이터 출처를 살펴보았습니다. 품질이라는 표현이 맞을진 모르겠으나, 각 출처의 특성에 따라서 ***어느 수준의 cleansing***을 해야할지가 차이가 날 것으로 보입니다.
<br><br>
**1. 주요사항보고서**{: style="color: #4682B4;"}<br>
* 취득방법(장내, 장외)을 기재할 때 선택지에서 선택하는 방식이 아닌 free text로 기재하는 방식이기 때문에, 일부 표준화가 덜된 항목이 있습니다.
* 회사가 수기로 입력한다는 면에서 오타 등의 가능성을 배제할 수는 없습니다.
* ***그러나 제출된 공시의 수량과 기간 정보는 KRX 정보데이터시스템에 등재되는 과정이 있으므로, 숫자상 오류가 날 가능성은 적습니다.*** 
<br><br>

**2. 거래소 데이터**{: style="color: #4682B4;"}<br>
* 주문정보와 체결정보는 모두 숫자로 전산화된 과정을 거치기 때문에 데이터를 바로 사용가능합니다.
* ***그러나 거래소의 관할영역 밖인 장외 데이터가 없다는 단점은 여전히 있습니다.*** 
<br><br>

**3. 정기보고서**{: style="color: #4682B4;"}<br>
* 취득/처분 뿐만 아니라 소각 수량까지 함께 갖고 있기에 활용성이 높습니다.
* 장내 뿐만 아니라 장외 수량까지 있기 때문에 전체를 파악하기에 유용합니다.
* ***그러나 수기로 입력되고 있으며, 표준화가 덜된 부분이 있어서 전처리가 필요합니다.***