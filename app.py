import streamlit as st
import pandas as pd
import joblib

# Load saved model and scaler
kmeans = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("🛍️ Customer Segmentation")
st.write("Find the customer segment using income and spending score.")

# User inputs
income = st.number_input(
    "Annual Income ($)",
    min_value=0,
    max_value=200000,
    value=90000,
    step=1000
)

score = st.slider(
    "Spending Score",
    min_value=1,
    max_value=100,
    value=85
)

if st.button("Predict Customer Segment"):

    customer = pd.DataFrame({
        "Annual Income (k$)": [income / 1000],
        "Spending Score (1-100)": [score]
    })

    customer_scaled = scaler.transform(customer)
    cluster = int(kmeans.predict(customer_scaled)[0])

    segments = {
        0: "Average Income - Average Spending",
        1: "High Income - High Spending",
        2: "Low Income - High Spending",
        3: "High Income - Low Spending",
        4: "Low Income - Low Spending"
    }

    st.success(f"Predicted Cluster: {cluster}")
    st.write("Customer Segment:", segments[cluster])