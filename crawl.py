import json
import base64
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# GitHub Actions 환경 변수에서 토큰 로드 (필요 시 확장 가능)
GITHUB_TOKEN = os.environ.get("GH_PAT")

# 1. 링크 로딩 (GitHub Actions가 변경 감지한 파일)
with open("crawl_trigger.json", "r") as f:
    # GitHub Contents API 구조로 인코딩되어 있음
    api_data = json.load(f)
    decoded = base64.b64decode(api_data["content"]).decode("utf-8")
    link_data = json.loads(decoded)
    link = link_data["link"]

# 2. Selenium 헤드리스 브라우저 설정
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

# 3. 블로그 본문 수집
driver.get(link)
time.sleep(2)

try:
    driver.switch_to.frame("mainFrame")
    time.sleep(1)
    # 최신 네이버 블로그 본문 구조 (스마트에디터 ONE)
    content = driver.find_element(By.CLASS_NAME, "se-main-container")
    text = content.text
except Exception as e:
    print("❌ 본문 수집 실패:", e)
    text = "본문을 수집할 수 없습니다."

driver.quit()

# 4. 출력 디렉토리 생성
os.makedirs("output", exist_ok=True)

# 5. 파일 저장 (링크 일부로 고유 이름 지정)
output_filename = link.split("/")[-1] + ".txt"
output_path = os.path.join("output", output_filename)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(text)

print(f"✅ 저장 완료: {output_path}")
