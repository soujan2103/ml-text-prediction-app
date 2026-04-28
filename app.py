import streamlit as st
import numpy as np

st.title("Text Prediction App")

user_input = st.text_input("Enter text:")

if st.button("Predict"):
    if user_input:
        # Simple logic (no tokenizer, no keras)
        prediction = len(user_input) * np.random.rand()

        st.write("Prediction:", prediction)
    else:
        st.warning("Enter some text!")
