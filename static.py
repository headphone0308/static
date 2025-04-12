from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import csv
import json

# 設定無頭模式（不開瀏覽器）
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# 啟動 ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Yahoo 股市網址
url = "https://tw.stock.yahoo.com/quote/2330.TW"
driver.get(url)

# 等待 JS 載入
time.sleep(5)

# 抓取資料
try:
    # 使用 xpath 更穩定抓價格
    price_element = driver.find_element(By.XPATH, '//span[contains(@class,"Fz(32px) Fw(b)")]')
    price = price_element.text
except:
    price = "N/A"

try:
    time_element = driver.find_element(By.TAG_NAME, "time")
    time_text = time_element.text
except:
    time_text = "N/A"

driver.quit()

# 整理資料
stock_data = {
    "symbol": "2330.TW",
    "price": price,
    "time": time_text
}

# 輸出 JSON
with open("static.json", "w", encoding="utf-8") as f:
    json.dump(stock_data, f, ensure_ascii=False, indent=2)

# 輸出 CSV
with open("static.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=stock_data.keys())
    writer.writeheader()
    writer.writerow(stock_data)

print("✅ 抓取成功：", stock_data)
