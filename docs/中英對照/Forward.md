### 信用卡詐欺偵測機器學習實務手冊
### 前言
支付卡詐欺對企業主、支付卡發卡機構和交易服務公司來說是一個重大挑戰，每年造成巨大且不斷增長的財務損失。根據2019年尼爾森報告，全球支付卡詐欺損失從2011年的98.4億美元增加到2018年的278.5億美元，預計到2027年將超過400億美元 {cite}`NilsonReport2019`。

在支付卡交易中偵測詐欺模式是一個非常困難的問題。隨著支付卡交易產生的資料量不斷增長，人工分析師已無法在交易資料集中偵測詐欺模式，這些資料集通常具有大量樣本、多個維度和線上更新的特點。因此，在過去十年中，支付卡詐欺偵測技術的設計越來越專注於基於機器學習（ML）技術的方法，這些技術可以自動化從大量資料中識別詐欺模式的過程 {cite}`priscilla2019credit,carcillo2019combining,sadgali2018detection,dal2015adaptive`。

將ML技術整合到支付卡詐欺偵測系統中，大大提高了其更有效偵測詐欺的能力，並協助支付處理中介機構識別非法交易。儘管近年來詐欺交易的數量持續增加，但自2016年起，因詐欺造成的損失比例開始下降，這種反向趨勢與ML解決方案的日益採用有關 {cite}`NilsonReport2019`。除了節省資金外，實施基於ML的詐欺偵測系統如今已成為機構和企業贏得客戶信任的必要之舉。

在支付卡詐欺偵測的ML這個新領域中，一個廣受認可且反覆出現的問題是大多數已發表研究工作缺乏可重製性 {cite}`lucas2020credit,priscilla2019credit,patil2018survey,zojaji2016survey`。一方面，支付卡交易資料因保密原因無法公開共享。另一方面，作者們在提供程式碼和使其結果可重製方面的努力不夠。

本書旨在為支付卡詐欺偵測技術基準測試的可重製性邁出第一步。由於該領域已發表的研究數量龐大，我們無法詳盡審查和實施所有現有技術。相反，我們選擇專注於一些我們認為最重要的技術，這是基於我們與工業合作夥伴Worldline長達十年的合作經驗。

本書介紹的一些技術，如處理類別不平衡或模型集成的技術，被廣泛認可為信用卡詐欺偵測系統設計中的重要組成部分。我們還涵蓋了一些較少記錄但我們認為值得更多關注的主題。這些特別包括建模過程的設計方面，如性能指標和驗證策略的選擇，以及有前景的預處理和學習策略，如特徵嵌入和神經網路等。

雖然本書專注於信用卡/支付卡詐欺，但我們相信本書中呈現的大多數技術和討論對於從事更廣泛詐欺偵測主題的其他實踐者也會有所幫助。

### 目錄
- 第一章：書籍概述（本章）
- 第二章：背景
- 第三章：入門指南
- 第四章：績效指標
- 第五章：模型選擇
- 第六章：不平衡學習
- 第七章：深度學習

### 目標讀者
- 對信用卡詐騙偵測這個特定問題有興趣，並希望從實務角度了解的學生或專業人士
- 更廣泛來說，處理涉及表格式序列資料和/或不平衡分類問題之機器學習問題的資料實務工作者和資料科學家

### 基本知識
- 熟悉 Python 程式語言和 scikit-learn 函式庫
- 熟悉資料科學和機器學習流程

### 推薦書籍：
- Gianluca Bontempi：機器學習的統計基礎，第二版。布魯塞爾自由大學，2021 [Bon21]
- Andreas C Müller 與 Sarah Guido：Python機器學習入門：資料科學家指南。O'Reilly Media出版社，2016 [MullerG16]
- Wes McKinney：Python資料分析：使用Pandas、NumPy和IPython進行資料處理 - 第二版。O'Reilly Media出版社，2017 [McK17]

