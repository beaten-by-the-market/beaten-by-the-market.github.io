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
      white-space: normal;
      width: 300%;
      max-width: 600%;
      height: 300px;  /* 고정 높이 유지 */
      display: inline-block;
      overflow-x: scroll;  /* 가로 스크롤 */
      overflow-y: scroll;  /* 세로 스크롤 */
      font-family: Arial, sans-serif;
      font-size: 0.9rem;
      line-height: 20px;
      text-align: center;
      border: 0px !important;
    }

    table.dataframe th {
      text-align: center;
      font-weight: bold;
      padding: 8px;
    }

    table.dataframe td {
      text-align: center;
      padding: 8px;
    }

    table.dataframe tr:hover {
      background: #b8d1f3; 
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
      margin: 0 0 0px !important;
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



