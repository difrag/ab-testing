# Experiment Design Notes

## Original Experiment

The MineThatData challenge describes a randomized e-mail campaign experiment:

- One third of customers received a Mens merchandise e-mail.
- One third received a Womens merchandise e-mail.
- One third received no e-mail.
- Customer behavior was tracked for two weeks after the campaign.

## Project Context

This project uses the public retail marketing experiment as a product analytics case study about lifecycle messaging. The decision problem is whether a campaign should be rolled out, which treatment should be prioritized, and which customer segments should be targeted first.

The source context remains transparent: this is a retail marketing experiment, not literal SaaS free-trial data. The analytical structure is still relevant to product and growth analytics because it includes randomized assignment, a control group, conversion outcomes, spend outcomes, and segment-level rollout decisions.

## Unit of Randomization

The unit of randomization is the customer. Each row represents one customer assigned to exactly one campaign group.

## Primary Decision Metric

The primary metric is conversion rate. A treatment is more attractive when it improves conversion while also increasing spend per customer and estimated incremental revenue.

## Key Risk

Segment findings are exploratory. They are useful for prioritizing a staged rollout, but they should be validated with a follow-up targeting test before being treated as final personalization rules.