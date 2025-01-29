import streamlit as st
from fds_subs import fds_sidebar

fds_sidebar()


# Customize page title
st.subheader("詐欺偵測教學應用系統(Fraud Detection Applications)")

st.markdown(
    """
    此應用程式展示了各種互動式網路應用程式，用以展示詐欺偵測手冊。
    """
)

st.subheader("請選擇左列功能列功能")

markdown = """
1. Theory-背景知識、理論與發展現況
2. Simulator-交易資料模擬器
3. 機器學習方法
4. 機器學習效能評估
5. 機器學習模型驗證與模型選擇
6. 非平衡資料演算法
7. 深度學習
8. Fraud Detection dashboard-詐欺偵測儀表板

"""

st.markdown(markdown)