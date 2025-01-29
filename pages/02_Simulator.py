import streamlit as st
import pandas as pd
from shared_functions import generate_customer_profiles_table

n_customers = 5
customer_profiles_table = generate_customer_profiles_table(n_customers, random_state = 0)

st.dataframe(customer_profiles_table)