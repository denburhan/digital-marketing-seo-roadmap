# AI Search Claims: Verified and Unverified

Checked against official documentation on 20 November 2026. Documentation changes, so re-check before using it in paid material or client reports.

## Verified from official sources
| Claim | Source | Status |
|---|---|---|
| No special technical optimization for AI Overview or AI Mode, no special schema or file | Generative AI optimization guide, Google Search Central | Verified |
| Ignore content chunking, unnecessary AI text files (llms.txt), and inauthentic mentions | Same guide, myth-busting section | Verified |
| llms.txt has no positive or negative effect on Google ranking | Changelog note, 15 June 2026 | Verified |
| Non-commodity content is the focus of the guide | Generative AI optimization guide | Verified |
| Query fan-out: the model creates several related queries at once | Same guide | Verified |
| Creating separate content for every query variation to manipulate ranking violates the scaled content abuse policy | Same guide | Verified |
| Spam policies also apply to generative AI responses | Changelog, 15 May 2026 | Verified |
| The FAQ rich result feature no longer appears in Google results from 7 May 2026 | Changelog, 8 May 2026, deprecation notice | Verified |
| Limit for one sitemap: 50MB uncompressed or 50,000 URLs | Build sitemap documentation | Verified |
| Good Core Web Vitals thresholds: LCP 2.5 seconds, INP 200 ms, CLS 0.1, 75th percentile | web.dev/articles/vitals | Verified |

## Carried over from internal material without re-verification in this session
Marked so the reader knows the confidence level. Re-check before using as a basis for decisions.
- Content structure (short paragraphs, clear headings) as a help for understanding: consistent with general guidance, but not an explicitly stated "ranking factor".
- Discover: authority per topic, local content priority, less clickbait. Comes from the Discover Core Update announcement recorded in internal notes, not re-checked in this session.
- SpamBrain neutralizes manipulative links without notice. A general Google statement about SpamBrain exists. The symptom "backlinks up in Ahrefs but clicks stagnant" is a heuristic from practice, not an official statement.

## Claims with no basis, do not use
- An "AI Citation Probability" score or predictions of being cited by AI.
- Percentage increases in citations or traffic from FAQ, pillar pages, or llms.txt without a source.
- Telling AI to write example statistics as "proof" on production pages.
- Image EXIF, IPTC, or geotags as a ranking factor.
- Keyword density and "LSI keywords" as a ranking factor.
- AggregateRating on Organization without real reviews.
- SearchAction schema for the sitelinks search box (no longer used).

## Rules of use
1. Check numeric and predictive claims against official sources before using them.
2. If it cannot be verified, write "author's claim".
3. If two materials conflict, choose the one that matches official documentation and note the conflict.
4. Do not carry fabricated numbers into the next deliverable just because they exist in the source material.
