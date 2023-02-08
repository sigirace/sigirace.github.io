---
layout: single
title:  'LSTM의 모든것 (1) 이론'
toc: true
categories: [Deep Learning]
tags: [timeseries, lstm, gru]

---

본 게시물은 LSTM의 이론에 대해 [해당 포스트](https://medium.com/towards-data-science/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21)를 정리하는 글이다.
{: .notice}

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm/lstm_m_1.gif?raw=true" width="600"></p>

## 1. Introduction

### 1. The Problem, Short-term Memory

순환 신경망(RNN)은 short-term memory 문제가 있다. 이는 sequence(문장의 길이, 시계열 등)가 충분히 길 때, 앞선 time step의 정보를 뒤의 step으로 전달할때 손실이 발생한다는 것이다. 



만약 예측하기 위해  sequence를 처리하는 경우, RNN은 앞선 time step의 중요한 정보를 잃어버릴 수 있다.

Back propagation 중, RNN은 vanishing  

후방 전파 중에 반복 신경망은 소멸 그레이디언트 문제로 어려움을 겪는다. 그레이디언트는 신경망 가중치를 업데이트하는 데 사용되는 값이다. 사라지는 기울기 문제는 기울기가 시간을 통해 역전파됨에 따라 감소하는 것이다. 기울기 값이 극단적으로 작아지면 학습에 크게 기여하지 않습니다.



