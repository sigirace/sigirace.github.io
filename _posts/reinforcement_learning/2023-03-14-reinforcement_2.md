---
layout: single
title:  'Markov Decision Process(MDP)'
toc: true
categories: [Reinforcement Learning]
tags: [Markov Process, Markov Reward Process]
---

본 게시물은 David Silver의 [강의](https://www.youtube.com/watch?v=lfHX2hHRMVQ&list=PLhhVkSH_JBI8ofvmbrG7m86wmVXq_7dit&index=2)와 팡요랩 Pang-Yo Lab의 [유튜브 강의 2강](https://www.youtube.com/watch?v=wYgyiCEkwC8&list=PLpRS2w0xWHTcTZyyX8LMmtbcMXpd3s4TU) 을 보고 정리하는 글이다.<br>강의노트는 [이곳](https://www.davidsilver.uk/teaching/)에서 참고하였다. 😗
{: .notice}

## 1. Markov Proceses

### 1.1 Introduction to MDPs

- Markov decision process(markov process가 아님!)는 reinforcement learning(=RL)에서의 환경을 설명하는 것이다.
- MDP는 environment가 모두 다 관측 가능한 상황이다.<br>ex) 현재 state가 process를 완전히 표현하는 것 = markov property
- 거의 모든 강화학습 MDP 형태로 만들 수 있다.

### 1.2 Markov Property

👀 **Definition**

```
미래는 현재가 주어졌을 때, 과거에 독립적이다.
```

$$
P[S_{t+1}|S_{t}] = P[S_{t+1}|S_1, ..., S_{t}]
$$

- State(=현재)가 hitory(=과거)에 있는 관련된 모든 정보를 갖고 있기 때문에, 현재를 알면 과거는 모두 버려도 무방하다.

### 1.3 State Transition Matrix

- Markov state s에서 다음 state s`로 전이될 확률은 다음과 같이 정의된다.

$$
P_{ss^{`}} = [S_{t+1} = s^{`}|S_{t} = s]
$$

- 어떠한 state s에서 다음 state s`로 전이될 확률을 모아 matrix로 표현한 것이 state transition matrix 이다.
- 이때 matrix의 모든 합은 1이다.

### 1.4 Markov Process

- Markov process는 memoryless random process이다.
- memoryless는 내가 어떤 경로를 통해서 왔던, 현재 state에 온 순간 다음 경로는 matrix의 확률을 따른다는 것이다. 
- random process는 샘플링을 할 수 있다는 의미로, 하나의 state로 이동하고 끝이 아니라 sequence를 샘플링 한다는 것이다.<br>(random process에 대한 자세한 내용은 추후 업데이트...)

👀 **Definition**

````
Markov Process (or Markov Chain)은 <S, P>로 이루어진 튜플이다.
- S: 유한 state 집합
- P: state transition probability matrix
````

📍 **Example**

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/reinforcement/lec2/RL-2-2.png?raw=true" width="600" height="350"></p>

> S1 = C1에서 시작하는 Student Markov Chain을 샘플링 한것이고, Transition Matrix는 아래와 같다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/reinforcement/lec2/RL-2-3.png?raw=true" width="400" height="250"></p>

<br><br>

## 2. Markov Reward Process

### 2.1 Markov Reward Process

👀 **Definition**

````
Markov Reward Process는 <S, P, R, r>로 이루어진 튜플이다.
- S: 유한 state 집합
- P: state transition probability matrix
- R: reward function
- r: discount factor
````

$$
R_{s} = E[R_{t+1} |R_{t} ]
$$

$$
r \in [0, 1]
$$

📍 **Example**

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/reinforcement/lec2/RL-2-4.png?raw=true" width="600" height="500"></p>

### 2.2 Retrun

👀 **Definition**

````
Return Gt는 각 time-step t에서 얻은 discounted reward의 합이다.
````

$$
G_t = R_{t+1} + rR_{t+2} + ... = \sum\limits_{k=0}^{\infty} r^{k}R_{t+k+1}
$$

