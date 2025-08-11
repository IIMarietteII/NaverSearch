import json
import base64
import os
import requests

# Naver API 인증 정보
CLIENT_ID = "MToyAl6U23_D3TEbgjUZ"
CLIENT_SECRET = "L5hDYjkvku"

# crawl_trigger.json 파일에서 검색어 가져오기
with open("crawl_trigger.json", "r") as f:
    raw = json.load(f)
    decoded = base64.b64decode(raw["content"]).decode("utf-8")
    query_data = json.loads(decoded)
    query = query_data["query"]

print(f"🔍 검색어: {query}")

# 네이버 블로그 검색 API 호출
url = f"https://openapi.naver.com/v1/search/blog?query={requests.utils.quote(query)}"
headers = {
    "X-Naver-Client-Id": CLIENT_ID,
    "X-Naver-Client-Secret": CLIENT_SECRET
}
response = requests.get(url, headers=headers)
data = response.json()

# 결과 저장
with open("results.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ results.json 저장 완료")
