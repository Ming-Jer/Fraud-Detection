import streamlit as st
import pandas as pd
import os
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid', {'axes.facecolor': '0.9'})

# FDS UI
from pyFraudDetection import fds_sidebar
from pyFraudDetection import read_markdown_file
from pyFraudDetection import save_object
from pyFraudDetection import restore_object
from pyFraudDetection import save_simulated_data
from pyFraudDetection import print_directory_structure

# FDS simulator modules
from pyFraudDetection import generate_customer_profiles_table
from pyFraudDetection import generate_terminal_profiles_table
from pyFraudDetection import get_list_terminals_within_radius
from pyFraudDetection import generate_transactions_table
from pyFraudDetection import generate_dataset
from pyFraudDetection import add_frauds
from pyFraudDetection import get_stats

# Customize the sidebar
fds_sidebar()

# hidden div with anchor
st.markdown("<div id='linkto_top'></div>", unsafe_allow_html=True) 
st.subheader("交易資料模擬器 (Transaction data simulator)")

# Tabs Menu
tab_intro, tab_customer, tab_terminal, tab_list, tab_trans, tab_scale, tab_fraud = st.tabs(["模擬器簡介","客戶資料", "終端機配置", "客戶與終端機關聯", "交易生成", "擴展交易資料","詐欺情境生成"])

# 交易資料模擬器-簡介
with tab_intro:
    # sim_tab_intro()
    # reading markdown file
    intro_markdown = read_markdown_file(os.getcwd()+'/docs/Simulator.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)
    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)

# 交易資料模擬器-模擬客戶資料
with tab_customer:
    #sim_tab_customer()
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

# 交易資料模擬器-模擬終端機配置
with tab_terminal:
    #sim_tab_terminal()
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
    
