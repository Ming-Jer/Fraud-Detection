import streamlit as st
import pandas as pd
import os
import numpy as np


import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid', {'axes.facecolor': '0.9'})

from fds_subs import fds_sidebar
from fds_subs import read_markdown_file
from fds_subs import generate_customer_profiles_table
from fds_subs import generate_terminal_profiles_table
from fds_subs import get_list_terminals_within_radius
from fds_subs import generate_transactions_table
from fds_subs import generate_dataset


# Customize the sidebar
fds_sidebar()

# hidden div with anchor
st.markdown("<div id='linkto_top'></div>", unsafe_allow_html=True) 
st.subheader("交易資料模擬器 (Transaction data simulator)")

# Tabs Menu
tab_intro, tab_customer, tab_terminal, tab_list, tab_trans, tab_scale = st.tabs(["模擬器簡介","客戶資料", "終端機配置", "客戶與終端機關聯", "交易生成", "擴展交易資料"])

with tab_intro:
    # reading markdown file
    intro_markdown = read_markdown_file(os.getcwd()+'/docs/Simulator.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)
    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)


with tab_customer:
    # reading markdown file
    intro_markdown = read_markdown_file(os.getcwd()+'/docs/Simulator_customer.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)

    st.write("產生的客戶資料")
    with st.expander("顯示原始碼 See Source Code"):
        with st.echo():
            n_customers = 5
            customer_profiles_table = generate_customer_profiles_table(n_customers, random_state = 0)
            st.dataframe(customer_profiles_table, hide_index = True)
            
    st.dataframe(customer_profiles_table, hide_index = True)
    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)

with tab_terminal:
    # reading markdown file
    intro_markdown = read_markdown_file(os.getcwd()+'/docs/Simulator_terminal.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)

    with st.expander("顯示原始碼 See Source Code"):
        with st.echo():
            n_terminals = 5
            terminal_profiles_table = generate_terminal_profiles_table(n_terminals, random_state = 0)
            st.dataframe(terminal_profiles_table, hide_index = True)

    st.dataframe(terminal_profiles_table, hide_index = True)

    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)

with tab_list:
    # reading markdown file
    intro_markdown = read_markdown_file(os.getcwd()+'/docs/Simulator_list_terminal.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)

    with st.expander("顯示原始碼 See Source Code"):
        with st.echo():
            # We first get the geographical locations of all terminals as a numpy array
            x_y_terminals = terminal_profiles_table[['x_terminal_id','y_terminal_id']].values.astype(float)

            # And get the list of terminals within radius of $50$ for the last customer
            avaiale_terminials=get_list_terminals_within_radius(customer_profiles_table.iloc[4], x_y_terminals=x_y_terminals, r=50)
            
            st.write(avaiale_terminials[0], avaiale_terminials[1])
    
    st.write(avaiale_terminials[0], avaiale_terminials[1] )
    
    intro_markdown="""
    為了更好的視覺化，讓我們繪製
    - 所有終端機的位置（以紅色表示）
    - 最後一位客戶的位置（以藍色表示）
    - 第一位客戶半徑50範圍內的區域（以綠色表示）
    """
    st.markdown(intro_markdown, unsafe_allow_html=True)

    with st.expander("顯示原始碼 See Source Code"):
        with st.echo():
            terminals_available_to_customer_fig, ax = plt.subplots(figsize=(5,5))

            # Plot locations of terminals
            ax.scatter(terminal_profiles_table.x_terminal_id.values, 
                    terminal_profiles_table.y_terminal_id.values, 
                    color='blue', label = 'Locations of terminals')

            # Plot location of the last customer
            customer_id=4
            ax.scatter(customer_profiles_table.iloc[customer_id].x_customer_id, 
                    customer_profiles_table.iloc[customer_id].y_customer_id, 
                    color='red',label="Location of last customer")

            ax.legend(loc = 'upper left', bbox_to_anchor=(1.05, 1))

            # Plot the region within a radius of 50 of the last customer
            circ = plt.Circle((customer_profiles_table.iloc[customer_id].x_customer_id,
                            customer_profiles_table.iloc[customer_id].y_customer_id), radius=50, color='g', alpha=0.2)
            ax.add_patch(circ)

            fontsize=15

            ax.set_title("Green circle: \n Terminals within a radius of 50 \n of the last customer")
            ax.set_xlim([0, 100])
            ax.set_ylim([0, 100])
                
            ax.set_xlabel('x_terminal_id', fontsize=fontsize)
            ax.set_ylabel('y_terminal_id', fontsize=fontsize)
            st.pyplot(terminals_available_to_customer_fig)
    
    st.pyplot(terminals_available_to_customer_fig)

    intro_markdown="""
    使用 pandas 的 `apply` 函式來計算每位客戶可用的終端機清單相當簡單直觀。我們將結果儲存為客戶檔案表中的新欄位 `available_terminals`。
    值得注意的是，半徑 $r$ 控制了每位客戶平均可用的終端機數量。隨著終端機數量的增加，應該調整此半徑以符合模擬中期望的每位客戶平均可用終端機數量。
    """
    st.markdown(intro_markdown, unsafe_allow_html=True)
    with st.expander("顯示原始碼"):
        with st.echo():
            customer_profiles_table['available_terminals']=customer_profiles_table.apply(lambda x : get_list_terminals_within_radius(x, x_y_terminals=x_y_terminals, r=50), axis=1)
            st.dataframe(customer_profiles_table, hide_index = True)
    
    st.dataframe(customer_profiles_table, hide_index = True)

    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)

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
    - 基本資料 (5位客戶、5個終端機、5天(65筆交易資料)
    - 中等資料 (500位客戶、1,000個終端機、18天(65筆交易資料)
    - 真實資料 (5,000位客戶、10,000個終端機、183天(1,754,155筆交易資料)
    """
    st.markdown(intro_markdown, unsafe_allow_html=True)

    nc1=5
    nt1=5
    nd1=5
    options = st.selectbox(
        "選擇模擬資料規模",
        ("基本資料", "中等資料", "真實資料"),index=0,
    )

    with st.expander("顯示原始碼 See Source Code"):
        with st.echo():
            if (options=="基本資料"):
                nc1=5
                nt1=5
                nd1=5
            elif (options=="中等資料"):
                nc1=500
                nt1=1000
                nd1=18
            elif (options=="真實資料"):
                nc1 = 5000
                nt1 = 10000
                nd1=183

            st.write("You selected:", options, nc1, nt1, nd1)
            (customer_profiles_table, terminal_profiles_table, transactions_df)=\
                generate_dataset(n_customers = nc1,
                     n_terminals = nt1, 
                     nb_days=nd1, 
                     start_date="2024-04-01", 
                     r=5)
            st.dataframe(transactions_df, hide_index = True)

    st.dataframe(transactions_df, hide_index = True)
    st.write(transactions_df.shape)


    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)