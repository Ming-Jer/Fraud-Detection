## 2.4. 交易資料生成

客戶檔案現在已包含我們生成交易所需的所有資訊。交易生成將透過`generate_transactions_table`函式來執行，該函式接受客戶檔案、起始日期以及要生成交易的天數作為輸入參數。它將回傳一個交易表格，格式如上所述（尚未包含交易標記，這部分將在[詐欺情境生成](https://fraud-detection-handbook.github.io/fraud-detection-handbook/Chapter_3_GettingStarted/SimulatedDataset.html#fraud-scenarios-generation)階段加入）。

讓我們以第一位客戶為例，從2024-04-01開始生成五天的交易：

我們可以快速檢查生成的交易是否符合客戶檔案的屬性：

- 終端機ID確實來自可用終端機清單（0、1、2和3）
- 交易金額似乎符合客戶的金額參數（`mean_amount`=62.26和`std_amount`=31.13）
- 每日交易次數根據客戶的交易頻率參數（`mean_nb_tx_per_day`=2.18）而變化

