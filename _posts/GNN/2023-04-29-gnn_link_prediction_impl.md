---
layout: single
title:  'Graph Neural Networks: Link Prediction Implemetation'
toc: true
categories: [Graph Neural Network]
tags: [GNN]

---

해당 포스팅은 Graph Neural Network(=GNN)의 link prediction을 구현하는 과정을 소개한다.
{: .notice}

## Installation

````python
import torch
from torch import Tensor
print(torch.__version__)

# Install required packages.
import os
os.environ['TORCH'] = torch.__version__

!pip install torch-scatter -f https://data.pyg.org/whl/torch-${TORCH}.html
!pip install torch-sparse -f https://data.pyg.org/whl/torch-${TORCH}.html
!pip install pyg-lib -f https://data.pyg.org/whl/nightly/torch-${TORCH}.html
!pip install git+https://github.com/pyg-team/pytorch_geometric.git
````

## Dataset

실습을 위해 [MovieLens](https://grouplens.org/datasets/movielens/)의 데이터를 사용한다. 데이터 셋에는 600명 이상의 사용자와 9,000편 이상의 영화가 약 100,000개의 등급으로 연결되어있다. 이 데이터를 사용하여 영화와 사용자에 대한 노드를 등급인 엣지로 연결하는 heterogeneous graph를 생성할 것이며, 이후 사용자가 특정 영화에 대해 어떤 평가를 내릴지 예측하는 모델을 생성할 것이다.

````python
from torch_geometric.data import download_url, extract_zip

url = 'https://files.grouplens.org/datasets/movielens/ml-latest-small.zip'
extract_zip(download_url(url, '.'), '.')

movies_path = './ml-latest-small/movies.csv'
ratings_path = './ml-latest-small/ratings.csv'
````

````python
import pandas as pd

print('movies.csv:')
print('===========')
print(pd.read_csv(movies_path)[["movieId", "genres"]].head())
print()
print('ratings.csv:')
print('============')
print(pd.read_csv(ratings_path)[["userId", "movieId"]].head())
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/gnn/link_predict/lpimp1.png?raw=true" width="500" height="300"></p>

movie.csv의 movieId는 각 영화에 고유 식별자를 할당하고 장르 열은 해당 영화의 장르를 나타낸다. 해당 정보는 그래프를 생성시 노드의 feature로 사용할 수 있다.

````python
movies_df = pd.read_csv(movies_path, index_col='movieId')

# 장르를 분류함
genres = movies_df['genres'].str.get_dummies('|')
print(genres[["Action", "Adventure", "Drama", "Horror"]].head())

# 장르를 영화의 특징으로 사용하기 위해 torch로 변환
movie_feat = torch.from_numpy(genres.values).to(torch.float)
assert movie_feat.size() == (9742, 20)  # 20 genres in total.
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/gnn/link_predict/lpimp2.png?raw=true" width="500" height="200"></p>

또한, ratings.csv는 사용자(userId)와 영화(movieId)를 연결하는 정보를 가지고 있다. 



## Heterogeneous Graph Creation

그래프 생성을 위해 먼저 각 항목의 ID를 {0, ..., num_rows-1}의 인덱스에 매핑하는 과정을 수행한다. 그런 다음 ratings_df(모든 사용자-영화 간의 상호작용이 담겨있는 데이터 프레임)와의 merge를 통해 [2, num_ratings]의 COO matrix 형식의 edge_index 표현을 얻는다.

````python
ratings_df = pd.read_csv(ratings_path)

# Unique한 사용자에 인덱스 매핑을 수행한다
unique_user_id = ratings_df['userId'].unique()
unique_user_id = pd.DataFrame(data={
    'userId': unique_user_id,
    'mappedID': pd.RangeIndex(len(unique_user_id)),
})

print("Mapping of user IDs to consecutive values:")
print("==========================================")
print(unique_user_id.head())
print()

# Unique한 영화에 인덱스 매핑을 수행한다
unique_movie_id = ratings_df['movieId'].unique()
unique_movie_id = pd.DataFrame(data={
    'movieId': movies_df.index,
    'mappedID': pd.RangeIndex(len(movies_df)),
})
print("Mapping of movie IDs to consecutive values:")
print("===========================================")
print(unique_movie_id.head())
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/gnn/link_predict/lpimp3.png?raw=true" width="500" height="400"></p>

````python
# 사용자와 영화 사이의 연결된 정보를 얻기 위해 rating_df와 merge 수행
ratings_user_id = pd.merge(ratings_df['userId'], unique_user_id,
                            left_on='userId', right_on='userId', how='left')
ratings_movie_id = pd.merge(ratings_df['movieId'], unique_movie_id,
                            left_on='movieId', right_on='movieId', how='left')

print("original dataframe rating userId-movieId-rating:")
print("=================================================")
print(ratings_df.head())
print("userId - mappedId")
print("=================================================")
print(ratings_user_id.head())
print("movieId - mappedId")
print("=================================================")
print(ratings_movie_id.head())
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/gnn/link_predict/lpimp4.png?raw=true" width="500" height="400"></p>

````python
# 사용자와 영화의 'edge_index'를 COO format으로 만듦
edge_index_user_to_movie = torch.stack([ratings_user_id, ratings_movie_id], dim=0)
assert edge_index_user_to_movie.size() == (2, 100836)

print("Final edge indices pointing from users to movies:")
print("=================================================")
print(edge_index_user_to_movie)
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/gnn/link_predict/lpimp5.png?raw=true" width="500" height="150"></p>

````python
# 사용자와 영화의 'edge_index'를 COO format으로 만듦
edge_index_user_to_movie = torch.stack([ratings_user_id, ratings_movie_id], dim=0)
assert edge_index_user_to_movie.size() == (2, 100836)

print("Final edge indices pointing from users to movies:")
print("=================================================")
print(edge_index_user_to_movie)
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/gnn/link_predict/lpimp6.png?raw=true" width="500" height="100"></p>

# TODO

https://medium.com/@pytorch_geometric/link-prediction-on-heterogeneous-graphs-with-pyg-6d5c29677c70