"""Instant lookup over HTTP using the Actor's Standby mode (no run to start, usually 2-5 s)."""
import os

import requests

resp = requests.get(
    "https://graylark--google-trends-scraper.apify.actor/",
    params={"q": "bitcoin,ethereum", "geo": "US", "timeRange": "today 3-m", "regions": "0"},
    headers={"Authorization": f'Bearer {os.environ["APIFY_TOKEN"]}'},
    timeout=300,
)
resp.raise_for_status()
for item in resp.json()["results"]:
    print(item["searchTerm"], item["status"], item.get("averageInterest"))
