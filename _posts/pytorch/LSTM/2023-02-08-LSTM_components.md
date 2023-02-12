---
layout: single
title:  'LSTM의 모든것 (2) PyTorch 공식 문서로 보는 구성요소'
toc: true
categories: [Deep Learning]
tags: [lstm, pytorch]
---

본 게시물은 [Pytorch 공식 문서](https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html)를 참고하여 LSTM의 구성요소에 대해 정리하는 글이다.
{: .notice}

## 1. Parameters

```python
torch.nn.LSTM(input_size, hidden_size, num_layers, bias, batch_first, dropout, bidirectional, proj_size)
```

### 1.1 input_size / hidden_size

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm/lstm_c_4.png?raw=true" width="600" height="300"></p>

- input_size는 입력되는 데이터의 차원이다. 입력되는 데이터는 보통 (batch_size, sequence_length, input_size)로 구성되며, sequence_length는 시계열 혹은 문장의 길이, input_size는 시계열에 포함된 feature 수 혹은 단어의 임베딩의 차원으로 볼 수 있다.

- hidden_size는 hidden state의 차원이다. 입력된 데이터가 연산을 통해 가지게 될 차원으로 볼 수 있다.

### 1.2 num_layers

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm/lstm_c_5.png?raw=true" width="350" height="350"></p>

- num_layers는 LSTM cell을 stack하는 수이다. 유의할 점은 첫번째 layer에서는 input으로 입력 데이터가 들어가나 두번째 layer는 input으로 첫번째 layer의 hidden state가 들어간다는 것이다. 따라서 두번째 lstm의 input과 연산되는 weight의 차원이 바뀌게 된다.

### 1.3 bias

- bias는 hidden state와 input이 각 gate에서 선형결합시 따라오는 것으로 hidden sate의 차원과 동일하다.

### 1.4 batch_first

### 1.5 dropout

### 1.6 bidirectional

### 1.7 proj_size

## 2. CLASS

### 2.1 Componenets

- $i_t, f_t, o_t$ : input / forget/ output gate의 출력
- $c_t, g_t$ : cell state와 이를 구하기 위한 중간 연산(i_t와 element-wise 곱을 수행함)
- $W_i, W_h$ : input과 hidden의 선형결합시에 사용되는 가중치
- $b_i, h_i$ : bias

### 2.2 Calculate

📍 **예시**

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm/lstm_c_6.png?raw=true" width="900" height="500"></p>

> Hidden size: 2, Input size 3, Num layers 1일때 각 cell에서 component들이 연산되는 과정

### 1.3 Component Shape

- $x_t$ : [input_size, 1]
- $h_t$ : [hidden_size, 1]
- $W_{i}$
  - at first layer : [hidden_size, input_size]  
  - otherwise : [hidden_size, num_directions * hidden_size] 
  - proj_size > 0 : [hidden_size, proj_size] not at first layer
- $W_{h}$
  - at first layer : [hidden_size, hidden_size]
  - proj_size > 0 : [hidden_size, proj_size]
- $b_i$ : [hidden_size]
- $b_h$ : [hidden_size]

## 3. Inputs

## 4. Outputs

## 5. Variables



