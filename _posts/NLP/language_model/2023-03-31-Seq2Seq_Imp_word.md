---
layout: single
title:  'LM(5) Sequence to Sequence 구현'
toc: true
categories: [Language Model]
tags: [LM]

---

이번 포스팅에서는 Pytorch로 seq2seq 영한 번역기를 구현해본다.
{: .notice}

## 1. Prepare

### 1.1 Mecab 설치

이번 실습은 colab 환경에서 수행하며, 한국어 tokenizing을 위한 mecab 설치 코드는 [여기]()에서 복붙해온다.

### 1.2 Import module

설치가 끝났다면 아래 모듈들을 import 시킨다. 만약 wandb를 사용하지 않는다면 wandb 관련 코드를 모두 삭제해도 무방하다.

````python
import os

import wandb
import torch
import torch.nn as nn
import torch.optim as optim
from torch.nn.utils.rnn import pad_sequence
from torchtext.data.metrics import bleu_score
from sklearn.model_selection import train_test_split

from collections import Counter
import random
import pandas as pd

import re
import nltk
from konlpy.tag import Mecab
nltk.download('punkt')

os.environ["WANDB_API_KEY"] = 'your api key'
os.environ['WANDB_SILENT']="true"
````



## 2. Dataset

### 2.1 데이터 불러오기

번역기 모델을 훈련시키기 위해서는 훈련 데이터로 병렬 코퍼스(parallel corpus)가 필요하다.

📍**병렬 코퍼스(parallel corpus)란?**

> 두 개 이상의 언어가 병렬적으로 구성된 코퍼스를 의미한다.<br>ex) 영어-한국어/ 프랑스어-영어 ..

