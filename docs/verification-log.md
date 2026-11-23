# 檢查紀錄：範本與實際操作

## A. 目前已實施的檔案層檢查
本專案提供 `python run_checks.py`，用以驗證頁數、五篇來源檔、來源對應、Wiki 概念檔、HTML 控制鍵與本機連結。**這是靜態檢查，不代表已在你的電腦上操作 LLM Wiki 擴充套件或已部署網站。**

## A2. 已完成的自動化瀏覽器測試（2026-11-23）
- 測試方式：以本機 Chromium headless 透過 Playwright `set_content` 載入 HTML（執行 HTML 內的 CSS/JavaScript）；因執行環境阻擋 file:// 和 localhost 導覽，**此項測試不代表 GitHub Pages 上線測試**。
- 桌面 1366×768：通過首頁渲染、右方向鍵至第 2 頁、下一頁至第 3 頁、End 至第 14 頁、上一頁回第 12 頁、練習題正確選項回饋；並另外確認 #slide-12 深連結可正確開啟第 12 頁。
- 手機 390×844：通過相同操作與渲染；Wiki 搜尋可過濾卡片；Workflow 有 4 條修正路線。
- 兩個視窗的 JavaScript page error = 0；封面截圖：`docs/screenshots/generated-preview-desktop.png` 和 `generated-preview-mobile.png`。
- 這是 HTML 功能檢查，不包含 PDF 全文 ingest、GitHub Pages URL 驗證、手機實機測試或已安裝的 LLM Wiki 官方工具操作。這些項目仍須補做。

## B. 需要你實際執行後填寫（不可事先宣稱通過）
| 節點 | 實際執行紀錄 | 結果 | 證據截圖 |
|---|---|---|---|
| Ingest 五份來源 | 在擴充套件中選擇五個檔案 | 待執行 | 01-ingest.png |
| Wiki Status | 查詢原始來源數與概念頁 | 待執行 | 02-status.png |
| Wiki Lint | 檢查缺來源/斷鏈/孤兒頁 | 待執行 | 03-lint.png |
| Wiki Query | 查詢「為何 LLM 會幻覺？」並附來源 | 待執行 | 04-query.png |
| HTML 瀏覽 | 本機打開 index.html，測試鍵盤、手機寬度、練習題 | 待執行 | 05-html.png |
| Pages 發布 | 開啟公開 URL，確認非 404 | 待執行 | 06-pages.png |

## C. 反思寫法：依你的真實測試結果補寫
最需要留意的節點是「簡報內容核對」，因為生成結果可能比 Wiki 原文更肯定，甚至補進未經驗證的數字。為避免到了簡報最後才發現錯誤，設計上把來源檢查前移到 Wiki ingest 後的 G2，以及製作 HTML 前的 G3 主張-來源對照。若你實際遇到其他問題，應將本段改寫成真正遇到的問題，例如引文找不到、按鈕不會切頁，並寫出實際修正。

## D. 範例紀錄（示範，不是已發生事件）
- 症狀：某頁宣稱 Grounding 可以「完全杜絕」幻覺。
- 判定：與 S04/S05 支持的「降低風險」不符。
- 回返：G3 → G（Wiki query / 重擬大綱）。
- 修改：改成「協助降低幻覺，但仍需驗證引文」。
- 複測：重新與 S04/S05 比對語義相符。
