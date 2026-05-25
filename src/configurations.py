import pandas as pd


def build_configurations(
    df,
    conditions,
    threshold=0.5
):
    """
    Convert fuzzy memberships into
    binary logical configurations.
    """

    config_df = df.copy()

    for condition in conditions:

        config_df[condition] = (
            config_df[condition] >= threshold
        ).astype(int)

    config_df["configuration"] = (
        config_df[conditions]
        .astype(str)
        .agg("".join, axis=1)
    )

    return config_df