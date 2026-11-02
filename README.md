# SMS Spam Detection

A machine-learning project that classifies text messages as **spam** or **ham** (legitimate). The repository demonstrates a complete text-classification workflow, from preprocessing to interactive prediction.

## Core workflow
1. Load and inspect labelled SMS data.
2. Clean and normalize message text.
3. Convert text into numerical features with TF-IDF.
4. Train a Multinomial Naive Bayes classifier.
5. Evaluate predictions using precision, recall, F1-score and a confusion matrix.
6. Use the Streamlit interface to test messages.

## Technology
Python · Pandas · Scikit-learn · TF-IDF · Multinomial Naive Bayes · Streamlit

## Run locally
```bash
git clone https://github.com/Ravi506051/spam_detection.git
cd spam_detection
python -m venv .venv
# Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python -m streamlit run app.py
```
If a requirements file is not present, install the dependencies used by the project before launching the app.

## Evaluation and responsible use
Report metrics from an actual held-out test run; do not assume an accuracy score. Review false positives as well as false negatives. Keep the fitted vectorizer and classifier together, validate empty input, and never upload private SMS conversations to a public demo.

## Possible extensions
- Compare Naive Bayes with Logistic Regression and linear SVM.
- Add tests for URLs, misspellings, punctuation and unseen vocabulary.
- Save a reproducible evaluation report and model version.

## Maintainer
**Ravi Kumar Rao** · [GitHub](https://github.com/Ravi506051)
