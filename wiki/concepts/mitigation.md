# 如何降低風險

來源提出的做法各有用途，沒有任何一項能保證錯誤完全消失：

- **允許表達不確定**：當資訊不足時，讓模型可以說不知道或要求補充資料（[S02](../sources/S02.md)、[S05](../sources/S05.md)）。
- **以資料 grounding**：要求回答根據指定資料，提供可追溯的來源連結；仍要核對資料和引用是否支持回答（[S04](../sources/S04.md)、[S05](../sources/S05.md)）。
- **覆核重要主張**：逐項檢查引文和來源；高風險用途應由人確認。S03 的輸入筆記提到 NIST 風險管理，但本次尚未核實報告正文，詳見 [S03 使用界線](../sources/S03.md#使用界線)。

## 依據來源

- [S02｜OpenAI：不確定與評估誘因](../sources/S02.md)
- [S03｜NIST：待核對原報告正文](../sources/S03.md)
- [S04｜Google Cloud：Grounding](../sources/S04.md)
- [S05｜Anthropic：引文及限制來源](../sources/S05.md)

## 延伸概念

- [為什麼會發生](causes.md)：對應可能成因。
- [Grounding 與 RAG](grounding.md)：詳述來源連接方式。
- [查核五步驟](fact-checking.md)：執行逐項核驗。
- [幻覺是什麼](definition.md)：辨認要降低的錯誤輸出。
