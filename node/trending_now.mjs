// Daily trending searches for a country.
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('graylark/google-trends-scraper').call({
  mode: 'trendingNow',
  geo: 'US',
  trendingHours: '24',
  maxTrendingItems: 25,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
items.filter((t) => t.status === 'ok').forEach((t) => console.log(`${t.rank}. ${t.title} (${t.searchVolume}+)`));
