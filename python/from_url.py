"""Scrape a trends.google.com explore link exactly as shown (terms, country, dates, category, search type)."""
import os

from apify_client import ApifyClient

url = "https://trends.google.com/trends/explore?date=today%205-y&geo=GB&q=tea,coffee"

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("graylark/google-trends-scraper").call(run_input={"trendsUrls": [url]})
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["searchTerm"], item["status"], item.get("averageInterest"))
