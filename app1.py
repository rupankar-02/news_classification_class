import streamlit as st
import joblib

model= joblib.load("news-classification-model.pkl")

sentiment_labels= {'0':'tech', '1':'business', '2':'sport', '3':'entertainment', '4':'politics'}

st.title("news-classification")

user_input= st.text_area("enter your text here:")

if st.button("predict"):
    print(user_input)
    predicted_sentiment = model.predict([user_input])[0]
    print("predicted_label:"+ str(predicted_sentiment))
    predicted_sentiment_label = sentiment_labels[str(predicted_sentiment)]
    
    st.info(f"predicted sentiment : {predicted_sentiment_label}")