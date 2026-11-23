# [學校簡稱] [學號] [系級簡稱] [姓名] AI 幻覺與事實查核

## 1. LLM Wiki 主題與簡介
我的 LLM Wiki 主題為「AI 也會說謊？認識生成式 AI 幻覺與事實查核」。目標是整理 AI 幻覺的定義、成因、風險及查核方式，讓第一次接觸生成式 AI 的同學也能理解。知識來源使用 IBM、OpenAI、NIST、Google Cloud、Anthropic 五份資料，各自以 S01–S05 編號追蹤。

## 2. LLM Wiki 連結或成果
- Wiki 網頁：[部署後填入 https://你的帳號.github.io/你的repo/wiki.html]
- 原始 Wiki / 來源資料：[部署後填入 GitHub Repo 的 wiki 資料夾連結]
- 已 ingest 來源：[完成後填入工具實際回報的數量，至少 5]
- 截圖：docs/screenshots/01-ingest.png、02-status.png、03-lint.png

## 3. 教學 HTML 簡報連結
[部署後填入 https://你的帳號.github.io/你的repo/]
簡報從定義、成因、案例，延伸到 Grounding、查核步驟與互動練習。支援鍵盤、上一頁/下一頁與手機瀏覽。

## 4. Loop / Graph 設計
蒐集資料 → G1 來源審查 → Ingest 到 Wiki → G2 Wiki 健檢 → Query Wiki / 大綱 → G3 主張與來源核對 → HTML 生成 → G4 功能測試 → GitHub Pages。若來源或 Wiki 有問題返回 ingest；若內容不符則返回 query；若只有介面問題則回到 HTML 調整。詳細圖見 docs/workflow.md。

## 5. 一次實際執行與檢查紀錄
[完成後描述：日期、工具顯示的 ingest 數量、Wiki lint 實際結果、問了一個什麼問題、HTML 點擊測試如何、公開 URL 是否正常。參見 docs/verification-log.md。]

## 6. 反思
[請依你真的遇到的問題修改：最常出錯的節點是 ______。原本在 ______ 才查核；後來把檢查提前到 ______，因為 ______。我把 Graph 修改成 ______，並以 ______ 再次測試。]
