"""Interest over time, interest by region and related queries for a few keywords."""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("graylark/google-trends-scraper").call(run_input={
    "searchTerms": ["bitcoin", "ethereum"],
    "geo": "US",               # empty string = worldwide
    "timeRange": "today 12-m",
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    if item["status"] != "ok":  # "noData" / "failed" items are free and have no values
        print(item["searchTerm"], item["status"], item.get("error"))
        continue
    print(f'{item["searchTerm"]}: average {item["averageInterest"]}, peak {item["peak"]["date"]}')
    print("  top regions:", item["topRegions"])
    print("  rising queries:", item["risingRelatedQueries"])
    last = item["interestOverTime"][-3:]
    print("  last points:", [(p["date"], p["value"]) for p in last])
