import streamlit as st

# Customize the sidebar
markdown = """
[信用卡詐欺偵測之可重製機器學習 - 實務手冊 (Reproducible Machine Learning for Credit Card Fraud Detection - Practical Handbook)](https://fraud-detection-handbook.github.io/fraud-detection-handbook/Foreword.html)
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "./images/MIT-Fraud-Detection-PRESS.jpg"
st.sidebar.image(logo)

# creating threshold slider
st.title("詐欺偵測簡介 (Introduction to Fraud Detection)")

markdown = """
## 第一講：什麼是異常偵 Lecture 1: What is Anomaly Detection
![Anomaly detection]("./images/anomaly_detection.png" "Anomaly detection")
"""
st.header(markdown)