### 機器學習小組 - 推薦文獻：
- Wissam Siblini、Guillaume Coter、Rémy Fabry、Liyun He-Guelton、Frédéric Oblé、Bertrand Lebichot、Yann-Aël Le Borgne 與 Gianluca Bontempi：信用卡詐欺檢測的遷移學習：從研究到生產的歷程。發表於資料科學與進階分析會議（DSAA 2021），2021 [SCF+21]
- Bertrand Lebichot、Théo Verhelst、Yann-Aël Le Borgne、Liyun He-Guelton、Frédéric Oblé 與 Gianluca Bontempi：信用卡詐欺檢測的遷移學習策略。IEEE access期刊，9:114754–114766，2021 [LVLB+21]
- Be*rtrand Lebichot、Gian Marco Paldino、W Siblini、L He-Guelton、F Oblé 與 G Bontempi：信用卡詐欺檢測的增量學習策略。國際資料科學與分析期刊，頁1–10，2021 [LPS+21]
- Bertrand Lebichot、Yann-Aël Le Borgne、Liyun He-Guelton、Frédéric Oblé 與 Gianluca Bontempi：信用卡詐欺檢測的深度學習領域適應技術。發表於INNS大數據與深度學習會議，78–88。Springer出版社，2019 [LLBHG+19] Fabrizio Carcillo、Yann-Aël Le Borgne、Olivier Caelen、
- Yacine Kessaci、Frédéric Oblé 與 Gianluca Bontempi：在信用卡詐欺檢測中結合無監督與監督學習。資訊科學期刊，2019 [CLBC+19]
- Fabrizio Carcillo、Andrea Dal Pozzolo、Yann-Aël Le Borgne、Olivier Caelen、Yannis Mazzer 與 Gianluca Bontempi：Scarff：基於Spark的可擴展信用卡詐欺檢測串流框架。資訊融合期刊，41:182–194，2018 [CDPLB+18]
- Fabrizio Carcillo、Yann-Aël Le Borgne、Olivier Caelen 與 Gianluca Bontempi：實際信用卡詐欺檢測的串流主動學習策略：評估與視覺化。國際資料科學與分析期刊，5(4):285–300，2018 [CLBCB18]
- Fabrizio Carcillo：超越信用卡詐欺檢測中的監督學習：半監督與分散式學習的深入探討。布魯塞爾自由大學，2018 [Car18]
- Andrea Dal Pozzolo、Giacomo Boracchi、Olivier Caelen、Cesare Alippi 與 Gianluca Bontempi：信用卡詐欺檢測：實際建模與新穎學習策略。IEEE神經網路與學習系統期刊，29(8):3784–3797，2017 [DPBC+17]
- Andrea Dal Pozzolo：信用卡詐欺檢測的自適應機器學習。布魯塞爾自由大學，2015 [DP15]
- Andrea Dal Pozzolo、Olivier Caelen、Yann-Ael Le Borgne、Serge Waterschoot 與 Gianluca Bontempi：從實踐者角度看信用卡詐欺檢測的經驗教訓。專家系統與應用期刊，41(10):4915–4928，2014 [DPCLB+14]

### 本書貢獻
本書相對於現有文獻的原創性貢獻：

- 合成交易資料模擬器：本書提出一個交易資料模擬器，可用於創建不同複雜程度的合成交易資料集。特別是，該模擬器允許調整類別不平衡程度（欺詐交易的低比例），包含數值和類別變數（具有大量可能值的類別特徵），並具有時間相依的欺詐情境。模擬器在第三章第二節中介紹。
- 可重現性：本書是一本Jupyter Book，允許互動式執行或修改包含程式碼的章節。結合合成資料生成器，本書中呈現的所有實驗和結果都是可重現的。關於如何在雲端或個人電腦上執行本書的說明在第二章第三節中提供。
- 最新技術綜述：本書綜合了信用卡詐欺檢測機器學習（ML for CCFD）領域的最新調查研究。它強調了這些調查中提出的核心原則，並總結了詐欺檢測系統的主要挑戰。相關綜述在第三章第三節中呈現。
- 評估方法：本書的一個主要貢獻是詳細介紹和討論了可用於評估詐欺檢測系統效能的性能指標和驗證方法。性能指標在第四章中討論。驗證方法和模型選擇策略在第五章中討論。
- 不平衡學習：本書對不平衡學習方法進行了廣泛的實驗評估，涵蓋成本敏感、重採樣和集成技術。對於每種方法，實驗評估包括一個玩具示例、模擬交易數據集和真實世界數據集。該主題在第六章中涵蓋。所提出的實驗評估的主要結論是，不平衡學習技術的效益是有限的，並且與目標性能指標密切相關。
- 深度學習：深度學習技術的最新發展使研究界越來越關注其在詐欺檢測中的應用。本書是首次深入探討這些方法在信用卡詐欺檢測問題上的使用和實現細節。第七章涵蓋了全連接前饋神經網絡等技術的實現和評估，以及更進階的技術，如自編碼器的表示學習或卷積或長短期記憶網絡等序列模型。