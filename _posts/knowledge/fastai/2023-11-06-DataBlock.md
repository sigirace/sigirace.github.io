---
layout: single
title:  'Constructing a DataBlock using Fastai'
toc: true
categories: [Fastai]
tags: [DataBlock, DataSets, DataLoaders, RandomResizedCrop, ImageBlock, CategoryBlock]

---

이번 포스팅에서는 Fastai의 `DataBlock`에 대한 [Medium의 글](https://medium.com/mlearning-ai/constructing-a-datablock-using-fastai-7703752ae17a)을 소개한다.
{: .notice}

## 1. Introduce

Fastai의 공식문서에서 `DataBlock`에 대해 아래와 같이 소개하고 있다.

- High level API to quickly get your data in a `DataLoaders`
- Generic container to quickly build [`Datasets`](https://docs.fast.ai/data.core.html#datasets) and [`DataLoaders`](https://docs.fast.ai/data.core.html#dataloaders).

즉, `DataBlock`은 소유한 데이터로부터 빠르게 `Datasets`와 `DataLoaders`를 구축하고 사용할 수 있게 하는 API이다.



## 2. Jargons about data

### 2.1 Dataset

- 독립변수(feature) 그리고 종속변수(target)를 하나의 튜플로써 반환하는 집합

### 2.2 DataLoader

- `DataLoader`는 mini-batches를 제공하는 iterator(반복기)
- Mini-batches는 독립변수와 종속변수로 구성된 여러 쌍을 의미함

Fastai에는 이러한 개념에 더해 training 그리고 validation set을 함께 가져오기 위한 Datasets와 DataLoaders를 제공함

### 2.3 Datasets

- Training 과 validation dataset을 포함한 iterator
- 하나의 튜플이 아닌 train과 valid set을 반환

### 2.4 DataLoaders

- Training과 validation dataloader를 포함한 객체
- `Datasets`를 생성 및 테스트 한 후 `DataLoaders`를 확인하는 것이 이해하기 쉬움



## 3. Example

☀️ **데이터 불러오기**

````python
import os
import pandas as pd
import torchvision
import numpy as np
from PIL import Image
from tqdm.notebook import tqdm

train_dataset = torchvision.datasets.CIFAR10(root='./cifar10_data', train=True, download=True)

class_mapping = {
    0: "Airplane",
    1: "Automobile",
    2: "Bird",
    3: "Cat",
    4: "Deer",
    5: "Dog",
    6: "Frog",
    7: "Horse",
    8: "Ship",
    9: "Truck"
}

save_dir = './cifar10_images/train'
os.makedirs(save_dir, exist_ok=True)

data = {'fname': [], 'label': []}

for i, (image, label) in tqdm(enumerate(train_dataset), total=len(train_dataset)):
    image = np.array(image)
    img = Image.fromarray((image * 255).astype(np.uint8))
    img_filename = f'image_{i}.png'
    img.save(f'{save_dir}/{img_filename}')
    
    data['fname'].append(img_filename)
    data['label'].append(class_mapping[label])

df = pd.DataFrame(data)

df['is_valid'] = True
num_samples = len(df)
num_samples_to_set_false = int(0.2 * num_samples)
indices_to_set_false = np.random.choice(num_samples, num_samples_to_set_false, replace=False)

df.loc[indices_to_set_false, 'is_valid'] = False

df.head()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/fastai/datablock/1.png?raw=true" width="300" height="200"></p>

- 데이터 소스 불러오기

☀️ **Datasets 생성**

````python
from fastai.data.core import DataLoaders, DataLoaders
import pandas as pd
from fastai.data.block import DataBlock

dblock = DataBlock()
````

- 빈 `DataBlock` 객체를 생성

````python
dblock = DataBlock()
dsets = dblock.datasets(df)
dsets[0:5]
````

````
[(Pandas(Index=0, fname='image_0.png', label='Frog', is_valid=True),
  Pandas(Index=0, fname='image_0.png', label='Frog', is_valid=True)),
 (Pandas(Index=1, fname='image_1.png', label='Truck', is_valid=True),
  Pandas(Index=1, fname='image_1.png', label='Truck', is_valid=True)),
 (Pandas(Index=2, fname='image_2.png', label='Truck', is_valid=True),
  Pandas(Index=2, fname='image_2.png', label='Truck', is_valid=True)),
 (Pandas(Index=3, fname='image_3.png', label='Deer', is_valid=True),
  Pandas(Index=3, fname='image_3.png', label='Deer', is_valid=True)),
 (Pandas(Index=4, fname='image_4.png', label='Automobile', is_valid=True),
  Pandas(Index=4, fname='image_4.png', label='Automobile', is_valid=True))]
````

````python
dsets.train[0]
````

````
(fname       image_18920.png
 label              Airplane
 is_valid               True
 Name: 18920, dtype: object,
 fname       image_18920.png
 label              Airplane
 is_valid               True
 Name: 18920, dtype: object)
````

- 보유한 데이터 소스로 부터 `Datasets`를 생성

😗 **why it’s been printed out two times?**

> 출력이 두번 나오는 이유는 Fastai의 `DataBlock`이 기본적으로 `Datasets`를 생성할 때, Input(입력)과 Target(목표) 두 가지를 가정하기 때문

````python
def get_x(r): return os.path.join(save_dir, r['fname'])

def get_y(r): return r['label']

dblock = DataBlock(get_x= get_x, get_y=get_y)
dsets = dblock.datasets(df)
dsets.train[0]
````

````
('./cifar10_images/train/image_21295.png', 'Ship')
````

- 그러나 위와 같이 모든 데이터가 필요하지 않기에 `get_x`와 `get_y`를 통해 적절하게 배분하여 사용할 수 있음

☀️ **Transforms**

````python
from fastai.vision.data import ImageBlock
from fastai.data.block import CategoryBlock

dblock = DataBlock(blocks=(ImageBlock, CategoryBlock), get_x=get_x, get_y=get_y)
dsets = dblock.datasets(df)
dsets.train[0]
````

````
(PILImage mode=RGB size=32x32, TensorCategory(5))
````

- Image와 label을 tensor 형태로 변환하기 위해 `ImageBloc`과 `CategoryBlock`을 사용

````python
import torch

dsets.train[1][0].show()
idx = dsets.train[1][1].item()
print(dsets.train.vocab[idx])
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/fastai/datablock/2.png?raw=true" width="150" height="150"></p>

☀️ **데이터 분할**

````python
def splitter(df):
  train = df.index[~df['is_valid']].tolist()
  valid = df.index[df['is_valid']].tolist()
  return train, valid

dblock = DataBlock(blocks=(ImageBlock, CategoryBlock),
                   splitter = splitter,
                   get_x = get_x,
                   get_y = get_y)

dsets = dblock.datasets(df)
dsets.train[4]
````

````
(PILImage mode=RGB size=32x32, TensorCategory(9))
````

````python
dsets.valid[4]
````

````
(PILImage mode=RGB size=32x32, TensorCategory(1))
````

- 지금까지는 `is_valid` 열을 사용하지 않았기에 DataBlock이 랜덤하게 분할을 사용함
- splitter 함수를 인자로 추가하여 `is_valid` 열을 사용하여 데이터를 분할 시킴

☀️ **DataLoaders**

````python
from fastai.vision.augment import RandomResizedCrop

dblock = DataBlock(blocks=(ImageBlock , CategoryBlock) , 
                   splitter = splitter , 
                   get_x = get_x , 
                   get_y = get_y , 
                   item_tfms = RandomResizedCrop(128 , min_scale=0.353))

dls = dblock.dataloaders(df)
dls.show_batch()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/fastai/datablock/3.png?raw=true" width="700" height="500"></p>

- `Dataloaders`가 동일한 이미지 사이즈를 가진 데이터를 반복시킬 수 있도록 `RandomResizedCrop`을 사용

## 4. Result

- 이번 포스팅을 통해 fastai가 제공하는 모델에 사용할 수 있는 데이터를 구축하였음
- 즉, `Learner`를 사용하여도 변경되는 것은 없음









