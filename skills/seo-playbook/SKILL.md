---
name: seo-playbook
description: "Use for SEO work: keyword and intent research, page audit, indexing diagnosis, AI Search claims. Verifies claims, never invents numbers."
version: 1.0.0
license: MIT (code) and CC BY 4.0 (text)
---

# SEO Playbook

A working guide for AI agents or humans: keyword and intent research, page audits, diagnosing pages that are not indexed, and judging AI Search claims. The full curriculum is in the parent repo (folders `01-basic` to `04-expert` in Indonesian, English in `en/`). This skill is the short, ready-to-use procedure version. An Indonesian version is in `skills/seo-playbook-id`.

## When to use
- Asked for keyword research, clustering, intent, or mapping keywords to URLs.
- Asked to audit one page or judge whether a page is ready to compete.
- A page or site is not indexed, or impressions dropped sharply.
- Asked about AI Overview, AI Mode, AEO, GEO, llms.txt, FAQ schema.
- External SEO material (course, blog, deck) needs to be judged before use.

Not for: writing style, design, or mass execution in a CMS.

## Always-on rules
1. **Never invent numbers.** No example statistics, volume, CPC, position, or percentage predictions without data. No data: write N/A.
2. **Label confidence.** Every number that is not your own measurement gets a source. What cannot be verified is marked "author's claim". Predictions are written as estimates, not promises.
3. **Google data is not third-party tool data.** Search Console and your own analytics are data. Volume, DR, difficulty from other tools are estimates. Do not mix them in one table without source labels.
4. **Verify tactic claims** against official documentation (Google Search Central, web.dev) before using them. Documentation changes, so state the check date.
5. **Measure, do not claim.** Track through Search Console, not screenshots or guesses.
6. **End with one firm recommendation** backed by numbers, not a neutral list of options.
7. **Do not write fabricated experience or case studies.** If you need an example, label it "example scenario".
8. **Do not touch live ads or production sites destructively** (delete, mass redirect, noindex) without the owner's confirmation.
9. **Do not leak credentials.** Tokens and API keys stay out of documents, repos, and logs.

## Procedure A: Keyword and intent research
1. Collect seeds from services, competitors, autocomplete, and real queries in Search Console.
2. One page, one primary keyword. Add a few secondary ones with the same intent.
3. Group by intent and SERP pattern, not word similarity. If the SERP was not checked, write "likely", do not state it as certain.
4. Classify the funnel stage (TOFU, MOFU, BOFU) and intent type. Use `scripts/cluster_queries.py` for a first draft, then correct manually.
5. Map to URLs: cluster, target URL, intent, status (exists, needs creating, needs revision). Template: `templates/keyword-intent-map.csv`.
6. Check cannibalization: several URLs alternating for the same query in Search Console. Fixes: merge with 301, differentiate intent, or canonical.
7. Prioritize: business value first, then pages at position 5 to 15 that need a push.

## Procedure B: Page audit
Five layers: intent, content, structure, technical, trust and conversion. Give each layer a status of pass, needs improvement, or fail with a one-sentence reason. Every finding needs a measuring tool (page fetch, PageSpeed or field data, Search Console data). A finding without evidence does not go in the report. Do not invent scores. Template: `templates/audit-halaman.md`.

## Procedure C: Page not indexed
Diagnosis order, do not skip ahead:
1. URL Inspection: known, last crawled, index status.
2. Blockers: noindex (meta or header), robots.txt, canonical to another URL, redirect, non-200 status, login wall. Helper: `scripts/check_urls.py`.
3. Discovery: is it in the sitemap and does it have internal links?
4. Quality: thin, duplicate, or mass-similar.
5. Spam policy and Manual Actions in Search Console.
Resubmitting a URL many times does not guarantee indexing.

## Procedure D: Judging AI Search claims
- Per Google's official guidance checked 20 November 2026: there is no special technical optimization for AI Overview or AI Mode, and tactics like chunking, llms.txt files, and inauthentic mentions can be ignored.
- The FAQ rich result no longer appears in Google since 7 May 2026 (per Google documentation notes).
- An "AI Citation Probability" score and percentage-increase claims in citations without a source: mark as author's claim.
- Full table and verification status: `references/klaim-ai-search-terverifikasi.md`. Re-check against the sources in `references/sumber-resmi.md` before using for decisions.

## Answer format
1. Situation (numbers and their sources).
2. Diagnosis (hypothesis, evidence, confidence level).
3. Options (at most three, with trade-offs).
4. One firm recommendation and its reason.
5. How to measure and when to review.
Plain language. No em dash or en dash.

## Common pitfalls
- Measuring article length with a raw count. HTML entities like `&#8211;` skew the count. Unescape first.
- Outdated tactics still circulating: keyword density, LSI keywords as a ranking factor, SearchAction schema for the sitelinks search box, image EXIF as a ranking factor, AggregateRating without real reviews.
- Two URLs for the same intent: merge them with a 301 to the winner based on Search Console data, rather than adding another hub page.
- SEO materials that contradict each other: pick the version that matches official documentation and state the conflict.

## Supporting files
- `references/klaim-ai-search-terverifikasi.md`
- `references/sumber-resmi.md`
- `references/glosarium.md`
- `templates/audit-halaman.md`, `templates/keyword-intent-map.csv`, `templates/laporan-keputusan.md`
- `scripts/cluster_queries.py` (--lang id, en, both), `scripts/check_urls.py` (Python 3, no dependencies)
