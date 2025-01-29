import streamlit as st
import pandas as pd
import os
import numpy as np
import datetime
import time
import random

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid', {'axes.facecolor': '0.9'})

from fds_subs import fds_sidebar
from fds_subs import read_markdown_file
from fds_subs import generate_customer_profiles_table
from fds_subs import generate_terminal_profiles_table
from fds_subs import get_list_terminals_within_radius


# Customize the sidebar
fds_sidebar()

# hidden div with anchor
st.markdown("<div id='linkto_top'></div>", unsafe_allow_html=True) 
st.subheader("交易資料模擬器 (Transaction data simulator)")

tab_intro, tab_customer, tab_terminal, tab_terminal_list = st.tabs(["模擬器簡介","客戶資料", "終端機配置", "客戶與終端機關聯"])

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
    with st.expander("顯示原始碼See Source Code"):
        with st.echo():
            n_customers = 5
            customer_profiles_table = generate_customer_profiles_table(n_customers, random_state = 0)
            
    st.dataframe(customer_profiles_table)
    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)

with tab_terminal:
    # reading markdown file
    intro_markdown = read_markdown_file(os.getcwd()+'/docs/Simulator_terminal.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)

    with st.expander("顯示原始碼See Source Code"):
        with st.echo():
            n_terminals = 5
            terminal_profiles_table = generate_terminal_profiles_table(n_terminals, random_state = 0)

    st.dataframe(terminal_profiles_table)

    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)

with tab_terminal_list:
    # reading markdown file
    intro_markdown = read_markdown_file(os.getcwd()+'/docs/Simulator_list_terminal.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)

    with st.expander("顯示原始碼"):
        with st.echo():
            # We first get the geographical locations of all terminals as a numpy array
            x_y_terminals = terminal_profiles_table[['x_terminal_id','y_terminal_id']].values.astype(float)
            # And get the list of terminals within radius of $50$ for the last customer
            get_list_terminals_within_radius(customer_profiles_table.iloc[4], x_y_terminals=x_y_terminals, r=50)
    
    intro_markdown="""
    為了更好的視覺化，讓我們繪製
    - 所有終端機的位置（以紅色表示）
    - 最後一位客戶的位置（以藍色表示）
    - 第一位客戶半徑50範圍內的區域（以綠色表示）
    """
    st.markdown(intro_markdown, unsafe_allow_html=True)

    with st.expander("顯示原始碼"):
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

    intro_markdown="""
    使用 panda 的 apply 函數來計算每個客戶可用的終端機清單相當簡單直接。我們將結果儲存為客戶資料表中的新欄位 available_terminals。
    """
    st.markdown(intro_markdown, unsafe_allow_html=True)
    with st.expander("顯示原始碼"):
        with st.echo():
            customer_profiles_table['available_terminals']=customer_profiles_table.apply(lambda x : get_list_terminals_within_radius(x, x_y_terminals=x_y_terminals, r=50), axis=1)
    
    st.dataframe(customer_profiles_table)

    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)
