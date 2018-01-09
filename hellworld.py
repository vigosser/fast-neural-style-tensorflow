#code: utf-8
import tensorflow as tf
from preprocessing import preprocessing_factory
import reader
import model
import time
import os
print("helloworld")
a = [[2, 3], [4, 5]]
b = tf.expand_dims(a, 0)
print(b)
