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

### 1.2 Charateristics of Reinforcement Learning<br>

☀️ **강화학습과 다른 머신러닝의 차이점**

- supervisor가 없고 reward signal 만이 있다.<br>☞ 정답을 알려주는 supervisor가 없이 reward 신호만을 통해 정답을 찾아 나간다.
- 피드백(reward)이 즉각적이지 않을 수 있다.
- 시간(=순서)이 중요하다.<br>☞ 지도학습에서는 i.i.d(independent and identical distribution) data를 가정한다.<br>☞ 즉, 각 샘플이 독립적으로 뽑혀 서로간의 영향이 없고 동일한 확률분포에서 나온 것<br>☞ 강화학습은 iid를 가정하지 않고, 순서가 있는(=독립적이지 않은) 데이터를 사용한다.
- Agent의 action이 이후에 받게되는 데이터에 영향을 준다<br>☞ 지도학습과 비지도학습은 정해진 데이터 셋 안에서 이루어진다면 강화학습은 매번 데이터가 달라진다.

## 2. The RL Problem

해당 chapter에서는 강화학습(RL)의 용어를 정리한다.

### 2.1 Rewards

- Reward $R_t$는 scalar feedback signal이다.<br>☞ t번째 time(=step)에 scalar로 주어지는 것으로 해당 step에서 agent의 평가 척도가 된다.
- Agent의 목적은 cumulative reward를 maximise하는 것이다.<br>☞ 강화학습은 <mark style='background-color: #f6f8fa'>reward hypothesis</mark>를 근거로 한다.

👀 **Definition of Reward Hypothesis**

```
모든 목적은 reward의 총 합을 극대화 하는 것으로 설명 될 수 있다.
```

### 2.2 Sequential Decision Making

한번의 reward를 잘 받는것이 아닌 순차적인 의사결정을 통해 reward의 총 합이 극대화 되는 것을 목표로 한다.

- Goal: 미래에 받을 reward의 총 합을 극대화하는 action을 선택하는 것
- Action의 결과(reward)가 나중에 확인될 수 있다.
- 당장은 손해를 보더라도 추후에 더 나은 결과를 얻을 수 있다.

📍 **예시**

> 체스의 경우 당장 폰을 하나 먹히는 action을 하더라도 후에 퀸을 먹을 수 있다면 좋은 선택으로 결정하여야 한다.

### 2.3 Agent and Environment

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/reinforcement/lec1/intro_RL-17.png?raw=true" width="400" height="400"></p>

- **Agent** : 주인공, 학습하는 대상으로, 환경속에서 행동하는 개체를 말한다. (ex. 강아지, 로봇, 플레이어)
- **Environment** : Agent와 상호작용하는 환경. 강화학습은 Agent와 Environment간의 상호작용간에 일어나는 과정이다.
- **State** : Agent(또는 Environment)가 필요한 구체적 정보(ex. 위치, 속도)를 말한다. (뒤에서 설명)
- **Observation** : Agent가 state중 일부를 받는데 이 정보를 Observation이라 한다.<br>☞ 대개의 경우 Agent가 state 전부를 아는 것은 불가능하다. 가능한 경우를 fully observable이라고 한다. 

<center>출처: https://namu.wiki/w/강화학습/용어</center><br>

☀️ **Agent와 Environment의 상호작용**

- Agent가 어떠한 action을 수행한다. ☞ $A_t$
- Environment가 두가지 신호를 준다.
  - Action에 대한 reward ☞ $R_{t+1}$
  - Action으로 인해 변경된 상황(=observation) ☞ $O_{t+1}$

### 2.4 History and State

- History는 observations, actions, rewards의 순차적인 기록이다.

$$
H_t = O_1, R_1, A_1, ... , A_{t-1}, O_t, R_t
$$

- **State**는 Agent(또는 Environment)가 다음에 어떤 결정을 할 지 결정하기 위한 정보들이다.<br>☞ State는 history의 정보를 가공하여 만드는 것, 즉 history 함수이다.

### 2.5 Environment State

- Environment의 state $S^{e}_{t}$는 envirionment의 private한 표현이다.<br>☞ 보통 agent에게 보이지 않으며, 보이더라도 관계없는 정보들이다.
- environment가 다음 observation/ reward를 주기 위해 사용한 data이다.

📍 **예시**

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/reinforcement/lec1/intro_RL-38.png?raw=true" width="400" height="400"></p>

