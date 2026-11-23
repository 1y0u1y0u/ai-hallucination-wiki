# Wiki 執行紀錄

## 2026-11-23｜逐篇 Markdown ingest 與 Wiki query

### 執行方式與範圍

- 逐一讀取 `ingest/S01_ibm.md` 至 `ingest/S05_anthropic.md`，並保留各自的來源 ID、機構、原始網址及摘要筆記性質。
- 逐一核對五個原始網址的可讀取頁面內容，再更新對應的 `wiki/sources/S01.md` 至 `S05.md`；不是只重新命名或複製原有 Wiki 初稿。
- 更新全部五個概念頁及 `wiki/index.md` 的來源對照與交叉連結。
- 本次實際執行的是本地 Markdown Wiki ingest。檢查 VS Code 擴充套件清單時未發現 Microsoft LLM Wiki 擴充套件，也未找到 `llmwiki` 命令；因此**沒有執行**擴充套件的 Initialize、Ingest、Status 或 Run Lint 命令，也不將本紀錄冒稱為該擴充套件的執行輸出。
- S03 的 NIST 出版資料頁可讀取，但 PDF 無法由本次工具解析出正文；相關摘要已標示為待核對原報告，未當成已驗證的正文引述。

### 逐來源處理

| 來源 | 實際處理 | 檢查結果 |
|---|---|---|
| [S01](sources/S01.md) | 讀取 [輸入筆記](../ingest/S01_ibm.md) 和 IBM 網頁；重寫來源頁，摘錄定義、生成模式、資料限制及風險；連結定義、成因、查核、降低風險頁。 | 網頁可讀取；摘要主張對應 S01。 |
| [S02](sources/S02.md) | 讀取 [輸入筆記](../ingest/S02_openai.md) 和 OpenAI 網頁；重寫來源頁，區分猜測誘因與直接成因；連結定義、成因及降低風險頁。 | 網頁可讀取；保留「評估方式不直接造成幻覺」的界線。 |
| [S03](sources/S03.md) | 讀取 [輸入筆記](../ingest/S03_nist.md) 和 NIST 出版資料頁；保留 PDF 連結及未能核實正文的限制；僅連結風險降低頁。 | 出版頁可讀取；PDF 正文未能解析，摘要標示待核對，未提升為已驗證事實。 |
| [S04](sources/S04.md) | 讀取 [輸入筆記](../ingest/S04_google-cloud.md) 和 Google Cloud 文件；重寫來源頁，區分 Grounding 與 RAG；連結 Grounding、查核及降低風險頁。 | 文件可讀取；未把降低機會誇大為正確性保證。 |
| [S05](sources/S05.md) | 讀取 [輸入筆記](../ingest/S05_anthropic.md) 和 Anthropic 文件；重寫來源頁，整理不確定性、直接引文與逐項核對；連結 Grounding、查核及降低風險頁。 | 文件可讀取；保留方法不能完全消除錯誤的限制。 |

### Wiki query

**問題**：為什麼大型語言模型會產生幻覺？如何降低風險？

**依 Wiki 得出的回答**：大型語言模型依訓練資料與前文模式產生看似合適的後續內容；文字看似合理，不代表符合真實資料。資料錯誤、缺漏或含糊也可能增加不可靠輸出（[S01](sources/S01.md)）。此外，若評估只重視答對率、不鼓勵承認不確定，模型可能更傾向猜測；這是評估誘因之一，不是所有幻覺的唯一成因（[S02](sources/S02.md)）。

可降低風險的方法包括允許模型說不知道或要求補充資料（[S02](sources/S02.md)、[S05](sources/S05.md)）；要求回答根據可查驗的資料，並檢查引用是否真實且支持主張（[S04](sources/S04.md)、[S05](sources/S05.md)）；重要內容仍由人核驗，因為這些方法只能降低風險，不能保證沒有錯誤（[S01](sources/S01.md)、[S05](sources/S05.md)）。S03 對風險管理的摘要尚待原報告正文核實，本回答不依賴該項未核實主張。

### Lint 與檢查結果

- **Wiki 連結與關聯 lint：通過。** 以一次性 Python 檢查遍歷 `wiki/` 的 Markdown 檔案：12 個 Wiki 頁面、101 個本地連結；未發現斷裂連結或錨點、無效來源 ID、索引遺漏、缺少來源—概念回鏈或從索引不可達的頁面。
- **人工內容檢查：通過（有明示來源限制）。** 修正舊成因頁將「輸入不清」當成已支持主張的問題；來源頁補齊相關概念回鏈；將 OpenAI 的評估誘因明確限縮為可能原因而非唯一成因；S04/S05 的「降低風險」未寫成保證。S03 報告正文仍未核實，已在來源頁和概念頁明確標示，不作為已驗證正文主張。
- **專案檢查：通過。** `py -3 run_checks.py` 輸出 `PASS: 14 slides; 5 source notes; 5 source pages; 5 concept pages; source-to-slide links; controls; supporting documents.` 該腳本是靜態投影片檢查，不代表 Microsoft LLM Wiki 擴充套件執行成功。
- **剩餘限制：** 本次沒有 Microsoft LLM Wiki 擴充套件可供執行，因此以上是本地 Markdown Wiki ingest 與手動 query/lint，不是該擴充套件的 Status 或 Run Lint 結果。自動連結檢查也不能取代逐段來源事實審查；尤其 S03 正文仍待核對。
