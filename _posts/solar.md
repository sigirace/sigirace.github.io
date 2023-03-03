ReduceLROnPlateau -> https://bo-10000.tistory.com/95

LSTM -> https://jiwonkoh.tistory.com/188

optuna -> https://towardsdatascience.com/hyperparameter-tuning-of-neural-networks-with-optuna-and-pytorch-22e179efc837

optima wandb -> https://github.com/nzw0301/optuna-wandb/blob/main/part-1-with-optuna-v3/wandb_optuna.py

캐글: https://www.kaggle.com/code/nicapotato/keras-timeseries-multi-step-multi-output

영: https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/structured_data/time_series.ipynb#scrollTo=35qoSQeRVfJg

한: https://colab.research.google.com/github/tensorflow/docs-l10n/blob/master/site/ko/tutorials/structured_data/time_series.ipynb?hl=ko#scrollTo=2jZ2KkqGCfzu

lstm 유형: https://blog.naver.com/chunjein/221589624838

optuna + keras : https://precommer.tistory.com/79

ds = ds.concatenate(ds)

[2023. 2. 27. 오후 2:24:14] 신강식: 그럼 학습시에
[2023. 2. 27. 오후 2:24:26] 신강식: KMA_SNOW 만 쓰는거고
[2023. 2. 27. 오후 2:24:34] 신강식: 예측시에는 웨더빗 *0.1



def make_dataset(self, dataframe):

​    for row, cid in enumerate(dataframe.CBP_GEN_ID.unique()):

​      data = dataframe[dataframe.CBP_GEN_ID == cid].copy()

​      data = np.array(data, dtype=np.float32)

​      ds = tf.keras.utils.timeseries_dataset_from_array(

​          data=data,

​          targets=None,

​          sequence_length=self.total_window_size,

​          sequence_stride=1,

​          shuffle=True,

​          batch_size=self.batch_size)

​      if row == 0:

​        ds = ds.map(self.split_window)

​      else:

​        ds = ds.concatenate(ds)

​    return ds



​      df = pd.read_csv('/content/drive/MyDrive/solar/new/jena_climate_2009_2016.csv')

​    



['CBP_GEN_ID', 'DATE', 'HOUR', 'CAPACITY']

['GEN', 'GEN_EFF']

['LA', 'LO'] -> Y/N

['GHI', 'DNI', 'DHI', 'UV'] -> Default

['APP_TEMP', 'CLOUDS', 'DEWPT', 'PRECIP', 'PRES', 'RH', 'SLP', 'BIT_TEMP', 'VIS', 'KMA_TEMP', 'SKY', 'RAIN', 'HUMIDITY', 'KMA_SNOW'] -> correlation 0.5~0.1

['Wx', 'Wy'] -> Y/N

['Day sin', 'Day cos'] -> Y/N

['Year sin', 'Year cos'] -> Y/N

['EWM3', 'EWM6', 'EWM9'] -> 0~3



num_layer = [1, 2, 3]

units1 = [32, 64, 128, 256]

recurrent_dropout1 = [0.0, 0.3, 0.5]

units2 = [32, 64, 128, 256]

recurrent_dropout2 = [0.0, 0.3, 0.5]

units3 = [32, 64, 128, 256]

recurrent_dropout3 = [0.0, 0.3, 0.5]

dropout_layer= [0.0, 0.3, 0.5]







gradient clipping: https://stackoverflow.com/questions/36498127/how-to-apply-gradient-clipping-in-tensorflow

cnn-lstm(uni): https://pseudo-lab.github.io/Tutorial-Book/chapters/time-series/Ch5-CNN-LSTM.html#

cnn-lstm: https://towardsdatascience.com/cnn-lstm-based-models-for-multiple-parallel-input-and-multi-step-forecast-6fe2172f7668

keras loss, metric: https://stackoverflow.com/questions/51256695/loss-metrics-and-scoring-in-keras

optuna + wandb: https://github.com/nzw0301/optuna-wandb/blob/main/part-1/wandb_optuna.py

api: add32e093cd85d238c6d390e5d59c238637259f8
