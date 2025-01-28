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

st.header("詐欺偵測簡介 (Introduction to Fraud Detection)")

tab_forward, tab_fds, tab_ml, tab_ref = st.tabs(["前言", "詐欺偵測", "機器學習","參考文獻"])
with tab_forward:
    st.image("./images/MIT-Fraud-Detection-PRESS.jpg", caption="Fraud Detection")
    # reading markdown file
    cwd = os.getcwd()
    intro_markdown = read_markdown_file(cwd+'/docs/Forward.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)

with tab_fds:
    st.image("./images/anomaly_detection.png", caption="Anomaly Detection")
    # reading markdown file
    cwd = os.getcwd()
    intro_markdown = read_markdown_file(cwd+'/docs/FDS.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)

with tab_ml:
    # reading markdown file
    cwd = os.getcwd()
    intro_markdown = read_markdown_file(cwd+'/docs/Lecture_ML.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)

with tab_ref:
    # reading markdown file
    cwd = os.getcwd()
    intro_markdown = read_markdown_file(cwd+'/docs/References.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)