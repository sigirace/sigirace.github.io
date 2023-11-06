---
layout: single
title:  'Colab에서 Mecab 실행하기'
toc: true
categories: [Knowledge]
tags: [Mecab, Colab]

---

본 게시물에서는 colab 환경에서 mecab을 실행하는 코드를 공유한다.
{: .notice}

## Old code

최종 확인일 2023년 4월 -> 오류 발생 아래 최신버전 업데이트

````python
import os
# install konlpy, jdk, JPype
!pip install konlpy
!apt-get install openjdk-8-jdk-headless -qq > /dev/null
!pip3 install JPype1-py3

# install mecab-ko
os.chdir('/tmp/')
!curl -LO https://bitbucket.org/eunjeon/mecab-ko/downloads/mecab-0.996-ko-0.9.2.tar.gz
!tar zxfv mecab-0.996-ko-0.9.2.tar.gz
os.chdir('/tmp/mecab-0.996-ko-0.9.2')
!./configure
!make
!make check
!make install

# install mecab-ko-dic
!apt-get install automake
os.chdir('/tmp')
!curl -LO https://bitbucket.org/eunjeon/mecab-ko-dic/downloads/mecab-ko-dic-2.1.1-20180720.tar.gz
!tar -zxvf mecab-ko-dic-2.1.1-20180720.tar.gz
os.chdir('/tmp/mecab-ko-dic-2.1.1-20180720')
!./autogen.sh
!./configure
!make
!make install

# install mecab-python
os.chdir('/content')
!git clone https://bitbucket.org/eunjeon/mecab-python-0.996.git
os.chdir('/content/mecab-python-0.996')
!python3 setup.py build
!python3 setup.py install
````

위 코드 실행 후 런타임 재시작

````python
!apt-get update
!apt-get install g++ openjdk-8-jdk 
!pip3 install konlpy JPype1-py3
!bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)
````

## New code

최종 확인일 2023년 6월

````python
!pip install Korpora
````

위 코드 실행 후 런타임 재시작

````python
!git clone https://github.com/SOMJANG/Mecab-ko-for-Google-Colab.git
ls
cd Mecab-ko-for-Google-Colab/
!bash install_mecab-ko_on_colab_light_220429.sh

from konlpy.tag import Mecab
mecab = Mecab()
print(mecab.pos("솜씨좋은장씨의 개발블로그"))
````

````
(['안녕', '하', '세요'], [['안녕', '하', '세요'], ['안녕', '?']])
````

