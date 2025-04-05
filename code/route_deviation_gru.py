"""
File: route_deviation_gru.py
Description: GRU-based binary classifier for route deviation detection.
"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense

# Assume input shape is (timesteps, features)
model = Sequential([
    GRU(64, input_shape=(None, 5)),  # Adjust shape based on input
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')  # Binary: 1 = Deviated, 0 = Normal
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()

