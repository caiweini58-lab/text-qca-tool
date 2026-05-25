import streamlit as st
import pandas as pd

from src.data_loader import (
    load_csv,
    validate_text_dataset,
    validate_prototypes
)

from src.scoring import (
    generate_condition_scores
)

from src.normalization import (
    min_max_normalize
)

from src.calibration import (
    crisp_calibration,
    fuzzy_calibration
)

from src.truth_table import (
    generate_truth_table
)

from src.qca_analysis import (
    necessity_analysis
)

from src.visualization import (
    plot_membership_heatmap,
    plot_score_distribution,
    plot_truth_table,
    plot_consistency_coverage
)

from src.configurations import (
    build_configurations
)


st.set_page_config(
    page_title="Text-to-QCA Tool",
    layout="wide"
)

st.title(
    "Text Classification to QCA Analysis Tool"
)

st.sidebar.header("Upload Files")

text_file = st.sidebar.file_uploader(
    "Upload Text Dataset",
    type=["csv"]
)

prototype_file = st.sidebar.file_uploader(
    "Upload Prototype Dataset",
    type=["csv"]
)

if not (text_file and prototype_file):

    st.subheader("Research Workflow")

    workflow_df = pd.DataFrame({
        "Step": [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7"
        ],
        "Process": [
            "Upload Raw Text",
            "Define Conceptual Prototypes",
            "Generate Semantic Embeddings",
            "Compute Cosine Similarity",
            "Normalize Scores",
            "Calibrate Membership",
            "Generate QCA Outputs"
        ],
        "Output": [
            "Citizen statements",
            "Research conditions",
            "Semantic vectors",
            "Condition scores",
            "[0,1] normalized values",
            "Crisp/fuzzy sets",
            "Truth tables & configurations"
        ]
    })

    st.table(workflow_df)

