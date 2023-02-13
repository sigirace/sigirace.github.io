---
layout: single
title:  'LSTM의 모든것 (2) PyTorch 공식 문서로 보는 구성요소'
toc: true
categories: [Deep Learning]
tags: [lstm, pytorch]
---

본 게시물은 [Pytorch 공식 문서](https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html)를 참고하여 LSTM의 구성요소에 대해 정리하는 글이다.
{: .notice}

<div class="notice">
<li><a href="https://sigirace.github.io/deep%20learning/LSTM_method///">LSTM의 모든것 (1) LSTM 및 내부 Gate에 대한 이해</a></li>
</div>


## 1. Parameters

```python
LSTM(input_size, hidden_size, num_layers, bias, batch_first, dropout, bidirectional, proj_size)
```

### 1.1 input_size / hidden_size

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm_c/lstm_c_2.png?raw=true" width="800" height="300"></p>

```
input_size – The number of expected features in the input x
hidden_size – The number of features in the hidden state h
```

- <mark style='background-color: #f6f8fa'>&nbsp;input_size </mark>는 입력되는 **데이터의 차원**이다. 단일로 입력되는 데이터는 (sequence_length, input_size)로 구성되며, sequence_length는 시계열 혹은 문장의 길이, input_size는 시계열에 포함된 feature 수 혹은 단어의 임베딩의 차원으로 볼 수 있다.

- <mark style='background-color: #f6f8fa'>&nbsp;hidden_size </mark>는 **hidden state의 차원**이다. 입력된 데이터가 연산을 통해 가지게 될 차원으로 볼 수 있다.

### 1.2 num_layers

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm_c/lstm_c_3.png?raw=true" width="350" height="350"></p>

```
num_layers – Number of recurrent layers.
E.g., setting num_layers=2 would mean stacking two LSTMs together to form a stacked LSTM,
with the second LSTM taking in outputs of the first LSTM and computing the final results.
[Default: 1]
```

- <mark style='background-color: #f6f8fa'>&nbsp;num_layers </mark>는 **LSTM cell을 stack하는 수**이다. 유의할 점은 첫번째 layer에서는 input으로 입력 데이터가 들어가나 두번째 layer는 input으로 첫번째 layer의 output인 hidden state가 들어간다는 것이다. 따라서 두번째 lstm의 input과 연산되는 weight는 차원이 바뀌게 된다. (✤ 참고: variables의 weight_ih_l[k], weight_hh_l[k])

### 1.3 bias

```
bias – If False, then the layer does not use bias weights b_ih and b_hh. 
[Default: True]
```

- <mark style='background-color: #f6f8fa'>&nbsp;bias </mark>는 hidden state와 input이 각 gate에서 matrix와 vector의 곱 연산(선형변환)시 따라오는 것으로 **hidden sate의 차원과 동일**하다.

### 1.4 batch_first

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm_c/lstm_c_5.png?raw=true" width="850" height="500"></p>

```
batch_first – If True, then the input and output tensors are provided as (batch, seq, feature) 
instead of (seq, batch, feature). Note that this does not apply to hidden or cell states. 
See the Inputs/Outputs sections below for details. 
[Default: False]
```

- <mark style='background-color: #f6f8fa'>&nbsp;batch_first </mark>는 mini batch 학습시 batch size가 데이터 shape의 가장 첫번째 요소인지 확인하는 것이다. 아래는 단방향(bidirectional=False)일때의 batch_first에 따른 data set과 output의 형 변화 예시이다.

📍**예시**

> True ☞ [batch_size, sequence length, input_size] / [batch_size, sequence length, hidden_size]
>
> False ☞ [sequence length, batch_size, input_size] /  [sequence length, batch_size, hidden_size]

### 1.5 dropout

```
dropout – If non-zero, introduces a Dropout layer on the outputs of each LSTM layer 
except the last layer, with dropout probability equal to dropout.
[Default: 0]
```

- <mark style='background-color: #f6f8fa'>&nbsp;dropout </mark>은 0이 아닐시 마지막 layer를 제외한 각 LSTM의 각 layer의 출력에 입력한 인자의 확률을 가진 dropout layer를 추가 한다.

### 1.6 bidirectional

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm_c/lstm_c_6.png?raw=true" width="850" height="500"></p>

```
bidirectional – If True, becomes a bidirectional LSTM. 
[Default: False]
```

- <mark style='background-color: #f6f8fa'>&nbsp;bidirectional </mark>은 각 layer를 양방향 LSTM cell로 구성할지 결정하는 것이다. 일반적으로 양방향 LSTM을 사용할 경우 sequence 데이터에서 많은 정보를 추출할 수 있기 때문에 성능이 좋게 나타난다. 어느 한 time step의 hidden state는 보통 순방향과 역방향의 hidden state를 concatenation하여 다음 layer로 전달하는데, 이때 hidden state는 2*hidden_size의 크기를 가진다.

### 1.7 proj_size

- <mark style='background-color: #f6f8fa'>&nbsp;proj_size </mark>는 LSTM cell의 output 중 하나인 $h_t$을 learnable projection matrix를 통해 선형변환시키는 인자이다. (개인적으로 왜 사용해야 하는지 아직 의문이기 때문에 공식문서에서 첨부한 논문을 보고 추후 업데이트 하기로 한다.)

## 2. Inputs

```
input, (h_0, c_0)
```

### 2.1 Shape

- input : $(N, L, H_{in})$ when batch_first=True
- $h_0$ : $(D*layers, N, H_{out})$
- $c_0$ : $(D*layers, N, H_{cell})$

### 2.2 Components

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm_c/lstm_c_7.png?raw=true" width="450" height="200"></p>

## 3. Outputs

```
output, (h_n, c_n)
```

### 3.1 Shape

- output : $(N, L, D*H_{out})$ when batch_first=True
- $h_n$ : $(D*layers, N, H_{out})$
- $c_n$ : $(D*layers, N, H_{cell})$

## 4. Class

### 4.1 Componenets

- $i_t, f_t, o_t$ : input / forget/ output gate의 출력
- $c_t, g_t$ : cell state/ cell state를 구하기 위한 중간 연산(i_t와 element-wise 곱을 수행함)
- $W_i, W_h$ : input과 hidden의 선형결합시에 사용되는 가중치
- $b_i, h_i$ : bias

### 4.2 Calculate

📍 **예시**

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm_c/lstm_c_4.png?raw=true" width="900" height="500"></p>

> Hidden size: 2, Input size 3 일때 (첫번째 layer의) 각 cell 내부에서 연산되는 과정

### 4.3 Component Shape at Calculate

- $x_t$ : [batch_size, input_size]
- $h_t$ : [batch_size, hidden_size]
- $W_{i}$
  - at first layer : [hidden_size, input_size] ☞ transpose at calculate
  - otherwise : [hidden_size, num_directions * hidden_size] 
  - proj_size > 0 : [hidden_size, proj_size] not at first layer
- $W_{h}$
  - [hidden_size, hidden_size]
  - proj_size > 0 : [hidden_size, proj_size]
- $b_i$ : [hidden_size]
- $b_h$ : [hidden_size]

## 5. Variables

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm_c/lstm_c_8.png?raw=true" width="650" height="550"></p>

