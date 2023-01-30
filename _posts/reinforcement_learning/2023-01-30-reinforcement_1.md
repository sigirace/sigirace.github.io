---
layout: single
title:  'Introduction to Reinforcement Learning'
toc: true
categories: Reinforcement Learning
tags: [RL]

---

본 게시물은 David Silver의 [강의](https://www.youtube.com/watch?v=2pWv7GOvuf0&list=PLhhVkSH_JBI8ofvmbrG7m86wmVXq_7dit)와 팡요랩 Pang-Yo Lab의 유튜브 [강의](https://www.youtube.com/watch?v=wYgyiCEkwC8&list=PLpRS2w0xWHTcTZyyX8LMmtbcMXpd3s4TU) 를 보고 정리하는 글이다.<br>강의노트는 [이곳](https://www.davidsilver.uk/wp-content/uploads/2020/03/intro_RL.pdf)에서 참고하였다.
{: .notice}

<div class="notice">
<li><a href="https://sigirace.github.io/autoencoder/autoencoder_2/">강의 목록 추후 업로드</a></li>
</div>

## 1. About Reinforcement Learning

### 1.1 Branches of Machine Learning

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/reinforcement/lec1/intro_RL-07.png?raw=true" width="650" height="400"></p>

### 1.2 Charateristics of Reinforcement Learning

☀️ **강화학습과 다른 머신러닝의 차이점**

- supervisor가 없고 reward signal 만이 있다.<br>☞ 정답을 알려주는 supervisor가 없이 reward 신호만을 통해 정답을 찾아 나간다.
- 피드백(reward)이 즉각적이지 않을 수 있다.
- 시간(=순서)이 중요하다.<br>☞ 지도학습에서는 i.i.d(independent and identical distribution) data를 가정한다.<br>    즉, 각 샘플이 독립적으로 뽑혀 서로간의 영향이 없고 동일한 확률분포에서 나온 것<br>☞ 강화학습은 iid를 가정하지 않고, 순서가 있는(=독립적이지 않은) 데이터를 사용한다.
- Agent의 action이 이후에 받게되는 데이터에 영향을 준다<br>☞ 지도학습과 비지도학습은 정해진 데이터 셋 안에서 이루어진다면 강화학습은 매번 데이터가 달라진다.

## 2. The RL Problem

해당 chapter에서는 강화학습(RL)의 용어를 정리한다.

### 2.1 Rewards

- Reward $R_t$는 scalar feedback signal이다.



























