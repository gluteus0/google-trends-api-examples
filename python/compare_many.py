"""Compare more than 5 keywords on one 0-100 scale (Google's own UI stops at 5)."""
import os

from apify_client import ApifyClient

phones = ["iphone", "samsung galaxy", "google pixel", "oneplus", "xiaomi", "motorola", "nokia", "sony xperia"]

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("graylark/google-trends-scraper").call(run_input={
    "searchTerms": phones,      # put a steady, well-known term first: it is the shared anchor
    "compareTerms": True,
    "geo": "US",
    "timeRange": "today 12-m",
    "includeInterestByRegion": False,
})

rows = [i for i in client.dataset(run["defaultDatasetId"]).iterate_items() if i["status"] == "ok"]
for item in sorted(rows, key=lambda i: i["averageInterest"], reverse=True):
    print(f'{item["searchTerm"]:16s} {item["averageInterest"]:6.2f}')
