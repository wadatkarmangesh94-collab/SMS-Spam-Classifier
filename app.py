import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("Spam Message Classifier")

message = st.text_input("Enter a message:")

if st.button("Predict"):
    data = vectorizer.transform([message])
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Spam Message 🚫")
    else:
        st.success("Not Spam ✅")