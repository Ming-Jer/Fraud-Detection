### 客戶檔案生成

每位客戶將由以下屬性定義：

- `CUSTOMER_ID`：客戶唯一識別碼
- (`x_customer_id`, `y_customer_id`)：在100 x 100網格中的一對實數座標，用於定義客戶的地理位置
- (`mean_amount`, `std_amount`)：客戶交易金額的平均值和標準差，假設交易金額遵循常態分配。`mean_amount`將從均勻分配(5,100)中抽取，而`std_amount`將設定為`mean_amount`的一半
- `mean_nb_tx_per_day`：客戶的每日平均交易次數，假設每日交易次數遵循卜瓦松分配。此數值將從均勻分配(0,4)中抽取

`generate_customer_profiles_table`函式提供了生成客戶檔案表格的實作。它接受要生成檔案的客戶數量作為輸入參數，以及用於確保可重現性的隨機狀態。該函式會回傳一個包含每位客戶屬性的DataFrame。
