# A/B Testing Case Study: Lifecycle Campaign Impact

This project analyzes a real randomized email campaign experiment and turns it into a product analytics decision memo. The business question is simple:

> Should the company roll out a lifecycle campaign, and if so, which customers should receive it?

The analysis evaluates campaign lift, statistical significance, revenue impact, and segment-level targeting opportunities using Python, pandas, and standard A/B testing methods.

## Key Result

**Recommendation: prioritize Mens E-Mail for rollout analysis, using a staged targeted rollout.**

Mens E-Mail was the strongest treatment overall:

| Metric | Mens E-Mail Result |
|---|---:|
| Control conversion rate | 0.57% |
| Treatment conversion rate | 1.25% |
| Absolute conversion lift | +0.68 percentage points |
| Relative conversion lift | +118.8% |
| Spend lift | +$0.77 per customer |
| Estimated revenue impact | +$76,983 per 100k targeted customers |

Womens E-Mail also improved performance, but the effect was smaller: about **+$42,441 per 100k targeted customers**.

## Final Deliverables

- Final decision memo: [`reports/decision_memo.md`](reports/decision_memo.md)
- Final figures: [`reports/figures/`](reports/figures)
- Tableau dashboard guide and CSV extracts: [`tableau/`](tableau/)
- Main notebooks:
  - [`01_data_audit.ipynb`](notebooks/01_data_audit.ipynb)
  - [`02_experiment_analysis.ipynb`](notebooks/02_experiment_analysis.ipynb)
  - [`03_segment_uplift_analysis.ipynb`](notebooks/03_segment_uplift_analysis.ipynb)
  - [`04_decision_memo_figures.ipynb`](notebooks/04_decision_memo_figures.ipynb)

## Portfolio Framing

The original dataset comes from the MineThatData E-Mail Analytics challenge, a retail email experiment with three randomized groups: `No E-Mail`, `Mens E-Mail`, and `Womens E-Mail`.

For portfolio purposes, I frame the work as a lifecycle/product analytics case study similar to a SaaS trial-nurture decision. The source context remains transparent: this is not literal SaaS free-trial data. The project demonstrates how to structure an A/B testing analysis, interpret lift, estimate business impact, and communicate a recommendation.

## Business Question

Should the company send a lifecycle campaign to customers, and should the campaign be rolled out broadly or targeted to specific segments?

The final recommendation considers:

- conversion lift
- spend per customer lift
- estimated revenue impact
- customer segment performance
- risks and caveats

## Analysis Workflow

| Notebook | Purpose |
|---|---|
| `01_data_audit.ipynb` | Validate the raw dataset, check missing values, document category issues, and confirm randomization balance. |
| `02_experiment_analysis.ipynb` | Run the formal A/B test: group metrics, lift, confidence intervals, p-values, and revenue impact. |
| `03_segment_uplift_analysis.ipynb` | Explore whether treatment effects differ across customer segments and identify targeting opportunities. |
| `04_decision_memo_figures.ipynb` | Create final report figures and a concise recommendation summary table. |

## Methodology Summary

The project starts by preserving the raw data in `data/raw/` and creating cleaned working files only in ignored intermediate folders. The data audit confirms that the experiment has **64,000 customers**, no missing values, balanced assignment across groups, and strong pre-treatment balance.

The primary metric is **conversion rate**. Secondary metrics include **visit rate**, **spend per customer**, and **estimated incremental revenue**. Conversion and visit outcomes are tested with two-proportion z-tests. Spend per customer is evaluated with bootstrap confidence intervals because spend is zero-inflated and skewed.

Segment analysis is treated as exploratory. It helps shape a targeting recommendation, but the overall randomized experiment remains the strongest evidence for whether the campaign worked.

## Final Recommendation

Mens E-Mail should be prioritized because it produced the highest conversion lift, highest spend lift, and largest estimated revenue impact.

The best rollout path is staged:

1. Start with high-opportunity segments such as new customers, web-channel customers, recent customers, and prior Mens-only customers.
2. Monitor conversion, revenue, unsubscribe behavior, customer complaints, and repeat purchase.
3. Use Womens E-Mail selectively for segments where it appears more relevant, especially customers with prior Womens affinity.
4. Run a follow-up targeting test to confirm whether segmented messaging outperforms a broad Mens E-Mail rollout.

## Project Structure

```text
ab-testing/
  data/
    raw/          Original downloaded dataset
    interim/      Cleaned working files, ignored by Git
    processed/    Generated analysis outputs, ignored by Git
  docs/           Experiment design, data dictionary, setup notes
  notebooks/      Analysis notebooks
  reports/        Final decision memo and report figures
  sql/            Optional SQL analysis starter
  src/            Reusable Python helper functions
```

## Data Source

- Dataset description: https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html
- CSV source: http://www.minethatdata.com/Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Start JupyterLab:

```powershell
.\scripts\start_jupyter.ps1
```

Rerun a notebook:

```powershell
.\scripts\execute_notebook.ps1 notebooks\02_experiment_analysis.ipynb
```

The helper scripts create a local Jupyter kernel named `Python (ab-testing)`. See [`docs/setup_jupyter.md`](docs/setup_jupyter.md) for setup details.

## Tools Used

- Python
- pandas
- NumPy
- SciPy
- Matplotlib
- Jupyter Notebook
- Git/GitHub