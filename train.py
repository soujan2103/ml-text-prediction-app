# Install tensorflow (only first time if needed)
# pip install tensorflow

import numpy as np
import pickle
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding
from tensorflow.keras.preprocessing.text import Tokenizer

# STEP 1: Text data
texts = [
    "i love machine learning",
    "deep learning is powerful",
    "ai is the future",
    "machine learning is amazing",
    "deep learning improves ai"
]

# STEP 2: Tokenizer
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)

with open("tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)

print("✅ tokenizer saved")

# STEP 3: Dummy dataset
X = np.random.randint(100, size=(100, 10))
y = np.random.randint(2, size=(100, 1))

# STEP 4: Model
model = Sequential()
model.add(Embedding(input_dim=100, output_dim=64, input_length=10))
model.add(LSTM(64))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# STEP 5: Train
model.fit(X, y, epochs=5)

# STEP 6: Save model
model.save("lstm_model.h5")

print("✅ model saved")