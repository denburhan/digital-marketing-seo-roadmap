# 01. Keyword Clusters and Cannibalization

**Level:** Intermediate | **Reading time:** 15 minutes | **Prerequisite:** 01-basic/05

## Goal
Group hundreds of queries into intent-based clusters, then find and fix pages that compete with each other.

## Intent-based clusters
Group by search intent, not word similarity. "How to install parquet" and "parquet installation service" look similar in words but have different intent (education vs transaction), so they get different pages.

Quick test: if two queries show nearly the same SERP (page types and topics), they are candidates for one page. If the SERPs differ, separate them.

## Detecting cannibalization
From a GSC export (query x page):
1. Find queries that show more than one of your URLs.
2. Check whether the position alternates between URLs or both stay stuck low.
3. Decide the winning URL based on intent and content strength.

## How to fix it
- **Merge:** move the content of the weak URL into the strong one, then 301 redirect.
- **Differentiate:** change the angle and intent of one page so they no longer overlap.
- **Canonical:** only when pages are true technical duplicates. It is not a solution for competing content.
- **Strengthen internal links** to the winning URL with consistent anchors.

## Helper script
This repo includes `scripts/cluster_queries.py`, which groups queries from a CSV by base words and intent modifiers. The result is a starting point, not a final decision. Always check the SERP manually before merging pages.

## Verify your counts
If you produce a summary table, recount it with code. For example, the number of queries in a cluster must equal the number of items in the query list column. Hand-counted tables are often wrong.

## Exercise
1. Export 3 months of query x page data from GSC.
2. Run the cluster script. Pick 3 clusters and check their SERPs manually.
3. Write a merge, differentiate, or leave-as-is decision for each cluster, with reasons.

## Comprehension check
- Why is canonical not a cure for content cannibalization?
- What is the sign that you should split two queries into two pages?
