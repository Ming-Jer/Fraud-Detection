#### 3.3. 客戶ID轉換

第二種轉換為RFM分析（近期性、頻率、金額值）：追蹤並分析顧客的消費行為模式，包含最近一次消費時間（Recency）、消費頻率（Frequency）及消費金額（Monetary value）。
此種轉換涉及顧客ID，主要是建立能表徵顧客消費行為的特徵。我們將遵循RFM（近期性、頻率、金額）分析框架，追蹤每位顧客在三個不同時間窗口的平均消費金額和交易次數。這將產生六個新的特徵。

現在讓我們進行客戶ID的轉換。我們將參考RFM（近期性、頻率、金額）架構[[VVBC+15](https://fraud-detection-handbook.github.io/fraud-detection-handbook/Chapter_References/bibliography.html#id65)]，並在三個時間窗口內計算其中兩個特徵。
- 第一個特徵是在時間窗口內發生的交易次數（頻率）；
- 第二個特徵是這些交易的平均金額（金額值）。
時間窗口將設定為一天、七天和三十天。這將產生六個新特徵。值得注意的是，這些時間窗口後續可以透過模型選擇程序與模型一同進行最佳化（請參考[第5章](https://fraud-detection-handbook.github.io/fraud-detection-handbook/Chapter_5_ModelValidationAndSelection/ModelSelection.html#model-selection)）。

讓我們透過撰寫`get_customer_spending_behaviour_features`函式來實作這些轉換。此函式接受客戶的交易資料集和一組時間窗口大小作為輸入參數，並回傳包含六個新特徵的資料框。我們的實作仰賴Pandas的`rolling`函式，該函式能夠輕鬆計算時間窗口內的聚合值。

讓我們先為第一位客戶計算這些聚合值。

我們可以驗證這些新特徵與客戶檔案是否一致（參見先前的筆記本）。對於客戶0，平均金額為`mean_amount`=62.26，每日交易頻率為`mean_nb_tx_per_day`=2.18。這些數值確實與特徵`CUSTOMER_ID_NB_TX_30DAY_WINDOW`和`CUSTOMER_ID_AVG_AMOUNT_30DAY_WINDOW`非常接近，特別是在30天後的數值。

現在讓我們為所有客戶產生這些特徵。使用Pandas的`groupby`和`apply`方法可以輕鬆完成這項工作。