if text_file and prototype_file:

    text_df = load_csv(text_file)

    prototype_df = load_csv(prototype_file)

    valid_text, text_message = (
        validate_text_dataset(text_df)
    )

    valid_proto, proto_message = (
        validate_prototypes(prototype_df)
    )

    if valid_text and valid_proto:

        st.sidebar.info(
            "Datasets ready for analysis."
        )

    else:

        if valid_text:

            st.sidebar.success(text_message)

        if valid_proto:

                st.sidebar.success(proto_message)

    if valid_text and valid_proto:

        st.subheader("Dataset Preview")

        st.dataframe(text_df)

        scores_df = generate_condition_scores(
            text_df,
            prototype_df
        )

        condition_df = prototype_df[
            prototype_df["type"] == "condition"
        ]

        conditions = condition_df[
            "condition_name"
        ].tolist()

        normalized_df = min_max_normalize(
            scores_df,
            conditions
        )

        st.subheader("Semantic Scoring Method")
        st.latex(r"""
        \text{Similarity}(Text_i, Prototype_j)
        =
        \cos(\mathbf{E}_{text_i}, \mathbf{E}_{prototype_j})
        """)
        formula_df = pd.DataFrame({
            "Component": [
                "Text_i",
                "Prototype_j",
                "E",
                "cos()"
            ],
            "Meaning": [
                "Citizen text case",
                "Conceptual condition prototype",
                "Multilingual semantic embedding",
                "Cosine similarity measure"
            ]
        })
        st.table(formula_df)

        st.subheader("Similarity Scores")
      
        st.dataframe(scores_df)
        
        st.subheader("Normalized Similarity Scores")

        st.markdown("""
        Raw cosine similarity scores are normalized into a [0,1]
        range before QCA calibration.

        Normalization improves comparability across conditions
        with different similarity score distributions.
        """)
        st.latex(r"""
        x_{normalized}
        =
        \frac{x - x_{min}}
        {x_{max} - x_{min}}
        """)
        
        norm_df = pd.DataFrame({
            "Term": [
                "x",
                "x_min",
                "x_max"
            ],
            "Definition": [
                "Raw cosine similarity score",
                "Minimum similarity value",
                "Maximum similarity value"
            ]
        })
        st.table(norm_df)

        st.dataframe(normalized_df)
        
        st.subheader("Calibration")

        mode = st.sidebar.selectbox(
            "Calibration Mode",
            [
                "Crisp-set",
                "Fuzzy-set"
            ]
        )

        if mode == "Crisp-set":

            threshold = st.sidebar.slider(
                "Threshold",
                0.0,
                1.0,
                0.5
            )

            calibrated_df = crisp_calibration(
                normalized_df,
                conditions,
                threshold
            )

            st.subheader("Crisp-set Calibration Logic")
            st.markdown(f"""
            Calibration transforms normalized semantic scores
            into binary set memberships required for csQCA.
            """)
            st.latex(r"""
            \text{Membership}(x)=
            \begin{cases}
            1, & x \geq \text{threshold} \\
            0, & x < \text{threshold}
            \end{cases}
            """)
            threshold_df = pd.DataFrame({
                "Range": [
                    f"x ≥ {threshold:.2f}",
                    f"x < {threshold:.2f}"
                ],
                "Membership": [
                    1,
                    0
                ]
            })

            st.table(threshold_df)

            st.subheader("Binary Membership Scores")

            st.markdown("""
            Crisp-set memberships used directly for:
            - truth table construction
            - configurational analysis
            - necessity analysis
            """)

            st.dataframe(calibrated_df)

            st.subheader("Calibration Traceability")
            with st.expander(
                "Calibration Traceability Pipeline",
                expanded=False
            ):

                st.markdown("""
                Inspect the complete methodological transformation pipeline:

                raw text
                → semantic similarity
                → normalized score
                → calibrated membership
                """)

                selected_condition = st.selectbox(
                    "Select Condition",
                    conditions,
                    key=f"pipeline_{mode}"
                )

                pipeline_df = pd.DataFrame({
                    "Case ID": scores_df["case_id"],
                    "Raw Text": scores_df["text"],
                    "Raw Similarity": scores_df[selected_condition],
                    "Normalized Score": normalized_df[selected_condition],
                    "Membership Value": calibrated_df[selected_condition]
                })

                st.dataframe(
                    pipeline_df,
                    use_container_width=True
                )

            truth_table = generate_truth_table(
                calibrated_df,
                conditions
            )

        
        else:

            full_membership = st.sidebar.slider(
                "Full Membership",
                0.0,
                1.0,
                0.8
            )

            crossover = st.sidebar.slider(
                "Crossover",
                0.0,
                1.0,
                0.5
            )

            full_nonmembership = st.sidebar.slider(
                "Full Nonmembership",
                0.0,
                1.0,
                0.2
            )

            calibrated_df = fuzzy_calibration(
                normalized_df,
                conditions,
                full_membership,
                crossover,
                full_nonmembership
            )

            st.subheader("Fuzzy-set Calibration Logic")
            st.markdown(f"""
            Calibration transforms normalized semantic scores
            into binary set memberships required for fsQCA.
            """)
            st.latex(r"""
            Membership(x)=
            \begin{cases}

            1
            &
            x \geq FM
            \\[10pt]

            0
            &
            x \leq FNM
            \\[10pt]

            0.5
            &
            x = CO
            \\[10pt]

            0.5 +
            \left(
            \frac{x-CO}{FM-CO}
            \right)\times0.5
            &
            CO < x < FM
            \\[12pt]

            \left(
            \frac{x-FNM}{CO-FNM}
            \right)\times0.5
            &  
            FNM < x < CO

            \end{cases}
            """)

            symbol_df = pd.DataFrame({
                "Symbol": [
                    "x",
                    "FM",
                    "CO",
                    "FNM"
                ],
                "Meaning": [
                    "Normalized semantic similarity score",
                    "Full membership threshold",
                    "Crossover threshold",
                    "Full non-membership threshold"
                ]
            })

            st.table(symbol_df)
            
            interpret_df = pd.DataFrame({
                "Region": [
                    f"x ≥ {full_membership:.2f}",
                    f"x = {crossover:.2f}",
                    f"x ≤ {full_nonmembership:.2f}",
                    f"{crossover:.2f} < x < {full_membership:.2f}",
                    f"{full_nonmembership:.2f} < x < {crossover:.2f}"
                ],
                "Membership Interpretation": [
                    "Full membership (1.0)",
                    "Maximum ambiguity (0.5)",
                    "Full non-membership (0.0)",
                    "Increasing membership",
                    "Decreasing membership"
                ]
            })

            st.table(interpret_df)

            st.subheader("Fuzzy Membership Scores")

            st.markdown("""
            Continuous fuzzy memberships used for:
            - necessity analysis
            - sufficiency consistency
            - coverage calculations
            """)

            st.dataframe(calibrated_df)

            st.subheader("Calibration Traceability")
            with st.expander(
                "Calibration Traceability Pipeline",
                expanded=False
            ):

                st.markdown("""
                Inspect the complete methodological transformation pipeline:

                raw text
                → semantic similarity
                → normalized score
                → calibrated membership
                """)

                selected_condition = st.selectbox(
                    "Select Condition",
                    conditions,
                    key=f"pipeline_{mode}"
                )

                pipeline_df = pd.DataFrame({
                    "Case ID": scores_df["case_id"],
                    "Raw Text": scores_df["text"],
                    "Raw Similarity": scores_df[selected_condition],
                    "Normalized Score": normalized_df[selected_condition],
                    "Membership Value": calibrated_df[selected_condition]
                })

                st.dataframe(
                    pipeline_df,
                    use_container_width=True
                )

            configuration_df = build_configurations(
                calibrated_df,
                conditions,
                threshold=0.5
            )

            st.subheader("QCA-ready Dataset Construction")
            st.markdown("""
            Fuzzy-set memberships are continuous values between 0 and 1.

            However, truth table construction and logical minimization
            require simplified binary causal configurations.

            """)
            st.markdown("""
            The resulting binary strings represent causal
            configurations used in truth table analysis.

            - truth table construction
            - configurational analysis
            - logical minimization
            """)

            st.latex(r"""
            Condition(x)=
            \begin{cases}
            1, & Membership(x) \geq 0.5 \\
            0, & Membership(x) < 0.5
            \end{cases}
            """)

            config_explain_df = pd.DataFrame({
                "Configuration": [
                    "111",
                    "011",
                    "100",
                    "000"
                ],
                "Interpretation": [
                    "All conditions present",
                    f"{conditions[1]} and {conditions[2]} present",
                    f"Only {conditions[0]} present",
                    "All conditions absent"
                ]
            })

            st.table(config_explain_df)

            display_columns = (
                ["case_id"]
                + conditions
                + ["configuration"]
            )

            st.dataframe(
                configuration_df[display_columns],
                use_container_width=True
            )

            truth_table = generate_truth_table(
                configuration_df,
                conditions
            )

        
        st.subheader("Membership Heatmap")

        heatmap_fig = plot_membership_heatmap(
            calibrated_df,
            conditions
        )

        st.plotly_chart(
            heatmap_fig,
            use_container_width=True
        )

        st.subheader("Score Distribution")

        selected_condition = st.selectbox(
            "Select Condition",
            conditions
        )

        if mode == "Crisp-set":

            dist_fig = plot_score_distribution(
                normalized_df,
                selected_condition,
                threshold=threshold
            )

        else:

            dist_fig = plot_score_distribution(
                normalized_df,
                selected_condition,
                crossover=crossover,
                full_membership=full_membership,
                full_nonmembership=full_nonmembership
            )

        st.plotly_chart(
            dist_fig,
            use_container_width=True
        )

        if mode == "Crisp-set":

            region_df = pd.DataFrame({
                    "Region": [
                        f"x ≥ {threshold:.2f}",
                        f"x < {threshold:.2f}"
                     ],
                    "Interpretation": [
                        "In Set",
                        "Out of Set"
                    ]
            })

        else:

            region_df = pd.DataFrame({
                "Region": [
                    f"x ≥ {full_membership:.2f}",
                    f"{crossover:.2f} < x < {full_membership:.2f}",
                    f"x = {crossover:.2f}",
                    f"{full_nonmembership:.2f} < x < {crossover:.2f}",
                    f"x ≤ {full_nonmembership:.2f}"
                ],
                "Interpretation": [
                    "Full Membership",
                    "Upper Partial Membership",
                    "Maximum Ambiguity",
                    "Lower Partial Membership",
                    "Full Non-membership"
                ]
            })

        st.table(region_df)

        st.subheader("Truth Table")

        st.dataframe(truth_table)

        truth_fig = plot_truth_table(
            truth_table,
            conditions
        )

        st.plotly_chart(
            truth_fig,
            use_container_width=True
        )

        st.subheader("Solution Configurations")

        solution_df = truth_table.copy()

        # Strong configurations
        strong_configs = solution_df[
            solution_df["outcome_consistency"] >= 0.8
        ]

        # Weak configurations
        weak_configs = solution_df[
            (solution_df["outcome_consistency"] >= 0.5)
            &
            (solution_df["outcome_consistency"] < 0.8)
        ]

        # Contradictory configurations
        contradictory_configs = solution_df[
            (solution_df["outcome_consistency"] > 0.4)
            &
            (solution_df["outcome_consistency"] < 0.6)
        ]

        if len(strong_configs) > 0:

            st.markdown("### Strong Solution Configurations")
            st.markdown("""
                        - consistency ≥ 0.80
                        - configuration strongly associated with the outcome
                        """)

            strong_configs = strong_configs[
                [
                    "configuration",
                    "n_cases",
                    "outcome_consistency",
                    "coverage"
                ]
            
            ]
            strong_configs["interpretation"] = (
                "Strong sufficient configuration"
            )

            st.dataframe(strong_configs)

        else:

            st.info(
                "No strong solution configurations detected."
            )


        if len(weak_configs) > 0:

            st.markdown("### Weak Configurations")
            st.markdown("""
                        - 0.50 ≤ consistency < 0.80
                        - moderate or unstable association with the outcome
                        """)

            weak_configs = weak_configs[
                [
                    "configuration",
                    "n_cases",
                    "outcome_consistency",
                    "coverage"
                ]
            ]

            weak_configs["interpretation"] = (
                "Weak or moderately sufficient configuration"
            )

            st.dataframe(weak_configs)


        if len(contradictory_configs) > 0:

            st.markdown("### Contradictory Configurations")
            st.markdown("""
                        - 0.40 < consistency < 0.60
                        - configuration associated with both presence and absence of the outcome
                        """)

            contradictory_configs = contradictory_configs[
                [
                    "configuration",
                    "n_cases",
                    "outcome_consistency",
                    "coverage"
                ]
            ]

            contradictory_configs["interpretation"] = (
                "Contradictory configuration"
            )

            st.dataframe(contradictory_configs)

        necessity_df = necessity_analysis(
            calibrated_df,
            conditions
        )

        st.subheader("Necessity Analysis")

        st.dataframe(necessity_df)

        cc_fig = plot_consistency_coverage(
            necessity_df
        )

        st.plotly_chart(
            cc_fig,
            use_container_width=True
        )

        st.subheader("Export Results")

        st.download_button(
            label="Download Scores CSV",
            data=scores_df.to_csv(index=False),
            file_name="scores.csv",
            mime="text/csv"
        )

        st.download_button(
            label="Download Normalized CSV",
            data=normalized_df.to_csv(index=False),
            file_name="normalized_scores.csv",
            mime="text/csv"
        )

        st.download_button(
            label="Download Calibrated CSV",
            data=calibrated_df.to_csv(index=False),
            file_name="calibrated.csv",
            mime="text/csv"
        )

        st.download_button(
            label="Download Truth Table CSV",
            data=truth_table.to_csv(index=False),
            file_name="truth_table.csv",
            mime="text/csv"
        )