"""Daily trending searches for a country (Google Trends "Trending now")."""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("graylark/google-trends-scraper").call(run_input={
    "mode": "trendingNow",
    "geo": "GB",
    "trendingHours": "24",     # "4", "24", "48" or "168"
    "maxTrendingItems": 25,
})

for t in client.dataset(run["defaultDatasetId"]).iterate_items():
    if t["status"] == "ok":
        print(f'{t["rank"]:3d}. {t["title"]}  ({t["searchVolume"]}+ searches, started {t["startedAt"]})')
