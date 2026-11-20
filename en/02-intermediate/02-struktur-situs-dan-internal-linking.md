# 02. Site Structure and Internal Linking

**Level:** Intermediate | **Reading time:** 15 minutes | **Prerequisite:** 01-basic/06

## Goal
Design a structure that helps users and crawlers understand how pages relate.

## Pillar and supporting page pattern
- **Pillar page:** covers a broad topic comprehensively.
- **Supporting pages:** cover specific sub-topics and link to the pillar.
- The pillar links back to the most relevant supporting pages.

This is an organizing pattern, not a ranking formula. The benefit is real for navigation and topic clarity.

## Internal link principles
1. A link must be a crawlable `<a href>` element.
2. Anchor text explains the destination, not "click here".
3. Place links inside the main content where relevant, not only in the footer.
4. Avoid orphan pages (no incoming links).
5. Watch click depth: important pages should ideally be reachable in few clicks from the homepage.

## Quick audit
- Crawl the site with a crawler (the free version of Screaming Frog is enough for small sites).
- List pages with zero internal incoming links.
- List important pages with high click depth.
- List generic anchors.

## Breadcrumbs and navigation
Breadcrumbs help users know where they are. Breadcrumb structured data can be added following Google documentation, but its display is not guaranteed.

## Exercise
1. Draw a pillar and supporting page map for one topic.
2. Find 5 orphan pages on your site and give them sensible incoming links.

## Comprehension check
- Why is a "click here" anchor less helpful?
- What is the risk of putting all important links only in the footer?
