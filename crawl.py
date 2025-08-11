import sys
import json
import requests

query = sys.argv[1]
print(f"🔍 검색어: {query}")

CLIENT_ID = "MToyAl6U23_D3TEbgjUZ"
CLIENT_SECRET = "L5hDYjkvku"

url = f"https://openapi.naver.com/v1/search/blog?query={requests.utils.quote(query)}"
headers = {
    "X-Naver-Client-Id": CLIENT_ID,
    "X-Naver-Client-Secret": CLIENT_SECRET
}
response = requests.get(url, headers=headers)
data = response.json()

with open("results.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ results.json 저장 완료")
