from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import asyncio

# Create FastAPI App
app = FastAPI()


# Load Model
model = joblib.load("model.pkl")

# Load Scaler
scaler = joblib.load("scaler.pkl")


# Request Body Schema
class LoanInput(BaseModel):
    Dependents: int
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float


# Home Route
@app.get("/")
async def home():
    return {"message": "Loan Prediction API Running"}


# Prediction Route
@app.post("/predict")
async def predict_loan(data: LoanInput):

    # Simulate async work
    await asyncio.sleep(0.1)

    # Convert to DataFrame
    input_data = pd.DataFrame(
        [
            {
                "Dependents": data.Dependents,
                "ApplicantIncome": data.ApplicantIncome,
                "CoapplicantIncome": data.CoapplicantIncome,
                "LoanAmount": data.LoanAmount,
                "Loan_Amount_Term": data.Loan_Amount_Term,
                "Credit_History": data.Credit_History,
            }
        ]
    )

    # Scale Data
    scaled_data = scaler.transform(input_data)

    # Predict
    prediction = model.predict(scaled_data)[0]

    # Probability
    probability = model.predict_proba(scaled_data)[0][1]

    # Final Result
    result = "Approved" if prediction == 1 else "Rejected"

    return {"prediction": result, "approval_probability": round(float(probability), 2)}
