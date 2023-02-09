---
layout: single
title:  'LSTM의 모든것 (1) 이론'
toc: true
categories: [Deep Learning]
tags: [timeseries, lstm]

---

본 게시물은 LSTM의 이론에 대해 [해당 포스트](https://medium.com/towards-data-science/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21)를 정리하는 글이다.
{: .notice}

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm/lstm_m_1.gif?raw=true" width="600"></p>

## 1. Introduction

### 1.1 The Problem, Short-term Memory

순환 신경망(RNN)은 sequence(문장의 길이, 시계열 등)가 길 때, 앞선 time step의 정보를 뒤의 step으로 전달하는 과정에서 손실이 발생하는 문제가 있다. 이를 short-term memory라고 하며, 이로인해 앞선 time step의 중요한 정보를 잃어버릴 수 있다. short-term memory는 backpropagation 중 발생하는 gradient  vanishing으로 야기된다. gradient는 신경망 가중치를 업데이트 하기 위해 사용되는 값, 즉 문장의 한 부분(time step)의 정보이다. 따라서 gradient vanishing은 문장이 길어질수록 한 부분에서 전달하는 gradient가 점차 감소하여 소멸되는 것으로, 앞선 time step의 정보가 뒤의 step에 전달되지 않음을 의미한다.

📍 **예시**

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm/lstm_m_2.png?raw=true" width="600" height="150"></p>

> gradient가 작아 신경망 가중치를 업데이트 시키지 못하는 것

RNN에서 매우 작은 gradient를 전달받는 계층은 학습을 중단한다. 이는 보통 앞쪽의 layer에서 발생하며, 이로인해 RNN은 긴 문장에서 본 내용을 잊을 수 있다. 이를 short-term memory(단기 기억)이라고 한다.

### 1.2 LSTM and GRU as a solution

LSTM과 GRU는 위와 같은 short-term memory 문제를 해결하기 위해 고안되었다. 이것들은 gate라고 불리는 내부 메커니즘을 가지고 있어 sequence에서의 정보 흐름을 조절할 수 있다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm/lstm_m_3.png?raw=true" width="600"></p>

위 그림에 표시된 gate (forget, input, output in LSTM/ reset, update in GRU)들은 sequence와 같은 순차적인 데이터가 입력될 때, 어떤 데이터를 보관하거나 버리는 것이 중요한지 학습할 수 있다. 이를 통해 관련된 정보를 긴 sequence에서도 전달 할 수 있게 된다. 

즉, LSTM 및 GRU에서 short-term memory를 해결하기 위해 gate가 중요한 역할임을 알 수 있다. 따라서 이번 글에서는 LSTM이 gate를 활용하여 정보를 전달하는 방법을 이해하는 것을 목표로 한다.

### 1.3 Review of Recurrent Neural Network

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm/lstm_m_5.gif?raw=true" width="600"></p>

LSTM을 이해하기 위해, 먼저 RNN 방식에 대해 리뷰한다. RNN의 첫번째 단계는 sequence의 데이터를(문장의 단어)를 기계가 읽을 수 있는 vector로 변환하는 것이다. 그런 다음 RNN은 vector의 sequence를 하나씩 처리한다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm/lstm_m_6.gif?raw=true" width="600"></p>

RNN은 이전의 hidden state를 다음 step으로 전달한다. 여기서의 hidden state는 네트워크가 이전 step에서 본 정보이며, 신경망의 메모리 역할을 수행한다. (=이전의 정보를 내재하고 있다.)

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm/lstm_m_7.gif?raw=true" width="600"></p>

RNN은 RNN cell들의 연속적인 결합으로 되어있으며, hidden state는 각 RNN cell에서 연산된다. hidden state의 연산 과정은 아래와 같다.

```
1. 입력(vector)과 이전 hidden state를 결합시켜, 현재 입력과 이전 입력에 대한 정보를 갖도록 한다. 
2. 이후 tanh를 사용한 activation function을 거쳐 새로운 hidden state 상태를 출력 값으로 전달한다.
3. 다음 step에서 위 과정 반복
```

### 1.4 Tanh activation

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm/lstm_m_8.gif?raw=true" width="600"></p>

Tanh는 입력 값들을 항상 -1과 1사이로 조절하며, 신경망을 통해 흐르는 값들을 조절하는 activation function 중 하나이다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm/lstm_m_9.gif?raw=true" width="600"></p>

vetocr가 신경망을 통해 전달될 때, 다양한 수학 연산을 거치게 된다. 만약 계속 3을 곱하는 신경망이 구성되어 있다면, 입력된 vector가 신경망을 연속적으로 통과할 시 어떠한 값은 폭발할 것이며 이로 인해 다른 값은 상대적으로 매우 작아보이게 된다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm/lstm_m_10.gif?raw=true" width="600"></p>

Tanh 함수는 출력 값을 -1과 1 사이에 있도록 하여 위와 같이 신경망의 출력을 조절한다. 

위 과정에서 소개한 Input vector와 hidden state의 연속적인 연산이 RNN의 처리 과정이다. 이를통해 연속된 데이터, 즉 sequence에 대한 정보처리가 가능하게 된다.

## 2. LSTM

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm/lstm_m_11.png?raw=true" width="600"></p>

LSTM은 RNN과 유사한 데이터 처리 흐름을 가지고 있다. RNN과의 차이점은 hidden state를 연산하기 위해 각 cell 내에서의 정보를 처리하는 과정이다. 앞서 말했듯 본 글에서는 LSTM의 동작 과정을 이해하기 위해 위 요소와 과정들에 대해 단계적으로 살펴본다.

### 2.1 Core Concept

LSTM의 핵심은 cell state와 다양한 gate들이다. cell state는 cell에서 가장 위에 그어진 윗 선에 해당하며(hidden state는 아래 그어진 선), sequence chain(반복되는 cell의 구조)을 통해 관련된 정보를 전달하는 역할을 한다. Cell state는 각 gate에서 전달된 정보(hidden state와 input vector의 연산)들과 linear한 연산들을 수행하는데, 이를 통해 sequence가 길어짐에도 이전의 정보를 포함할 수 있게 한다. 즉, short-term memory 문제를 완화시킴으로 네트워크의 memory 역할을 수행하게 한다. 각 gate는 input vector가 cell state와 연산되기 전, 어떤 정보를 기억하고 잊을지 결정하는 역할을 수행한다.

### 2.2 Sigmoid

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm/lstm_m_12.gif?raw=true" width="600"></p>

LSTM의 sigmoid는 RNN의 tanh와 유사한 역할을 한다. 차이점은 -1에서 1의 값을 갖는 tanh와 달리 sigmoid는 0에서 1사이로 값을 조정한다는 것이다. 이때, sigmoid를 통해 0이 되는 값들은 향후 cell state와 연산 시 사라지므로 정보를 **잊어버리는** 것으로 볼 수 있으며, 1이 되는 값은 정보를 **기억하는** 것으로 볼 수 있다.

### 2.3 Forget Gate

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm/lstm_m_13.gif?raw=true" width="600"></p>

앞서 sigmoid는 forget gate를 구성하는데 사용된다. 위 그림의 예시는 이전 step에서의 hidden state $h_{t-1}$와 현재 step의 input vector $X_t$의 vector간 덧셈 연산을 진행 후, 이를 sigmoid로 전달하는 것이다. 이때 sigmoid의 연산 결과가 0에 가까우면 잊으라는 뜻이고 1에 가까우면 기억하라는 뜻이다.

### 2.4 Input Gate

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm/lstm_m_14.gif?raw=true" width="600"></p>

Input gate는 먼저 forget gate와 같이 hidden state $h_{t-1}$와 input vector $X_t$의 vector간 덧셈 결과를 sigmoid와 tanh 함수로 전달한다. 그런 다음 두 출력을 곱하는데, 이때 sigmoid의 출력은 tanh의 출력 중 중요하게 볼 부분을 결정하는 역할을 하게 된다.

### 2.5 Cell State

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm/lstm_m_15.gif?raw=true" width="600"></p>

Cell state는 앞선 gate들의 결과를 통해 update를 진행한다. 먼저 cell state는 forget gate의 출력과 [element wise 곱셈](https://ko.wikipedia.org/wiki/아다마르_곱) 연산을 수행한다. 그 다음 input gate의 출력과 element wise 덧셈 연산을 수행한다. 이러한 과정을 통해 다음 step으로 새로운 cell state를 전달하게 된다.

### 2.6 Output Gate

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm/lstm_m_16.gif?raw=true" width="600"></p>

Output gate는 다음 step으로 전달할 hidden state를 결정한다. hidden state에는 이전 input에 대한 정보가 포함되어 있다. 또한 hidden state는 input에 대한 결과를 뜻하므로 최종 예측에도 사용될 수 있다. 먼저 앞서 방식과 같이 hidden state $h_{t-1}$와 input vector $X_t$의 vector간 덧셈 결과를, sigmoid 함수로 전달한다. 다음으로 update된 cell state를 tanh 함수로 전달한 뒤, 두 출력을 곱한다. 이는 hidden state가 다음 step으로 어떤 정보를 전달해야 하는지 결정하는 과정이다.

위와 같은 과정을 거쳐서 나온 새로운 cell state와 hidden state는 다음 step의 LSTM cell로 전달되게 된다.

## 3. Conclusion

RNN은 sequence 데이터에 대한 처리에 효과적이지만, 입력 데이터(sequence)의 길이가 길수록 앞부분의 정보를 잃어버리는 short-term memory 문제가 있다. 이를 해결하기 위한 방법으로 LSTM 및 GRU가 고안되었으며, 이는 gate를 통해 정보의 흐름을 효과적으로 제어하는 방식을 사용한다. LSTM과 GRU는 음성, 자연어, 시계열 등의 에측 및 분류에 사용될 수 있으며, 이와 같은 task를 수행하는 다양한 알고리즘들에 영감을 주었다.



