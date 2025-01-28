import streamlit as st
from pathlib import Path
import os

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

# Customize the sidebar
markdown = """
[信用卡詐欺偵測之可重製機器學習 - 實務手冊 (Reproducible Machine Learning for Credit Card Fraud Detection - Practical Handbook)](https://fraud-detection-handbook.github.io/fraud-detection-handbook/Foreword.html)
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "./images/MIT-Fraud-Detection-PRESS.jpg"
st.sidebar.image(logo)

'''
# creating threshold slider
st.title("詐欺偵測簡介 (Introduction to Fraud Detection)")

markdown = """
1. 什麼是異常偵 Lecture (What is Anomaly Detection)
"""
st.header(markdown)
'''

# reading markdown file
cwd = os.getcwd()
intro_markdown = read_markdown_file(cwd+'/docs/Lecture1.md')
st.markdown(intro_markdown, unsafe_allow_html=True)