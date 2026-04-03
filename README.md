# 📩 Spam Message Classifier

This is a simple Machine Learning project that classifies SMS messages as **Spam** or **Not Spam (Ham)** using Natural Language Processing (NLP) techniques.

---

## 🚀 Project Overview

The goal of this project is to build a basic spam detection system using:

* Text preprocessing
* TF-IDF vectorization
* Logistic Regression model
* Streamlit web application

---

## 🧠 Technologies Used

* Python
* pandas
* scikit-learn
* Streamlit
* pickle

---

## 📂 Project Structure

```
spam-classifier/
│── model.py              # Model training script
│── app.py                # Streamlit app
│── spam.csv              # Dataset
│── model.pkl             # Saved trained model
│── vectorizer.pkl        # Saved TF-IDF vectorizer
```

---

## ⚙️ Installation

1. Clone the repository:

```
git clone https://github.com/your-username/spam-classifier.git
cd spam-classifier
```

2. Install required libraries:

```
pip install pandas scikit-learn streamlit
```

---

## ▶️ How to Run

### Step 1: Train the model

```
python model.py
```

This will:

* Train the model
* Print accuracy
* Save `model.pkl` and `vectorizer.pkl`

---

### Step 2: Run the Streamlit app

```
streamlit run app.py
```

---

## 🧪 Example

| Message                              | Prediction |
| ------------------------------------ | ---------- |
| "Congratulations! You won a lottery" | Spam 🚫    |
| "Hey, are we meeting today?"         | Not Spam ✅ |

---

## 📊 Model Details

* Algorithm: Logistic Regression
* Feature Extraction: TF-IDF
* Accuracy: ~95%

---

## 📸 Screenshot

(Add your app screenshot here)

---

## 📌 Future Improvements

* Use advanced models (Naive Bayes, SVM, Deep Learning)
* Deploy app online (Streamlit Cloud / Render)
* Improve text preprocessing
* Add more dataset

---

## 🙌 Conclusion

This project demonstrates how Machine Learning can be used for real-world text classification problems like spam detection.
