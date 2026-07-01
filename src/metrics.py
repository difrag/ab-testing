from __future__ import annotations

import pandas as pd


def group_summary(df: pd.DataFrame, group_col: str = "segment") -> pd.DataFrame:
    """Return group-level counts, rates, and revenue metrics."""
    summary = (
        df.groupby(group_col, dropna=False)
        .agg(
            customers=("conversion", "size"),
            visits=("visit", "sum"),
            conversions=("conversion", "sum"),
            total_spend=("spend", "sum"),
            spend_per_customer=("spend", "mean"),
        )
        .reset_index()
    )
    summary["visit_rate"] = summary["visits"] / summary["customers"]
    summary["conversion_rate"] = summary["conversions"] / summary["customers"]
    summary["spend_per_converter"] = summary["total_spend"] / summary["conversions"].replace(0, pd.NA)
    return summary


def treatment_lift(
    summary: pd.DataFrame,
    control_group: str = "No E-Mail",
    group_col: str = "segment",
) -> pd.DataFrame:
    """Compare each treatment group with the control group."""
    control = summary.loc[summary[group_col] == control_group].iloc[0]
    rows = []

    for _, treatment in summary.loc[summary[group_col] != control_group].iterrows():
        conversion_lift = treatment["conversion_rate"] - control["conversion_rate"]
        visit_lift = treatment["visit_rate"] - control["visit_rate"]
        spend_lift = treatment["spend_per_customer"] - control["spend_per_customer"]

        rows.append(
            {
                group_col: treatment[group_col],
                "control_group": control_group,
                "customers": treatment["customers"],
                "conversion_rate_lift": conversion_lift,
                "relative_conversion_lift": conversion_lift / control["conversion_rate"],
                "incremental_conversions": conversion_lift * treatment["customers"],
                "visit_rate_lift": visit_lift,
                "spend_per_customer_lift": spend_lift,
                "incremental_revenue": spend_lift * treatment["customers"],
            }
        )

    return pd.DataFrame(rows)
