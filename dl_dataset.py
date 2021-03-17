import tensorflow_datasets as tfds

builder = tfds.builder('beans')
builder.download_and_prepare()

#https://www.tensorflow.org/datasets/overview