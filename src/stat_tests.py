from __future__ import annotations

import numpy as np
from scipy import stats


def two_proportion_z_test(
    successes_a: int,
    n_a: int,
    successes_b: int,
    n_b: int,
) -> dict[str, float]:
    """Two-sided z-test for the difference between two proportions."""
    p_a = successes_a / n_a
    p_b = successes_b / n_b
    pooled = (successes_a + successes_b) / (n_a + n_b)
    se = np.sqrt(pooled * (1 - pooled) * ((1 / n_a) + (1 / n_b)))
    z_score = (p_b - p_a) / se
    p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))

    return {
        "rate_a": p_a,
        "rate_b": p_b,
        "difference": p_b - p_a,
        "z_score": z_score,
        "p_value": p_value,
    }


def proportion_diff_ci(
    successes_a: int,
    n_a: int,
    successes_b: int,
    n_b: int,
    confidence: float = 0.95,
) -> dict[str, float]:
    """Wald confidence interval for an unpooled difference in proportions."""
    p_a = successes_a / n_a
    p_b = successes_b / n_b
    diff = p_b - p_a
    z_crit = stats.norm.ppf(1 - (1 - confidence) / 2)
    se = np.sqrt((p_a * (1 - p_a) / n_a) + (p_b * (1 - p_b) / n_b))

    return {
        "difference": diff,
        "ci_low": diff - z_crit * se,
        "ci_high": diff + z_crit * se,
        "confidence": confidence,
    }


def bootstrap_mean_diff(
    values_a,
    values_b,
    n_bootstrap: int = 10_000,
    confidence: float = 0.95,
    random_state: int = 42,
) -> dict[str, float]:
    """Bootstrap confidence interval for mean(values_b) - mean(values_a)."""
    rng = np.random.default_rng(random_state)
    a = np.asarray(values_a)
    b = np.asarray(values_b)
    diffs = np.empty(n_bootstrap)

    for i in range(n_bootstrap):
        sample_a = rng.choice(a, size=len(a), replace=True)
        sample_b = rng.choice(b, size=len(b), replace=True)
        diffs[i] = sample_b.mean() - sample_a.mean()

    alpha = 1 - confidence
    return {
        "difference": b.mean() - a.mean(),
        "ci_low": float(np.quantile(diffs, alpha / 2)),
        "ci_high": float(np.quantile(diffs, 1 - alpha / 2)),
        "confidence": confidence,
    }
