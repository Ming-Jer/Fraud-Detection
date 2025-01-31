import streamlit as st
import pandas as pd
import os
import numpy as np


import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid', {'axes.facecolor': '0.9'})

from pyFraudDetection import fds_sidebar
from pyFraudDetection import read_markdown_file
from pyFraudDetection import generate_customer_profiles_table
from pyFraudDetection import generate_terminal_profiles_table
from pyFraudDetection import get_list_terminals_within_radius
from pyFraudDetection import generate_transactions_table
from pyFraudDetection import generate_dataset
from pyFraudDetection import add_frauds
from pyFraudDetection import get_stats

from pyFraudDetection import sim_tab_intro
from pyFraudDetection import sim_tab_customer
from pyFraudDetection import sim_tab_terminal
from pyFraudDetection import sim_tab_list


# Customize the sidebar
fds_sidebar()

# hidden div with anchor
st.markdown("<div id='linkto_top'></div>", unsafe_allow_html=True) 
st.subheader("交易資料模擬器 (Transaction data simulator)")

# Tabs Menu
tab_intro, tab_customer, tab_terminal, tab_list, tab_trans, tab_scale, tab_fraud = st.tabs(["模擬器簡介","客戶資料", "終端機配置", "客戶與終端機關聯", "交易生成", "擴展交易資料","詐欺情境生成"])

# 交易資料模擬器-簡介
with tab_intro:
    sim_tab_intro()

# 交易資料模擬器-模擬客戶資料
with tab_customer:
    sim_tab_customer()

# 交易資料模擬器-模擬終端機配置
with tab_terminal:
    sim_tab_terminal()
    
# 交易資料模擬器-客戶與終端機關聯
with tab_list:
    sim_tab_list()

with tab_trans:
    # reading markdown file
    intro_markdown = read_markdown_file(os.getcwd()+'/docs/Simulator_transactions.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)

    with st.expander("顯示原始碼 See Source Code"):
        with st.echo():
            transaction_table_customer_0=generate_transactions_table(customer_profiles_table.iloc[0], 
                                                                start_date = "2018-04-01", 
                                                                nb_days = 5)
            st.dataframe(transaction_table_customer_0, hide_index = True)

    st.dataframe(transaction_table_customer_0, hide_index = True)

    intro_markdown="""
    現在讓我們為所有客戶生成交易。這可以使用pandas的`groupby`和`apply`方法輕鬆完成：
    這樣我們就得到了一組包含5位客戶、5個終端機、5天期間內共65筆交易的資料集。
    """
    st.markdown(intro_markdown, unsafe_allow_html=True)
    with st.expander("顯示原始碼 See Source Code"):
        with st.echo():
            transactions_df=customer_profiles_table.groupby('CUSTOMER_ID').apply(lambda x : generate_transactions_table(x.iloc[0], nb_days=5)).reset_index(drop=True)
            st.dataframe(transactions_df, hide_index = True)
            
    st.dataframe(transactions_df, hide_index = True)

    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)

