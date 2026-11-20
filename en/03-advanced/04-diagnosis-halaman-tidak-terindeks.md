# 04. Diagnosing Pages That Are Not Indexed

**Level:** Advanced | **Reading time:** 18 minutes | **Prerequisite:** 01-basic/03

## Goal
Find why a page, or a whole site, does not appear in the index.

## Diagnosis order
1. **Check URL Inspection.** Does Google know the URL? When was it last crawled? What is the index status?
2. **Check blockers:** `noindex` (meta or header), robots.txt, canonical pointing to another URL, redirect, non-200 status, login wall.
3. **Check discovery:** is the URL in the sitemap and does it have internal links?
4. **Check quality:** thin, duplicate, or mass-similar to other pages.
5. **Check spam policy:** does the site contain prohibited patterns (scaled content abuse, link spam, cloaking, and others)?

## GSC statuses that often confuse
- **Discovered - currently not indexed:** Google knows the URL but has not crawled it. Common causes: a new site, server capacity, or Google judging its priority as low.
- **Crawled - currently not indexed:** Google has read it but decided not to include it yet. Check quality and uniqueness.
- **Duplicate, Google chose different canonical than user:** Google disagrees with your canonical. Align the signals: content, internal links, sitemap, canonical.

## What does not help
- Submitting the URL again and again. Requesting indexing does not guarantee indexing.
- Adding a sitemap with thousands of thin URLs.
- Assuming the problem is "surely a penalty". Most cases are quality, technical, or crawl priority.

## Manual action
Check the Manual Actions report in GSC. If there is one, follow the instructions there and request a review after fixing the problem.

## Exercise
Take 10 URLs that are not indexed. Classify the cause into one of the five diagnosis steps. Write the fix and re-measure in a few weeks.

## Comprehension check
- What is the difference between "Discovered" and "Crawled" not indexed?
- Why is resubmitting a URL many times ineffective?
