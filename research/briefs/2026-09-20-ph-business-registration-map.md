# Brief: Philippine business registration map

- Date: 2026-09-20
- Status: draft
- Sources: `research/library/2026-09-20-dti-start-grow.md`, `research/library/2026-09-20-dti-bnrs.md`

## Question
Which agencies does a new Philippine enterprise register with, by legal form?

## What the local files say
From DTI Start and Grow (fetched 2026-09-20):

| Form | Name / legal personality | Then always |
|------|--------------------------|-------------|
| Sole proprietor | DTI business name (BNRS or regional/provincial office) | LGU mayor’s permit + BIR TIN |
| Partnership / corporation | SEC | LGU + BIR |
| Cooperative | CDA (RA 6938/6939) | LGU + BIR |

Also: SSS for employers; DOLE required at 50+ workers. Sector regulators extra (e.g. PCA for coconut exports). BMBE Certificate of Authority is issued by DTI at Negosyo Centers (DAO 16-01, 2016) — incentives listed on that page need a current-law check.

## Gaps (catalog IDs to ingest)
- BIR static registration circular (homepage is a JS shell)
- SEC registration how-to (sec.gov.ph returned 403)
- Current BMBE law / DAO, not 2016 only
- LGU-specific mayor’s permit (cannot be nationwide)

## Implication for the directory
Every idea file’s Licenses section should name DTI vs SEC vs CDA, then BIR + LGU. Do not skip LGU. Fees stay `unknown` until a dated circular is on disk.
