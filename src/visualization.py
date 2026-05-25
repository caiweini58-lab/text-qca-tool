import plotly.express as px
import pandas as pd


def plot_membership_heatmap(
    df,
    conditions
):

    fig = px.imshow(
        df[conditions],
        labels={
            "x": "Conditions",
            "y": "Cases",
            "color": "Membership"
        },
        aspect="auto"
    )

    fig.update_layout(
        title="Condition Membership Heatmap"
    )

    return fig



def plot_score_distribution(
    df,
    condition,
    threshold=None,
    crossover=None,
    full_membership=None,
    full_nonmembership=None
):

    fig = px.histogram(
        df,
        x=condition,
        nbins=20,
        title=f"{condition} Score Distribution"
    )

    # Crisp-set threshold
    if threshold is not None:

        fig.add_vline(
            x=threshold,
            line_dash="dash",
            annotation_text="Threshold",
            annotation_position="top"
        )

    # Fuzzy-set crossover
    if crossover is not None:

        fig.add_vline(
            x=crossover,
            line_dash="dot",
            annotation_text="Crossover",
            annotation_position="top"
        )

    # Full membership
    if full_membership is not None:

        fig.add_vline(
            x=full_membership,
            line_dash="dash",
            annotation_text="Full Membership",
            annotation_position="top"
        )

    # Full non-membership
    if full_nonmembership is not None:

        fig.add_vline(
            x=full_nonmembership,
            line_dash="dash",
            annotation_text="Full Nonmembership",
            annotation_position="top"
        )

    fig.update_layout(
        xaxis_title="Normalized Score",
        yaxis_title="Frequency"
    )

    return fig



def build_readable_configuration(
    row,
    conditions
):
    """
    Convert binary configurations
    into readable QCA notation.

    Example:
    101 -> A * ~B * C
    """

    labels = []

    for condition in conditions:

        if row[condition] == 1:
            labels.append(condition)

        else:
            labels.append(f"~{condition}")

    return " * ".join(labels)



def plot_truth_table(
    truth_table,
    conditions
):

    truth_table = truth_table.copy()

    # Binary configuration string
    truth_table["configuration"] = (
        truth_table[conditions]
        .astype(str)
        .agg("".join, axis=1)
    )

    # Readable QCA notation
    truth_table["configuration_label"] = (
        truth_table.apply(
            lambda row: build_readable_configuration(
                row,
                conditions
            ),
            axis=1
        )
    )

    # Sort by frequency
    truth_table = truth_table.sort_values(
        by="n_cases",
        ascending=False
    )

    fig = px.bar(
        truth_table,
        x="configuration_label",
        y="n_cases",
        color="outcome_consistency",
        hover_data=[
            "configuration",
            "coverage",
            "outcome_consistency",
            "n_cases"
        ],
        title="Truth Table Configurations"
    )

    # IMPORTANT FIX:
    # Force categorical axis
    fig.update_xaxes(
        type="category",
        categoryorder="total descending"
    )

    fig.update_layout(
        xaxis_title="Configurations",
        yaxis_title="Number of Cases",
        coloraxis_colorbar_title="Consistency"
    )

    return fig



def plot_consistency_coverage(df):

    fig = px.scatter(
        df,
        x="coverage",
        y="consistency",
        text="condition",
        size="consistency",
        title="Consistency vs Coverage"
    )

    fig.update_traces(
        textposition="top center"
    )

    return fig