import pandas as pd

def crisp_calibration(
    df,
    conditions,
    threshold=0.5
):

    calibrated = df.copy()

    for condition in conditions:

        calibrated[condition] = (
            calibrated[condition] >= threshold
        ).astype(int)

    return calibrated



def fuzzy_membership(
    x,
    full_membership,
    crossover,
    full_nonmembership
):

    if x >= full_membership:
        return 1.0

    if x <= full_nonmembership:
        return 0.0

    if x == crossover:
        return 0.5

    if x > crossover:

        return round(
            0.5 + (
                (x - crossover)
                / (full_membership - crossover)
            ) * 0.5,
            4
        )

    return round(
        (
            (x - full_nonmembership)
            / (crossover - full_nonmembership)
        ) * 0.5,
        4
    )



def fuzzy_calibration(
    df,
    conditions,
    full_membership=0.8,
    crossover=0.5,
    full_nonmembership=0.2
):

    calibrated = df.copy()

    for condition in conditions:

        calibrated[condition] = calibrated[
            condition
        ].apply(
            lambda x: fuzzy_membership(
                x,
                full_membership,
                crossover,
                full_nonmembership
            )
        )

    return calibrated