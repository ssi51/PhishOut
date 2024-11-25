import streamlit as st
import joblib
import re

# Load the model
model = joblib.load('phishing_model.pkl')

# Feature extraction
def extract_features(url):
    return [
        len(url),
        int(bool(re.search(r'\d+\.\d+\.\d+\.\d+', url))),
        len(re.findall(r'[@#?&]', url))
    ]

st.title("Phishing Detection System")
st.write("Enter a URL to check if it is phishing or legitimate.")

# Input from user
user_input = st.text_input("URL:", placeholder="e.g., http://example.com")

if st.button("Analyze"):
    features = extract_features(user_input)
    prediction = model.predict([features])[0]
    result = "Phishing" if prediction == 1 else "Legitimate"
    st.write(f"Result: **{result}**")
