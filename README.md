# 軟體正規方法 小組作業

- 程式語言：Python（HW1／HW2 原文件選定 3.14；HW3 本機實測 3.12.14）
- 測試工具：pytest + pytest-cov（coverage.py）
- 測試目標：每個作業的指定涵蓋率準則達到 100%，且使用最少個測試案例

| 作業 | 內容 |
| --- | --- |
| [hw1](hw1/README.md) | 選定程式語言與測試工具、工具介紹與功能說明 |
| [hw2](hw2/README.md) | Line coverage：以最少測試案例達到 100% |
| [hw3](hw3/README.md) | Graph Coverage：健走集點，3 個案例涵蓋全部邊、邊對與完整路徑 |

## 執行方式（Windows PowerShell）

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python -m pytest hw1 -v
.venv\Scripts\python -m pytest hw2 -v
.\.venv\Scripts\python.exe -m pytest hw3 -v -s --cov-branch
```

執行 `pytest` 時會自動產生 Line Coverage 報表，涵蓋率未達 100% 即判定失敗（設定見 [pyproject.toml](pyproject.toml)）。
