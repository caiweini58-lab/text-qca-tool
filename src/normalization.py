import pandas as pd


def min_max_normalize(
    df,
    conditions
):
    """
    Normalize semantic similarity scores
    into [0, 1] range.
    """

    normalized = df.copy()

    for condition in conditions:

        min_value = normalized[
            condition
        ].min()

        max_value = normalized[
            condition
        ].max()

        if max_value == min_value:

            normalized[condition] = 0.5

        else:

            normalized[condition] = (
                (
                    normalized[condition]
                    - min_value
                )
                /
                (
                    max_value
                    - min_value
                )
            )

        normalized[condition] = normalized[
            condition
        ].round(4)

    return normalized