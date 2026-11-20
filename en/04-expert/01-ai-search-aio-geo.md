# 01. AI Search, AEO, and GEO

**Level:** Expert | **Reading time:** 20 minutes | **Prerequisite:** 03-advanced

## Goal
Understand what is and is not true about optimizing for AI Overview, AI Mode, and other answer engines.

## What is verified (official Google statements)
- **There is no special technical optimization** to appear in AI Overview or AI Mode. No special schema and no required llms.txt file. The requirement: the page can be indexed and meets Search Essentials.
- **Google does not use llms.txt** for ranking. Creating one does no harm, but do not expect an effect in Google.
- **There is no special "AI-friendly" writing formula.** Writing for humans is enough.
- **Splitting content into many small pages for AI (excessive chunking) is unnecessary.**
- **Structured data helps understanding**, it is not a VIP lane.

Summary source: `references/klaim-ai-search-terverifikasi.md` in this repo, which copies the verification results from Google's official guidance.

## Additions from Google's generative AI optimization guide (checked 20 November 2026)
- The official guide advises ignoring content "chunking" tactics, unnecessary AI text files (such as llms.txt), and inauthentic mentions.
- Creating separate content for every query variation or fan-out query mainly to manipulate ranking or AI answers violates the scaled content abuse policy.
- Search Console has a Generative AI performance report. Check in your own Search Console whether that report is available for your property, then use it as the main data source before manual testing.

## Understood patterns (reasonable heuristics)
- AI Overview is built on top of the core ranking systems: ranking happens first, then the answer is assembled. SEO is not dead. Success indicators shift to two: position and whether you are cited as a source.
- **Query fan-out:** a big question is split into sub-questions. A strong page answers the core question and anticipates its sub-questions.
- **Clear structure helps:** tidy headings, short paragraphs, one idea per paragraph, core answer first.
- **Non-commodity content holds up better:** original data, first-hand experience, real case studies.

## What to be suspicious of
- An "AI Citation Probability" score or similar: no tool can predict that.
- Percentages without a source in GEO material (for example "citations up by X percent"): treat them as an author's claim.
- Advice to write example statistics to raise authority: it produces fake data. Do not do it.
- Buying mentions or citations: web sentiment is read and spam mentions are filtered.

## About FAQ schema
Per Google documentation checked 20 November 2026, the FAQ rich result feature no longer appears in Google search results (the documentation update says it applies from 7 May 2026). Writing an FAQ for readers is still useful, but do not promise a rich result display. Note: older material often still mentions the 2023 restriction and traffic increase claims without sources. Check the current documentation before using it.

## Measuring
- Track queries and pages through GSC.
- Record yourself whether your pages appear as a source in AI answers for a fixed set of queries (manual test, record date and results as they are). This is a small sample, not market statistics.

## Exercise
1. Pick 10 valuable queries. Test manually every month and record whether your site is cited.
2. Write one page that answers a core question and 3 sub-questions, with one piece of original evidence.

## Comprehension check
- Why does creating llms.txt not add ranking in Google?
- What does query fan-out mean for your page structure?
