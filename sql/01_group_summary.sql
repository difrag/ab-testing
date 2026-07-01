-- Group-level experiment summary.
-- Assumes a table named email_ab_test with the same columns as the raw CSV.

SELECT
    segment,
    COUNT(*) AS customers,
    SUM(visit) AS visits,
    AVG(CAST(visit AS REAL)) AS visit_rate,
    SUM(conversion) AS conversions,
    AVG(CAST(conversion AS REAL)) AS conversion_rate,
    SUM(spend) AS total_spend,
    AVG(spend) AS spend_per_customer,
    CASE
        WHEN SUM(conversion) = 0 THEN NULL
        ELSE SUM(spend) / SUM(conversion)
    END AS spend_per_converter
FROM email_ab_test
GROUP BY segment
ORDER BY segment;
