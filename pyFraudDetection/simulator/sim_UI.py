
from pathlib import Path
import streamlit as st
import os


from pyFraudDetection.fds_utils.fds_UI import read_markdown_file


"""
交易資料模擬器-使用者介面套件
"""
#
# 交易資料模擬器-簡介功能
def sim_tab_intro():
    # reading markdown file
    intro_markdown = read_markdown_file(os.getcwd()+'/docs/Simulator.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)
    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)