# 交易資料模擬器-客戶與終端機關聯
with tab_list:
    #sim_tab_list()
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
                                                                start_date = "2024-04-01", 
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
    請選擇模擬資料處理說明:
    - 產生真實資料 (5,000位客戶、10,000個終端機、183天(1,754,155筆交易資料)，約需1-3分鐘左右，端賴您的電腦效能而定。
    - 儲存真實資料 (便於後續使用)。
    - 載入先前已經產生真實資料 (便於後續使用)。
    """
    st.markdown(intro_markdown, unsafe_allow_html=True)
    s_customers=500
    s_terminals=1000
    s_nb_days=18
    s_date="2024-04-01"

    options = st.selectbox(
        "模擬資料處理選項",
#        ("產生簡易資料","產生實真資料", "儲存實真資料", "載入實真資料"),index=0,
        ("產生簡易資料","產生實真資料"),index=0,

    )
    with st.expander("顯示原始碼 See Source Code"):
        with st.echo():
            if (options=="產生簡易資料"):
                # 先產生一個小的檔案，加速系統運作
                # 保留未來可以讓使用者調整的空間
                s_customers=500
                s_terminals=1000
                s_nb_days=18
                s_date="2024-04-01"
                (customer_profiles_table, terminal_profiles_table, transactions_df)=\
                                generate_dataset(n_customers = s_customers,
                                     n_terminals = s_terminals, 
                                     nb_days=s_nb_days, 
                                     start_date=s_date, 
                                     r=5)
                st.dataframe(transactions_df, hide_index = True)                     
            elif (options=="產生實真資料"):
                s_customers=5000
                s_terminals=10000
                s_nb_days=183
                s_date="2024-04-01"
                st.write("You selected:", options, s_customers, s_terminals, s_nb_days,s_date)
                (customer_profiles_table, terminal_profiles_table, transactions_df)=\
                    generate_dataset(n_customers = s_customers,
                         n_terminals = s_terminals, 
                         nb_days=s_nb_days, 
                         start_date=s_date, 
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
            #sns.histplot(amount_val, ax=ax[0], color='r', kde = False)
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
    # reading markdown file
    intro_markdown = read_markdown_file(os.getcwd()+'/docs/Simulator_generate_fraud.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)
    
    st.write("我們根據這些情境加入詐欺交易：")
    with st.expander("顯示原始碼 See Source Code"):
        with st.echo():
            transactions_df = add_frauds(customer_profiles_table, terminal_profiles_table, transactions_df)
            st.dataframe(transactions_df, hide_index = True)

            st.write("詐欺交易數量： ", transactions_df.TX_FRAUD.sum())
            st.write("三種詐欺情境數量")
            st.write(transactions_df[transactions_df.TX_FRAUD_SCENARIO==1].shape)
            st.write(transactions_df[transactions_df.TX_FRAUD_SCENARIO==2].shape)
            st.write(transactions_df[transactions_df.TX_FRAUD_SCENARIO==3].shape)
            st.write("詐欺交易百分比： ",transactions_df.TX_FRAUD.mean())
    
    st.write("詐欺交易數量： ", transactions_df.TX_FRAUD.sum())
    st.write("三種詐欺情境數量")
    st.write(transactions_df[transactions_df.TX_FRAUD_SCENARIO==1].shape)
    st.write(transactions_df[transactions_df.TX_FRAUD_SCENARIO==2].shape)
    st.write(transactions_df[transactions_df.TX_FRAUD_SCENARIO==3].shape)
    st.write("詐欺交易百分比： ",transactions_df.TX_FRAUD.mean())
    
    st.write("我們的交易資料模擬集現已完成，所有交易都已加入詐欺標記。")
    st.dataframe(transactions_df, hide_index = True)
    with st.expander("顯示原始碼 See Source Code"):
        with st.echo():
            (nb_tx_per_day,nb_fraud_per_day,nb_fraudcard_per_day)=get_stats(transactions_df)

            n_days=len(nb_tx_per_day)
            tx_stats=pd.DataFrame({"value":pd.concat([nb_tx_per_day/50,nb_fraud_per_day,nb_fraudcard_per_day])})
            tx_stats['stat_type']=["nb_tx_per_day"]*n_days+["nb_fraud_per_day"]*n_days+["nb_fraudcard_per_day"]*n_days
            tx_stats=tx_stats.reset_index()

    intro_markdown="""
    接下來讓我們檢視每日的交易總數、詐欺交易數量，以及遭入侵卡片數量的變化情形。
    這個模擬每天產生約10,000筆交易，其中每日詐欺交易約85筆，涉及的詐欺卡片約80張。值得注意的是，第一個月的詐欺交易數量較少，這是因為情境二和情境三的詐欺行為分別持續28天和14天所致。
    這個結果資料集具有以下特點：類別不平衡（詐欺交易不到1%）、混合數值與類別特徵、特徵間存在非簡單的關聯性，以及具有時間相依性的詐欺情境。
    """
    st.markdown(intro_markdown, unsafe_allow_html=True)

    with st.expander("顯示原始碼 See Source Code"):
        with st.echo():
            sns.set(style='darkgrid')
            sns.set(font_scale=1.4)
            
            fraud_and_transactions_stats_fig, ax = plt.subplots(figsize=(15,8))

            #fraud_and_transactions_stats_fig.set_size_inches(15, 8)

            sns_plot = sns.lineplot(x="TX_TIME_DAYS", y="value", data=tx_stats, hue="stat_type", hue_order=["nb_tx_per_day","nb_fraud_per_day","nb_fraudcard_per_day"], legend=False)

            sns_plot.set_title('Total transactions, and number of fraudulent transactions \n and number of compromised cards per day', fontsize=20)
            sns_plot.set(xlabel = "Number of days since beginning of data generation", ylabel="Number")

            sns_plot.set_ylim([0,300])

            labels_legend = ["# transactions per day (/50)", "# fraudulent txs per day", "# fraudulent cards per day"]

            sns_plot.legend(loc='upper left', labels=labels_legend,bbox_to_anchor=(1.05, 1), fontsize=15)
            st.pyplot(fraud_and_transactions_stats_fig)
    
    st.pyplot(fraud_and_transactions_stats_fig)

    intro_markdown="""
    最後，讓我們將這個資料集儲存起來，以供本書後續使用。
    我們不會儲存整個交易資料集，而是將其分割成每日批次。這樣做可以讓我們之後只需載入特定時期的資料，而不是整個資料集。為了加快載入速度，我們使用pickle格式而非CSV格式。所有檔案都會儲存在`DIR_OUTPUT`資料夾中，檔案名稱即為日期，副檔名為`.pkl`。
    """
    st.markdown(intro_markdown, unsafe_allow_html=True)
    
    #st.button("Save Data")
    if st.button("Save Data"):
        DIR_OUTPUT = os.getcwd()+"/data/simulated-data-raw/"
        save_simulated_data(DIR_OUTPUT,transactions_df)
        
    # add the link at the bottom of each page
    st.markdown("<a href='#linkto_top'>返回頁首(Top)</a>", unsafe_allow_html=True)