#from eval import get_metrics_df
import streamlit as st
import pandas as pd
import os

#from fds_subs import get_metrics_df
#from fds_subs import fds_sidebar
from pyFraudDetection.fds_utils.fds_modules import get_metrics_df
from pyFraudDetection.fds_utils.fds_UI import fds_sidebar

# Customize the sidebar
fds_sidebar()

# creating threshold slider
st.title("詐欺偵測儀表板 (Fraud Detection dashboard)")
st.markdown("### 建立一個有效的機器學習應用程式以偵測金融犯罪案例。")

# reading csv
cwd = os.getcwd()
error_df = pd.read_csv(cwd+'/data/error_df.csv')
error_df.columns = ['Index', 'Target variable', 'Score']
error_df = error_df[['Target variable', 'Score']]

tab_dashboard, tab_performance = st.tabs(["Dashboard", "Performance"])

with tab_dashboard:
    threshold = st.slider("Threshold (default of 50%)", min_value=0.00, max_value=1.00, step=0.05, value=0.50)
    threshold_df, metrics, metrics_default = get_metrics_df(error_df, threshold=threshold)
    # input box for cost, then display total cost of fraud
    number1 = st.number_input('正確偵測詐欺的成本(真陽性) (Cost of correctly detecting fraud)') # true positive
    number2 = st.number_input('將正常交易錯誤分類為詐欺的成本(假陽性) (Cost of incorrectly classifying normal transactions as fraudulent)') # false positive
    number3 = st.number_input('未能偵測詐欺交易的成本(假陰性)(Cost of not detecting transactions)') # false negative
    number4 = st.number_input('正確偵測正常交易的成本 (真陰性) (Cost of correctly detecting normal transactions)') # true negative

    # setting cost defaults
    tp_default = 0
    fp_default = 0
    fn_default = 0
    tn_default = 0

    for i, row in threshold_df.iterrows():
        if row['Target variable'] == 1 and row['Classification_default'] == 1:
            tp_default += 1
        elif row['Target variable'] == 0 and row['Classification_default'] == 1:
            fp_default += 1
        elif row['Target variable'] == 1 and row['Classification_default'] == 0:
            fn_default += 1
        elif row['Target variable'] == 0 and row['Classification_default'] == 0:
            tn_default += 1

    st.write('The default cost of fraud is ', (number1 * tp_default) + (number2 * fp_default) + (number3 * fn_default) + (number4 * tn_default))

    tp = 0
    fp = 0
    fn = 0
    tn = 0

    for i, row in threshold_df.iterrows():
        if row['Target variable'] == 1 and row['Classification'] == 1:
            tp += 1
        elif row['Target variable'] == 0 and row['Classification'] == 1:
            fp += 1
        elif row['Target variable'] == 1 and row['Classification'] == 0:
            fn += 1
        elif row['Target variable'] == 0 and row['Classification'] == 0:
            tn += 1

    st.write('The updated cost of fraud is ', (number1 * tp) + (number2 * fp) + (number3 * fn) + (number4 * tn))
with tab_performance:
    # updated
    metrics.loc[len(metrics.index)] = ['Number of fraudulent transactions detected', tp, '']
    metrics.loc[len(metrics.index)] = ['Number of fraudulent transactions not detected', fn, '']
    metrics.loc[len(metrics.index)] = ['Number of good transactions classified as fraudulent', fp, '']
    metrics.loc[len(metrics.index)] = ['Number of good transactions classified as good', tn, '']
    metrics.loc[len(metrics.index)] = ['Total number of transactions assessed', tp + fp + fn + tn, '']
    st.dataframe(metrics.assign(hack="").set_index("hack"))

    # default
    metrics_default.loc[len(metrics_default.index)] = ['Number of fraudulent transactions detected', tp_default, '']
    metrics_default.loc[len(metrics_default.index)] = ['Number of fraudulent transactions not detected', fn_default, '']
    metrics_default.loc[len(metrics_default.index)] = ['Number of good transactions classified as fraudulent', fp_default, '']
    metrics_default.loc[len(metrics_default.index)] = ['Number of good transactions classified as good', tn_default, '']
    metrics_default.loc[len(metrics_default.index)] = ['Total number of transactions assessed', tp_default + fp_default + fn_default + tn_default, '']
    st.dataframe(metrics_default.assign(hack="").set_index("hack"))