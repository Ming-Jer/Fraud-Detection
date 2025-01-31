
from pathlib import Path
import streamlit as st


# 讀取Markdown文件
def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

# Customize the sidebar
def fds_sidebar():
    markdown = """
    [信用卡詐欺偵測之可重製機器學習 - 實務手冊 (Reproducible Machine Learning for Credit Card Fraud Detection - Practical Handbook)](https://fraud-detection-handbook.github.io/fraud-detection-handbook/Foreword.html)
    """

    st.sidebar.title("About")
    st.sidebar.info(markdown)
    logo = "./images/MIT-Fraud-Detection-PRESS.jpg"
    st.sidebar.image(logo)
