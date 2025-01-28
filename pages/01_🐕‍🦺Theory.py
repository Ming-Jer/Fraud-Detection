import os
import streamlit as st
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

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

tab_forward, tab_fds, tab_ml, tab_ref, tab_ad = st.tabs(["前言", "詐欺偵測", "機器學習","參考文獻", "異常偵測範例"])
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

with tab_ad:
    markdown="""
    #### 線性異常偵測範例 Linear Anomaly Detection Example
    - 假設單一陣列/列表中包含某一群體的智商分數分布 Assuming a single array/list of data contains a distribution of IQ scores within a given population
    """
    st.markdown(markdown)

    mu, sigma = 100, 10
    s = np.random.normal(mu, sigma, 1000)
    fig, ax = plt.subplots()
    ax.hist(s, 40)
    st.pyplot(fig)

    markdown="""
    #### Box Plot
    - 「最小值」：第25百分位數 - (1.5 × 四分位距)
    - 四分位距：第25至第75百分位數的範圍
    - 中位數
    - 「最大值」：第75百分位數 + (1.5 × 四分位距)
    - 離群值落在「最大值」之上或「最小值」之下
    """
    st.markdown(markdown)

    fig, ax = plt.subplots()
    ax.boxplot(s)
    st.pyplot(fig)

    markdown="""
    - 雖然這些技術適用於一維資料（即單一欄位），但在高維度的情況下，這些方法就變得過於複雜。While these techniques work for 1d data i.e. single columns, the higher-dimensional case is too complicated for these approaches.
    - 因此需要採用非線性方法，因為我們必須確定特徵空間中不同欄位的資料如何相互作用，從而增強方法的預測能力。A non-linear approach is therefore required, as we need to determine how the data from different columns in the feature space interacts with each other, adding to the predictive ability of the approach.

    """
    st.markdown(markdown)

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