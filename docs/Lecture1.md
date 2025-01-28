# 詐欺偵測簡介 (Introduction to Fraud Detection)
## 前言
支付卡詐欺對企業主、支付卡發卡機構和交易服務公司來說是一個重大挑戰，每年造成巨大且不斷增長的財務損失。根據2019年尼爾森報告，全球支付卡詐欺損失從2011年的98.4億美元增加到2018年的278.5億美元，預計到2027年將超過400億美元 {cite}`NilsonReport2019`。

在支付卡交易中偵測詐欺模式是一個非常困難的問題。隨著支付卡交易產生的資料量不斷增長，人工分析師已無法在交易資料集中偵測詐欺模式，這些資料集通常具有大量樣本、多個維度和線上更新的特點。因此，在過去十年中，支付卡詐欺偵測技術的設計越來越專注於基於機器學習（ML）技術的方法，這些技術可以自動化從大量資料中識別詐欺模式的過程 {cite}`priscilla2019credit,carcillo2019combining,sadgali2018detection,dal2015adaptive`。

將ML技術整合到支付卡詐欺偵測系統中，大大提高了其更有效偵測詐欺的能力，並協助支付處理中介機構識別非法交易。儘管近年來詐欺交易的數量持續增加，但自2016年起，因詐欺造成的損失比例開始下降，這種反向趨勢與ML解決方案的日益採用有關 {cite}`NilsonReport2019`。除了節省資金外，實施基於ML的詐欺偵測系統如今已成為機構和企業贏得客戶信任的必要之舉。

在支付卡詐欺偵測的ML這個新領域中，一個廣受認可且反覆出現的問題是大多數已發表研究工作缺乏可重製性 {cite}`lucas2020credit,priscilla2019credit,patil2018survey,zojaji2016survey`。一方面，支付卡交易資料因保密原因無法公開共享。另一方面，作者們在提供程式碼和使其結果可重製方面的努力不夠。

本書旨在為支付卡詐欺偵測技術基準測試的可重製性邁出第一步。由於該領域已發表的研究數量龐大，我們無法詳盡審查和實施所有現有技術。相反，我們選擇專注於一些我們認為最重要的技術，這是基於我們與工業合作夥伴Worldline長達十年的合作經驗。

本書介紹的一些技術，如處理類別不平衡或模型集成的技術，被廣泛認可為信用卡詐欺偵測系統設計中的重要組成部分。我們還涵蓋了一些較少記錄但我們認為值得更多關注的主題。這些特別包括建模過程的設計方面，如性能指標和驗證策略的選擇，以及有前景的預處理和學習策略，如特徵嵌入和神經網路等。

雖然本書專注於支付卡詐欺，但我們相信本書中呈現的大多數技術和討論對於從事更廣泛詐欺偵測主題的其他實踐者也會有所幫助。

以實驗的可重製性作為本書的主要驅動力，Jupyter Book格式比傳統印刷書籍格式更為適合。特別是，本書所有包含程式碼的章節都是Jupyter筆記本，讀者可以通過克隆書籍儲存庫在自己的電腦上獨立執行，或通過Google Colab或Binder在線上執行。此外，本書的開源特性——完全公開於Github儲存庫——允許讀者通過Github issues討論書籍內容，或通過拉取請求提出修改或改進建議。

### 授權條款

筆記本中的程式碼以 [GNU GPL v3.0 授權](https://www.gnu.org/licenses/gpl-3.0.en.html) 發布。文字和圖片以 [CC BY-SA 4.0 授權](https://creativecommons.org/licenses/by-sa/4.0/) 發布。

如果您想引用本書，可以使用以下格式：

<pre>
@book{leborgne2022fraud,
title={Reproducible Machine Learning for Credit Card Fraud Detection - Practical Handbook},
author={Le Borgne, Yann-A{\"e}l and Siblini, Wissam and Lebichot, Bertrand and Bontempi, Gianluca},
url={https://github.com/Fraud-Detection-Handbook/fraud-detection-handbook},
year={2022},
publisher={Universit{\'e} Libre de Bruxelles}
}
</pre>

### 作者

- [Yann-Aël Le Borgne](https://yannael.github.io/)（聯絡作者 - [yann-ael.le.borgne@ulb.be](mailto:yann-ael.le.borgne@ulb.be)）- [比利時布魯塞爾自由大學機器學習組](http://mlg.ulb.ac.be)
- [Wissam Siblini](https://www.linkedin.com/in/wissam-siblini) - [Worldline Labs 機器學習研究部門](https://worldline.com)
- [Bertrand Lebichot](https://b-lebichot.github.io/) - [盧森堡大學跨學科安全、可靠性與信任中心](https://wwwfr.uni.lu/snt)
- [Gianluca Bontempi](https://mlg.ulb.ac.be/wordpress/members-2/gianluca-bontempi/) - [比利時布魯塞爾自由大學機器學習組](http://mlg.ulb.ac.be)

### 致謝

本書是[比利時布魯塞爾自由大學機器學習組](http://mlg.ulb.ac.be)與[Worldline](https://worldline.com)十年合作的成果。

- ULB-MLG，首席研究員：Gianluca Bontempi
- Worldline，研發經理：Frédéric Oblé

我們要感謝在此合作期間參與這個主題的所有同事：Olivier Caelen (ULB-MLG/Worldline)、Fabrizio Carcillo (ULB-MLG)、Guillaume Coter (Worldline)、Andrea Dal Pozzolo (ULB-MLG)、Jacopo De Stefani (ULB-MLG)、Rémy Fabry (Worldline)、Liyun He-Guelton (Worldline)、Gian Marco Paldino (ULB-MLG)、Théo Verhelst (ULB-MLG)。

本合作得以實現要感謝[Innoviris](https://innoviris.brussels)（布魯塞爾地區研究創新研究所）自2012年起至2021年止的一系列資助。*2018至2021年：*DefeatFraud：深度特徵工程與學習解決方案在詐欺偵測中的評估與驗證*。Innoviris團隊計劃。*2015至2018年：*BruFence：用於自動化防禦系統的可擴展機器學習*。Innoviris橋接計劃。*2012至2015年：*信用卡詐欺偵測的自適應即時機器學習*。Innoviris博士計劃。

本合作目前在[數據工程與數據科學(DEDS)項目](https://deds.ulb.ac.be/)框架下持續進行 - 該項目屬於地平線2020 - 瑪麗·斯克沃多夫斯卡-居里創新培訓網絡(H2020-MSCA-ITN-2020)計劃。

## 1: 什麼是異常偵 (What is Anomaly Detection)
![alt text](../images/anomaly_detection.png "Anomaly detection")

- 異常可被視為與常態有顯著偏離的資料 An anomaly can be seen as data that deviates substantially from the norm 
- 異常偵測是一個識別罕見觀測值的過程，這些觀測值與其所屬的大多數資料有顯著差異 Anomaly detection is the process of identifying rare observations which differ substantially from the majority of the data from where they are drawn
- 應用範圍包括入侵偵測、詐欺偵測、故障偵測、醫療監控等 Applications include intrusion detection, fraud detection, fault detection, healthcare monitoring etc



### Example
- Assuming a single array/list of data contains a distribution of IQ scores within a given population