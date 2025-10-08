# 🎓 Student Depression Prediction App

A machine learning web application that predicts the depression level of university students based on academic and psychological indicators using a trained logistic regression model.

🚀 Live App: Click to [Open](https://student-mental-health-analysis.streamlit.app/)  
 📦 Model: Logistic Regression (Multiclass)  
 🧠 Target: Depression Label (PHQ-9 inspired classification)

## 📌 Features

### 🔢 Predicts 6 levels of depression:

- No Depression

- Minimal

- Mild

- Moderate

- Moderately Severe

- Severe

### 🎛️ User inputs:

- Scholarship status

- Psychological questionnaire (9 factors)

- Academic metrics (CGPA, year)

- Demographics (Age, Gender)

- and more...

### 📊 Real-time prediction with visual feedback (color-coded result)

- 🔐 Backend model is pre-trained and scaled

- 🧼 Clean, responsive interface via Streamlit

## 🧠 Tech Stack

| Component         | Technology                         |
| ----------------- | ---------------------------------- |
| Frontend          | Streamlit                          |
| Model             | Logistic Regression (scikit-learn) |
| Preprocessing     | StandardScaler                     |
| Model Persistence | joblib                             |
| Deployment        | Streamlit Cloud                    |

## 📦 Setup & Run Locally

```bash
git clone https://github.com/Abh3shek/mental-health-analysis
cd mental-health-analysis
pip install -r requirements.txt
streamlit run app.py
```

## 🧪 Model Info

- Trained on survey dataset

- Encodes:

  - CGPA ranges

  - Academic year

  - Gender

  - Age groups

## 🔐 Notes

- Model & scaler are pre-trained and bundled

- Data is not collected or stored during use

## Author

[Abh3shek](https://github.com/Abh3shek/)
