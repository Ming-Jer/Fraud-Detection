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

    with st.expander("See source code"):
        with st.echo():
            n_customers = 5
            customer_profiles_table = generate_customer_profiles_table(n_customers, random_state = 0)

    st.write("產生的客戶資料")
    st.dataframe(customer_profiles_table)

    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)

with tab_terminal:
    
    st.write("例如，讓我們生成一個終端機資料表內含五個終端機：")
    n_terminals = 5
    terminal_profiles_table = generate_terminal_profiles_table(n_terminals, random_state = 0)
    st.dataframe(terminal_profiles_table)

    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)

with tab_terminal_list:
    
    st.write("舉例來說，讓我們取得最後一位客戶半徑$r=50$範圍內的終端機清單：")
    # We first get the geographical locations of all terminals as a numpy array
    x_y_terminals = terminal_profiles_table[['x_terminal_id','y_terminal_id']].values.astype(float)
    # And get the list of terminals within radius of $50$ for the last customer
    
    st.write(get_list_terminals_within_radius(customer_profiles_table.iloc[4], x_y_terminals=x_y_terminals, r=50))

    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)
