### 信用卡欺詐檢測的機器學習 Machine learning for credit card fraud detection

信用卡欺詐檢測 (CCFD) 就像大海撈針，它需要從數百萬的日常交易中找出哪些是欺詐性的。由於資料量不斷增加，人類專家現在幾乎不可能從交易資料中檢測出有意義的模式。出於這個原因，機器學習技術的使用，現在廣泛用於欺詐檢測領域，其中需要從大型資料集中提取信息[Car18, DP15, LJ20, PP19]。
Credit card fraud detection (CCFD) is like looking for needles in a haystack. It requires finding, out of millions of daily transactions, which ones are fraudulent. Due to the ever-increasing amount of data, it is now almost impossible for a human specialist to detect meaningful patterns from transaction data. For this reason, the use of machine learning techniques is now widespread in the field of fraud detection, where information extraction from large datasets is required [Car18, DP15, LJ20, PP19].

機器學習 (ML) 是研究通過經驗自動改進的算法  [Bon21, FHT01].。 ML 與統計、模式識別和數據挖掘等領域密切相關。同時，它作為計算機科學和人工智能的一個子領域出現，並特別關注知識提取過程的算法部分。 ML 在許多科學學科中發揮著關鍵作用，它的應用是我們日常生活的一部分。例如，它用於過濾垃圾郵件、天氣預報、醫療診斷、產品推薦、人臉檢測、欺詐檢測等 [Bis06, DP15]。

Machine Learning (ML) is the study of algorithms that improve automatically through experience [Bon21, FHT01]. ML is closely related to the fields of Statistics, Pattern Recognition, and Data Mining. At the same time, it emerges as a subfield of computer science and artificial intelligence and gives special attention to the algorithmic part of the knowledge extraction process. ML plays a key role in many scientific disciplines and its applications are part of our daily life. It is used for example to filter spam email, for weather prediction, in medical diagnosis, product recommendation, face detection, fraud detection, etc [Bis06, DP15].

ML 技術有效應對 CCFD 提出的挑戰的能力導致了過去十年中大量且不斷增長的研究。如圖 1 所示，在 2010 年至 2020 年間，已有數千篇與該主題相關的論文發表，僅 2020 年就發表了約 1500 篇論文。
The ability of ML techniques to effectively address the challenges raised by CCFD has led to a large and growing body of research in the last decade. As reported in Fig. 1, thousands of papers related to this topic have been published between 2010 and 2020, with about 1500 papers published in 2020 alone.