이번 실습에서는 영어-한국어 병렬 코퍼스를 사용할 것이며, [여기](http://www.manythings.org/anki)에서 kor-eng.zip 파일을 다운로드 받을 수 있다. 다운로드 받은 파일을 구글 드라이브에 저장하고, 코랩을 통해 확인해본다.

````python
data_path = 'your data path'

# data load
df = pd.read_csv(data_path, delimiter='\t', names=['src', 'trg', 'etc'])[['src', 'trg']]
print('전체 데이터 개수 :',len(df))
````

````
전체 데이터 개수 : 5749
````

전체 코퍼스를 구성하는 전체 병렬 데이터 쌍은 총 5749개이다. 구성을 확인하면 아래와 같다.

````
df.head()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/nlp/seq2seq/seq_imp1.png?raw=true" width="150"></p>

### 2.2 데이터 전처리

데이터 전처리를 위한 함수를 작성 및 수행한다. 전처리는 정규표현식을 통해 특수문자와 공백을 제거하고 각 문장에 대해 토크나이징을 수행하며, 영어의 경우 nltk, 한국어의 경우 mecab을 사용한다.

````python
def preprocess(text, text_type):
  pattern = "[^\w\s]+" # \w: word character (a-z, A-Z, 0-9), \s: whitespace character
  result = re.sub(pattern, "", text)
  if text_type == 'eng':
    tokens = nltk.word_tokenize(result)
  else:
    mecab = Mecab()
    tokens = mecab.morphs(result)
  return tokens
````

````python
df['src'] = df['src'].apply(lambda x: preprocess(x, 'eng'))
df['trg'] = df['trg'].apply(lambda x: preprocess(x, 'kor'))
df.tail()
````

수행한 결과는 아래와 같다. 이번 실습에서는 전처리가 아닌 모델에 집중할 것이기에 단순한 전처리를 수행하였다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/nlp/seq2seq/seq_imp2.png?raw=true" width="700"></p>

### 2.3 데이터 셋 분리

보유한 문장이 많지 않기에, 데이터 셋은 약 7:2:1 정도로 분리한다.

````python
train_val, test = train_test_split(df, test_size=0.1, random_state=42)
train, val = train_test_split(df, test_size=0.22, random_state=42)

# 인덱스 정렬
train.reset_index(drop=True, inplace=True)
val.reset_index(drop=True, inplace=True)
test.reset_index(drop=True, inplace=True)

print("Train set size:", len(train))
print("Validation set size:", len(val))
print("Test set size:", len(test))
````

````
Train set size: 4484
Validation set size: 1265
Test set size: 575
````

### 2.4 단어 집합 생성

단어 집합, 단어장을 만드는 작업은 문자를 인덱스화 시켜 정수로 변환하기 위한 작업으로, 영어와 한국어 문장 각각 수행하여야 한다. 단어장에는 문장 시작, 끝, 빈칸, 모름을 뜻하는 토큰을 기본적으로 추가하고, 이후 문장에서 나오는 단어의 빈도 순서대로 배열에 저장한다. 이후 배열의 인덱스와 단어를 매핑하는 단계를 거쳐 각 단어의 인덱스 및 인덱스에 해당하는 단어를 찾을 수 있게 해주는 딕셔너리도 생성한다.

📍 **Example**

> 단어 집합의 0번 인덱스에 해당하는 단어는 `<sos>` 토큰이고, 1번에 해당하는 단어는 `<eos>`...

````python
def build_vocab(sentence_list):
  word_counts = Counter()
  for words in sentence_list:
      for word in words:
          word_counts[word] += 1
  # 빈도가 높은 순서대로 정렬된 단어 리스트 생성
  vocab = ['<sos>', '<eos>', '<pad>', '<unk>'] + [word for word, _ in word_counts.most_common()]

  # 단어와 인덱스를 매핑해주는 딕셔너리 생성
  word_to_idx = {word: idx for idx, word in enumerate(vocab)}
  idx_to_word = {idx: word for idx, word in enumerate(vocab)}

  return word_to_idx, idx_to_word, vocab
````

````python
eng_word_to_idx, eng_idx_to_word, eng_vocab = build_vocab(train['src'])
kor_word_to_idx, kor_idx_to_word, kor_vocab = build_vocab(train['trg'])
````

실제 학습은 train data로만 수행될 것이기 때문에 train data의 문장으로만 단어 집합을 만든다. 이후 각 데이터 셋에 시작과 끝에 해당하는 토큰을 붙여준다.

````python
train['src'] = train['src'].apply(lambda x: ['<sos>'] + x + ['<eos>'])
train['trg'] = train['trg'].apply(lambda x: ['<sos>'] + x + ['<eos>'])

val['src'] = val['src'].apply(lambda x: ['<sos>'] + x + ['<eos>'])
val['trg'] = val['trg'].apply(lambda x: ['<sos>'] + x + ['<eos>'])

test['src'] = test['src'].apply(lambda x: ['<sos>'] + x + ['<eos>'])
test['trg'] = test['trg'].apply(lambda x: ['<sos>'] + x + ['<eos>'])
````

### 2.5 Padding

우리가 구성한 데이터 셋의 각 문장의 길이는 모두 다르다. 따라서 토큰나이징을 거쳐 생성된 배열도 모두 다른 길이를 가지고 있음을 알 수 있다. 길이가 다른 것은 rnn 구조에서 문제가 되지 않으나, 배치단위의 학습시 문제가 된다. 만약 batch size를 3이라고 가정하고 배열 그대로 데이터 셋을 구성한다면 아래와 같은 문제가 발생한다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/nlp/seq2seq/seq_imp3.png?raw=true" width="300"></p>

이는 모델(RNN)을 구성시 미리 내부 Input size를 정해주기 때문에 발생한다. 위의 경우 각 time-step마다 모델은 3개의 인풋을 받기로 되어있으나 6, 7번째의 step에서는 그렇지 않기 때문이다. 따라서 각 배치마다 모두 같은 길이로 맞춰주기 위해 짧은 문장은 `<pad>` token으로 채워주는 함수가 필요하다. 또한 우리는 앞서 단어 집합을 train 단위로만 구성하였다. 따라서 train에 등장하지 않은 단어가 val 및 test dataset에 등장할 수 있기에 모르는 단어를 `<unk>` token으로 치환하여야 한다. 만약 이를 고려하지 않는다면 단어 집합에 없는 단어가 나왔을 때 이를 인덱스로 변환하는 과정에서 오류가 발생할 것이다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/nlp/seq2seq/seq_imp4.png?raw=true" width="300"></p>

````python
def collate_fn(batch):
    # 영어와 한국어 문장을 배치에서 각각 추출
    english_sentences = [row['src'] for row in batch]
    korean_sentences = [row['trg'] for row in batch]
    
    # 영어와 한국어 문장을 정수로 변환
    english_seqs = [torch.LongTensor([eng_word_to_idx.get(word, eng_word_to_idx['<unk>']) for word in row]) for row in english_sentences]
    korean_seqs = [torch.LongTensor([kor_word_to_idx.get(word, eng_word_to_idx['<unk>']) for word in row]) for row in korean_sentences]

    # 최대길이 100으로 패딩
    english_padded = pad_sequence(english_seqs, batch_first=True, padding_value=0)
    korean_padded = pad_sequence(korean_seqs, batch_first=True, padding_value=0)
    
    max_len = min(100, english_padded.shape[1])
    english_padded = english_padded[:, :max_len]

    max_len = min(100, korean_padded.shape[1])
    korean_padded = korean_padded[:, :max_len]

    return {'english': english_padded, 'korean': korean_padded}
````

우리가 현재 가지고 있는 데이터는 dataframe 형태이다. 이를 pytorch가 학습할 수 있는 배치 단위의 데이터로 구성하기 위해선 DataLoader를 적용해야 하며, 적용시 앞서 작성했던 padding 및 unknown에 관한 함수를 parameter로 넣게 되면 이를 배치단위로 수행하게 된다.

````python
# train 데이터셋과 데이터로더 생성
train_dataset = train.to_dict('records')
train_dataloader = torch.utils.data.DataLoader(train_dataset, batch_size=32, shuffle=True, collate_fn=collate_fn)

# valid 데이터셋과 데이터로더 생성
val_dataset = train.to_dict('records')
val_dataloader = torch.utils.data.DataLoader(val_dataset, batch_size=32, shuffle=True, collate_fn=collate_fn)

# test 데이터셋과 데이터로더 생성
test_dataset = train.to_dict('records')
test_dataloader = torch.utils.data.DataLoader(test_dataset, batch_size=32, shuffle=True, collate_fn=collate_fn)
````



## 3. Model

모델은 Encoder, Decoder 그리고 이를 합친 Seq2sq으로 구성할 것이며 내부 layer는 lstm을 사용할 것이다.

### 3.1 Encoder

````python
class Encoder(nn.Module):
    def __init__(self, input_dim, emb_dim, hid_dim, n_layers, dropout):
        super().__init__()
        
        self. hid_dim = hid_dim
        self.n_layers = n_layers
        
        self.embedding = nn.Embedding(input_dim, emb_dim)
        self.rnn = nn.LSTM(emb_dim, hid_dim, n_layers, dropout = dropout, batch_first=True)
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, src):
        # src = [batch_size, src len]
        embedded = self.dropout(self.embedding(src))
        
        # embedded = [batch_size, src len, emb dim]
        outputs, (hidden, cell) = self.rnn(embedded)
        
        # outputs = [batch size, src len, hid dim]
        # hidden = [batch size, n layers, hid dim]
        # cell = [batch size, n layers, hid dim]
        
        return hidden, cell
