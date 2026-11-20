# 07. Free Tools: GSC, GA4, PageSpeed

**Level:** Basic | **Reading time:** 15 minutes | **Prerequisite:** module 04

## Goal
Set up and read three free tools that are the basis of all SEO work.

## Google Search Console (GSC)
Direct data from Google about how your site appears.
1. Verify the property (Domain type via DNS is recommended).
2. Submit the sitemap.
3. Learn three reports: **Performance** (clicks, impressions, CTR, position per query and per page), **Pages** (index status and reasons for not being indexed), **URL Inspection** (check one URL).
4. Remember: Performance data has a limited window. Export regularly if you want a long history.

## Google Analytics 4 (GA4)
Measures behavior after people arrive on your site. GA4 uses an **event**-based model: every interaction (page_view, click, scroll, purchase) is recorded as an event. Mark important events as **key events** (conversions). GSC answers "how do people find me", GA4 answers "what do they do afterward".

## PageSpeed Insights
Gives two kinds of data: **field data** (real users, if traffic is sufficient) and **lab data** (simulation). Prioritize field data for decisions. The "good" Core Web Vitals thresholds according to web.dev: LCP 2.5 seconds or less, INP 200 milliseconds or less, CLS 0.1 or less.

## Good habits
- Export monthly data to your own archive.
- Record the date of every major site change so you can connect it to data changes.
- Do not draw conclusions from a single day of data.

## Exercise
1. Verify your site in GSC and submit the sitemap.
2. Find 5 queries with high impressions but low CTR. Those are title improvement candidates.
3. Run PageSpeed Insights on 3 pages and record LCP, INP, CLS.

## Comprehension check
- What question does GSC answer, and what does GA4 answer?
- Why is field data prioritized over lab data?
