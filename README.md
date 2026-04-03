
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

## 📌 Future Improvements

* Use advanced models (Naive Bayes, SVM, Deep Learning)
* Deploy app online (Streamlit Cloud / Render)
* Improve text preprocessing
* Add more dataset

---
## 📸Screenshot
![WhatsApp Image 2026-04-03 at 11 58 24 PM](https://github.com/user-attachments/assets/2a1afa91-93d3-455d-ab86-68081829b7f1)
<img width="1907" height="746" alt="Screenshot 2026-04-04 002141" src="https://github.com/user-attachments/assets/2cf537af-07c4-49f5-adc7-a8530e1af39d" />

## 🙌 Conclusion

This project demonstrates how Machine Learning can be used for real-world text classification problems like spam detection.

## 🧠 Approach

In this project, I built a Spam Message Classifier using Machine Learning.

First, I collected the SMS Spam dataset and loaded it using pandas. Then, I cleaned the text data by converting all messages to lowercase and removing unnecessary characters.

Next, I converted the text into numerical form using TF-IDF vectorization, which helps the model understand the importance of words.

After that, I split the data into training and testing sets and trained a Logistic Regression model on the training data.

Finally, I evaluated the model using accuracy, which was around 95%. I also saved the trained model and vectorizer using pickle.

To make the project user-friendly, I created a simple Streamlit web app where users can enter a message and instantly see whether it is spam or not.
