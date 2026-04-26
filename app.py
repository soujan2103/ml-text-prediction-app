import streamlit as st
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load tokenizer
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# Load model
model = load_model("lstm_model.h5")

st.title("Text Prediction App")

user_input = st.text_input("Enter text:")

if st.button("Predict"):
    if user_input:
        seq = tokenizer.texts_to_sequences([user_input])
        padded = pad_sequences(seq, maxlen=10)
        pred = model.predict(padded)
        st.write("Prediction:", pred[0][0])
    else:
        st.warning("Enter some text!")