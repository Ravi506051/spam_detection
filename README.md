# SMS Spam Detection

A machine-learning application that classifies text messages as **spam** or **ham** (legitimate). The project demonstrates a text-classification workflow from preprocessing to interactive prediction.

## Pipeline
1. Load and inspect labelled SMS data.
2. Clean and normalize message text.
3. Convert text into numerical features using TF-IDF.
4. Train a Multinomial Naive Bayes classifier.
5. Evaluate with precision, recall, F1-score, and a confusion matrix.
6. Test messages through the Streamlit interface.

## Technology
Python · Pandas · Scikit-learn · TF-IDF · Multinomial Naive Bayes · Streamlit

## Run Locally
```bash
git clone https://github.com/Ravi506051/spam_detection.git
cd spam_detection
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m streamlit run app.py
```
If the dependency file or application entry point differs in your checkout, use the paths present in the repository.

## Evaluation and Responsible Use
Report metrics from a held-out test set rather than assuming a fixed accuracy. Review false positives and false negatives, validate empty or unusual input, and keep the fitted vectorizer paired with its classifier. Do not submit private SMS conversations to a public demo.

## Future Improvements
- Compare Naive Bayes with Logistic Regression and linear SVM.
- Test URLs, misspellings, punctuation, and unseen vocabulary.
- Add reproducible evaluation reports and model versioning.

## Maintainer
**Ravi Kumar Rao** · [GitHub](https://github.com/Ravi506051)
