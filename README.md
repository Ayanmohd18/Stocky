Stocky-Your smart companion for next-day stock price predictions.
Just feed in the last 60 days of stock prices — Stocky does the thinking so you don’t have to.

📈 Stock Price Prediction using Deep Learning

This project is a mini AI/ML application that predicts the next day's stock price using the past 60 days of closing prices. The application is built using a trained deep learning model (LSTM/Conv1D or similar), integrated into a Streamlit web interface for easy user interaction.

🚀 Features

✅ Predicts stock prices using a pre-trained Keras model (stock_dl_model.h5)

🎛️ Two input modes:

Text area (comma-separated values)

Slider-based input (interactive per-day value entry)

📊 Visualizes the 60-day trend and predicted price on a line chart

🧠 Uses deep learning for time-series forecasting

🧠 Model Overview

The model is trained on historical stock data (powergrid.csv) using deep learning techniques (BiLSTM or similar)

Model Input Shape: (1, 60, 1) – 60 time steps of single features

Output: Predicted price for the next day

📂 File Structure

.
├── app.py                  # Streamlit web app

├── stock_dl_model.h5       # Trained deep learning model

├── powergrid.csv           # Source dataset (used for training)

├── Stock Price Prediction.ipynb  # Jupyter Notebook for model development

└── README.md               # Project documentation

🛠️ Installation

1. Clone the repository

git clone 
cd stock-price-prediction

2. Install Dependencies
3. 
Make sure you have Python 3.8+ installed. Then run:

pip install -r requirements.txt
Or install manually:

pip install streamlit tensorflow matplotlib numpy

▶️ Run the Application

Start the Streamlit app:
streamlit run app.py
Then open the URL shown in the terminal (usually http://localhost:8501) in your browser.

📌 Usage

Input 60 past closing stock prices using:

The text box (comma-separated), or

Sliders for each day’s price

Click 🔍 Predict Next Price

View the predicted next day price and trend visualization


📚 Project Motivation

This project demonstrates the practical use of deep learning (e.g., LSTM, BiLSTM) in financial forecasting. It's built as part of an academic mini-project for hands-on experience in:

Time-series prediction

Model deployment using Streamlit

Interactive UI development for ML applications

📎 Requirements

Python 3.8+

TensorFlow 2.x

Streamlit

NumPy

Matplotlib

🤝 Credits
Dataset: [Yahoo Finance / Kaggle / Custom Dataset]

