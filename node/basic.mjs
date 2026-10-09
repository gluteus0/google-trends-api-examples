// Interest over time, regions and related queries for a few keywords.
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('graylark/google-trends-scraper').call({
  searchTerms: ['bitcoin', 'ethereum'],
  geo: 'US',
  timeRange: 'today 12-m',
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) {
  if (item.status !== 'ok') {
    console.log(item.searchTerm, item.status, item.error); // noData / failed items are free
    continue;
  }
  console.log(`${item.searchTerm}: average ${item.averageInterest}, peak ${item.peak.date}`);
  console.log('  top regions:', item.topRegions);
}
