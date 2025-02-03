#### 3.1. 載入資料集

首先，讓我們載入在先前筆記本中模擬的交易資料。我們將載入從四月到九月的交易檔案。這些檔案可以使用`read_from_files`函式來載入，該函式位於[共用函式](https://fraud-detection-handbook.github.io/fraud-detection-handbook/Chapter_References/shared_functions.html#shared-functions)筆記本中。由於這個函式在本書中會經常使用到，因此我們將它放在這個筆記本中。

這個函式接受兩個輸入參數：資料檔案所在的資料夾位置，以及定義要載入期間的日期（介於`BEGIN_DATE`和`END_DATE`之間）。函式會回傳一個交易資料框（DataFrame），其中的交易記錄依照時間順序排序。
