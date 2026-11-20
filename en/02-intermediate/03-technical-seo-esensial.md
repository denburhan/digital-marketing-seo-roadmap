# 03. Essential Technical SEO

**Level:** Intermediate | **Reading time:** 20 minutes | **Prerequisite:** 01-basic/03

## Goal
Make sure the technical foundation does not block crawling, indexing, and user experience.

## Core checklist
1. **HTTPS** across the whole site, with no mixed content.
2. **One URL version.** Choose www or non-www, with or without trailing slash, then 301 the rest.
3. **Correct status codes.** Live pages 200, permanently moved 301, gone 404 or 410. Avoid soft 404 (empty page that returns 200).
4. **robots.txt** does not block CSS, JS, and important content.
5. **Sitemap** contains only canonical, indexable URLs with status 200.
6. **Canonical** is consistent and points to the main version.
7. **Mobile friendly.** Content and links match the desktop version.
8. **Structured data** is valid and matches the page content.
9. **Custom error pages** that help users.

## Core Web Vitals
"Good" thresholds according to web.dev: LCP 2.5 seconds or less, INP 200 milliseconds or less, CLS 0.1 or less, assessed at the 75th percentile of field data.
- **LCP:** usually affected by the largest image or text on the first screen. Compress, use modern formats, do not lazy-load the main image.
- **INP:** responsiveness. Reduce heavy JavaScript on the main thread.
- **CLS:** layout shift. Set dimensions for images and ads.

## JavaScript SEO
If content is rendered on the client side, make sure important content appears in the rendered HTML and can be seen through URL Inspection. Server-side or static rendering is safer for content you want indexed.

## Redirects
- 301 for permanent moves. Avoid redirect chains.
- During a migration, build a one-by-one map of old to new URLs and test it before launch.

## Exercise
1. Audit one site with the list above. Mark each item pass or fail.
2. Take 3 pages, measure Core Web Vitals from field data, and note the data source.

## Comprehension check
- What is the difference between a soft 404 and a real 404?
- Why must a sitemap not contain URLs that are redirected or noindex?
