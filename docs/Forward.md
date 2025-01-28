### 信用卡詐欺偵測機器學習實務手冊
#### 前言
支付卡詐欺對企業主、支付卡發卡機構和交易服務公司來說是一個重大挑戰，每年造成巨大且不斷增長的財務損失。根據2024年尼爾森報告，全球支付卡詐欺損失從2011年的98.4億美元、2018年的278.5億美元、2022 年的334.5億美元，增加到2023 年的338.3億美元，預計到2027年將超過400億美元，參考[Nilson Report 2019 Issue 1164](https://nilsonreport.com/newsletters/1164/)。2033年全球所有支付卡簽帳金額預估將達到81.800兆美元，而全球支付卡詐欺損失金額則預估為485.1億美元，或每100美元，損失金額為5.93分。[聯合信用卡中心摘譯的Nilson Report-第1276期](https://www.nccc.com.tw/wps/wcm/connect/188aedbc-431d-46eb-b816-cc7e838f1f6a/Nilson+Report%E7%AC%AC1276%E6%9C%9F%E9%87%8D%E9%BB%9E%E6%91%98%E8%AD%AF.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-188aedbc-431d-46eb-b816-cc7e838f1f6a-pi80Spt)。


在支付卡交易中偵測詐欺模式是個極具挑戰性的問題。支付卡交易所產生的資料量持續增長，這些資料集不僅包含大量樣本，還具有多維度性質且需要即時更新，使得人工分析師難以有效偵測其中的詐欺模式。有鑑於此，近十年來，支付卡詐欺偵測技術逐漸轉向採用機器學習（ML）方法，以自動化方式從海量資料中識別詐欺模式 [CLBC+19][1], [DP15][2], [PP19][3], [SSB18][4]。

在支付卡交易中偵測詐欺模式是個極具挑戰性的問題。支付卡交易所產生的資料量持續增長，這些資料集不僅包含大量樣本，還具有多維度性質且需要即時更新，使得人工分析師難以有效偵測其中的詐欺模式。有鑑於此，近十年來，支付卡詐欺偵測技術逐漸轉向採用機器學習（ML）方法，以自動化方式從海量資料中識別詐欺模式。

將ML技術整合到支付卡詐欺偵測系統中，不僅大幅提升了詐欺偵測的效能，也協助支付處理機構更準確地識別非法交易。儘管詐欺交易的數量持續增加，但自2016年起，詐欺造成的損失比例反而開始下降，這個正面趨勢與ML解決方案的廣泛採用密切相關 [Nilson Report 2019 Issue 1164](https://nilsonreport.com/newsletters/1164/)。如今，實施基於ML的詐欺偵測系統不僅能節省資金，更已成為機構和企業建立客戶信任的關鍵要素。

在支付卡詐欺偵測的ML領域中，一個普遍存在的問題是已發表研究缺乏可重製性[LJ20][5] [PL18, PP19, ZAM+16]。這個問題源於兩個主要因素：支付卡交易資料因隱私考量無法公開分享，以及研究者在提供程式碼和確保結果可重製方面的投入不足。

本書致力於為支付卡詐欺偵測技術的基準測試建立可重製性的基礎。鑑於此領域研究成果豐富，我們無法涵蓋所有現有技術，而是根據與工業合作夥伴Worldline十年來的合作經驗，精選了最具影響力的技術進行深入探討。

本書詳細介紹了多項核心技術，包括處理類別不平衡和模型整合等公認的信用卡詐欺偵測系統重要元素。我們同時也探討了一些較少受到關注但極具潛力的領域，特別是在建模過程的設計方面，如性能指標的選擇、驗證策略的制定，以及創新的預處理和學習方法，例如特徵嵌入和神經網路等技術。

雖然本書聚焦於信用卡和支付卡詐欺，但書中提出的技術和見解對於其他類型詐欺偵測的實務工作者同樣具有參考價值。

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

- 合成交易資料模擬器：本書提出一個創新的交易資料模擬器，可產生不同複雜程度的合成交易資料集。該模擬器具有三大特色：可調整類別不平衡程度（欺詐交易的低比例）、支援數值和類別變數（包含大量可能值的類別特徵），以及能模擬時間相依的欺詐情境。詳細說明請見第三章第二節。
- 可重現性：本書採用Jupyter Book格式，讓讀者能互動式執行或修改程式碼。搭配合成交易資料模擬器，本書所有實驗和結果皆可重現。第二章第三節提供在雲端或個人電腦上執行本書的完整指引。
- 最新技術綜述：本書全面整理信用卡詐欺檢測機器學習（ML for CCFD）領域的最新研究成果，凸顯關鍵原則，並歸納詐欺檢測系統的主要挑戰。相關內容請見第三章第三節。
- 評估方法：本書深入探討評估詐欺檢測系統的性能指標和驗證方法。第四章聚焦於性能指標，第五章則詳述驗證方法和模型選擇策略。
- 不平衡學習：本書透過簡易範例、模擬交易資料集和真實世界資料集，全面評估不平衡學習方法，包括成本敏感、重採樣和整合技術。第六章的實驗結果顯示，不平衡學習技術的效益與目標性能指標密切相關，且實際改善程度有限。
- 深度學習：隨著深度學習技術快速發展，其在詐欺檢測領域的應用備受關注。本書首次深入剖析這些方法在信用卡詐欺檢測的實作細節。第七章涵蓋從基礎的全連接前饋神經網路到進階技術，如自編碼器的表示學習，以及卷積網路和長短期記憶網路等序列模型。

#### Reference

以實驗的可重製性為本書核心理念，Jupyter Book格式相較傳統印刷書籍更具優勢。本書所有含程式碼的章節皆以Jupyter筆記本形式呈現，讀者可透過克隆書籍儲存庫在個人電腦上執行，或經由Google Colab或Binder在雲端運行。此外，本書採用開源模式，完整內容公開於Github儲存庫，讀者可透過Github issues參與討論，也能以拉取請求方式提供修改或改進建議。

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

[1]: <../docs/References.md> "CLBC+19"

[2]: <../docs/References.md> "DP15"

[3]: <../docs/References.md> "PP19"

[4]: <../docs/References.md> "SSB18"

[5]: <../docs/References.md> "LJ20"

[6]: <../docs/References.md> "PL18"