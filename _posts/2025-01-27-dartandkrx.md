---
layout: single
title:  "금감원과 거래소의 데이터를 결합하기 위한 고려사항"
categories: 한국시장
tag: [data background, 무상증자는 기업가치에 영향을 미칠까?, opendart, krx]
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

## 간단해 보이는 질문...
이제 금감원에서 기업별로 공시도 불러왔으니, **'그냥 주가 데이터도 갖다 붙여서'**{: style="color: #4682B4;"} 분석하면 되는거 아니야?<br>
**그냥**{: style="color: #4682B4;"} 갖다 붙일 수 있을까요...? 생각보다 쉽지 않습니다.

## 데이터출처 배경설명
우리가 공시데이터를 불러온 방시은 OpenDart API는 아니고, OpenDart의 웹크롤링 방식이었습니다. 각 데이터출처별 어떤 장단점이 있는지 보겠습니다.
### OpenDart API 사용의 장점과 단점
OpenDart API를 통해 데이터를 취득하면, 대상 회사가 명확하게 식별이 됩니다. 즉, 금감원의 CIK(corpcode)와 거래소의 종목코드(stock_code)가 각 행마다 기재됩니다. 따라서 ***'이 회사가 그 회사다'***{: style="color: #4682B4;"}를 명확히 알 수 있습니다.<br>
반면 OpenDart API의 단점으로는 시장 전체 데이터를 ***'한번에'***{: style="color: #4682B4;"} 긁을 수 없다는 것이 있습니다. <br>
### OpenDart 웹크롤링의 장점과 단점
OpenDart API의 이러한 번거로움을 우회하고자, 이전 포스팅에서는 OpenDart의 웹페이지內 '공시정보활용마당' 화면에서 requests.post 방식으로 데이터를 수집했습니다. 이렇게 하면 시장전체의 데이터를 한번에 받아 올 수 있습니다. 그러나 아래와 같은 단점도 있습니다.<br>
* **회사명 표출**{: style="color: #4682B4;"} : 예를 들어, 코스피 상장법인 '보령'의 경우 ***'유보령 IR'***{: style="color: #4682B4;"}이라고 데이터가 수집됩니다. 이는 아래 사진을 보면 이해하실 수 있는데요, DART 페이지에서는 회사명을 띄울 때, ***"시장구분 + 회사명 + IR로고(IR웹페이지가 있는경우)"***{: style="color: #4682B4;"}로 띄워줍니다. 이 부분은 이전 사례에서처럼 간단히 데이터 전처리할 수 있으므로 크게 문제가 되진 않습니다.<br><br>
![example]({{site.url}}/assets/images/2025-01-27-dartandkrx/example.png)
<br><br>

