## 簡介 Introduction

本章提供了信用卡欺詐檢測問題的背景，探討問題是什麼，目前如何解決，以及為什麼機器學習可以幫助提供有效的解決方案。本章結構如下。

This chapter provides the background to the problem of credit card fraud detection. It addresses what the problem is, how it is currently solved, and why machine learning can help in providing effective solutions. The chapter is structured as follows. 

首先，"信用卡欺詐場景" 討論信用卡欺詐問題及其原因和相關損失，依據本書撰寫時有關該主題的最新權威報告（特別是 2019 年的最新 Nilson 報告 [rep19] 和歐洲中央銀行 2020 年關於信用卡欺詐檢測的報告 [Ban20]），我們簡要總結了已知欺詐者用來進行欺詐交易的技術及其相關成本，本節並且討論欺詐預防技術，範圍從眾所周知的 PIN 碼到更高級的技術，例如生物特徵識別。

** Credit Card Fraud Scenarios: ** First, addresses the problem of credit card fraud together with its causes and related losses. Relying on the latest authoritative reports on the topic at the writing of this book (in particular, the latest Nilson report from 2019 {cite}`NilsonReport2019` and the European Central Bank report on credit card fraud detection from 2020 {cite}`ECB2020`), we briefly summarise the techniques known to be employed by fraudsters to perform fraudulent transactions, and their associated costs. The section also discusses *fraud prevention* techniques, which range from the well-known PIN codes to more advanced techniques such as biometric identification.

接著，詐欺偵測系統介紹欺詐檢測系統的操作層面，概述如何在現實世界的欺詐檢測系統中執行欺詐檢測。理解這部份很重要，因為它證明有效的檢測需要自動化系統和欺詐調查員的組合，這具有重要意義。首先，自動化系統應該優化欺詐調查員的工作量。其次，自動化系統和人工調查員在不同的時間尺度上工作：雖然自動化系統通常會在不到一秒的時間內為交易提供風險評分，但欺詐調查通常需要聯繫客戶以確認欺詐行為，這可能需要幾天或幾週的時間。這些特性對本書使用的方法有重要影響。

** Fraud_Detection_System** covers the operational side of a fraud detection system. It provides an overview of how fraud detection is performed in a real-world fraud detection system. Its understanding is important since it puts into evidence that effective detection requires both a mix of automated systems and fraud investigators. This has non-trivial implications. First, automated systems should optimize the workload of fraud investigators. Second, automated systems and human investigators work at different time scales: while automated systems usually provide risk scores for transactions in less than a second, fraud investigations usually require contacting a client to confirm a fraud, which can take days, or weeks. These peculiarities have important implications in the methodology used throughout this book.

最後，在信用卡機器學習章節，回顧用於信用卡欺詐檢測的機器學習技術的主題。 現在很明顯，機器學習技術可以為信用卡欺詐檢測問題提供有效的解決方案，並且關於該主題的研究文獻在過去十年中呈指數增長。 該部分對過去五年（2015-2020）對該領域的最新調查進行綜合回顧，強調這些調查中提出的核心原則，並總結欺詐檢測系統的主要挑戰。

Finally, [Section 2.4](ML_For_CCFD) reviews the topic of machine learning techniques for credit card fraud detection. It is now clear that machine learning techniques can provide effective solutions to the problem of credit card fraud detection, and the research literature on the topic has grown exponentially in the last decade. The section makes a metareview of the latest surveys on the domain in the last five years (2015-2020). It highlights the core principles presented in these surveys and summarizes the main challenges of fraud detection systems. 

### 信用卡詐騙場景 Credit card fraud scenarios

信用卡欺詐活動造成的全球經濟損失價值數百億美元，根據 Statistic Brain Research Institute [Ins18]統計，十歲以上的美國人即曾經成為信用卡欺詐的受害者（中位數為 $399 美元）。根據最新的歐洲中央銀行 (ECB) 報告 [Ban20]，總水平2018 年，單一歐洲支付區 (SEPA) 的信用卡欺詐損失達 18 億歐元。

Worldwide financial losses caused by credit card fraudulent activities are worth tens of billions of dollars. One American over ten has been a victim of credit card fraud (median amount of $399), according to the Statistic Brain Research Institute {cite}`StatisticBrain2018`. According to the latest European Central Bank (ECB) report {cite}`ECB2020`, the total level of card fraud losses amounted to €1.8 billion in 2018 in the Single European Payment Area (SEPA).

存在多種可能導致欺詐者成功地使用信用卡進行欺詐性支付的場景，目前還沒有關於信用卡欺詐類型的明確分類法，儘管已知某些模式比其他模式更頻繁地發生。還應該注意的是，欺詐檢測是一場貓捉老鼠的遊戲，欺詐模式會隨著時間而變化。隨著技術的發展，無論是在欺詐預防還是支付系統的易用性方面，欺詐技術也在不斷發展。他們因應時代變遷，從舊的（現在是固定的）目標，轉移到新技術的脆弱性，他們還受益於真實交易的數量和特徵的不斷變化。

