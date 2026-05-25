import streamlit as st
import requests

st.title("Loan Approval Prediction System")


# User Inputs
dependents = st.number_input("Dependents", min_value=0)

applicant_income = st.number_input("Applicant Income")

coapplicant_income = st.number_input("Coapplicant Income")

loan_amount = st.number_input("Loan Amount")

loan_term = st.number_input("Loan Amount Term")

credit_history = st.selectbox("Credit History", [0, 1])


# Predict Button
if st.button("Predict Loan Status"):

    payload = {
        "Dependents": dependents,
        "ApplicantIncome": applicant_income,
        "CoapplicantIncome": coapplicant_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_term,
        "Credit_History": credit_history,
    }

    # API Call
    response = requests.post("http://127.0.0.1:8000/predict", json=payload)

    result = response.json()

    st.subheader(f"Prediction: {result['prediction']}")

    st.write(f"Approval Probability: {result['approval_probability']}")
