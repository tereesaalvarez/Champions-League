# test_tensorflow.py
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

print("TensorFlow version:", tf.__version__)
model = Sequential([
    Dense(10, activation='relu', input_shape=(10,))
])
print("Model created successfully!")
