import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.metrics import roc_auc_score, average_precision_score
import streamlit as st

# 讀取Markdown文件
def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

# Customize the sidebar
def fds_sidebar():
    markdown = """
    [信用卡詐欺偵測之可重製機器學習 - 實務手冊 (Reproducible Machine Learning for Credit Card Fraud Detection - Practical Handbook)](https://fraud-detection-handbook.github.io/fraud-detection-handbook/Foreword.html)
    """

    st.sidebar.title("About")
    st.sidebar.info(markdown)
    logo = "./images/MIT-Fraud-Detection-PRESS.jpg"
    st.sidebar.image(logo)

"""
Packages from Fraud Detection Handbook
"""
def get_metrics_df(error_df, threshold=0.50):

    yhat_default = np.where(error_df["Score"] >= 0.5, 1, 0)
    auc_score_default = roc_auc_score(error_df["Target variable"], yhat_default)
    ap_score_default = average_precision_score(error_df["Target variable"], yhat_default)
    error_df['Classification_default'] = yhat_default
    error_df['Default threshold'] = 0.5

    yhat = np.where(error_df["Score"] >= threshold, 1, 0)
    auc_score = roc_auc_score(error_df["Target variable"], yhat)
    ap_score = average_precision_score(error_df["Target variable"], yhat)
    error_df['Classification'] = yhat
    error_df['Updated threshold'] = threshold

    metrics_df = pd.DataFrame(
        {
            "Metric name": ["Area under the curve", "Average Precision", "Threshold"],
            "Score": [
                auc_score,
                ap_score,
                threshold
            ],
            "Cut-off score": [0.8, 0.01, ''],
        }
    )

    metrics_df_default = pd.DataFrame(
                {
                    "Metric name": ["Area under the curve", "Average Precision", "Threshold"],
                    "Score": [
                        auc_score_default,
                        ap_score_default,
                        0.50
                    ],
                    "Cut-off score": [0.8, 0.01, ''],
                }
            )

    return error_df, metrics_df, metrics_df_default

def generate_customer_profiles_table(n_customers, random_state=0):
    
    np.random.seed(random_state)
        
    customer_id_properties=[]
    
    # Generate customer properties from random distributions 
    for customer_id in range(n_customers):
        
        x_customer_id = np.random.uniform(0,100)
        y_customer_id = np.random.uniform(0,100)
        
        mean_amount = np.random.uniform(5,100) # Arbitrary (but sensible) value 
        std_amount = mean_amount/2 # Arbitrary (but sensible) value
        
        mean_nb_tx_per_day = np.random.uniform(0,4) # Arbitrary (but sensible) value 
        
        customer_id_properties.append([customer_id,
                                      x_customer_id, y_customer_id,
                                      mean_amount, std_amount,
                                      mean_nb_tx_per_day])
        
    customer_profiles_table = pd.DataFrame(customer_id_properties, columns=['CUSTOMER_ID',
                                                                      'x_customer_id', 'y_customer_id',
                                                                      'mean_amount', 'std_amount',
                                                                      'mean_nb_tx_per_day'])
    
    return customer_profiles_table