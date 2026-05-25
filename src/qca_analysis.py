import pandas as pd

def necessity_analysis(
    df,
    conditions,
    outcome_col="outcome"
):

    results = []

    outcome_sum = df[outcome_col].sum()

    for condition in conditions:

        numerator = (
            df[[condition, outcome_col]]
            .min(axis=1)
        ).sum()

        consistency = (
            numerator / outcome_sum
        )

        coverage = (
            numerator / df[condition].sum()
        )

        results.append({
            "condition": condition,
            "consistency": round(
                consistency,
                4
            ),
            "coverage": round(
                coverage,
                4
            )
        })

    return pd.DataFrame(results)