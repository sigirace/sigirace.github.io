---
layout: single
title:  'Planning by Dynamic Programming'
toc: true
categories: [Reinforcement Learning]
tags: [Dynamic Programming, Policy Evaluation]
---

본 게시물은 David Silver의 [강의](https://www.youtube.com/watch?v=lfHX2hHRMVQ&list=PLhhVkSH_JBI8ofvmbrG7m86wmVXq_7dit&index=2)와 팡요랩 Pang-Yo Lab의 [유튜브 강의 3강](https://www.youtube.com/watch?v=rrTxOkbHj-M&list=PLpRS2w0xWHTcTZyyX8LMmtbcMXpd3s4TU&index=3) 을 보고 정리하는 글이다.<br>강의노트는 [이곳](https://www.davidsilver.uk/teaching/)에서 참고하였다. 😗
{: .notice}

## 1. Introduction

### 1.1 What is Dynamic Programming

👀 **Definition**

````
Dynamic Programming은 큰 문제를 작은 문제로 나누어 푸는 방법론이다.
````

- 복잡한 문제를 푸는 방식
- 작은 문제로 분할하는 방식

### 1.2 Requirements for Dynamic Programming

Dynamic Programming(=DP)은 일반적으로 두가지 조건을 만족하는 문제에 적용될 수 있다.

1. Optimal substructure: optimal solution이 작은 문제들로 나뉠 수 있어야 한다.
2. Overlapping subproblems: subproblem에 대한 solution을 저장해 놓았다가 다시 사용할 수 있다.

☞ MDP가 위 조건 두개를 포함하기에 DP로 접근하기 적합하다.

### 1.3 Planning by Dynamic Programming

DP는 MDP에 대한 모든 구성요소를 알고 있다고 가정한다. <br>☞ state, action, transition probability, reward, discount factor

📍**Step of Dynamic Programming**

DP는 prediction과 control 두가지 step으로 나뉘는데, 현재 진행하는 policy에 따라 value를 구하고(=prediction) 이를 토대로 policy를 optimal하게 발전(=control)시키는 흐름으로 진행된다.

1. Predcition<br>- input: MDP and policy/ MRP<br>- solution: Bellman expectaion Eqn<br>- output: value function<br>- policy evaluation

2. Control<br>- input: MDP<br>- solution: Bellman optimality Eqn<br>- output: optimal value function, optimal policy<br>- policy improvement

## 2. Policy Evaluation

### 2.1 Iterative Policy Evaluation

- Problem: policy를 평가하는 것<br> = policy를 따랐을 때 return을 구함<br>= value function
- Solution: 반복적인 Bellman expectation Eqn











