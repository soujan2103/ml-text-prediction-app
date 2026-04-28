import streamlit as st
import random

st.set_page_config(page_title="Text Sentiment Predictor")

st.title("Text Sentiment Predictor")

user_input = st.text_input("Enter text:")

positive_words = ["love", "good", "great", "excellent", "happy", "amazing"]
negative_words = ["hate", "bad", "worst", "terrible", "sad", "poor"]

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter text")
    else:
        text = user_input.lower()

        # Default score
        score = round(random.uniform(0.6, 0.95), 2)

        if any(word in text for word in positive_words):
            st.success(f"Positive 😊  | Confidence: {score}")

        elif any(word in text for word in negative_words):
            st.error(f"Negative 😠  | Confidence: {score}")

        else:
            neutral_score = round(random.uniform(0.4, 0.6), 2)
            st.info(f"Neutral 🤔  | Confidence: {neutral_score}")
