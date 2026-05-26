# Technical Note — NLP-Assisted Text-to-QCA Analysis Tool

## Introduction

This NLP-powered tool converts qualitative texts into QCA-ready results, supporting both crisp-set and fuzzy-set QCA. Built with Streamlit, it serves researchers in social science, policy and governance studies.

---

# What Does the Tool Do?

The tool operationalizes qualitative concepts computationally by converting raw textual data into measurable condition memberships for QCA analysis.

The platform supports:
- semantic similarity scoring
- crisp-set calibration
- fuzzy-set calibration
- truth table generation
- configurational analysis
- necessity analysis
- visualization of analytical outputs

The tool also provides visual and downloadable intermediate outputs to improve methodological transparency and reproducibility.

---

# What Data Does the Tool Require?

The platform requires two primary datasets.

## 1. Text Dataset

The text dataset contains the cases to be analyzed.

Required columns:
- `case_id` — unique identifier for each case
- `text` — raw textual content
- `outcome` — binary outcome variable (0 or 1)

---

## 2. Prototype Dataset

The prototype dataset defines the conceptual conditions used for semantic matching.

Required columns:
- `condition_name`
- `prototype`
- `type`

---

# What Outputs Does the Tool Produce?

The tool produces several analytical outputs throughout the workflow.

## Similarity Scores

The platform generates cosine similarity scores between text cases and conceptual prototypes. These scores estimate the semantic closeness between a case and a conceptual condition.

---

## Normalized Scores

Similarity scores are normalized into a comparable range between 0 and 1 using min-max normalization.

---

## Calibrated Membership Scores

The normalized scores are transformed into:
- crisp-set memberships (0 or 1)
- fuzzy-set memberships (continuous values between 0 and 1)

---

## QCA-ready Dataset

After calibration, the platform transforms the normalized condition scores into a QCA-ready dataset suitable for configurational analysis.

A QCA-ready dataset contains:
- binary values for each condition
- one row per case
- a generated logical configuration string

---

## Truth Tables

The platform constructs truth tables that summarize:
- logical configurations
- configuration frequencies
- consistency scores
- coverage scores

---

## Solution Configurations

The platform also generates solution configuration outputs from the truth table analysis. These outputs classify configurations according to their consistency with the outcome.

The analysis identifies:
- strong solution configurations
- weak or moderately sufficient configurations
- contradictory configurations

---

## Necessity Analysis

The platform also performs necessity analysis to evaluate whether individual conditions are consistently required for the outcome to occur.

Necessity analysis contains:
- necessity consistency
- necessity coverage

---

## Visual Outputs

The platform includes:
- membership heatmaps
- score distribution plots
- truth table visualizations
- consistency versus coverage plots

---

## Exportable Outputs

Users can export intermediate and final outputs as CSV files for reproducibility and further analysis.

---

# How Should the Results Be Interpreted?

## Semantic Similarity Scores

Higher similarity scores indicate stronger semantic alignment between a case and a conceptual prototype. However, similarity scores do not directly prove causal relationships.

---

## Crisp-set Membership

In crisp-set calibration, cases are either:
- fully in the set (1)
- fully out of the set (0)

This approach simplifies interpretation but may reduce nuance.

---

## Fuzzy-set Membership

Fuzzy-set calibration allows partial membership between 0 and 1.

### Membership Interpretation

| Membership Range | Interpretation |
|---|---|
| ≥ 0.80 | Fully in set |
| 0.50 < x < 0.80 | Increasing membership |
| 0.50 | Maximum ambiguity (crossover) |
| 0.20 < x < 0.50 | Decreasing membership |
| ≤ 0.20 | Fully out of set |

---

## Membership Heatmap

The heatmap provides a clear overview of how each case is coded across the three conditions, confirming wether that the crisp-set or fuzzy-set calibration has successfully dichotomized the texts into clear member/non-member categories for the subsequent QCA analysis.

---

## Truth Table

The table identifies which combinations of citizen communication attributes are most consistently associated with the outcome. Configurations with consistency ≥ 0.80 are strong candidates for inclusion in the final solution, while lower-consistency paths are less reliable.

The bar chart visualizes the frequency of each configuration, with color intensity reflecting outcome consistency, making it easy to spot both common and high-quality paths.

---

## Consistency

Consistency measures the extent to which a configuration is associated with the outcome. Higher consistency values indicate stronger configurational relationships.

---

## Coverage

Coverage measures the empirical relevance of a configuration by indicating how much of the outcome is explained by that configuration.

Researchers should interpret configurations substantively and theoretically rather than relying solely on numerical thresholds.

---

# What Assumptions Does the Tool Make?

The platform relies on several methodological assumptions.

- Semantic embeddings can approximate conceptual meaning within textual data.
- Conceptual prototypes are theoretically meaningful and representative of the intended conditions.
- Cosine similarity provides a reasonable approximation of conceptual closeness.
- Calibration thresholds meaningfully distinguish between set membership categories.
- Configurational causality can be represented through QCA logic and interpreted using consistency and coverage metrics.

---

# What Are the Main Limitations?

## Semantic Ambiguity

Semantic embeddings approximate meaning statistically and may fail to capture nuanced contextual interpretations, sarcasm, or domain-specific language.

---

## Prototype Sensitivity

The quality of results depends heavily on prototype definitions. Weak or vague prototypes can produce unreliable condition memberships.

---

## Calibration Dependence

- Threshold selection is partly subjective
- Small threshold changes can significantly alter QCA results
- Calibration may oversimplify semantic nuance
- Default thresholds may not fit all datasets
- Semantic similarity scores are not perfectly equivalent to theoretical meaning
- Risk of overfitting thresholds to obtain desirable configurations

---

## Small-N Sensitivity

QCA methods can become unstable with small datasets or sparse configurations.

---

## Limited Causal Inference

The tool identifies configurational associations rather than definitive causal relationships.

---

## Computational Simplification

The current implementation simplifies some advanced QCA procedures and does not yet implement advanced Boolean minimization techniques.

---

# What Would the Candidate Improve With More Time?

## Advanced Boolean Minimization

Implementing more sophisticated minimization algorithms would improve configurational analysis quality and theoretical rigor.

---

## Automated Calibration Recommendation

The platform could include data-driven threshold suggestions to support more systematic calibration decisions.

---

## Resolve Illogical Similarity Scores

- Use LLMs to validate and correct abnormal scores.
- Refine prototypes via LLMs to reduce noise.
- Set statistically supported thresholds to filter invalid results.

---

## Raw Text Standardization

Raw texts collected from citizen-government interactions contain extensive colloquial expressions, informal phrases and fragmented sentences. 
Add text normalization to standardize informal expressions and remove redundant oral words.

---

## Improved Visualization

Additional interactive visualizations and configuration heatmaps could improve interpretability.

---

## Enhanced Export Features

Additional export formats such as PDF reports and Excel workbooks would improve usability for researchers.

---

# Conclusion

This tool offers a transparent, reproducible workflow to convert texts into QCA results. It focuses on explainability and usability, with noted limitations in semantic analysis, calibration and prototype design.