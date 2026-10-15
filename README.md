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
-pip install streamlit

then run this to see the project working
-python -m streamlit run app.py

https://github.com/Ravi506051/spam_detection/blob/main/README.md


## 🔍 How It Works

1. The user enters or uploads an SMS message.
2. The text is cleaned and preprocessed.
3. TF-IDF converts the text into numerical features.
4. The trained Multinomial Naive Bayes classifier predicts whether the message is spam or ham.
5. The Streamlit interface displays the prediction.

## 📊 Model Evaluation

Evaluate the classifier using a separate test dataset and report:

- **Accuracy:** Overall proportion of correct predictions.
- **Precision:** Proportion of predicted spam messages that are actually spam.
- **Recall:** Proportion of actual spam messages correctly detected.
- **F1-Score:** Balance between precision and recall.
- **Confusion Matrix:** Shows correct and incorrect classifications.

Add the actual metric values after running the model; do not assume performance numbers.

## ⚠️ Limitations

- Unseen words, slang, spelling variations, and new spam patterns may affect predictions.
- False positives may cause legitimate messages to be classified as spam.
- Performance depends on the dataset and preprocessing steps.
- Avoid entering private or sensitive messages into a demo application.

## 🚀 Future Improvements

- Compare Naive Bayes with Logistic Regression and other text classifiers
- Improve preprocessing for misspellings and unusual text
- Add a confusion matrix and classification report
- Test the model on recent, unseen SMS examples
- Improve the interface with clearer prediction explanations

## 👨‍💻 Project Maintainer

Ravi Kumar Rao

GitHub: https://github.com/Ravi506051
