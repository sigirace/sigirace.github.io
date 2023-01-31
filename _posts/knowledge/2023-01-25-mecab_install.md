---
layout: single
title:  'Mac(M1)에 mecab 모듈 설치하기'
toc: true
categories: [install]
tags: [mecab, konlpy]

---

## 1. KoNLPy 설치

### 1.1 KoNLPy 란

KoNLPy(코엔엘파이)는 한국어 정보처리를 위한 파이썬 패키지이다. KoNLPy 패키지 안에는 Mecab, Komoran 등 다양한 클래스가 포함되어 있으며 추가적인 설치를 통해 발전된 형태소 분석 및 품사 태깅의 task를 수행할 수 있다.

### 1.2 설치 방법

**[Environments]**

- python 3.8.x

**Step1. [이 사이트](https://www.azul.com/downloads/?version=java-15-mts&os=macos&architecture=arm-64-bit&package=jdk)에 들어가 위와 같이 검색 조건을 설정해준다.**

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/mecab_install/mecab1_1.png?raw=true" width="700" height="300"></p>

**Step2. 해당 jdk 설치 후 터미널에서 경로를 확인한다.**

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/mecab_install/mecab1_2.png?raw=true" width="550" height="100"></p>

```
>> cd /Library/Java/JavaVirtualMachines
>> ls
```

**Step3. zshrc에 JAVA PATH를 등록한다.**

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/mecab_install/mecab1_3.png?raw=true" width="600" height="300"></p> 

- 터미널에서 open ./.zshrc 입력

```
# JAVA PATH
export JAVA_HOME=/Library/Java/JavaVirtualMachines/zulu-15.jdk/Contents/Home
export PATH=${PATH}:$JAVA_HOME/bin:
```

- 터미널에서 source ./.zshrc 입력

**Step4. konlpy 설치**

- conda install -c conda-forge jpype1
- pip install konlpy

**Step5. 설치 확인**

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/mecab_install/mecab1_4.png?raw=true" width="600" height="100"></p> 

- 터미널에서 python 실행 후 import

## 2. MeCab 설치

**[Environments]**

- python 3.8.x
- konlpy

**Step1. mecab-ko 설치**

- [이 사이트](https://bitbucket.org/eunjeon/mecab-ko/downloads/)에서 최신 버전 다운로드
- mecab-0.996-ko-0.9.2.tar.gz를 사용자 하위 본인 이름 폴더(/Users/[본인이름])에 저장
- 터미널에서 아래 커맨드 입력

```
>> cd ~
>> tar xvfz mecab-0.996-ko-0.9.2.tar.gz
>> cd mecab-0.996-ko-0.9.2
>> ./configure
>> make
>> sudo make install
```

- 아래 메세지가 나온다면 성공

```
/usr/bin/install -c -m 644 mecabrc (어쩌구 저쩌구)
```

**Step2. mecab-ko-dic 설치**

- [이 사이트](https://bitbucket.org/eunjeon/mecab-ko-dic/downloads/)에서 최신 버전 다운로드
- mecab-ko-dic-2.1.1-20180720.tar.gz을 사용자 하위 본인 이름 폴더(/Users/[본인이름])에 저장
- 터미널에서 아래 커맨드 입력

```
>> cd ~
>> tar xvfz mecab-ko-dic-2.1.1-20180720.tar.gz
>> cd mecab-ko-dic-2.1.1-20180720
>> ./autogen.sh 
>> ./configure
>> make
>> sudo make install
```

- 아래 메세지가 나온다면 성공

```
/usr/bin/install -c -m 644 model.bin (어쩌구 저쩌구)
```

* 터미널에 아래 커맨드 입력 후 텍스트 입력하여 실행 확인

```
mecab -d /usr/local/lib/mecab/dic/mecab-ko-dic
```

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/mecab_install/mecab1_6.png?raw=true" width="600" height="150"></p> 

**Step3. mecab python 설치**

- Mojave 이상일 경우

```
>> export CC=/usr/local/Cellar/gcc/8.2.0/bin/gcc
>> pip install mecab-python3
```

- 실행 확인

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/mecab_install/mecab1_5.png?raw=true" width="600" height="100"></p> 
