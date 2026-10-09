"""Save a keyword list's Google Trends summary to CSV (one row per keyword)."""
import csv
import os

from apify_client import ApifyClient

keywords = ["air fryer", "standing desk", "electric bike", "sourdough", "pickleball"]

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("graylark/google-trends-scraper").call(run_input={"searchTerms": keywords, "geo": "US"})

fields = ["searchTerm", "status", "averageInterest", "topRegions", "topRelatedQueries", "risingRelatedQueries"]
with open("google_trends.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields + ["peakDate"], extrasaction="ignore")
    w.writeheader()
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        w.writerow({**item, "peakDate": (item.get("peak") or {}).get("date")})
print("saved google_trends.csv")

# Tip: the dataset can also be downloaded directly as CSV or Excel, e.g.
# https://api.apify.com/v2/datasets/<datasetId>/items?format=csv&view=overview
