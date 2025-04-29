import streamlit as st
import pickle
with open('spam_classifier_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)
st.title("📩 Spam Message Classifier")
input_message = st.text_area("Enter the message:")
if st.button("Predict"):
    if input_message.strip() != "":
        input_vec = vectorizer.transform([input_message])
        prediction = model.predict(input_vec)[0]

        if prediction == 1:
            st.error(" Spam Message Detected!")
        else:
            st.success(" This is a Ham (Safe) Message.")
    else:
        st.warning("Please enter a message to classify.")
