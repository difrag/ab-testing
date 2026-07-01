# Analysis Plan

## Objective

Estimate whether sending an e-mail campaign increased customer visits, purchase conversion, and spend compared with a randomized no-email control group.

For the portfolio narrative, this maps to a SaaS lifecycle question: should a product team send a trial-nurture campaign to improve activation, paid conversion, and revenue?

## Experiment Groups

| Group | Role |
|---|---|
| `No E-Mail` | Control |
| `Mens E-Mail` | Treatment A |
| `Womens E-Mail` | Treatment B |

## Hypotheses

Primary hypothesis:

- The campaign changes conversion rate compared with the no-email control group.

Secondary hypotheses:

- The campaign changes visit rate.
- The campaign changes spend per customer.
- Effects differ across customer segments such as prior purchase history, channel, gender-affinity flags, recency, and new-customer status.

## Metrics

Primary metric:

- Conversion rate: `conversions / customers`

Secondary metrics:

- Visit rate: `visits / customers`
- Spend per customer: `total spend / customers`
- Average order value among converters: `total spend / conversions`
- Incremental conversions: `(treatment conversion rate - control conversion rate) * treatment customers`
- Incremental revenue per customer: `treatment spend per customer - control spend per customer`

Guardrail metrics:

- Negative lift in important customer segments
- Lower spend per converter
- Segment-level campaign harm for high-value users

## Statistical Approach

- Use a two-proportion z-test and confidence interval for visit and conversion rates.
- Use Welch's t-test or bootstrap confidence intervals for spend per customer because spend is zero-inflated.
- Report effect sizes in business terms, not only p-values.
- Treat segment analysis as exploratory unless we pre-register specific segments.

## Final Recommendation Format

The final memo should answer:

1. Which campaign, if any, should be rolled out?
2. What is the expected incremental conversion/revenue impact?
3. Which segments should be targeted or excluded?
4. What are the risks or caveats?
5. What should be tested next?
