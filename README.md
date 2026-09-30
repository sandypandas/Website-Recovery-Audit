# Archive Recovery Audit

This repository documents a realistic archive audit workflow for recovering a legacy website from a screenshot archive. The project focuses on evidence, structure, text recovery, and remediation planning rather than rebuilding the original site.

## Project purpose

The archive represents a public website that is no longer directly available. The goal is to determine:

- what was on the site,
- how it was structured,
- how trustworthy the recovered content is,
- and what should happen next for a future rebuild.

## Repository structure

- `_quarto.yml` — Quarto site configuration
- `index.qmd` — archive audit landing page
- `docs/audit/memo.qmd` — recovery memo and recommendations
- `docs/audit/sitemap.qmd` — reconstructed site architecture
- `docs/audit/inventory.qmd` — content inventory summary
- `docs/audit/recovery-workflow.qmd` — Tesseract and verification process
- `data/archive_inventory.db` — authoritative SQLite inventory
- `data/archive_inventory.csv` — CSV export of the inventory
- `data/site-sitemap.mmd` — Mermaid source for the sitemap
- `images/site-sitemap.png` — rendered sitemap image
- `data/archive/recovered_text/` — example OCR and verified text samples
- `data/ocr_error_log.csv` — documentation of OCR problems
- `scripts/` — database and diagram generation scripts

## Local preview

```bash
quarto render
quarto preview
```

## Methodology

The workflow uses a defensible audit sample from an archive of screenshots and reconstructs a site map before analyzing textual recovery. Text recovery is treated as a first-pass approximation and must be manually verified, especially on pages involving contact information, dates, and program details.

## Tools

- Quarto for the publishing site
- SQLite for the authoritative content inventory
- Tesseract for OCR-based text recovery
- CSV and text logs for audit evidence and comparison
