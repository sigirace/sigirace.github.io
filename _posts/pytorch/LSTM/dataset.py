import os
import datetime

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler

mpl.rcParams['figure.figsize'] = (8, 6)
mpl.rcParams['axes.grid'] = False

class WindowGenerator():
  def __init__(self, input_width, label_width, shift, batch_size, target,
              #  train_df=train_df, val_df=val_df, test_df=test_df,
               label_columns=None, download=True):
    
    self.download = download
    self.batch_size = batch_size
    train_df, val_df, test_df = self.get_data()

    self.target = target
    self.train_df, self.scaler_list = self.train_scaling(train_df, self.target)
    self.val_df = self.test_scaling(val_df, self.target, self.scaler_list)
    self.test_df = self.test_scaling(test_df, self.target, self.scaler_list)
    
    # # Store the raw data.
    # self.train_df = train_df
    # self.val_df = val_df
    # self.test_df = test_df
    
    
    # Work out the label column indices.
    self.label_columns = label_columns
    if label_columns is not None:
      self.label_columns_indices = {name: i for i, name in
                                    enumerate(label_columns)}
    self.column_indices = {name: i for i, name in
                           enumerate(train_df.columns)}

    # Work out the window parameters.
    self.input_width = input_width
    self.label_width = label_width
    self.shift = shift

    self.total_window_size = input_width + shift

    self.input_slice = slice(0, input_width)
    self.input_indices = np.arange(self.total_window_size)[self.input_slice]

    self.label_start = self.total_window_size - self.label_width
    self.labels_slice = slice(self.label_start, None)
    self.label_indices = np.arange(self.total_window_size)[self.labels_slice]

  # Min-Max scaling

  def train_scaling(self, df, target):

      X_scaler = StandardScaler()
      Y_scaler = StandardScaler()
      col_list = df.columns.to_list()
      col_list.remove(target)
      X = X_scaler.fit_transform(df[col_list])
      y = Y_scaler.fit_transform(df[[target]])

      scaler_list = {'X_scaler': X_scaler,
                    'Y_scaler': Y_scaler}

      df_scaled = pd.concat([pd.DataFrame(y, columns=[target]), pd.DataFrame(X, columns=col_list)], axis=1)

      return df_scaled, scaler_list

  def test_scaling(self, df, target,  scaler_list):
      
      col_list = df.columns.to_list()
      col_list.remove(target)

      X_scaler = scaler_list['X_scaler']
      Y_scaler = scaler_list['Y_scaler']
      
      df_scaled = pd.concat([pd.DataFrame(Y_scaler.transform(df[[target]]), columns=[target]),\
                            pd.DataFrame(X_scaler.transform(df[col_list]), columns=col_list)],\
                            axis=1)
      
      return df_scaled

  def __repr__(self):
    return '\n'.join([
        f'Total window size: {self.total_window_size}',
        f'Input indices: {self.input_indices}',
        f'Label indices: {self.label_indices}',
        f'Label column name(s): {self.label_columns}'])
  
  def get_data(self):
    if self.download:
      zip_path = tf.keras.utils.get_file(
                  origin='https://storage.googleapis.com/tensorflow/tf-keras-datasets/jena_climate_2009_2016.csv.zip',
                  fname='jena_climate_2009_2016.csv.zip',
                  extract=True)
      csv_path, _ = os.path.splitext(zip_path)
      df = pd.read_csv(csv_path)
    else:
      df = pd.read_csv('본인 경로')
    
    df = df[5::6]
    date_time = pd.to_datetime(df.pop('Date Time'), format='%d.%m.%Y %H:%M:%S')
    df['wv (m/s)']=df['wv (m/s)'].apply(lambda x: 0 if x < 0 else x)
    df['max. wv (m/s)'] = df['max. wv (m/s)'].apply(lambda x: 0 if x < 0 else x)
    wv = df.pop('wv (m/s)')
    max_wv = df.pop('max. wv (m/s)')

    # Convert to radians.
    wd_rad = df.pop('wd (deg)')*np.pi / 180

    # Calculate the wind x and y components.
    df['Wx'] = wv*np.cos(wd_rad)
    df['Wy'] = wv*np.sin(wd_rad)

    # Calculate the max wind x and y components.
    df['max Wx'] = max_wv*np.cos(wd_rad)
    df['max Wy'] = max_wv*np.sin(wd_rad)

    timestamp_s = date_time.map(pd.Timestamp.timestamp)
    day = 24*60*60
    year = (365.2425)*day

    df['Day sin'] = np.sin(timestamp_s * (2 * np.pi / day))
    df['Day cos'] = np.cos(timestamp_s * (2 * np.pi / day))
    df['Year sin'] = np.sin(timestamp_s * (2 * np.pi / year))
    df['Year cos'] = np.cos(timestamp_s * (2 * np.pi / year))

    n = len(df)
    train_df = df[0:int(n*0.7)]
    val_df = df[int(n*0.7):int(n*0.9)]
    test_df = df[int(n*0.9):]

    return train_df, val_df, test_df


  def split_window(self, features):
    inputs = features[:, self.input_slice, :]
    labels = features[:, self.labels_slice, :]
    if self.label_columns is not None:
      labels = tf.stack(
          [labels[:, :, self.column_indices[name]] for name in self.label_columns],
          axis=-1)

    # Slicing doesn't preserve static shape information, so set the shapes
    # manually. This way the `tf.data.Datasets` are easier to inspect.
    inputs.set_shape([None, self.input_width, None])
    labels.set_shape([None, self.label_width, None])

    return inputs, labels

  def make_dataset(self, data):
    data = np.array(data, dtype=np.float32)
    ds = tf.keras.utils.timeseries_dataset_from_array(
        data=data,
        targets=None,
        sequence_length=self.total_window_size,
        sequence_stride=1,
        shuffle=True,
        batch_size=self.batch_size)

    ds = ds.map(self.split_window)

    return ds

  @property
  def train(self):
    return self.make_dataset(self.train_df)

  @property
  def val(self):
    return self.make_dataset(self.val_df)

  @property
  def test(self):
    return self.make_dataset(self.test_df)

  @property
  def example(self):
    """Get and cache an example batch of `inputs, labels` for plotting."""
    result = getattr(self, '_example', None)
    if result is None:
      # No example batch was found, so get one from the `.train` dataset
      result = next(iter(self.train))
      # And cache it for next time
      self._example = result
    return result

  def plot(self, model=None, plot_col=None, max_subplots=3):
    if plot_col is None:
      plot_col = self.target
    inputs, labels = self.example
    plt.figure(figsize=(12, 8))
    plot_col_index = self.column_indices[plot_col]
    max_n = min(max_subplots, len(inputs))
    for n in range(max_n):
      plt.subplot(max_n, 1, n+1)
      plt.ylabel(f'{plot_col} [normed]')
      plt.plot(self.input_indices, inputs[n, :, plot_col_index],
              label='Inputs', marker='.', zorder=-10)

      if self.label_columns:
        label_col_index = self.label_columns_indices.get(plot_col, None)
      else:
        label_col_index = plot_col_index

      if label_col_index is None:
        continue

      plt.scatter(self.label_indices, labels[n, :, label_col_index],
                  edgecolors='k', label='Labels', c='#2ca02c', s=64)
      if model is not None:
        predictions = model(inputs)
        plt.scatter(self.label_indices, predictions[n, :, label_col_index],
                    marker='X', edgecolors='k', label='Predictions',
                    c='#ff7f0e', s=64)

      if n == 0:
        plt.legend()

    plt.xlabel('Time [h]')