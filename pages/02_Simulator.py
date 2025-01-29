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

from fds_subs import generate_customer_profiles_table
from fds_subs import fds_sidebar
from fds_subs import read_markdown_file

# Customize the sidebar
fds_sidebar

# hidden div with anchor
st.markdown("<div id='linkto_top'></div>", unsafe_allow_html=True) 
st.subheader("交易資料模擬器 (Transaction data simulator)")
# reading markdown file
intro_markdown = read_markdown_file(os.getcwd()+'/docs/Simulator.md')
st.markdown(intro_markdown, unsafe_allow_html=True)

tab_customer, tab_terminal = st.tabs(["客戶資料", "終端機配置"])

with tab_customer:
    # reading markdown file
    intro_markdown = read_markdown_file(os.getcwd()+'/docs/Simulator_customer.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)

    n_customers = 5
    customer_profiles_table = generate_customer_profiles_table(n_customers, random_state = 0)

    st.dataframe(customer_profiles_table)