---
layout: single
title:  'Probability Theory (2) Measure Theory'
toc: true
categories: [Statistics]
tags: [Measure, Bayesian]

---

본 게시물은 최성준 교수님의 확률론 강의를 정리하는 글이다.
{: .notice}

## 1. Sigma Field

📍**Set Function**

> 함수는 set에 수를 할당함 (example:cardinality, length,area)

👀 **Axioms**

1. 공집합 포함
2. 하나의 집합이 포함되면 그 여집합 또한 포함
3. closed under countable union: 모든 부분 집합들의 '가산 합집합'이 또한 포함

☀️ **Properties**

1. 전체 집합 또한 sigma field
2. closed under countable intersection: 모든 부분 집합 '가산 교집합' 또한 포함
3. Power set 또한 sigma filed
4. finite하거나 uncountable하나 denumerable(=countable infinite ) 할 수 없음
5. a와 b 모두 sigma field라면 두 집합의 교집합은 sigma field이나 합집합은 sigma field가 아님

📍**uncountable & denumerable**

> 정수들의 집합은 0, 1, -1, 2, -2, 3, -3, ...과 같이 무한히 많은 원소를 포함하기에 정수의 개수는 가산 무한(infinite)하다. 이렇게 가산 무한한 원소를 가지는 집합의 개수를 세는 것은 현실적으로 불가능하다. 정수 집합의 power set은 2^(정수들의 개수)으로 원소의 개수가 정수들의 개수와 같기 때문에 가산 무한한 크기를 가지게 된다. 가산 무한한 크기를 가진 집합은 원소의 개수를 세는 것이 불가능하므로, 2^(정수들의 개수)는 가산 불가능한 크기를 가진다.
>
> 따라서, 2^(정수들의 개수)는 countable이 아니며, 가산 불가능한 크기를 가진 집합이다.

## 2. Measure Theory 

집합 U에 존재하는 부분집합에 양수인 실수를 매핑하는 것

👀 **Definition**

- set과 subset들로 이루어진 sigma field에 measure를 씌울 수 있으면 이를 measurable space라고 함
- measurable space에 있는 measure는 set function
  - 공집합에 대한 measure는 0
  - disjoint(=겹치는 부분이 없는, 서로소)한 sigma field에 대한 measure는 countable additivity
- 확률의 경우 전체 집합에 대한 measure는 1
- 비공식적으로, A가 B의 부분집합이면 measure 또한 A가 B보다 작음 (=단조성)



