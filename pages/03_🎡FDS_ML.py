import streamlit as st
import os

# FDS UI
from pyFraudDetection import fds_sidebar
from pyFraudDetection import read_markdown_file
from pyFraudDetection import read_from_files
from pyFraudDetection import is_weekend
from pyFraudDetection import is_night
from pyFraudDetection import get_customer_spending_behaviour_features
from pyFraudDetection import get_count_risk_rolling_window


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

# 3. 基線特徵轉換-簡介
with tab_fea_trans:
    # reading markdown file
    intro_markdown = read_markdown_file(os.getcwd()+'/docs/FDS_0_Feature_Transformation.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)
    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)
    
    # reading markdown file
    intro_markdown = read_markdown_file(os.getcwd()+'/docs/FDS_1_LoadData.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)
    #
    # 3.1 載入原始資料

    if st.button("Load raw Data"):
        DIR_INPUT=os.getcwd()+'/data/simulated-data-raw/' 

        BEGIN_DATE = "2024-04-01"
        END_DATE = "2024-09-30"

        #print("Load  files")
        transactions_df=read_from_files(DIR_INPUT, BEGIN_DATE, END_DATE)
        #st.write("{0} transactions loaded, containing {1} fraudulent transactions".format(len(transactions_df),transactions_df.TX_FRAUD.sum()))
        st.write("已載入 {0} 筆交易資料，其中包含 {1} 筆詐欺交易".format(len(transactions_df),transactions_df.TX_FRAUD.sum()))
        st.dataframe(transactions_df)
        
    
        #
        # 3.2 日期時間特徵轉換
        # reading markdown file
        intro_markdown = read_markdown_file(os.getcwd()+'/docs/FDS_2_DateTime_Trans.md')
        st.markdown(intro_markdown, unsafe_allow_html=True)
        with st.expander("顯示原始碼 See Source Code"):
            with st.echo():
                transactions_df['TX_DURING_WEEKEND']=transactions_df.TX_DATETIME.apply(is_weekend)
                transactions_df['TX_DURING_NIGHT']=transactions_df.TX_DATETIME.apply(is_night)

        intro_markdown="""
            讓我們檢查這些特徵是否已正確計算。
            2024年5月1日是星期三，而2024年9月29日是星期日。這些日期分別被正確標記為平日和週末。
            日夜特徵的設定也是正確的，第一筆交易發生在0點剛過後，最後一筆交易則發生在0點前不久。
            如頁面太窄，可以向右捲動欄位。
        """
        st.markdown(intro_markdown)
        st.dataframe(transactions_df[transactions_df.TX_TIME_DAYS>=30])
        # add the link at the bottom of each page
        st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)
        
        # 3.3 客戶ID轉換
        # reading markdown file
        intro_markdown = read_markdown_file(os.getcwd()+'/docs/FDS_3_CustID_Trans.md')
        st.markdown(intro_markdown, unsafe_allow_html=True)
        st.write("讓我們先為第一位客戶計算這些聚合值。")
        with st.expander("顯示原始碼 See Source Code"):
            with st.echo():
                spending_behaviour_customer_0=get_customer_spending_behaviour_features(transactions_df[transactions_df.CUSTOMER_ID==0])
                st.dataframe(spending_behaviour_customer_0)

        intro_markdown ="""
        我們可以驗證這些新特徵與客戶檔案是否一致（參見先前的筆記本）。
        對於客戶0，平均金額為`mean_amount`=62.26，每日交易頻率為`mean_nb_tx_per_day`=2.18。
        這些數值確實與特徵`CUSTOMER_ID_NB_TX_30DAY_WINDOW`和`CUSTOMER_ID_AVG_AMOUNT_30DAY_WINDOW`非常接近，特別是在30天後的數值。

        現在讓我們為所有客戶產生這些特徵。使用Pandas的`groupby`和`apply`方法可以輕鬆完成這項工作。
        """
        st.markdown(intro_markdown, unsafe_allow_html=True)
        with st.expander("顯示原始碼 See Source Code"):
            with st.echo():
                transactions_df=transactions_df.groupby('CUSTOMER_ID').apply(lambda x: get_customer_spending_behaviour_features(x, windows_size_in_days=[1,7,30]))
                transactions_df=transactions_df.sort_values('TX_DATETIME').reset_index(drop=True)
                st.dataframe(transactions_df)

        # add the link at the bottom of each page
        st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)
        
        # 
        # 3.4 終端機ID轉換
        # reading markdown file
        intro_markdown = read_markdown_file(os.getcwd()+'/docs/FDS_4_TermID_Trans.md')
        st.markdown(intro_markdown, unsafe_allow_html=True)
        st.dataframe(transactions_df[transactions_df.TX_FRAUD==1])
        
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
    