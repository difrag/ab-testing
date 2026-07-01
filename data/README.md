# Data

## Raw

`data/raw/mine_that_data_email_ab_test.csv` is the original downloaded CSV. Treat this file as read-only.

## Interim

Use `data/interim/` for cleaned intermediate files, such as standardized category labels or derived treatment flags.

## Processed

Use `data/processed/` for final analysis-ready outputs, such as group summaries, segment-level lift tables, and chart-ready extracts.

## Source Notes

The original dataset contains 64,000 customers randomly assigned to one of three groups:

- Mens E-Mail
- Womens E-Mail
- No E-Mail

The post-campaign outcome window is two weeks. Outcomes include website visit, purchase conversion, and spend.
