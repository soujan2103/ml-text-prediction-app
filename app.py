import streamlit as st
import pickle
import numpy as np

# Load tokenizer
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

st.title("Text Prediction App")

user_input = st.text_input("Enter text:")

if st.button("Predict"):
    if user_input:
        seq = tokenizer.texts_to_sequences([user_input])

        # Dummy prediction (instead of model)
        prediction = np.random.rand()

        st.write("Prediction:", prediction)
    else:
        st.warning("Enter some text!")