> 예시 environment는 게임기이고, 그 안에는 다음 화면(=observation)과 점수(=reward)를 계산하기 위한 현재 state, 들어온 agent의 action 등등이 있을 것이다. 이는 environment가 다음 obserbation과 reward를 계산하기 위해 필요한 정보(=environment state)이지만 사용자에게는 쓸모가 없는 데이터이다.

### 2.6 Agent State

- Agent state $S^{a}_{t}$는 agent의 내부적인 표현이다.
- Agent가 다음 action을 하기 위해 쓰이는 data이다.
- 이러한 정보는 강화학습 알고리즘에 사용된다.

### 2.7 Markov State

Markov state는 history에서 부터 온 모든 유용한 정보를 포함하고 있다.

👀 **Definition of Reward Markov**

```
만약 미래의 State가 현재에만 영향을 받으면, 현재의 State St는 Markov이다. (☞ 필요충분 조건)
```

$$
P[S_{t+1}|S_{t}] = P[S_{t+1}|S_1, ..., S_{t}]
$$

- 미래는 현재가 주어졌을 때 과거에 독립적이다.
- Environment state는 Markov이다.

### 2.8 Fully Observable Environments

- Full observability: agent가 environment state를 확인할 수 있을 때, Environment와 Agent의 state가 같다.<br>
- Markov Decision Process (MDP)라고 함

$$
O_t = S^a_t = S^e_t
$$

### 2.9 Partially Observable Environments

- Partial observility: environment와 agent의 state가 같지 않은 경우
- Agent는 자신의 state를 표현해야한다.
  - History 자체를 쓰거나
  - RNN같은 순차적인 정보를 쓰거나

## 3. Inside An RL Agent

해당 chapter에서는 agent의 구성요소를 살펴본다.

### 3.1 Policy

- Policy는 agent의 행동을 규정하는 것
- state가 주어졌을 때 행동을 규정함
- Deterministic policy: 하나의 action을 매핑함

$$
a = \pi(s)
$$

- Stochastic policy: 여러 action의 확률을 매핑함

$$
\pi(a|s) = P[A_t = a| S_t = s]
$$

### 3.2 Value Function

- Value Function은 미래의 reward를 예측하여 상황(=현재 state)이 얼마나 좋은지/나쁜지를 나타냄<br>☞ 이를 통해 action을 선택함
- 현재 state에서 policy를 따라 진행하였을 때 받게되는 총 reward의 기대값<br>☞ Stochastic일 경우 확률에 따라 policy가 달라져 reward가 달라지니 기대값을 취함<br>☞ Detrministic일 경우에도 environment로 부터 오는 확률이 존재하기 때문에 기대값을 취함
- Discount factor를 사용하여 미래의 reward에 불확실성을 포함시킴

$$
v_{\pi}(s)= E_{\pi}[R_{t+1}+\gamma R_{t+2}+ \gamma^2R_{t+3}+...|S_t=s]
$$

### 3.3 Model

- Model은 environment의 다음 행동을 예측하는 것
-  state s에서 action a를 했을때, reward 예측

$$
R^{a}_{s} = E[R_{t+1}|S_t=s, A_t=a]
$$

- state s에서 action a를 했을때, 다음 state s`가 나올 확률 (= probability of state transition)

$$
P^{a}_{ss^\prime} = P[S_{t+1}=s^\prime | S_t = s, A_t = a]
$$

### 3.4 Maze Example

☀️ **Definition**

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/reinforcement/lec1/intro_RL-30.png?raw=true" width="650" height="400"></p>

- Cumulative reward가 최대가 되기 위해 각 time-step의 action에 대한 reward를 1로 설정함

☀️ **Policy**

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/reinforcement/lec1/intro_RL-31.png?raw=true" width="650" height="400"></p>

- 여러 policy가 있겠지만, 예시는 각 state에서의 optimal policy를 나타냄

☀️ **Value Function**

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/reinforcement/lec1/intro_RL-32.png?raw=true" width="650" height="400"></p>

- Policy를 따랐을 때, 각 state에서의 value function

☀️ **Model**

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/reinforcement/lec1/intro_RL-33.png?raw=true" width="650" height="400"></p>

- Model은 1. next reward와 2. next state를 정해야함
- Next reward는 모두 -1
- Next state는

1:02:10
