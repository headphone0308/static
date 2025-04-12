# api.py
import requests
import csv
from datetime import datetime

# API URL（台灣證交所）
url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY"

# 設定股票代號、日期範圍等參數
params = {
    "response": "json",    # JSON 格式
    "date": "20230411",    # 查詢日期：格式 yyyyMMdd
    "stockNo": "2330"      # 股票代號（台積電）
}

# 發送請求
response = requests.get(url, params=params)

# 處理 API 回傳結果
if response.status_code == 200:
    data = response.json()
    if "data" in data:
        stock_data = data["data"]
        # 輸出 CSV
        with open("ap.csv", "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow(["日期", "開盤價", "最高價", "最低價", "收盤價", "成交量"])
            for row in stock_data:
                writer.writerow(row)
        print("✅ API 資料成功儲存到 CSV")
    else:
        print("❌ API 回傳錯誤：", data["stat"])
else:
    print("❌ API 請求失敗")
