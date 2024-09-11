import streamlit as st
import pickle
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from keras.preprocessing.sequence import pad_sequences

# Loading model
model = load_model("artifacts/sentiment_model.h5")

# Load Tokenizer
with open('artifacts/tokenizer.pickle','rb') as handle:
    tokenizer = pickle.load(handle)

max_sequence_len = 43


def predict_sentiment(text):
  input_text = [text]
  tokenized_text = tokenizer.texts_to_sequences(input_text)
  input_sentances = np.array(pad_sequences(tokenized_text,maxlen = max_sequence_len,padding='post'))
  print(input_sentances)
  sentiment = model.predict(input_sentances,batch_size=1,verbose = 3)[0]
  print(sentiment)

  if(np.argmax(sentiment) == 0):
      return "Negative"
  elif (np.argmax(sentiment) == 1):
      return "Neutral"
  elif (np.argmax(sentiment) == 2):
      return "Positive"


st.title("This is home page of sentiment analysis")

text = st.text_input("Enter the Review")

if st.button("Predict Sentiment"):
    result = predict_sentiment(text)

    st.write(result)