````

<br>

### 3.2 Decoder

````python
class Decoder(nn.Module):
    def __init__(self, output_dim, emb_dim, hid_dim, n_layers, dropout):
        super().__init__()
        
        self.output_dim = output_dim
        self.hid_dim = hid_dim
        self.n_layers = n_layers
        
        self.embedding = nn.Embedding(output_dim, emb_dim)
        self.rnn = nn.LSTM(emb_dim, hid_dim, n_layers, dropout=dropout, batch_first=True)
        self.fc_out = nn.Linear(hid_dim, output_dim)
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, input, hidden, cell):
        # input = [batch_size]
        # hidden = [batch_size, n layers, hid dim]
        # cell = [batch_size, n layers, hid dim]
        # context = [n layers, batch size, hid dim]
        
        # input = [1, batch_size]
        input = input.unsqueeze(0)
        
        # embedded = [batch_size, 1, emb dim]
        embedded = self.dropout(self.embedding(input)).permute(1,0,2).contiguous()
        
        output, (hidden, cell) = self.rnn(embedded, (hidden, cell))
        
        # output = [batch size, seq len, hid dim]
        # hidden = [batch size, n layers, hid dim]
        # cell = [batch size, n layers, hid dim]
        
        # output = [batch size, 1, hid dim]
        # hidden = [batch size, n layers, hid dim]
        # cell = [batch size, n layers, hid dim]
        
        # prediction = [batch size, output dim]
        prediction = self.fc_out(output.squeeze(1))
        
        return prediction, hidden, cell
````

### 3.3 Seq2Seq

