import requests
from config import SERPER_API_KEY

def web_search(query):
    url = "https://google.serper.dev/search"
    headers = {"X-API-KEY": SERPER_API_KEY}
    data = {"q": query}
    res = requests.post(url, headers=headers, json=data)
    return res.json()["organic"][0]["snippet"]