There exists a wide variety of scenarios that may lead a fraudster to successfully perform fraudulent payments with a credit card. There is currently no definite taxonomy on credit card fraud types, though certain patterns are known to occur more frequently than others. It should also be noted that fraud detection is a cat and mouse game, where fraudulent patterns change over time. As technology evolves, both in terms of fraud prevention and ease of use of payment systems, so do fraudster techniques. They adapt by moving from the old (and by now fixed) targets to the vulnerability of the new technologies. They also benefit from the constant changes in volume and characteristics of genuine transactions.

### 有卡與無卡欺詐 Card-present vs Card-not-present frauds

區分下列兩種實務場景很有用，第一種稱為有卡 (CP) 場景，是指需要實體卡的場景，例如商店交易（也稱為銷售點 - POS）或現金點交易（例如在自動櫃員機 - ATM）。第二種稱為無卡（CNP）場景，是指不需要使用實體卡的場景，包括通過網際網路、電話或電子郵件進行的支付。

It is useful to distinguish two transaction scenarios. The first, called *card-present* (CP) scenarios, refer to scenarios where a physical card is needed, such as transactions at a store (also referred to as a point-of-sale - POS) or transactions at a cashpoint (for instance at an automated teller machine - ATM). The second, called *card-not-present* (CNP) scenarios, refers to scenarios where a physical card does not need to be used, which encompasses payments performed on the Internet, by phone, or by mail. 

這種區別很重要，因為用於破獲卡片的技術會有所不同，具體取決於是否需要製作卡片的實體副本。更重要的是，與 CP 相比，欺詐者最近更有可能利用 CNP 場景的缺陷，這可能是因為 CP 場景已經存在了 20 多年，並且對欺詐攻擊變得相當強大，這主要歸功於 EMV 技術（Europay Mastercard和 Visa，即芯片嵌入卡）。另一個原因是對阻止實體卡片的簡單考慮，通常有助於防止 CP 欺詐。正如 2019 年 Nilson 報告所述，CNP 情景佔 2018 年所有欺詐損失的 54%，而僅佔全球所有購買量 (CNP+POS+ATM) [rep19] 的不到 15%。在歐洲，CNP 欺詐的比例甚至更高，在歐洲中央銀行的 2020 年卡欺詐報告 [Ban20] 中，據報導佔 SEPA 內發行的卡的所有交易的 79%，如下圖所示。

This distinction is important since the techniques used to compromise a card vary, depending on whether a physical copy of the card needs to be produced or not. More importantly, fraudsters are recently more likely to exploit the deficiencies of CNP scenarios than CP ones, probably because CP scenarios have existed for more than two decades now, and have become pretty robust to fraud attacks, notably thanks to the EMV technology (Europay Mastercard and Visa, i.e. chip-embedded cards). Another reason is that simple considerations on physical barriers can often help to prevent CP frauds. As stated in the 2019 Nilson report, CNP scenarios accounted for 54% of all losses to fraud for the year 2018, while only accounting for less than 15% of all purchase volume worldwide (CNP+POS+ATM) {cite}`NilsonReport2019`. The proportion of CNP fraud is even higher in Europe and was reported to account for 79% of all transactions from cards issued within SEPA in the 2020 report on card fraud of the European Central Bank {cite}`ECB2020`, as reported in the figure below. 