* **종목코드 미포함**{: style="color: #4682B4;"} : 더 큰 문제는 '회사명'만 있다는 점입니다. 회사명이 있는데 뭐가 문제냐고요? 생각보다 간단하지 않습니다.<br>
코스피 상장사 **'현대엘리베이터'**{: style="color: #4682B4;"}를 네이버증권에서 검색해보겠습니다. **현대엘리베이...? 오타가 아닙니다.**{: style="color: #4682B4;"} 거래소 [정보데이터시스템](https://data.krx.co.kr)에도, 코스콤 체크단말기에도 모두 '현대엘리베이'로 되어있습니다. **공식 종목명이 맞습니다.**{: style="color: #4682B4;"} 한편 **DART에서는 '현대엘리베이터'**{: style="color: #4682B4;"} 표시됩니다.<br>
다른 예를 보겠습니다. 코스닥 상장사 **브릿지바이오테라퓨틱스**{: style="color: #4682B4;"}라는 회사가 네이버증권에서 조회됩니다. 반면 **DART에서는 '브릿지바이오'**{: style="color: #4682B4;"}입니다.<br>
따라서 금감원 OpenDart 웹페이지 크롤링 결과에서 **회사명을 기준으로 거래소 홈페이지의 종목코드를 맵핑(vlookup)하려고 하면 맵핑이 안되는 회사들이 나올 수 있습니다.**{: style="color: #4682B4;"}<br><br>
![comparison]({{site.url}}/assets/images/2025-01-27-dartandkrx/comparison.png)<br>

## 종목코드는 반드시 필요합니다!
상장사에 대한 정보를 조회할 때 기준이 되는 가장 대표적인 정보는 **종목코드**{: style="color: #4682B4;"}입니다. 즉, **종목코드는 상장사 정보의 식별자(ID)**{: style="color: #4682B4;"}라고 볼 수 있습니다. 하나의 데이터셋(공시항목)은 금감원에서, 다른 데이터셋(주가)은 한국거래소에서 받아왔을 때(**즉 데이터의 출처가 다를때**{: style="color: #4682B4;"}), **이 데이터들을 엮어줄 수 있는 것은 종목코드(데이터ID)입니다.**{: style="color: #4682B4;"}<br>
그럼에도 불구하고 한국거래소와 금융감독원의 많은 페이지에서 종목코드 없이 회사명만으로 데이터가 표출되는 것이 ***개인적으로는 데이터 분석의 관점에서*** 아쉽습니다.

## 같은 출처에서 데이터의 ID를 찾자!
다시 주제로 돌아와봅시다. 우리의 메인 데이터인 **주요사항보고서 공시정보**{: style="color: #4682B4;"}는 **회사명만 있고 종목코드가 없습니다.**{: style="color: #4682B4;"} 그렇다고 **한국거래소 정보데이터시스템**{: style="color: #4682B4;"}에서 불러온 상장종목 리스트를 vlookup 걸자니, **회사명이 달라 맵핑되지 않는 경우**{: style="color: #4682B4;"}가 있습니다. 해결방법은 두가지로 보입니다.
1. **수작업으로 종목코드 맵핑**{: style="color: #4682B4;"}<br>아마 '현대엘리베이'와 '브릿지바이오(테라퓨틱스)'와 같은 사례가 많지는 않을 것입니다. 따라서 vlookup과정에서 에러가 난 종목들을 확인하고, 종목코드를 수기로 넣어주는 방법이 가능합니다. <br>그러나 이 방법은 **'유지보수'가 필요한 방법**{: style="color: #4682B4;"}입니다. 새로운 상장사가 생길때, 또는 회사명을 변경할 때 얼마든지 이런 상황이 발생할 수 있습니다. 따라서 주기적으로 에러 맵핑을 수행해줘야 합니다.
<br>

2. **금감원에서 '회사명-종목코드' 맵핑 정보를 뒤져보기**{: style="color: #4682B4;"}<br>DART를 사용하다보면 사용자 편의를 위해 노력을 정말 많이 한 것을 느낄 수 있습니다. 그렇다면... DART의 어딘가에는 '회사명-종목코드' 맵핑 정보를 조회할 수 있는 곳이 있지 않을까요...?<br><br>![dartstockcode]({{site.url}}/assets/images/2025-01-27-dartandkrx/dartstockcode.png)<br><br>있습니다! DART(OpenDart가 아니라 그냥 DART) 메뉴중 '기업개황'에 가면 시장별로 상장사 목록을 조회할 수 있는 기능이 있습니다. 여기서 requests.get 방식으로 엑셀을 받아올 수 있습니다. ***금감원의 데이터에서 회사정보와 종목코드를 맵핑할 수 있는 해결방법을 찾았습니다!***{: style="color: #4682B4;"}<br><br>  

> 분석을 위해선 **데이터식별자(우리의 경우 '종목코드')가 필요**{: style="color: #4682B4;"}합니다. 그리고 그 **데이터식별자는 동일한 출처에서 찾는 것이 이상적**{: style="color: #4682B4;"}입니다.




