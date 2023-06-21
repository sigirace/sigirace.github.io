---
layout: single
title:  'Probability Theory (1) Set Theory'
toc: true
categories: [Statistics]
tags: [Statistics, PDF, PMF, 확률질량함수, 확률밀도함수]

---

본 게시물은 최성준 교수님의 확률론 강의를 정리하는 글이다.
{: .notice}

<div class="notice">
<li><a href="https://sigirace.github.io/autoencoder/autoencoder_2/">강의 목록 추후 업로드</a></li>
</div>


## 1. Intorduction

👀 **Definition**

```
Set theory is the branch of mathematical logic that studies sets, which can be informally described as collections of objects. Although objects of any kind can be collected into a set, set theory, as a branch of mathematics, is mostly concerned with those that are relevant to mathematics as a whole.
```

<center>출처: https://en.wikipedia.org/wiki/Set_theory</center><br>

집합론은 집합을 연구하는 수학 논리학의 한 분야로 collections of objects로 기술될 수 있다. objects는 어떤 것이든 될 수 있지만, 집합론은 수학의 한분야로 수학 전체와 관련된 것들과 대부분 관계가 있다.

## 2. Terms

☀️ **set**

- collections of objects<br>☞ {1, 2, 3, 4, 5}

☀️ **element**

- member of a set<br>☞ 1 $\in$ {1, 2, 3}

☀️ **subset**

- 부분집합

  ☞ {a, b} is a subset of $ \lbrace a, b, c \rbrace$

☀️ **universal set**

- subset들의 전체 집합<br>☞ $ \lbrace x, y, z \rbrace$ is a universal set of {x, y} and {y, z}<br>

☀️ **disjoint sets**

- 서로 공통 원소가 없는 집합들<br>☞ $ A \cap B = \varnothing $

☀️ **partition**

- 공집합이 아닌 부분집합들로 이루어진 집합<br>☞ if $A = \lbrace 1, 2, 3, 4 \rbrace$, then partition of $A: \lbrace \lbrace 1, 2 \rbrace , \lbrace 3 \rbrace , \lbrace 4 \rbrace \rbrace$

☀️ **cartesian product**

- 각 집합의 원소를 성분으로하는 튜플들의 집합이며 원소들의 순서는 곱의 순서와 같음<br>☞ $A_1 \times A_2 \times ... A_n = \lbrace (x_1, x_2, ... x_m) | x_1 \in A_1, x_2 \in A_2, ... , x_n \in A_n \rbrace$

☀️ **power set**

- 집합의 모든 부분집합 (공집합도 포함)<br>☞ $2^A$ the set of all subsets of A

☀️ **cardinality**

- 집합의 원소 개수

☀️ **denumerable**

- countably infinite, all denumerable sets are of the same cardinality<br>📍짝수의 집합은 denumerable

## 3. Function or Mapping

$$
f\, : \, U \rightarrow V
$$

- domain: $U$
- codomain: $V$
- image: 정의역의 원소에 대응하는 공역의 원소들<br>☞ $f(A) = \lbrace f(x) \in V : x \in A \rbrace$ where $A \subseteq U$
- range: $f(U)$ (image of domain)





