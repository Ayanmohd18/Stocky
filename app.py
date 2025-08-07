import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model  # type: ignore
import matplotlib.pyplot as plt

# Load your trained model
model = load_model("stock_dl_model.h5")


# Preprocess input (update this to match your real notebook's logic)
def preprocess_input(data):
    data = np.array(data).reshape(1, 60, 1)
    return data


# App title and description
st.set_page_config(page_title="Stock Price Prediction", layout="centered")
st.title("📈 Stock Price Predictor")
st.write(
    "Provide stock closing prices for the last 60 days to predict the next day's price."
)

# Tabs for input method
tab1, tab2 = st.tabs(["🔢 Text Input", "🎛️ Slider Input"])

input_data = []

with tab1:
    st.subheader("Enter 60 comma-separated values")
    raw_input = st.text_area("Input prices (e.g., 101.5, 102.3, ...):")
    if raw_input:
        try:
            input_data = [float(x) for x in raw_input.split(",")]
            if len(input_data) != 60:
                st.warning("Please enter exactly 60 values.")
                input_data = []
        except ValueError:
            st.error("Invalid input: Please ensure all values are numbers.")

with tab2:
    st.subheader("Adjust sliders for 60 days")
    cols = st.columns(6)
    input_data = []
    for i in range(60):
        col = cols[i % 6]
        val = col.number_input(
            f"Day {i + 1}", min_value=0.0, value=100.0, step=1.0, key=f"day_{i}"
        )
        input_data.append(val)

# Predict button
if st.button("🔍 Predict Next Price"):
    if len(input_data) == 60:
        processed = preprocess_input(input_data)
        prediction = model.predict(processed)
        predicted_price = prediction[0][0]
        st.success(f"📊 Predicted Next Day Price: **${predicted_price:.2f}**")

        # Optional chart
        st.subheader("📉 Input Trend + Prediction")
        fig, ax = plt.subplots()
        ax.plot(range(1, 61), input_data, label="Past 60 Days")
        ax.scatter(61, predicted_price, color="red", label="Predicted Next Day")
        ax.set_xlabel("Days")
        ax.set_ylabel("Price")
        ax.legend()
        st.pyplot(fig)
    else:
        st.warning("Please provide exactly 60 values for prediction.")
