# 05. Automation and Measurement

**Level:** Expert | **Reading time:** 18 minutes | **Prerequisite:** 02-intermediate/07

## Goal
Automate data collection and routine checks so data-based decisions are consistent.

## What is worth automating
- Daily or weekly exports from the Search Console API to your own storage.
- HTTP status checks for important pages and the sitemap.
- Checks for robots.txt and accidental noindex after a deployment.
- A short weekly report.

## What not to automate without human control
- Mass content publishing without review.
- Changes to live ads.
- Mass deletions or redirects.

## Safe practices
- Keep credentials in environment variables or a secret manager. Do not put them in a repo or document.
- Run scripts in read mode first (dry run).
- Log results and errors.
- Verify counts with code, not manual estimates.

## Examples in the repo
- `scripts/cluster_queries.py`: grouping queries from a CSV.
- `scripts/check_urls.py`: check HTTP status, redirects, and the noindex tag from a list of URLs.

## Exercise
1. Run `check_urls.py` on 20 important URLs and save the results.
2. Design a weekly automatic schedule for that script.

## Comprehension check
- Why is a dry run important before automation touches production?
- What must never go into a code repo?
