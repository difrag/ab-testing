# A/B Testing Case Study: Lifecycle Campaign Impact

This project analyzes a real randomized marketing experiment from the MineThatData E-Mail Analytics challenge. The portfolio framing is a SaaS/product analytics case study: should a company send a lifecycle/trial-nurture campaign to users to increase visits, paid conversion, and revenue?

Important note: the original dataset comes from a retail e-mail campaign test with Mens E-Mail, Womens E-Mail, and No E-Mail groups. We will keep that context transparent, then translate the decision-making logic to a SaaS lifecycle campaign scenario.

## Business Question

Should the company roll out an outbound lifecycle campaign, and if so, which customer segments should receive it?

## Planned Analysis

1. Validate the raw data and document data quality issues.
2. Compare control vs treatment groups on visit rate, conversion rate, and spend per customer.
3. Estimate incremental lift and statistical uncertainty.
4. Analyze whether treatment effects vary by customer segment.
5. Write a decision memo with a clear ship/do-not-ship/segment recommendation.

## Data Audit

The first notebook, `01_data_audit.ipynb`, establishes whether the dataset is reliable enough for experiment analysis. Before estimating lift or running statistical tests, I validate the raw data, confirm the experiment groups, check for missing values, review category labels, and assess whether the randomized groups are balanced before treatment.

The audit starts from the untouched raw CSV in `data/raw/`. This keeps the source data reproducible and separate from any cleaned or analysis-ready files. The notebook confirms that the dataset contains 64,000 rows, 12 original columns, no missing values, and three experiment groups: `No E-Mail`, `Mens E-Mail`, and `Womens E-Mail`.

During the category review, I identify a spelling issue in the raw `zip_code` field: `Surburban` appears instead of `Suburban`. Rather than editing the raw file, I create a cleaned working dataset in `data/interim/email_ab_test_clean.csv` and add helper fields such as `zip_code_clean`, `is_treatment`, and `campaign_type`.

The notebook also checks experiment group sizes and pre-treatment balance. In an A/B test, randomization is what makes the control and treatment groups comparable. If the groups look similar before the campaign, then differences observed after the campaign are more credible as treatment effects. I use standardized mean differences for numeric pre-treatment variables such as recency, prior spend, prior Mens/Womens purchase indicators, and new-customer status. The largest standardized mean difference is below 0.01, well under the common 0.10 rule-of-thumb threshold, which supports moving forward with formal experiment analysis.

This audit answers the question: can the dataset be trusted for an A/B test? In this case, the answer is yes. The file loads correctly, the randomized groups are evenly distributed, the raw data is preserved, and the pre-treatment balance checks do not show meaningful imbalance.

## Project Structure

```text
ab-testing/
  data/
    raw/          Original downloaded dataset
    interim/      Cleaned or lightly transformed working files
    processed/    Final analysis-ready tables
  docs/           Experiment design, data dictionary, analysis plan
  notebooks/      Exploratory and final analysis notebooks
  reports/        Final decision memo and exported visuals
  sql/            Optional SQL versions of analysis queries
  src/            Reusable Python helper functions
```


## Final Deliverables

- Final decision memo: `reports/decision_memo.md`
- Final report figures: `reports/figures/final_*.png`
- Main analysis notebooks: `notebooks/01_data_audit.ipynb` through `notebooks/04_decision_memo_figures.ipynb``r`n`r`n## Data Source

- Dataset description: https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html
- CSV source: http://www.minethatdata.com/Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

The helper scripts create a local Jupyter kernel named `Python (ab-testing)`.

To start JupyterLab:

```powershell
.\scripts\start_jupyter.ps1
```

See `docs/setup_jupyter.md` for full setup notes.

## Suggested Notebook Flow

1. `01_data_audit.ipynb`
2. `02_experiment_analysis.ipynb`
3. `03_segment_uplift_analysis.ipynb`
4. `04_decision_memo_figures.ipynb`
