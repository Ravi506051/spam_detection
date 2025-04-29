# 📧 Spam Message Detector using Machine Learning

This project is a simple yet powerful **Spam Message Detector** that uses machine learning to classify messages as "spam" or "ham" (not spam). The model is trained on a labeled dataset of SMS messages and is deployed using **Streamlit** for a user-friendly web interface.

## 🚀 Features

- Upload or enter a message to check if it's spam
- Machine learning model trained on a labeled CSV dataset
- Interactive and responsive UI using Streamlit

## 🧠 Model Overview

- **Data Source**: A CSV file containing labeled SMS messages (`spam` or `ham`)
- **Preprocessing**: Text cleaning, tokenization, stopword removal
- **Vectorization**: TF-IDF
- **Model**: Multinomial Naive Bayes (you can modify it to use other classifiers)
- **Evaluation**: Accuracy, Precision, Recall

## 🖥️ Streamlit Web App

Run the Streamlit app to interact with the model using a web interface.

## Requirements

run this on your terminal
pip install streamlit

then run this to see the project working
python -m streamlit run app.py

