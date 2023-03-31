---
layout: single
title:  'LM(5) Sequence to Sequence 구현 문자 단위'
toc: true
categories: [Language Model]
tags: [LM]

---

이번 포스팅에서는 Pytorch를 사용한 문자 단위의 seq2seq 번역기를 구현해본다.
{: .notice}

## 1. Dataset

### 1.1 데이터 불러오기

번역기 모델을 훈련시키기 위해서는 훈련 데이터로 병렬 코퍼스(parallel corpus)가 필요하다.

📍**병렬 코퍼스(parallel corpus)란?**

> 두 개 이상의 언어가 병렬적으로 구성된 코퍼스를 의미한다.<br>ex) 영어-한국어/ 프랑스어-영어 ..

이번 실습에서는 영어-한국어 병렬 코퍼스를 사용할 것이며, [여기](http://www.manythings.org/anki)에서 kor-eng.zip 파일을 다운로드 받을 수 있다. 다운로드 받은 파일을 구글 드라이브에 저장하고, 코랩을 통해 확인해본다.

````python
import pandas as pd

data_path = 'your_txt_file_path'
corpus = pd.read_csv(data_path, names=['eng', 'kor', 'etc'], sep='\t')
del corpus['etc']
print('전체 데이터 개수 :',len(corpus))
````

````
전체 데이터 개수 : 5749
````

전체 코퍼스를 구성하는 전체 병렬 데이터 쌍은 총 5749개이다. 구성을 확인하면 아래와 같다.

````
corpus.head()
````

🤪 [image1]

### 1.2 데이터 전처리

앞서 seq2seq에서 보았듯, 예측 시작시 들어가는 첫번째 input은 `<sos>`이며 예측 단어로 `<eos>`가 나올 경우 종료되도록 구성하여야 한다. 따라서 번역의 목표가 되는 kor의 문장 앞, 뒤에 `\t`와 `\n`을 붙여 문장의 시작과 끝을 알려준다. 이번 포스트에서 구성할 번역기는 문자 단위의 번역기이기 때문에 한 단어로 된 심볼을 사용하였다.

````python
corpus.kor = corpus.kor.apply(lambda x : '\t' +x + ' \n')
corpus.head()
````

🤪 [image2]

다음으로 각 문자를 기계가 이해할 수 있는 숫자로 할당하기 위한 문자 집합을 생성한다.

````python
# 문자 집합 구축
eng_vocab = set()
for line in corpus.eng:
    for char in line:
        eng_vocab.add(char)

kor_vocab = set()
for line in corpus.kor:
    for char in line:
        kor_vocab.add(char)
````

생성된 문자 집합을 확인해보니 특수 문자들이 들어가 있는 것을 확인하였다.

````python
print(corpus.eng.iloc[2959], corpus.kor.iloc[2959]) # eng에 ° 포함
print(corpus.eng.iloc[3119], corpus.kor.iloc[3119]) # eng에 ï 포함
print(corpus.eng.iloc[5717], corpus.kor.iloc[5717]) # eng에 " 포함
````

````
Actinium melts at 1,051°C.
악티늄은 1,050°C일 때 녹아. 

Tom is unbelievably naïve.
톰은 못 믿길 정도로 순진해. 

When the bus swerved to miss a cat, the driver said, "That was close." 	 
고양이를 비켜가기 위해 버스가 방향을 틀었을 때, 운전기사는 "큰일날 뻔했네"라고 말했다. 
````

별 다른 문제는 없을 듯 하여, ` ï`만을 i로 치환해 주고 문자열 집합에서 제거해 주었다.

````python
corpus.eng = corpus.eng.apply(lambda x: x.replace("ï","i"))
eng_vocab.discard("ï")
````

구성된 문자 단위의 집합을 배열로 변환한 뒤 정렬하여 크기 및 샘플을 보면 아래와 같다.

````python
eng_vocab = sorted(list(eng_vocab))
kor_vocab = sorted(list(kor_vocab))
print('Eng 문장의 char 집합 :',len(eng_vocab))
print(eng_vocab[45:75])
print('Kor 문장의 char 집합 :',len(kor_vocab))
print(kor_vocab[45:75])
````

````
Eng 문장의 char 집합 : 73
['Y', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
Kor 문장의 char 집합 : 1005
['~', '°', '가', '각', '간', '갇', '갈', '감', '갑', '값']
````

다음으로 영어, 한국어 문자 배열의 인덱스를 통해 각 문자(key)에 숫자(value)를 할당한 dictionary를 생성한다.

````python
eng_to_index = dict([(word, i+1) for i, word in enumerate(eng_vocab)])
kor_to_index = dict([(word, i+1) for i, word in enumerate(kor_vocab)])
print("Eng index:",eng_to_index)
print("Kor index:",kor_to_index)
````

````
Eng index: {' ': 1, '!': 2, '"': 3, '$': 4, ....}
Kor index: {'\t': 1, '\n': 2, ' ': 3, '!': 4, ... }
````

Copus를 구성하는 각 문자들이 숫자로 치환될 수 있기에, 먼저 인코더의 입력이 될 영어 문장에 대해 정수 인코딩을 수행한다.

````python
encoder_input = []

# 1개의 문장
for line in corpus.eng:
  encoded_line = []
  # 각 줄에서 1개의 char
  for char in line:
    # 각 char을 정수로 변환
    encoded_line.append(eng_to_index[char])
  encoder_input.append(encoded_line)
print('Eng 문장의 정수 인코딩 :',encoder_input[:5])
````

````
Eng 문장의 정수 인코딩 : [[29, 61, 9], [30, 55, 9], [40, 67, 60, 2], [40, 67, 60, 9], [45, 54, 61, 22]]
````

다음으로 디코더의 입력이 될 한국어 문장에 대해 정수 인코딩을 수행한다.

````python
decoder_input = []
for line in corpus.kor:
  encoded_line = []
  for char in line:
    encoded_line.append(kor_to_index[char])
  decoder_input.append(encoded_line)
print('Kor 문장의 정수 인코딩 :',decoder_input[:5])
````

````
Kor 문장의 정수 인코딩 : [[1, 3, 48, 11, 3, 2], [1, 3, 603, 214, 11, 3, 2], [1, 3, 317, 625, 4, 3, 2], [1, 3, 317, 625, 11, 3, 2], [1, 3, 225, 103, 24, 3, 2]]
````

정상적으로 정수 인코딩이 수행된 것을 볼 수 있으나 아직 인코딩 해야 할 것이 하나 더 남았다. Kor 문장의 인코딩된 정수들은 디코더의 입력으로 들어가게 될 것이다. 그런데 입력에 대한 예측은 그 다음 단어가 되어야 한다. 아래 그림을 통해 보면 이해가 쉬울 것이다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/nlp/seq2seq/seq3.png?raw=true" width="300"></p>

따라서 Kor 문장이 정수 인코딩된 배열에서 제일 앞 `<sos>`에 해당하는 `/t`를 제거한, 즉 입력에 대한 출력의 정답 비교를 위한 배열을 만들어야 한다.

````python
decoder_target = []
for line in corpus.kor:
  timestep = 0
  encoded_line = []
  for char in line:
    if timestep > 0:
      encoded_line.append(kor_to_index[char])
    timestep = timestep + 1
  decoder_target.append(encoded_line)
print('Kor 문장 입력에 대한 정답 정수 인코딩 :',decoder_target[:5])
````

````
Kor 문장 입력에 대한 정답 정수 인코딩  : [[3, 48, 11, 3, 2], [3, 603, 214, 11, 3, 2], [3, 317, 625, 4, 3, 2], [3, 317, 625, 11, 3, 2], [3, 225, 103, 24, 3, 2]]
````

### 1.3 Padding





## 참조

https://wikidocs.net/24996

https://wikidocs.net/86900

https://boysboy3.tistory.com/113

https://codlingual.tistory.com/91

pad seq - https://discuss.pytorch.org/t/how-to-do-padding-based-on-lengths/24442