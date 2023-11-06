---
layout: single
title:  '[MAC ERROR] Your shell has not been properly configured to use conda activate'
toc: true
categories: [troubleshooting]
tags: [Conda, Linux]

---

### 1. 원인

해당 에러는 mac에서 conda에 대한 환경변수 설정이 틀어져서 발생한 것이다.

### 2. 해결방법

Step1. 쉘에서 miniconda 위치 확인

```
cd ~
vim .zshrc
```

Step2. 환경변수 등록

```
export PATH="위치정보"
```

### 3. 추가 정보

- [shell이란?](https://rrecoder.tistory.com/62)

- [vim이란?](https://d-dual.tistory.com/8)