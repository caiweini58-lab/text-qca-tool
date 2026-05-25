import pandas as pd


def generate_truth_table(
    config_df,
    conditions
):
    """
    Generate truth table with:
    - frequency
    - consistency
    - coverage
    """

    total_positive = (
        config_df["outcome"].sum()
    )

    truth_table = (
        config_df.groupby(conditions)
        .agg(
            n_cases=("outcome", "count"),
            positive_cases=("outcome", "sum"),
            outcome_consistency=("outcome", "mean")
        )
        .reset_index()
    )

    # Coverage calculation
    truth_table["coverage"] = (
        truth_table["positive_cases"]
        / total_positive
    ).round(4)

    # Binary configuration string
    truth_table["configuration"] = (
        truth_table[conditions]
        .astype(str)
        .agg("".join, axis=1)
    )

    return truth_table