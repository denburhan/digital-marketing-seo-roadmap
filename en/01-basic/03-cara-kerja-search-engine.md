# 03. How Search Engines Work

**Level:** Basic | **Reading time:** 12 minutes | **Prerequisite:** module 01

## Goal
Understand the three core stages (crawling, indexing, serving) so you know where an SEO problem happens.

## Three stages
1. **Crawling.** A program (Googlebot) finds and downloads pages through links and sitemaps.
2. **Indexing.** The page content is analyzed and stored in the index. Not every crawled page enters the index.
3. **Serving.** When someone searches, the system selects and ranks pages from the index.

Basic diagnosis follows that order: page not found (crawl problem), found but not indexed (indexing or quality problem), indexed but not ranking high (relevance, authority, or competition problem).

## Things that get in the way
- A `robots.txt` that blocks crawling. Note: robots.txt controls crawling, it does not guarantee a URL stays out of the index. To keep a page out of search results, use `noindex` (and leave the page crawlable so the tag can be read).
- A `noindex` that was installed by accident, for example left over from development.
- Orphan pages with no internal links at all.
- Thin or duplicate content.
- A slow server or frequent errors.

## Mobile-first indexing
Google mainly uses the mobile version of a page for indexing and ranking. Content that exists only on desktop risks not being read. Make sure the mobile version contains the same important content and links.

## Sitemap
A sitemap helps URL discovery, it does not guarantee ranking. Limit for a single sitemap file: 50 MB uncompressed or 50,000 URLs (source: Google Search Central documentation on building a sitemap). If you exceed that, split into several files and register them through a sitemap index.

## Exercise
1. Open `yoursite.com/robots.txt` and read it. What is blocked?
2. In Google Search Console, run URL Inspection on one page. Note its crawl and index status.

## Comprehension check
- Why is robots.txt not the right way to remove a page from search results?
- At which stage is your problem if a page is "discovered, currently not indexed"?

## Official source
Google Search Central: How Search works, and the sitemap documentation.
