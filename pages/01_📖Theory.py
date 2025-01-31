import os
import streamlit as st
import numpy as np

import matplotlib.pyplot as plt

#from fds_subs import read_markdown_file
#from fds_subs import fds_sidebar
from pyFraudDetection.fds_utils.fds_UI import read_markdown_file
from pyFraudDetection.fds_utils.fds_UI import fds_sidebar


# Customize the sidebar
fds_sidebar()

# hidden div with anchor
st.markdown("<div id='linkto_top'></div>", unsafe_allow_html=True) 

st.subheader("詐欺偵測簡介 (Introduction to Fraud Detection)")

tab_forward, tab_cfs, tab_fds, tab_ml, tab_ref, tab_ad = st.tabs(["前言", "詐欺偵測場景", "詐欺偵測簡介",  "機器學習","參考文獻", "異常偵測範例"])
with tab_forward:
    st.image("./images/MIT-Fraud-Detection-PRESS.jpg", caption="Fraud Detection")
    # reading markdown file
    cwd = os.getcwd()
    intro_markdown = read_markdown_file(cwd+'/docs/Forward.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)

    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)

with tab_cfs:
    st.image("https://www.ecb.europa.eu/press/pr/date/2024/html/pr240801/ecb.pr240801.en_img0.png?0efabbbc959966f70a934562aab5df1f", 
             caption="各類支付工具的詐欺絕對值與相對水平")
    st.write("（左軸：詐欺總額（百萬歐元）；右軸：詐欺金額佔交易總額的比例）資料來源：歐洲經濟區支付服務提供商（不包括列支敦斯登，因其報告參考期僅始於2022年下半年）。")

    # reading markdown file
    cwd = os.getcwd()
    intro_markdown = read_markdown_file(cwd+'/docs/FraudDetection.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)

    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)

with tab_fds:
    st.image("./images/FDS.jpg", caption="Anomaly Detection")
    # reading markdown file
    cwd = os.getcwd()
    intro_markdown = read_markdown_file(cwd+'/docs/FDS.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)

    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)

with tab_ml:
    st.image("./images/baseline_ML_workflow.png", caption="CCFS ML")
    st.write("信用卡詐欺偵測的機器學習基線方法，以及最近關於該主題的調查中提出的大多數方法。")
    # reading markdown file
    cwd = os.getcwd()
    intro_markdown = read_markdown_file(cwd+'/docs/Lecture_ML.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)

    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)

with tab_ref:
    # reading markdown file
    cwd = os.getcwd()
    intro_markdown = read_markdown_file(cwd+'/docs/References.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)

    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)

with tab_ad:
    st.image("./images/anomaly_detection.png", caption="Anomaly Detection")
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

    # add the link at the bottom of each page    
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)