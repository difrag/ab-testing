# Data Dictionary

Source file: `data/raw/mine_that_data_email_ab_test.csv`

| Column | Type | Meaning |
|---|---|---|
| `recency` | Integer | Months since the customer's last purchase. |
| `history_segment` | Category | Bucketed prior-year spend segment. |
| `history` | Float | Actual prior-year customer spend. |
| `mens` | Binary | Whether the customer purchased Mens merchandise in the prior year. |
| `womens` | Binary | Whether the customer purchased Womens merchandise in the prior year. |
| `zip_code` | Category | Urban, Suburban, or Rural customer location category. |
| `newbie` | Binary | Whether the customer is new in the past twelve months. |
| `channel` | Category | Prior purchase channel, such as Phone, Web, or Multichannel. |
| `segment` | Category | Randomized experiment group: Mens E-Mail, Womens E-Mail, or No E-Mail. |
| `visit` | Binary | Whether the customer visited the website in the two-week outcome window. |
| `conversion` | Binary | Whether the customer purchased in the two-week outcome window. |
| `spend` | Float | Dollar spend in the two-week outcome window. Usually zero for non-converters. |

## Data Quality Notes

- The raw `zip_code` field contains the spelling `Surburban`. Preserve the raw value in `data/raw`; standardize only in cleaned outputs.
- `spend` is zero-inflated because most customers do not convert.
- Treatment assignment is stored in `segment`; the control group is `No E-Mail`.
