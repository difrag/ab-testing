# Tableau Dashboard Guide

This folder contains the clean CSV files needed to build a Tableau dashboard for the A/B testing case study.

The goal is not to recreate every notebook. The Tableau dashboard should communicate the final business story clearly:

> Mens E-Mail produced the strongest conversion lift, spend lift, and estimated revenue impact. It should be prioritized for a staged targeted rollout.

## Files to Use

Use the CSV files in `tableau/data/`:

| File | Purpose |
|---|---|
| `dashboard_kpis.csv` | KPI cards for the main recommendation. |
| `treatment_impact.csv` | Treatment-level lift, p-values, revenue impact, and recommendation labels. |
| `experiment_group_metrics.csv` | Raw group-level metrics: customers, visits, conversions, spend. |
| `segment_opportunities.csv` | Top customer segments for targeting analysis. |

## Tableau Basics

Tableau works by dragging fields into visual shelves.

Common shelves:

- **Rows**: controls what appears vertically.
- **Columns**: controls what appears horizontally.
- **Marks**: controls color, label, size, tooltip, and chart type.
- **Filters**: limits the data shown.
- **Pages**: optional; rarely needed for this project.

Important concept:

- **Dimensions** are categories, such as `treatment_group` or `segment_label`.
- **Measures** are numbers, such as `conversion_rate_lift` or `spend_per_customer_lift`.

For this dashboard, most charts will use dimensions on Rows and measures on Columns.

## Recommended Dashboard Layout

Create one dashboard named:

```text
A/B Testing Campaign Impact
```

Suggested layout:

1. Top row: KPI cards
2. Middle left: Conversion lift by treatment
3. Middle right: Spend lift by treatment
4. Lower left: Estimated revenue impact by treatment
5. Lower right: Top targeting opportunities
6. Footer or side note: recommendation and caveat

## Step 1: Connect to the Data

1. Open Tableau Public or Tableau Desktop.
2. Choose **Connect to Data**.
3. Select **Text File**.
4. Open `tableau/data/treatment_impact.csv`.
5. Go to a new worksheet.

You can add the other CSV files later from the **Data Source** tab using **Add** or **New Data Source**.

## Step 2: Create KPI Cards

Data file: `dashboard_kpis.csv`

Create a worksheet called:

```text
KPI Cards
```

Build:

1. Drag `metric` to **Rows**.
2. Drag `value_text` to **Text** on the Marks card.
3. Change Marks type to **Text**.
4. Format it so the values are large and easy to read.

Use this as the top section of the dashboard.

Key KPI values should include:

- Recommended treatment: Mens E-Mail
- Conversion lift: +0.68 percentage points
- Relative conversion lift: +118.8%
- Spend lift per customer: +$0.77
- Revenue lift per 100k customers: +$76,983

## Step 3: Conversion Lift Chart

Data file: `treatment_impact.csv`

Create a worksheet called:

```text
Conversion Lift by Treatment
```

Build:

1. Drag `treatment_group` to **Rows**.
2. Drag `conversion_rate_lift` to **Columns**.
3. Change Marks type to **Bar**.
4. Drag `treatment_group` to **Color**.
5. Drag `conversion_rate_lift` to **Label**.
6. Format `conversion_rate_lift` as **Percentage**.

Interpretation:

Mens E-Mail has the larger conversion lift, so this chart supports the primary recommendation.

## Step 4: Spend Lift Chart

Data file: `treatment_impact.csv`

Create a worksheet called:

```text
Spend Lift by Treatment
```

Build:

1. Drag `treatment_group` to **Rows**.
2. Drag `spend_per_customer_lift` to **Columns**.
3. Use a horizontal bar chart.
4. Drag `spend_per_customer_lift` to **Label**.
5. Format as currency.

Interpretation:

Mens E-Mail creates about +$0.77 per customer, compared with +$0.42 for Womens E-Mail.

## Step 5: Revenue Impact Chart

Data file: `treatment_impact.csv`

Create a worksheet called:

```text
Revenue Impact per 100k Customers
```

Build:

1. Drag `treatment_group` to **Rows**.
2. Drag `estimated_incremental_revenue_per_100k_customers` to **Columns**.
3. Use a horizontal bar chart.
4. Format the measure as currency.
5. Add labels.

Interpretation:

This is the easiest chart for a business reader. It translates the experiment into money.

## Step 6: Top Segment Opportunities

Data file: `segment_opportunities.csv`

Create a worksheet called:

```text
Top Targeting Opportunities
```

Build:

1. Drag `segment_label` to **Rows**.
2. Drag `incremental_revenue_per_100k_total_customers_if_targeted` to **Columns**.
3. Drag `treatment_group` to **Color**.
4. Sort descending by revenue impact.
5. Add `spend_per_customer_lift` and `conversion_rate_lift` to **Tooltip**.
6. Add a filter on `treatment_group` if you want to compare Mens vs Womens.

Interpretation:

This chart explains how the campaign could be targeted instead of blindly rolled out to everyone.

## Step 7: Build the Dashboard

1. Click **New Dashboard**.
2. Set size to **Automatic** or fixed desktop size such as `1200 x 800`.
3. Drag in the worksheets:
   - KPI Cards
   - Conversion Lift by Treatment
   - Spend Lift by Treatment
   - Revenue Impact per 100k Customers
   - Top Targeting Opportunities
4. Add a dashboard title:

```text
A/B Testing Campaign Impact
```

5. Add a short text box near the top:

```text
Mens E-Mail produced the strongest conversion, spend, and revenue lift. Recommend a staged targeted rollout, with follow-up testing for segment-level personalization.
```

## Step 8: Formatting Tips

Keep it clean and business-like:

- Use one color for Mens E-Mail and another for Womens E-Mail.
- Use short titles.
- Put the recommendation at the top.
- Avoid too many filters.
- Use currency formatting for revenue and spend.
- Use percentage formatting for conversion lift.
- Keep the dashboard focused on the decision, not every detail.

## Suggested Color Mapping

| Group | Color |
|---|---|
| Mens E-Mail | Blue |
| Womens E-Mail | Teal or orange |
| Control / reference | Gray |

## What to Say When Presenting

Use this short explanation:

> I used Tableau to turn the A/B test results into a decision dashboard. The dashboard focuses on conversion lift, spend lift, estimated revenue impact, and top targeting opportunities. The main takeaway is that Mens E-Mail generated the strongest business impact, with an estimated $76,983 incremental revenue per 100,000 targeted customers. Segment analysis suggests a staged rollout should start with new customers, web-channel customers, recent customers, and prior Mens-only customers.

## Important Caveat

The segment analysis is exploratory. The dashboard can show promising targeting opportunities, but the final recommendation should still rely mainly on the randomized experiment result.