with tab_scale:
    # reading markdown file
    intro_markdown = read_markdown_file(os.getcwd()+'/docs/Simulator_Scale_transcation.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)

    intro_markdown="""
    可選擇模擬資料規模說明:
    - 中等資料 (500位客戶、1,000個終端機、18天(17,067筆交易資料)
    - 真實資料 (5,000位客戶、10,000個終端機、183天(1,754,155筆交易資料)
    """
    st.markdown(intro_markdown, unsafe_allow_html=True)

    #s_customers=500
    #s_terminals=1000
    #s_nb_days=18
    options = st.selectbox(
        "選擇模擬資料規模",
        ("中等資料", "真實資料"),index=0,
    )

    with st.expander("顯示原始碼 See Source Code"):
        with st.echo():
            if (options=="中等資料"):
                s_customers=500
                s_terminals=1000
                s_nb_days=18
            elif (options=="真實資料"):
                s_customers = 5000
                s_terminals = 10000
                s_nb_days=183

            st.write("You selected:", options, s_customers, s_terminals, s_nb_days)
            (customer_profiles_table, terminal_profiles_table, transactions_df)=\
                generate_dataset(n_customers = s_customers,
                     n_terminals = s_terminals, 
                     nb_days=s_nb_days, 
                     start_date="2024-04-01", 
                     r=5)
            st.dataframe(transactions_df, hide_index = True)

    st.dataframe(transactions_df, hide_index = True)
    st.write(transactions_df.shape)

    st.write("為了進行合理性檢查，繪製交易金額和交易時間的分布圖。")
    with st.expander("顯示原始碼 See Source Code"):
        with st.echo():
            distribution_amount_times_fig, ax = plt.subplots(1, 2, figsize=(18,4))

            amount_val = transactions_df[transactions_df.TX_TIME_DAYS<10]['TX_AMOUNT'].sample(n=s_terminals).values
            time_val = transactions_df[transactions_df.TX_TIME_DAYS<10]['TX_TIME_SECONDS'].sample(n=s_terminals).values

            sns.distplot(amount_val, ax=ax[0], color='r', hist = True, kde = False)
            ax[0].set_title('Distribution of transaction amounts', fontsize=14)
            ax[0].set_xlim([min(amount_val), max(amount_val)])
            ax[0].set(xlabel = "Amount", ylabel="Number of transactions")

            # We divide the time variables by 86400 to transform seconds to days in the plot
            sns.distplot(time_val/86400, ax=ax[1], color='b', bins = 100, hist = True, kde = False)
            ax[1].set_title('Distribution of transaction times', fontsize=14)
            ax[1].set_xlim([min(time_val/86400), max(time_val/86400)])
            ax[1].set_xticks(range(10))
            ax[1].set(xlabel = "Time (days)", ylabel="Number of transactions")
            st.pyplot(distribution_amount_times_fig)

    st.pyplot(distribution_amount_times_fig)
    st.write("交易金額的分布主要集中在小額交易；而交易時間的分布則呈現以正午為中心的每日高斯分布。這兩種分布都符合先前章節中使用的模擬參數設定。")

    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)

with tab_fraud:

    with st.expander("顯示原始碼 See Source Code"):
        with st.echo():
            transactions_df = add_frauds(customer_profiles_table, terminal_profiles_table, transactions_df)
            st.dataframe(transactions_df, hide_index = True)

            st.write("Percentage of fraudulent transactions: ",transactions_df.TX_FRAUD.mean())
            st.write("Number of fraudulent transactions: ", transactions_df.TX_FRAUD.sum())
            st.write("三種詐欺情境數量")
            st.write(transactions_df[transactions_df.TX_FRAUD_SCENARIO==1].shape)
            st.write(transactions_df[transactions_df.TX_FRAUD_SCENARIO==2].shape)
            st.write(transactions_df[transactions_df.TX_FRAUD_SCENARIO==3].shape)

    with st.expander("顯示原始碼 See Source Code"):
        with st.echo():
            (nb_tx_per_day,nb_fraud_per_day,nb_fraudcard_per_day)=get_stats(transactions_df)

            n_days=len(nb_tx_per_day)
            tx_stats=pd.DataFrame({"value":pd.concat([nb_tx_per_day/50,nb_fraud_per_day,nb_fraudcard_per_day])})
            tx_stats['stat_type']=["nb_tx_per_day"]*n_days+["nb_fraud_per_day"]*n_days+["nb_fraudcard_per_day"]*n_days
            tx_stats=tx_stats.reset_index()

    with st.expander("顯示原始碼 See Source Code"):
        with st.echo():
            sns.set(style='darkgrid')
            sns.set(font_scale=1.4)

            fraud_and_transactions_stats_fig = plt.gcf()

            fraud_and_transactions_stats_fig.set_size_inches(15, 8)

            sns_plot = sns.lineplot(x="TX_TIME_DAYS", y="value", data=tx_stats, hue="stat_type", hue_order=["nb_tx_per_day","nb_fraud_per_day","nb_fraudcard_per_day"], legend=False)

            sns_plot.set_title('Total transactions, and number of fraudulent transactions \n and number of compromised cards per day', fontsize=20)
            sns_plot.set(xlabel = "Number of days since beginning of data generation", ylabel="Number")

            sns_plot.set_ylim([0,300])

            labels_legend = ["# transactions per day (/50)", "# fraudulent txs per day", "# fraudulent cards per day"]

            sns_plot.legend(loc='upper left', labels=labels_legend,bbox_to_anchor=(1.05, 1), fontsize=15)
            st.pyplot(fraud_and_transactions_stats_fig)

    st.dataframe(transactions_df, hide_index = True)
    st.pyplot(fraud_and_transactions_stats_fig)

    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)