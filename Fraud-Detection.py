import streamlit as st


# Customize the sidebar
markdown = """
[Reproducible Machine Learning for Credit Card Fraud Detection - Practical Handbook](https://fraud-detection-handbook.github.io/fraud-detection-handbook/Foreword.html)
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "./images/MIT-Fraud-Detection-PRESS.jpg"
st.sidebar.image(logo)


# Customize page title
st.title("詐欺偵測程式(Fraud Detection Applications)")

st.markdown(
    """
    此應用程式展示了各種互動式網路應用程式，用以展示詐欺偵測手冊。This application demonstrates various interactive web apps that showcase the Fraud Detection Handbook.
    """
)

st.header("請選擇左列功能列功能")

markdown = """
1. 背景知識、理論與發展現況
2. 交易資料模擬器
3. 機器學習效能評估
4. 機器學習模型驗證與模型選擇
5. 非平衡資料演算法
6. 深度學習
7. 詐欺偵測Dashboard

"""

st.markdown(markdown)