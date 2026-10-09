# Google Trends API examples (Python and Node.js)

Working examples for getting Google Trends data from code: interest over time, interest by region, related queries, Trending Now, and comparing **more than 5 keywords** on one scale. A practical alternative to pytrends, which was archived in April 2025 and often fails with `429 Too Many Requests`.

The examples call the [Google Trends Scraper & API](https://apify.com/graylark/google-trends-scraper) on Apify, which handles Google's rate limits by rotating IPs and retrying failed terms. *Disclosure: I maintain that Actor.* It costs $1.00 per 1,000 keywords on Apify's free plan, and terms that fail or have no data are free.

## Setup

1. Create a free Apify account and copy your API token (Console > Settings > API & Integrations).
2. Set it as an environment variable: `export APIFY_TOKEN=...` (PowerShell: `$env:APIFY_TOKEN="..."`).
3. Python: `pip install -r python/requirements.txt`. Node.js: `cd node && npm install`.

## Examples

| What | Python | Node.js |
|---|---|---|
| Interest over time, regions and related queries for a few keywords | [basic.py](python/basic.py) | [basic.mjs](node/basic.mjs) |
| Compare more than 5 keywords on one 0-100 scale | [compare_many.py](python/compare_many.py) | |
| Trending Now (daily trending searches) for a country | [trending_now.py](python/trending_now.py) | [trending_now.mjs](node/trending_now.mjs) |
| Export results to CSV | [to_csv.py](python/to_csv.py) | |
| Instant single lookup over HTTP (no run to start) | [instant_lookup.py](python/instant_lookup.py) | |
| Scrape a trends.google.com link exactly as shown | [from_url.py](python/from_url.py) | |

## Coming from pytrends

| pytrends | Here |
|---|---|
| `TrendReq().build_payload(kw_list, timeframe, geo, cat, gprop)` | `searchTerms`, `timeRange`, `geo`, `category`, `searchProperty` |
| `interest_over_time()` | `item["interestOverTime"]` |
| `interest_by_region(resolution="REGION")` | `item["interestByRegion"]` with `regionResolution` |
| `related_queries()` | `item["relatedQueries"]["top"]` and `["rising"]` |
| `trending_searches(pn="united_kingdom")` | `{"mode": "trendingNow", "geo": "GB"}` |
| max 5 keywords per comparison | any number with `compareTerms: true` |

`timeRange` uses the same strings as pytrends and Google Trends: `now 1-H`, `now 7-d`, `today 1-m`, `today 12-m`, `today 5-y`, `all`, or a custom range like `2024-01-01 2024-06-30`.

## Output

Each keyword comes back as one JSON item with `status` (`ok`, `noData` or `failed`), `interestOverTime` (date, timestamp, value 0-100, partial flag), `averageInterest`, `peak`, `interestByRegion`, `relatedQueries`, and plain-text `topRegions` / `topRelatedQueries` columns for spreadsheets. Only `ok` items are charged.

## Related

- [Google Autocomplete Scraper](https://apify.com/graylark/google-autocomplete-scraper): keyword ideas from Google suggestions (a-z and question expansion). Find ideas there, check their trend here.
- Google's official Trends API is in invite-only alpha: https://developers.google.com/search/apis/trends

## License

MIT