````python
class Seq2Seq(nn.Module):
   def __init__(self, encoder, decoder):
       super().__init__()
       
       self.encoder = encoder
       self.decoder = decoder
       
       # Encoder와 Decoder의 hid_dim과 n_layer가 같아야 함
       # Encoder의 마지막 은닉 상태가 Decoder의 초기 은닉상태로 쓰이기 때문
       assert encoder.hid_dim == decoder.hid_dim
       assert encoder.n_layers == decoder.n_layers
       
   def forward(self, src, trg, teacher_forcing_ratio=0.5):
       # src = [batch size, src len]
       # trg = [batch size, trg len]
       trg_len = trg.shape[1]
       batch_size = trg.shape[0]
       trg_vocab_size = self.decoder.output_dim
       
       # decoder 결과를 저장할 텐서
       outputs = torch.zeros(batch_size, trg_len, trg_vocab_size)
       
       # Encoder의 마지막 은닉 상태가 Decoder의 초기 은닉상태로 쓰임
       hidden, cell = self.encoder(src)
       
       # Decoder에 들어갈 첫 input은 <sos> 토큰
       input = trg[:, 0]
       
       # target length만큼 반복
       # range(0,trg_len)이 아니라 range(1,trg_len)인 이유 : 0번째 trg는 항상 <sos>라서 그에 대한 output도 항상 0 
       for t in range(1, trg_len):
           
           output, hidden, cell = self.decoder(input, hidden, cell)
           outputs[:,t] = output
           
           # random.random() : [0,1] 사이 랜덤한 숫자 
           # 랜덤 숫자가 teacher_forcing_ratio보다 작으면 True니까 teacher_force=1
           teacher_force = random.random() < teacher_forcing_ratio
           
           # 확률 가장 높게 예측한 토큰
           top1 = output.argmax(1) 
           
           # techer_force = 1 = True이면 trg[t]를 아니면 top1을 input으로 사용
           input = trg[:,t] if teacher_force else top1
       
       return outputs
````

### 3.4 Parameter 세팅

이번 실습시 사용할 parameter는 아래와 같다. 이는 본인 입맛에 맞추어 바꿔도 무방하다.

````python
# device setting
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

input_dim = len(eng_vocab)
output_dim = len(kor_vocab)

# Encoder embedding dim
enc_emb_dim = 256
# Decoder embedding dim
dec_emb_dim = 256

hid_dim=512
n_layers=2

enc_dropout = 0.5
dec_dropout=0.5

enc = Encoder(input_dim, enc_emb_dim, hid_dim, n_layers, enc_dropout).to(device)
dec = Decoder(output_dim, dec_emb_dim, hid_dim, n_layers, dec_dropout).to(device)

model = Seq2Seq(enc, dec).to(device)
model.init_weights()

optimizer = optim.Adam(model.parameters())

# <pad> = padding
trg_pad_idx = kor_word_to_idx["<pad>"]

# <pad> 토큰의 index를 넘겨 받으면 오차 계산하지 않고 ignore하기
criterion = nn.CrossEntropyLoss(ignore_index = trg_pad_idx)
````

loss를 계산하기 위한 criterion 부분에 ignore_index 부분이 추가됨을 확인 할 수 있다. 이는 앞서 구성한 batch 단위 학습을 위해 pad를 추가했기 때문이다. 만약 batch에 속한 문장의 길이는 긴 반면 어떤 한 문장의 길이가 매우 짧다면 대부분은 `<pad>` 토큰일 것이고, 이에대한 학습은 불필요하기 때문에 ignore을 통해 학습에서 제외시킨다.

## 4. Translate

이제 train 데이터를 통해 모델을 통해 학습을 진행하고, epoch마다 val 데이터를 통해 모델을 검증할 것이다. 또한 모든 학습이 끝났을 때, test 데이터를 통해 모델을 평가할 것이다. 이러한 과정을 tracking을 하고 싶다면 wandb를 사용함을 추천한다.

### 4.1 Train code

````python
def train(model, iterator, optimizer, criterion, clip):
    model.train()
    epoch_loss=0
    
    for i, batch in enumerate(iterator):
        src = batch['english'].to(device)
        trg = batch['korean'].to(device)
        
        optimizer.zero_grad()
        
        output = model(src, trg)
        
        # trg = [batch size, trg len]
        # output = [batch size, trg len, output dim]
        output_dim = output.shape[-1]
        
        # <sos>를 token을 제외하기 위한 indexing
        # loss 계산을 위한 tensor size 변경
        output = output[:,1:].contiguous().view(-1, output_dim).to(device)
        trg = trg[:,1:].contiguous().view(-1)

        # output = [(trg len-1) * batch size, output dim)]
        # trg = [(trg len-1) * batch size]
        # loss 계산시에 output dim은 softmax를 통해 원소 하나로 변환됨
        loss = criterion(output, trg)
        
        loss.backward()
        
        # 기울기 폭발 막기 위한 clip
        torch.nn.utils.clip_grad_norm_(model.parameters(), clip)
        
        optimizer.step()
        
        epoch_loss+=loss.item()
        
    return epoch_loss/len(iterator)
