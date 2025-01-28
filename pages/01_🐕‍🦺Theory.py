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

st.subheader("詐欺偵測簡介 (Introduction to Fraud Detection)")

tab_forward, tab_cfs, tab_fds, tab_ml, tab_ref, tab_ad = st.tabs(["前言", "詐欺偵測場景", "詐欺偵測", "機器學習","參考文獻", "異常偵測範例"])
with tab_forward:
    st.image("./images/MIT-Fraud-Detection-PRESS.jpg", caption="Fraud Detection")
    # reading markdown file
    cwd = os.getcwd()
    intro_markdown = read_markdown_file(cwd+'/docs/Forward.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)

with tab_cfs:
    st.image("./images/SEPA_FraudVolumePerType.png", caption="Fraud Volume")
    st.write("使用在 SEPA 內發行的卡進行的信用卡欺詐總價值的演變。無卡欺詐(圖中黃色部分)佔報告的欺詐的大部分。")
    st.image("./images/SEPA_FraudType_CardPresent.png", caption="Fraud Type")
    st.write("SEPA 內按類別劃分的持卡欺詐價值的演變和細分。")

    # reading markdown file
    cwd = os.getcwd()
    intro_markdown = read_markdown_file(cwd+'/docs/FraudDetection.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)

with tab_fds:
    st.image("./images/anomaly_detection.png", caption="Anomaly Detection")
    # reading markdown file
    cwd = os.getcwd()
    intro_markdown = read_markdown_file(cwd+'/docs/FDS.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)

with tab_ml:
    st.image("./images/baseline_ML_workflow.png", caption="CCFS ML")
    st.write("信用卡詐欺偵測的機器學習基線方法，以及最近關於該主題的調查中提出的大多數方法。")
    # reading markdown file
    cwd = os.getcwd()
    intro_markdown = read_markdown_file(cwd+'/docs/Lecture_ML.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)

with tab_ref:
    # reading markdown file
    cwd = os.getcwd()
    intro_markdown = read_markdown_file(cwd+'/docs/References.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)

with tab_ad:
    markdown="""
    #### 單維度異常偵測範例 Simple Anomaly Detection Example
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
    - 雖然這些技術適用於一維資料（即單一欄位），但高維度資料對這些方法而言，會變得太過複雜。While these techniques work for 1d data i.e. single columns, the higher-dimensional case is too complicated for these approaches.
    - 因此，我們需要採用非線性方法，以便了解特徵空間中不同欄位的資料如何相互影響，從而提升預測能力。A non-linear approach is therefore required, as we need to determine how the data from different columns in the feature space interacts with each other, adding to the predictive ability of the approach.

    """
    st.markdown(markdown)
