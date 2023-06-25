---
layout: single
title:  'Git Tutorial Merging vs Rebasing'
toc: true
categories: [Git]
tags: [merge, rebase]


---

본 게시물은 git rebase를 git merge 명령과 비교하는 [Git Tutorial](https://www.atlassian.com/git/tutorials/merging-vs-rebasing)을 글을 정리한 것이다.
{: .notice}

## 1. Conceptual Overview

가장 먼저 이해해야 할 것은 `git rebase`는 `git merge`와 동일한 문제를 해결한다는 것이다. 이 두 명령은 모두 한 `branch`에서 다른 `branch`로 변경사항을 통합하도록 설계되었기 때문이다. 하지만 이들은 서로 다른 방식으로 수행된다. 

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/git_tutorial/git1.png?raw=true" width="650" height="400"></p>

예를들어 새로운 기능을 위한 작업을 수행할 때, 다른 팀 멤버가 `main branch`에 `commit`을 `update`하는 것을 생각해보자. 또한 새로운 `commit`이 현재 작업중인 기능과 관련이 있다고 가정해본다. 이때 새로운 `commit`을 현재 작업중인 `feature branch`에 통합하기 위해서는 `rebase`와 `merge` 작업이 필요하다.

## 2. The Merge Option

가장 쉬운 방법은 아래와 같이 `main branch`를 현재 작업중인 'branch'로 병합하는 것이다.

````bash
git checkout feature
git merge main

# 한줄로 표현
git merge feature main
````

이러한 방식은 현재 작업중인 `feature branch`에 새로운 `merge commit`을 생성하며 아래와 같은 구조를 얻을 수 있다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/git_tutorial/git2.png?raw=true" width="650" height="400"></p>

`merge`는 `feature branch`가 변경되지 않는 비파괴적인 작업이기 때문에 권장된다. 이는 아래 설명하는 `rebase`의 모든 잠재적 위험을 방지할 수 있다. 하지만, 이는 `upstream`변경 사항을 통합해야 할 때마다 `feature branch`에 외부 `merge commit`이 있음을 의미한다. 즉, `main branch`의 변경이 잦다면 `feature branch`의 기록이 지저분해지고 다른 개발자가 프로젝트의 기록을 이해하는 것이 어려워 질 수 있다.

## 3. The Rebase Option

`merge`대신 `rebase`를 사용하여 `feature branch`를 `main branch`로 재배치 할 수 있다.

````bash
git checkout feature
git rebase main
````

이는 `feature branch` 전체를 `main branch`의 끝으로 옮겨 새로운 `commit`이 효과적으로 통합되게 한다. 그러나 원래 `branch`의 각 `commit`에 대해 완전히 새로운 `commit`을 만들어 프로젝트를 다시 작성한다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/git_tutorial/git3.png?raw=true" width="650" height="400"></p>

`rebase`의 주요 장점은 불필요한 `merge commit`을 제거하고, 프로젝트의 기록을 선형화하여 알기 쉽게 한다는 것이다. 하지만, 변경 추적과 안전성이라는 두가지 trade-off가 있다. Golden Rule of Rebasing을 따르지 않을 경우 프로젝트 기록을 다시 작성하면 공동 작업 워크플로우에 치명적일 수 있다.

## 4. Golden Rule of Rebasing

`rebase`에 대해 알게 된 후 가장 중요한 것은 `rebase`를 언제 하면 안되는지 배우는 것이다. `rebase`의 golden rule은 `public branch`에서 사용하지 않는 것이다. 예를들어 `feature branch`의 작업 후 `main branch`로 다시 사용할 경우를 생각해보자.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/git_tutorial/git4.png?raw=true" width="650" height="400"></p>

`rebase`는 `main`의 모든 `commit`을 `feature branch`의 뒤로 옮긴다. 이때 문제는 이것이 local repository에서 발생했다는 것이다. 다른 개발잗글은 여전히 원래의 `main`에서 작업을 하고 있다. `rebase`는 새로운 `commit`으로 이어지기 때문에 git은 `main`이 다른 사람들과 다르다고 파악할 것이다. local과 global 두 `main branch`를 통합하는 유일한 방법은, 두 `branch`를 다시 `merge`하여 추가적인 `commit`과 동일한 변경 사항이 포함된 `commit` 집합을 생성하는 것이다. 무슨말 하는지 모를 정도로 혼란스러운 상황이다. 따라서 `rebase`를 실행하기 전에 항상 해당 `branch`를 보고 있는 다른 사람이 있는지 확인하고, 그렇다면 비파괴적인 방법에 대해 생각해야 한다.  