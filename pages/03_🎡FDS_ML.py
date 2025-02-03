import streamlit as st
import os

# FDS UI
from pyFraudDetection import fds_sidebar
from pyFraudDetection import read_markdown_file
from pyFraudDetection import read_from_files
from pyFraudDetection import is_weekend

# Customize the sidebar
fds_sidebar()

# hidden div with anchor
st.markdown("<div id='linkto_top'></div>", unsafe_allow_html=True) 
st.subheader("詐欺偵測機器學習 (FDS ML)")

# Tabs Menu
# `tab_eval` is a variable that is being used to create a tab in the
# Streamlit application interface. In this specific code snippet,
# `tab_eval` is being used as one of the tabs in the Streamlit app
# interface for the section titled "效能評估" (Performance Evaluation).
tab_fea_trans, tab_fds_ds, tab_eval, tab_ml  = st.tabs(["基線特徵轉換","FDS-決策樹機器學習", "效能評估", "標準機器學習法"])

# 基線特徵轉換-簡介
with tab_fea_trans:
    # reading markdown file
    intro_markdown = read_markdown_file(os.getcwd()+'/docs/FDS_0_Feature_Transformation.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)
    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)
    
    # reading markdown file
    intro_markdown = read_markdown_file(os.getcwd()+'/docs/FDS_1_LoadData.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)
    # 載入原始資料
    if st.button("Load raw Data"):
        DIR_INPUT=os.getcwd()+'/data/simulated-data-raw/' 

        BEGIN_DATE = "2024-04-01"
        END_DATE = "2024-09-30"

        #print("Load  files")
        transactions_df=read_from_files(DIR_INPUT, BEGIN_DATE, END_DATE)
        #st.write("{0} transactions loaded, containing {1} fraudulent transactions".format(len(transactions_df),transactions_df.TX_FRAUD.sum()))
        st.write("已載入 {0} 筆交易資料，其中包含 {1} 筆詐欺交易".format(len(transactions_df),transactions_df.TX_FRAUD.sum()))
        st.dataframe(transactions_df)
    
    # reading markdown file
    intro_markdown = read_markdown_file(os.getcwd()+'/docs/FDS_2_DateTime_Trans.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)
    transactions_df['TX_DURING_WEEKEND']=transactions_df.TX_DATETIME.apply(is_weekend)
    
    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)
    
    
    # reading markdown file
    intro_markdown = read_markdown_file(os.getcwd()+'/docs/FDS_3_CustID_Trans.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)
    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)
    
    
    # reading markdown file
    intro_markdown = read_markdown_file(os.getcwd()+'/docs/FDS_4_TermID_Trans.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)
    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)
    
    
    # reading markdown file
    intro_markdown = read_markdown_file(os.getcwd()+'/docs/FDS_5_SaveData.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)
    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)

# FDS-決策樹機器學習
with tab_fds_ds:
    # reading markdown file
    intro_markdown = read_markdown_file(os.getcwd()+'/docs/FDS_0_Feature_Transformation.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)
    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)
    
# 效能評估
with tab_eval:
    # reading markdown file
    intro_markdown = read_markdown_file(os.getcwd()+'/docs/FDS_0_Feature_Transformation.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)
    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)
    
# 標準機器學習法
with tab_ml:
    # reading markdown file
    intro_markdown = read_markdown_file(os.getcwd()+'/docs/FDS_0_Feature_Transformation.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)
    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)
    