# AI 幻覺與事實查核｜LLM Wiki

本 Wiki 依序處理五份 `ingest/` 中文來源閱讀筆記，並以可追溯的來源 ID（S01–S05）整理概念。`ingest/` 檔案是原始網頁的摘要筆記，不是原文全文；各來源頁會標明本次核對範圍與限制。

## 知識概念

- [幻覺是什麼](concepts/definition.md) — 定義與可驗證主張
- [為什麼會發生](concepts/causes.md) — 生成模式、資料限制及評估誘因
- [查核五步驟](concepts/fact-checking.md) — 本 Wiki 的教學化核查流程
- [Grounding 與 RAG](concepts/grounding.md) — 連接外部資料及其限制
- [如何降低風險](concepts/mitigation.md) — 不確定性、引文與人工覆核

## 來源

- [S01 IBM｜What are AI hallucinations?](sources/S01.md) — 定義、可能成因、例子與風險
- [S02 OpenAI｜Why language models hallucinate](sources/S02.md) — 評估誘因與猜測
- [S03 NIST｜Generative AI Profile](sources/S03.md) — 風險管理；本次尚待核實報告正文
- [S04 Google Cloud｜Grounding overview](sources/S04.md) — Grounding 與 RAG
- [S05 Anthropic｜Reduce hallucinations](sources/S05.md) — 不確定性、引文核對與限制來源

## 來源到概念索引

| 來源 | 主要概念 |
|---|---|
| [S01](sources/S01.md) | [定義](concepts/definition.md)、[成因](concepts/causes.md)、[查核](concepts/fact-checking.md)、[風險降低](concepts/mitigation.md) |
| [S02](sources/S02.md) | [定義](concepts/definition.md)、[成因](concepts/causes.md)、[風險降低](concepts/mitigation.md) |
| [S03](sources/S03.md) | [風險降低](concepts/mitigation.md)（報告正文待核對） |
| [S04](sources/S04.md) | [Grounding 與 RAG](concepts/grounding.md)、[查核](concepts/fact-checking.md)、[風險降低](concepts/mitigation.md) |
| [S05](sources/S05.md) | [查核](concepts/fact-checking.md)、[Grounding 與 RAG](concepts/grounding.md)、[風險降低](concepts/mitigation.md) |

## 執行紀錄

- [wiki/log.md](log.md) — 本次逐篇處理、Wiki query 與 lint 紀錄
