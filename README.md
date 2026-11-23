# AI 也會說謊？｜LLM Wiki × 教學 HTML 簡報

> TAICA 作業專案範本（2026-11-23）。已附來源閱讀筆記、Wiki 內容初稿、可離線觀看的教學簡報、來源映射、Workflow 和檢查紀錄表。

## 立刻預覽

- 雙擊 `index.html`：14 張教學 HTML 簡報（←／→ 翻頁、進度條、互動練習）
- 雙擊 `wiki.html`：五篇來源與五個概念的可搜尋知識導覽
- 雙擊 `workflow.html`：Loop / Graph 流程圖與返工條件
- `wiki/`：Markdown Wiki 概念頁與來源頁初稿
- `ingest/`：**五份分開的中文來源閱讀筆記**；每份附官方原始連結。這是摘要筆記，不是假冒原文全文。

## Part A — 先討論、後生成
1. 在 ChatGPT / VS Code AI 助手中使用 `docs/prompts.md` 的 Prompt A 討論目標與架構，不要直接要求生成 HTML。
2. 核對五篇來源：S01 IBM、S02 OpenAI、S03 NIST、S04 Google Cloud、S05 Anthropic。
3. 取得確認後，再進行 wiki ingest 和簡報生成。

## Part B — 實際完成五篇 ingest（重要）
此專案目前包含**AI 輔助整理的 Wiki 初稿**與五份待 ingest 檔案；下載 ZIP 本身不代表你已在課堂要求的工具執行過 ingest。

### 路線 1：若老師指定或你可使用 Microsoft LLM Wiki 的 VS Code 擴充套件
依 https://github.com/microsoft/llmwiki 的官方安裝方式：需要 Node.js 20+、VS Code 1.109+ 和 GitHub Copilot 訂閱，原始碼 clone 後 `npm ci`、`npm run build`、`npm run package --workspace=packages/vscode`，最後從 `.vsix` 安裝。這些是工具的前置條件；如果沒有 Copilot，跳看路線 2。

1. 用 VS Code 開啟解壓縮後的這個專案資料夾。
2. `Ctrl+Shift+P` → `LLM Wiki: Initialize Wiki`：初始化專案的 `.wiki/`。
3. `Ctrl+Shift+P` → `LLM Wiki: Ingest Files or Folder`：選 `Files` 模式，選中 `ingest/` 五個 `.md` 檔。這些來源筆記是不同原始文章各自整理而成。**若教師要求原文整篇 ingest，先把五篇官方頁面經瀏覽器列印成 PDF，再選那五個 PDF。**
4. 透過擴充套件的 `LLM Wiki: Show Status` 記錄來源數（應至少 5）。
5. 開 Copilot Chat（Agent 模式），要求「依每個來源的概念建立交叉連結，檢查矛盾」。再用 `/wiki-research` 或 `/wiki-ask` 查詢「AI 幻覺有何原因？根據哪篇資料？」，保存輸出與來源。
6. `Ctrl+Shift+P` → `LLM Wiki: Run Lint`：檢查品質。
7. 截圖：ingest 前後／status／query 引文／lint；填入 `docs/verification-log.md`。
8. 如生成的 `.wiki/` Wiki 與本範本 `wiki/` 有差異，應以**實際生成的資料**為準，修改 `docs/source-mapping.csv` 與投影片，才能真實聲稱 Wiki 支持簡報。

### 路線 2：沒有 Copilot 或課堂沒有指定特定 Wiki 工具
用一般 AI 助手讀取五個 `ingest/S*.md`，請 AI 完成 Prompt B 的來源抽取、概念歸納、交叉連結與檢查，將結果存成 `wiki/` Markdown；每一步保存對話、輸入來源與檢查結果。這可呈現 LLM 維護的 Wiki 工作流程，但**不應謊稱使用了 Microsoft 擴充套件或其 `status/lint` 指令**。請向課堂確認是否接受此種 Markdown + LLM Wiki 模式。

## Part C — 查看 HTML 並驗證
- 本機雙擊三個 HTML。桌機按左右方向鍵切換；最後一頁應有五個來源連結；第 12 頁可點互動練習。
- 先執行 `python run_checks.py`，再親自手動測試 Chrome 視窗與縮窄寬度。
- 來源對應表在 `docs/source-mapping.csv`。如 wiki 被更新，以真實內容同步調整投影片；不能只保留舊版展示網站。
- 截圖與測試細節填入 `docs/verification-log.md`。

## Part D — 發布 GitHub Pages
1. 在 GitHub 建立新公開 Repository（例如 `ai-hallucination-wiki`）。
2. 以 VS Code 終端機（PowerShell）在**專案根目錄**執行：
   ```powershell
   git init
   git add .
   git commit -m "feat: add LLM wiki and interactive AI literacy slides"
   git branch -M main
   git remote add origin https://github.com/你的帳號/ai-hallucination-wiki.git
   git push -u origin main
   ```
   如果你用 GitHub 網頁上傳檔案，也可以直接拖曳解壓縮後檔案；要保留子資料夾結構。
3. Repository → Settings → Pages → Build and deployment → Deploy from a branch → Branch `main`, Folder `/(root)` → Save。
4. 完成後實際開啟 `https://你的帳號.github.io/ai-hallucination-wiki/`（投影片）、`/wiki.html`（Wiki）及 `/workflow.html`（Graph）。**真正公開 URL 必須等網站部署成功後才能填入作業。**
5. 手機開啟網站、檢查按鈕/來源；如果 GitHub Pages 404，檢查 repo 名稱、分支與 `index.html` 是否在根目錄。

## Part E — 繳交
將 `docs/submission-template.md` 的六個項目填成作業文字；標題依老師「學校 學號 系級 姓名 主題」格式；補上公開的 Wiki/簡報連結，以及實際操作截圖與**真實**反思。至少有：五篇 ingest、Wiki 查詢、來源映射、HTML、Graph、品質檢查、修正結果。

## 內容出處與限制
資料連結與摘要見 `ingest/`，不重製原文整篇內容。此專案內的 Wiki 初稿和 HTML 是基於公開來源協助撰寫的教學內容；本範本不虛構使用者已經執行的 LLM Wiki ingest、截圖、部署或真人反思。
