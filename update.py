import json
from pathlib import Path

import requests

secrets_path = Path(__file__).with_name("mysecrets.json")
secrets = json.loads(secrets_path.read_text(encoding="utf-8"))

API_TOKEN = secrets["API_TOKEN"]
ZONE_ID = secrets["ZONE_ID"]
RECORD_ID = secrets["RECORD_ID"]
RECORD_NAME = secrets["RECORD_NAME"]

ip = requests.get("https://api.ipify.org").text

url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{RECORD_ID}"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

payload = {
    "type": "A",
    "name": RECORD_NAME,
    "content": ip,
    "ttl": 120,
    "proxied": True
}

r = requests.put(url, headers=headers, json=payload)
print("cloudflare response:", r.json())
