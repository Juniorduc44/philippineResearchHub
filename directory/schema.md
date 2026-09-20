# Idea schema

Every `ideas/<slug>/idea.md` uses these headings in this order. Leave a field as `unknown` rather than deleting it.

| Field | Required | Notes |
|-------|----------|-------|
| Title | yes | Working name in PH English or Filipino + English |
| Slug | yes | Matches folder name |
| Status | yes | `stub` `draft` `reviewed` `example` |
| Category | yes | Key from `categories.md` |
| One-liner | yes | One sentence, who pays for what |
| Problem | yes | Who hurts, where, how often |
| Customer | yes | Segment + region/city |
| Offer | yes | What is sold, price band in PHP if known |
| Why Philippines | yes | Local constraint or advantage, not a generic "growing market" |
| Model | yes | How money comes in |
| Capital | yes | Low/mid/high band in PHP, year of estimate |
| Licenses | yes | DTI/SEC/CDA, BIR, LGU, plus sector permits. `unknown` allowed |
| Location | yes | Region, city, or "nationwide-digital" |
| Operations | no | Staffing, supply, hours |
| Competition | yes | Named PH players or explicit "none found as of DATE" |
| Risks | yes | Regulatory, supply, collection, disaster |
| Sources | yes | Paths under `research/library/` or catalog IDs |
| Open questions | yes | What to download or verify next |
| Last updated | yes | `YYYY-MM-DD` |
