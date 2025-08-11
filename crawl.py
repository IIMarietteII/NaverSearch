import json
import base64
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

# 1. 링크 로딩
with open("crawl_trigger.json", "r") as f:
    data = json.loads(base64.b64decode(json.load(f)["content"]))
    link = data["link"]

# 2. Selenium 설정
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

# 3. 블로그 본문 추출
driver.get(link)
driver.switch_to.frame("mainFrame")
time.sleep(2)

try:
    content = driver.find_element(By.CLASS_NAME, "se-main-container")
    text = content.text
except:
    text = "❌ 본문을 찾을 수 없습니다."

driver.quit()

# 4. 저장
os.makedirs("output", exist_ok=True)
with open("output/blog_text.txt", "w") as f:
    f.write(text)
