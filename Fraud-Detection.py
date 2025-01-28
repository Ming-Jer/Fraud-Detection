import streamlit as st


# Customize the sidebar
markdown = """
[信用卡詐欺偵測之可重製機器學習 - 實務手冊 (Reproducible Machine Learning for Credit Card Fraud Detection - Practical Handbook)](https://fraud-detection-handbook.github.io/fraud-detection-handbook/Foreword.html)
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "./images/MIT-Fraud-Detection-PRESS.jpg"
st.sidebar.image(logo)


# Customize page title
st.subheader("詐欺偵測程式(Fraud Detection Applications)")

st.markdown(
    """
    此應用程式展示了各種互動式網路應用程式，用以展示詐欺偵測手冊。This application demonstrates various interactive web apps that showcase the Fraud Detection Handbook.
    """
)

st.subheader("請選擇左列功能列功能")

markdown = """
1. Theory 背景知識、理論與發展現況
2. 交易資料模擬器
3. 機器學習方法
4. 機器學習效能評估
5. 機器學習模型驗證與模型選擇
6. 非平衡資料演算法
7. 深度學習
8. Fraud Detection dashboard 詐欺偵測儀表板

"""

st.markdown(markdown)