````

### 4.2 Validation code

````python
def validation(model, iterator, criterion):
    model.eval()
    epoch_loss = 0
    
    with torch.no_grad():
        for i, batch in enumerate(iterator):
            src = batch['english'].to(device)
            trg = batch['korean'].to(device)
            
            # teacher_forcing_ratio = 0 (학습이 아니기에 정답이 들어가지 않음)
            output = model(src, trg, 0)
            
            # trg = [batch size, trg len]
            # output = [batch size, trg len, output dim]
            output_dim = output.shape[-1]
            
            output = output[:,1:].contiguous().view(-1, output_dim).to(device)
            trg = trg[:,1:].contiguous().view(-1)

            # output = [(trg len - 1) * batch size, output dim]
            # trg = [(trg len - 1) * batch size]
            loss = criterion(output, trg)
            
            epoch_loss+=loss.item()
        
        return epoch_loss/len(iterator)
````

### 4.3 Train & Validation

학습의 총 epoch는 100으로 설정하였으며, early stop은 이번 실습에서는 적용하지 않았다.

````python
N_EPOCHS = 100
CLIP = 1
import time
import math 

best_valid_loss = float('inf')
wandb.init(project="nlp_translate", entity='sigi', name='Seq2Seq')

for epoch in range(N_EPOCHS):
    
    train_loss = train(model, train_dataloader, optimizer, criterion, CLIP)
    valid_loss = evaluate(model, val_dataloader, criterion) 
    
    if valid_loss < best_valid_loss:
        best_valid_loss = valid_loss
        torch.save(model.state_dict(), 'your path to save model')

    print(f'Epoch: {epoch+1:02}')
    print(f'\tTrain Loss: {train_loss:.3f}')
    print(f'\t Val. Loss: {valid_loss:.3f}')
    wandb.log({"train loss":train_loss, "val_loss": valid_loss})
````

### 4.4 Tracking

wnadb를 통해 train 및 val loss가 정상적으로 잘 떨어지고 있음을 확인할 수 있다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/nlp/seq2seq/seq_imp5.png?raw=true" width="800" height="300"></p>

### 4.5 Inference

마지막으로 번역이 잘 되는지 학습한 모델을 통해 test 데이터에 대한 추론을 진행해 본다.

````python
def get_result(sentence_list, wti, itw):    
  result = []
  for sentence in sentence_list:
    try:
      eos_index = sentence.index(wti['<eos>'])
      result.append([itw[word] for word in sentence[1:eos_index]])
    except:
      continue
  return result

def inference(model, iterator):
  model.eval()
  df_result = pd.DataFrame()

  with torch.no_grad():
    for i, batch in enumerate(iterator):
      src = batch['english'].to(device)
      trg = batch['korean'].to(device)
      
      output = model(src, trg, 0)
      output = output.squeeze(1)
      output = output.argmax(dim=-1).tolist()

      origin_sentence = get_result(src.tolist(), eng_word_to_idx, eng_idx_to_word)
      answer_sentence = get_result(trg.tolist(), kor_word_to_idx, kor_idx_to_word)
      translate_sentence = get_result(output, kor_word_to_idx, kor_idx_to_word)

      english = pd.Series(origin_sentence, name='english')
      korean = pd.Series(answer_sentence, name='korean')
      translate = pd.Series(translate_sentence, name='translate')

      df_tmp = pd.concat([english, korean, translate], axis=1)
      df_result = pd.concat([df_result, df_tmp]

  return df_result
````

````python
df_result = inference(model, test_dataloader)
df_result
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/nlp/seq2seq/seq_imp6.png?raw=true" width="800" height="350"></p>

### 5. Lessons & Learned

- 주어진 데이터 셋을 전처리 하는 과정
- pytorch에서 padding하는 과정
- NLP 평가 지표에 대한 정리가 필요함
- 번역 수행 후 이를 다시 자연스러운 문장으로 바꾸는 방법을 구현해야함

## 참조

https://codlingual.tistory.com/91

https://github.com/VumBleBot/Group-Activity/issues/7