![alt text](https://fraud-detection-handbook.github.io/fraud-detection-handbook/_images/ML_CCFD_GoogleScholar_2010_2020.png)
<p style="text-align: center;">
圖 1. 2010 年至 2020 年間機器學習和信用卡欺詐檢測主題的發表文章數量。來源：谷歌學術。
</p>

本節旨在通過總結主要研究挑戰以及可用於解決這些挑戰的關鍵機器學習概念，對近期研究進行概述。
This section aims at providing an overview of this body of recent research, by summarising the main research challenges, and the key machine learning concepts that can be used to address them.

## 最近的調查 Recent surveys

為了解 CCFD 機器學習研究的現狀，我們在 Google Scholar 上搜索了過去五年中關於該主題的所有評論和調查。 使用以下布爾搜索：（“機器學習”或“資料探勘”）和“信用卡”和“欺詐檢測”和（評論或調查）`("machine learning" OR "data mining") AND "credit card" AND "fraud detection" AND (review OR survey)`  並限制從 2015 年到 2021 年的搜索期，我們確定了十個評論/調查，其中 我們在下表中報告。
To get a picture of the current state of research on ML for CCFD, we searched Google Scholar for all reviews and surveys made on this topic in the last five years. Using the following boolean search: ("machine learning" OR "data mining") AND "credit card" AND "fraud detection" AND (review OR survey) and restricting the search period from 2015 to 2021, we identified ten reviews/surveys which we report in the following table.


| 標題 | 日期 | 參考文獻 |
|---|---|---|
|信用卡欺詐檢測技術調查：數據和技術導向的觀點 | 2016 | {cite}`zojaji2016survey`|
|基於機器學習和自然啟發的信用卡欺詐檢測技術調查 | 2017 | {cite}`adewumi2017survey`|
|使用機器學習進行信用卡欺詐檢測調查 | 2018 | {cite}`popat2018survey`|
|機器學習技術在欺詐檢測研究中的最新進展回顧 | 2018 | {cite}`sinayobye2018state`|
|信用卡欺詐檢測：技術現狀 | 2018 | {cite}`sadgali2018detection`|
|信用卡欺詐檢測中不同數據挖掘與機器學習方法的調查 | 2018 | {cite}`patil2018survey`|
|信用卡欺詐檢測的資料探勘方法系統性回顧 | 2018 | {cite}`mekterovic2018systematic`|
|信用卡欺詐檢測的機器學習技術與用戶驗證方法綜合調查 | 2019 | {cite}`yousefi2019comprehensive`|
|信用卡欺詐檢測：系統性回顧 | 2019 | {cite}`priscilla2019credit`|
|使用機器學習進行信用卡欺詐檢測

五年內的一組十次調查可以被認為是高的。 在如此短的時間內發布瞭如此多的調查（尤其是 2018 年發布的五項調查）這一事實反映了 CCFD 的 ML 主題的快速發展以及獨立研究人員團隊在綜合研究狀態方面的需求 在這個領域裡。
A set of ten surveys in five years can be considered high. The fact that so many surveys were published in such a short period (in particular for the five surveys published in 2018) reflects the rapid evolution of the topic of ML for CCFD and the need that teams of independent researchers felt in synthesizing the state of research in this field.

鑑於這些調查的共同目標，值得注意的是，在內容方面可以發現高度的冗餘。 特別是，它們都強調了一組共同的方法和挑戰，我們將在接下來的兩節中介紹。 我們首先介紹基線方法，即在處理使用 ML 技術解決 CCFD 的論文中通常遵循的通用工作流程。 然後，我們總結了該主題所面臨的挑戰。
Given the common goal of these surveys, it is worth noting that a high degree of redundancy can be found in terms of content. In particular, they all emphasize a common set of methodologies and challenges, that we present in the next two sections. We first cover the baseline methodology, that is, the common workflow that is typically followed in papers dealing with the use of ML techniques to address CCFD. We then summarize the challenges that characterize this topic.

## 基線方法 - 監督學習 Baseline methodology - Supervised learning

大量的機器學習技術可用於解決 CCFD 的問題。 這直接反映在過去十年中發表的大量有關該主題的論文中。 儘管有大量的研究工作，但大多數提出的方法都遵循通用的基線 ML 方法 [Bis06, FHT01, PL18]，我們在圖 2 中對其進行了總結。
A wide number of ML techniques can be used to address the problem of CCFD. This is directly reflected by the huge amount of published papers on the topic in the last decade. Despite this large volume of research work, most of the proposed approaches follow a common baseline ML methodology [Bis06, FHT01, PL18], which we summarize in Fig. 2.

![alt text](https://fraud-detection-handbook.github.io/fraud-detection-handbook/_images/baseline_ML_workflow.png)
<p style="text-align: center;">
圖 2. CCFD 的 ML：基線方法，以及最近關於該主題的調查中提出的大多數方法。  
Fig. 2. ML for CCFD: Baseline methodology followed by most of the proposed approaches in the recent surveys on the topic.
</p>

在信用卡欺詐檢測中，數據通常由交易資料組成，例如由支付處理器或銀行收集。交易資料可分為三組[AA17、LJ20、VVBC+15]
In credit card fraud detection, data typically consists of transaction data, collected for example by a payment processor or a bank. Transaction data can be divided into three groups [AA17, LJ20, VVBC+15]

- 帳戶相關功能：包括賬號、開戶日期、卡額度、卡到期日等。Account-related features: They include for example the account number, the date of the account opening, the card limit, the card expiry date, etc.
- 交易相關特徵：例如交易參考號、賬號、交易金額、終端（即POS）號碼、交易時間等。從終端上，還可以獲得額外的信息類別：與商家相關的特徵，例如其類別代碼（餐廳、超市……）或其位置。Transaction-related features: They include for example the transaction reference number, the account number, the transaction amount, the terminal (i.e., POS) number, the transaction time, etc. From the terminal, one can also obtain an additional category of information: merchant-related features such as its category code (restaurant, supermarket, …) or its location.
- 與客戶相關的特徵：它們包括例如客戶編號、客戶類型（低調、高調……）等。Customer-related features: They include for example the customer number, the type of customer (low profile, high profile, …), etc.

在最簡單的形式中，支付卡交易包括客戶在特定時間支付給商家的任何金額。一組歷史交易資料可以表示為如圖 3 所示的表格。對於欺詐檢測，通常還假設所有交易的合法性都是已知的（即交易是真實的還是欺詐的）。這通常由二進制標籤表示，真實交易的值為 0，欺詐交易的值為 1。
In its simplest form, a payment card transaction consists of any amount paid to a merchant by a customer at a certain time. A set of historical transaction data may be represented as a table such as illustrated in Fig. 3. For fraud detection, it is also generally assumed that the legitimacy of all transactions is known (that is, whether the transaction was genuine or fraudulent). This is usually represented by a binary label, with a value of 0 for a genuine transaction, and a value of 1 for fraudulent transactions.

![alt text](https://fraud-detection-handbook.github.io/fraud-detection-handbook/_images/tx_table.png)
<p style="text-align: center;">
圖 3. 交易資料表格範例。每一列代表從客戶到終端機的一筆交易。最後一個變數是標籤，表示該筆交易是合法（0）或詐騙（1）。 
Fig. 3. Example of transaction data represented as a table. Each row corresponds to a transaction from a customer to a terminal. The last variable is the label, which indicates whether the transaction was genuine (0) or fraudulent (1).  
</p>

在基於機器學習的欺詐檢測系統的設計中可以區分兩個階段。第一階段包括從一組標記的歷史資料構建預測模型（圖 2，上部）。這個過程稱為監督學習，因為交易的標籤（真實或欺詐）是已知的。在第二階段，從監督學習過程中獲得的預測模型用於預測新交易的標籤（圖 2，下半部分）。
Two stages can be distinguished in the design of an ML-based fraud detection system. The first stage consists of building a prediction model from a set of labeled historical data (Fig. 2, upper part). This process is called supervised learning since the label of the transactions (genuine or fraudulent) is known. In the second stage, the prediction model obtained from the supervised learning process is used to predict the label of new transactions (Fig. 2, lower part).

形式上，預測模型是帶有參數的參數函數θ，也稱為假設，它從輸入域X⊂Rn 中獲取輸入x ，並輸出預測 y^=h(x,θ)在輸出域Y⊂R [Car18, DP15] 上：
Formally, a prediction model is a parametric function with parameters θ, also called a hypothesis, that takes an input x from an input domain X⊂Rn, and outputs a prediction y^=h(x,θ) over an output domain Y⊂R [Car18, DP15]:

$$
h(x,\theta): \mathcal{X} \rightarrow \mathcal{Y}
$$

輸入域 X 通常不同於原始交易數據的空間，原因有兩個。首先，出於數學原因，大多數監督學習算法都要求輸入域是實值的，即  X⊂Rn，這需要轉換非實數的事務特徵（如時間戳、分類變量等）。其次，使用其他可能提高預測模型檢測性能的變量來豐富交易數據通常是有益的。此過程稱為特徵工程（也稱為特徵轉換、特徵提取或數據預處理）。
The input domain X usually differs from the space of raw transaction data for two reasons. First, for mathematical reasons, most supervised learning algorithms require the input domain to be real-valued, that is, X⊂Rn, which requires to transform transaction features that are not real numbers (such as timestamps, categorical variables, etc…). Second, it is usually beneficial to enrich transaction data with other variables that may improve the detection performance of the prediction model. This process is referred to as feature engineering (also known as feature transformation, feature extraction, or data preprocessing).

對於欺詐檢測，輸出域 Y 通常是給定輸入 x的預測類別，即Y={0,1}。鑑於輸出類是二元的，這些預測模型也稱為二元分類器。或者，輸出也可以用 Y=[0,1]表示為欺詐概率，或更一般地表示為風險評分，用 Y=R表示，其中較高的值表示較高的欺詐風險。
For fraud detection, the output domain Y is usually the predicted class for a given input x, that is Y={0,1}. Given that the output class is binary, these prediction models are also called binary classifiers. Alternatively, the output may also be expressed as a fraud probability, with Y=[0,1], or more generally as a risk score, with Y=R, where higher values express higher risks of fraud.

預測模型的訓練（或構建）包括找到提供最佳性能的參數。使用損失函數評估預測模型的性能，該損失函數將真實標籤與預測標籤進行比較對於輸入。在二元分類問題中，常見的損失函數是零/一損失函數，它在錯誤預測的情況下分配等於 1 的損失，否則分配為零：
The training (or building) of a prediction model h(x,θ) consists of finding the parameters θ that provide the best performance. The performance of a prediction model is assessed using a loss function, that compares the true label y to the predicted label y^=h(x,θ) for an input x. In binary classification problems, a common loss function is the zero/one loss function L0/1, which assigns a loss equal to one in the case of wrong prediction, and zero otherwise:

$$
\begin{align}
L_{0/1}: \mathcal{Y} \times \mathcal{Y} &\rightarrow& \{0,1\} \\
y,\hat{y} &= & 
\begin{cases}
    1,& \text{if } y \ne \hat{y}\\
    0,& \text{if } y=\hat{y}
\end{cases}
\end{align}
$$

> [!NOTE]'''
The zero/one loss function is a standard loss function for binary classification problems. It is however not well suited for credit card fraud detection problems, due to the high-class imbalance (much more genuine than fraudulent transactions). Estimating the performance of a fraud detection system is a non-trivial issue, which will be covered in depth in [Chapter 4[(Performance_Metrics).
```

To obtain a fair estimate of a prediction model performance, an important methodological practice, known as *validation*, is to evaluate the performance of a prediction model on data that were not used for training. This is achieved by splitting the dataset, before training, into a *training set* and a *validation set*.  The training set is used for the training of the prediction model (that is, to find the parameters $\theta$ that minimize the loss on the training set). Once the parameters $\theta$ have been fixed, the loss is estimated with the validation set, which gives a better estimate of the performance that the prediction model is expected to have on future (and unseen) transactions. 


```{note}
Particular care must be taken in practice when splitting the dataset into training and validation sets, due to the sequential nature of credit card transactions, and the delay in fraud reporting. These issues will be addressed in detail in [Chapter 5](Model_Validation_And_Selection).    
```

The supervised learning procedure typically consists of training a set of prediction models and estimating their performances using the validation set. At the end of the procedure, the model that is assumed to provide the best performance (that is, the lowest loss on the validation set) is selected, and used for providing predictions on new transactions (See Fig. 2).

A wide range of methods exists for designing and training prediction models. This partly explains the large research literature on ML for CCFD, where papers usually focus on one or a couple of prediction methods. The survey from Priscilla et al. in 2019 {cite}`priscilla2019credit` provides a good overview of the machine learning methods that have been considered for the problem of CCFD. Their survey covered close to one hundred research papers, identifying for each paper which ML techniques were used, see Fig. 4.  

![alt text](https://fraud-detection-handbook.github.io/fraud-detection-handbook/_images/ReviewMLforCCFD_2019_Table.png)
<p style="text-align: center;">
Fig. 4. Usage frequency of ML techniques in CCFD. Source: Priscilla et al., 2019 {cite}`priscilla2019credit`. References given in the table are in {cite}`priscilla2019credit`. 
</p>

The classification of learning techniques into 'high-level' categories is not a simple exercise since there often exists methodological, algorithmic, or historical connections among them. Priscilla et al. chose to divide approaches into four groups: Supervised learning, unsupervised learning, ensemble learning, and deep learning. It could be argued that ensemble learning and deep learning are part of supervised learning since they require labels to be known. Also, deep learning and neural networks can be considered to be part of the same category.  

Covering all ML techniques is out of scope for this book. Rather, our goal is to provide a reference and reproducible framework for CCFD. We decided, based on our research works, to cover five types of methods: logistic regression (LR), decision trees (DT), Random forests (RF), Boosting, and Neural networks/Deep learning (NN/DL). LR and DT were chosen due to their simplicity and interpretability. RF and Boosting were chosen since they are currently considered to be state-of-the-art in terms of performance. NN/DL methods were chosen since they provide promising research directions.  

(ML_For_CCFD_Challenges)=
## Overview of challenges

ML for CCFD is a notoriously difficult problem. We summarise below the challenges commonly highlighted in the reviews on the topic {cite}`lucas2020credit,priscilla2019credit,mekterovic2018systematic,adewumi2017survey,zojaji2016survey`.

**Class imbalance**: Transaction data contain much more legitimate than fraudulent transactions: The percentage of fraudulent transactions in a real-world dataset is typically well under 1%. Learning from imbalanced data is a difficult task since most learning algorithms do not handle well large differences between classes. Dealing with class imbalance requires the use of additional learning strategies like sampling or loss weighting, a topic known as *imbalanced learning*. 

**Concept drift**: Transaction and fraud patterns change over time. On the one hand, the spending habits of credit card users are different during weekdays, weekends, vacation periods, and more generally evolve over time. On the other hand, fraudsters adopt new techniques as the old ones become obsolete. These time-dependent changes in the distributions of transactions and frauds are referred to as *concept drift*. Concept drift requires the design of learning strategies that can cope with temporal changes in statistical distributions, a topic known as *online learning*. The concept drift problem is accentuated in practice by the delayed feedbacks (See section {ref}`Fraud_Detection_System`).

**Near real-time requirements**: Fraud detection systems must be able to quickly detect fraudulent transactions. Given the potentially high volume of transaction data (millions of transactions per day), classification times as low as tens of milliseconds may be required. This challenge closely relates to the *parallelization* and *scalability* of fraud detection systems.

**Categorical features**: Transactional data typically contain numerous *categorical* features, such as the ID of a customer, a terminal, the card type, and so on. Categorical features are not well handled by machine learning algorithms and must be transformed into numerical features. Common strategies for transforming categorical features include feature aggregation, graph-based transformation, or deep-learning approaches such as feature embeddings.

**Sequential modeling**: Each terminal and/or customer generates a stream of sequential data with unique characteristics. An important challenge of fraud detection consists in modeling these streams to better characterize their expected behaviors and detect when abnormal behaviors occur. Modeling may be done by aggregating features over time (for example, keeping track of the mean frequency or transaction amounts of a customer), or by relying on sequential prediction models (such as hidden Markov models, or recurrent neural networks for example). 

**Class overlap**: The last two challenges can be associated with the more general challenge of overlapping between the two classes. With only raw information about a transaction, distinguishing between a fraudulent or a genuine transaction is close to impossible. This issue is commonly addressed using feature engineering techniques, that add contextual information to raw payment information.  

**Performance measures**: Standard measures for classification systems, such as the mean misclassification error or the AUC ROC, are not well suited for detection problems due to the class imbalance issue, and the complex cost structure of fraud detection. A fraud detection system should be able to maximize the detection of fraudulent transactions while minimizing the number of incorrectly predicted frauds (false positives). It is often necessary to consider multiple measures to assess the overall performance of a fraud detection system. Despite its central role in the design of a fraud detection system, there is currently no consensus on which set of performance measures should be used. 

**Lack of public datasets**: For obvious confidentiality reasons, real-world credit card transactions cannot be publicly shared. There exists only one publicly shared dataset, which was made available on Kaggle {cite}`Kaggle2016` by our team in 2016. Despite its limitations (only two days of data, and obfuscated features), the dataset has been widely used in the research literature, and is one of the most upvoted and downloaded on Kaggle. The scarcity of datasets for fraud detection is also true with simulated data: No simulator or reference simulated datasets are yet available. As a result, most research works cannot be reproduced, making impossible the comparison of different techniques by independent researchers.    