![alt text](https://fraud-detection-handbook.github.io/fraud-detection-handbook/_images/SEPA_FraudVolumePerType.png)
<p style="text-align: center;">
圖 1. 使用在 SEPA 內發行的卡進行的信用卡欺詐總價值的演變。無卡欺詐(圖中黃色部分)佔報告的欺詐的大部分。
Fig. 1. Evolution of total value of card fraud using cards issued within SEPA. <br>Card-not-present frauds account for the majority of reported frauds.
</p>

#### 有卡欺詐 Card-present frauds

當欺詐者設法在 ATM 或 POS 上使用實體支付卡進行成功的欺詐交易時，就會發生有卡欺詐。在此環境中，欺詐場景通常分為卡丟失或被盜、偽造卡和卡未收到。

Card-present frauds occur when a fraudster manages to make a successful fraudulent transaction using a physical payment card, either at an ATM or a POS. In this setting, fraud scenarios are usually categorized as *lost or stolen cards*, *counterfeited cards*, and *card not received*.

**信用卡丟失或被盜**：該卡屬於合法客戶，在丟失或被盜後落入欺詐者手中。這是有卡欺詐設置中最常見的欺詐類型，只要卡未被其合法所有者阻止，欺詐者就可以進行交易。在這種情況下，欺詐者通常會盡可能快地花錢。

**Lost or stolen card**: The card belongs to a legitimate customer, and gets in the hands of a fraudster after a loss or a theft. This is the most common type of fraud in the card-present fraud setting and allows a fraudster to make transactions as long as the card is not blocked by its legitimate owner. In this scenario, the fraudster usually tries to spend as much as possible and as quickly as possible.

**假卡**：假卡是由欺詐者通過壓印卡的資訊製成的，此類資訊通常是通過側錄合法客戶的卡而獲得的，而他們不會注意到。由於合法所有者不知道他們的卡副本的存在，欺詐的來源可能更難以識別，因為欺詐者可能會等待很長時間才能使用假卡。芯片和 PIN（又名 EMV）技術的使用增加減少了這種類型的欺詐。

**Counterfeited card**: A fake card is produced by a fraudster, by imprinting the information of a card. Such information is usually obtained by *skimming* the card of the legitimate customer, without them noticing. Since the legitimate owners are not aware of the existence of a copy of their card, the source of the fraud might be more difficult to identify, since the fraudster can wait a long time before making use of the fake card. The increased use of chip-and-PIN (aka EMV) technology has reduced this type of fraud. 

**未收到卡**：該卡被合法客戶郵箱中的欺詐者截取。如果客戶訂購新卡被攔截，或者欺詐者設法在合法客戶不知情的情況下訂購新卡（例如通過欺詐性存取他們的銀行帳戶）並將其交付給不同的客戶，則可能會發生這種情況地址。在前一種情況下，客戶可能會迅速警告銀行沒有收到他們的信用卡，並將其凍結。後一種情況可能更難檢測，因為客戶不知道訂購了一張新卡。

**Card not received**: The card was intercepted by a fraudster in the mailbox of a legitimate customer. This may happen if a customer orders a new card, which gets intercepted, or if a fraudster manages to order a new card without the knowledge of the legitimate customer (for example by accessing fraudulently their bank account), and have it delivered to a different address. In the former case, the customers may quickly warn the bank that their card was not received, and have it blocked. The latter case can be harder to detect since the customer is not aware that a new card was ordered. 

歐洲中央銀行報告了 2018 年這些欺詐類型在有卡場景中所佔比例的統計數據，見下圖 [Ban20]。

Statistics on the proportion of these fraud types in card-present scenarios were reported by the European Central Bank for 2018, see the chart below {cite}`ECB2020`.

![alt text](https://fraud-detection-handbook.github.io/fraud-detection-handbook/_images/SEPA_FraudType_CardPresent.png)
<p style="text-align: center;">
圖2. SEPA 內按類別劃分的持卡欺詐價值的演變和細分。
Fig. 2. Evolution and breakdown of the value of card-present fraud by category within SEPA.
</p>

欺詐的主要類別是丟失和被盜，以及偽造卡，而未收到卡場景在欺詐損失中所佔比例非常小。 值得注意的是，無論是在 ATM 還是 POS 進行付款，這些欺詐比例大致相同，總體而言，有卡設置中的欺詐數量趨於減少。

The main categories of frauds are *lost and stolen*, and *counterfeited cards*, whereas *card not received* scenarios account for a very small proportion of fraud losses. It is worth noting that these fraud proportions are around the same whether payments were made at an ATM or a POS, and that overall, the amount of frauds in card-present settings tends to decrease.

#### 無卡欺詐 Card-not-present frauds

無卡是指通過郵件、電話或互聯網遠程進行的一般欺詐類別，僅使用卡上的部分資訊。

Card-not-present refers to the general category of frauds conducted remotely, either by mail, phone, or on the Internet, using only some of the information present on a card. 

總體而言，關於此類欺詐原因的統計數據較少。例如，與有卡欺詐相反，歐洲中央銀行只要求信用卡支付方案運營商，報告整體 CNP 欺詐損失。

Overall, there are fewer statistics available on the cause of such frauds. For example, contrary to card-present frauds, the European Central Bank only requires the card payment scheme operators to report the overall CNP fraud losses.

然而，眾所周知，大多數 CNP 欺詐是非法獲得支付憑證（例如卡號）的直接後果，若非來自資料洩露，即為直接來自持卡人（例如通過網絡釣魚、詐騙簡訊）。同樣值得注意的是，此類憑據通常不直接使用，而是在地下網絡市場（暗網）上出售，後來被犯罪集團使用。竊取資料的犯罪分子通常與實施欺詐的犯罪分子不同 [Ban20, rep19 ]。

It is however known that most CNP frauds are a direct consequence of illegally obtained payment credentials (e.g., card numbers), either from data breaches or sometimes directly from the cardholders (e.g. via phishing, scam text messages). Also worth noting, such credentials are usually not used directly, but rather put on sale on underground web marketplaces (the *dark web*), and later used by criminal groups. Criminals who steal data are usually a different group than criminals who perpetrate frauds {cite}`ECB2020,NilsonReport2019`. 

無卡欺詐通常涉及的資料包括卡號、卡到期日期、卡安全碼和個人賬單資訊（例如持卡人的地址）。

The data that is generally involved in card-not-present fraud involves the card number, card expiration date, card security code, and personal billing information (such as the cardholder’s address).
