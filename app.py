import streamlit as st
import joblib
import numpy as np

# Load your trained model and scaler
model = joblib.load("models/final_model.joblib")
scaler = joblib.load("models/scaler.joblib")

# App title
st.title("🎓 Student Depression Prediction App")

st.markdown("""
Welcome to the **Depression Detection Tool** for students.  
Please fill out the form below and click **Predict** to check the predicted depression level.
""")

st.header("🧠 Student Input Form")

# ---------- Scholarship ----------
scholarship = st.selectbox("Scholarship Received?", ["Yes", "No"])
scholarship_encoded = 1 if scholarship == "Yes" else 0
st.caption("Whether the student received a waiver or scholarship at their university.")

# ---------- Depression Symptom Inputs (PHQ-9 like scale) ----------
little_interest = st.slider("Little interest or pleasure in doing things", 0, 3)
feeling_down = st.slider("Feeling down, depressed, or hopeless", 0, 3)
sleep_issues = st.slider("Trouble falling/staying asleep or sleeping too much", 0, 3)
low_energy = st.slider("Feeling tired or having little energy", 0, 3)
appetite_issues = st.slider("Poor appetite or overeating", 0, 3)
self_worth = st.slider("Feeling bad about yourself / failure", 0, 3)
concentration_issues = st.slider("Trouble concentrating", 0, 3)
restlessness = st.slider("Restlessness / moving too slowly", 0, 3)
suicidal_thoughts = st.slider("Thoughts of self-harm or suicide", 0, 3)

# ---------- CGPA ----------
cgpa_map = {
    "Below 2.50": 0,
    "2.50 - 2.99": 1,
    "3.00 - 3.39": 2,
    "3.40 - 3.79": 3,
    "3.80 - 4.00": 4,
    "Other": 5
}
cgpa_label = st.selectbox("Current CGPA Range", list(cgpa_map.keys()))
cgpa_encoded = cgpa_map[cgpa_label]
st.caption("Select your cumulative GPA range.")

# ---------- Academic Year ----------
academic_year_map = {
    "First Year or Equivalent": 0,
    "Second Year or Equivalent": 1,
    "Third Year or Equivalent": 2,
    "Fourth Year or Equivalent": 3,
    "Other": 4
}
academic_year_label = st.selectbox("Academic Year", list(academic_year_map.keys()))
academic_year_encoded = academic_year_map[academic_year_label]

# ---------- Gender ----------
gender_map = {
    "Male": 0,
    "Female": 1,
    "Prefer not to say": 2
}
gender_label = st.selectbox("Gender", list(gender_map.keys()))
gender_encoded = gender_map[gender_label]

# ---------- Age Group ----------
age_map = {
    "Below 18": 0,
    "18-22": 1,
    "23-26": 2,
    "27-30": 3,
    "Above 30": 4
}
age_label = st.selectbox("Age Group", list(age_map.keys()))
age_encoded = age_map[age_label]

# ---------- Combine Features ----------
features = np.array([[
    scholarship_encoded, little_interest, feeling_down, sleep_issues,
    low_energy, appetite_issues, self_worth, concentration_issues,
    restlessness, suicidal_thoughts, cgpa_encoded,
    academic_year_encoded, gender_encoded, age_encoded
]])

# ---------- Predict Button ----------
if st.button("🔍 Predict Depression Level"):
    # Scale input
    features_scaled = scaler.transform(features)

    # Predict
    prediction = model.predict(features_scaled)[0]

    # Map prediction to readable label, emoji, and color
    label_map = {
        0: ("No Depression", "🟢", "#28a745"),
        1: ("Minimal Depression", "🟡", "#ffc107"),
        2: ("Mild Depression", "🟡", "#ffc107"),
        3: ("Moderate Depression", "🟠", "#fd7e14"),
        4: ("Moderately Severe Depression", "🟠", "#fd7e14"),
        5: ("Severe Depression", "🔴", "#dc3545")
    }

    label, emoji, color = label_map.get(prediction, ("Unknown", "❓", "#6c757d"))

    # Styled result display
    st.markdown(f"""
    <div style="padding: 1.2rem; border-radius: 8px; background-color: {color}; color: white; text-align: center; font-size: 1.5rem; font-weight: bold;">
        {emoji} Predicted Depression Level: {label}
    </div>
    """, unsafe_allow_html=True)
