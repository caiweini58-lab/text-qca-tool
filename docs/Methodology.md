# Methodology
## NLP-Assisted Text Classification → QCA Analysis Platform

---

# 1. Methodological Overview

This platform implements an explainable computational social science workflow that transforms qualitative text data into configurational analytical outputs using semantic similarity scoring and Qualitative Comparative Analysis (QCA).

The methodological objective is to operationalize abstract qualitative concepts into measurable analytical conditions while preserving:
- transparency
- interpretability
- reproducibility
- methodological defensibility

The workflow combines:
- Natural Language Processing (NLP)
- semantic embeddings
- calibration procedures
- set-theoretic configurational analysis

---

# 2. Research Logic

The system is designed around the principle that qualitative concepts can be operationalized through semantic similarity between:
- observed text cases
- conceptual prototypes

Instead of relying on opaque black-box classification systems, the platform uses:
- interpretable semantic embeddings
- explicit conceptual prototypes
- transparent calibration procedures

This approach aligns with:
- computational social science
- explainable AI principles
- reproducible qualitative research workflows

---

# 3. Conceptual Operationalization

## 3.1 Prototype-Based Concept Modeling

The platform operationalizes conditions using conceptual prototypes.

A prototype is a short semantic description representing a theoretical concept.

Example:

| Condition | Prototype |
|---|---|
| dissatisfaction | The citizen expresses dissatisfaction anger or frustration |

The methodological assumption is that texts semantically closer to the prototype exhibit stronger membership in the conceptual condition.

---

## 3.2 Why Prototype-Based Scoring

Prototype-based scoring was selected because it:
- preserves interpretability
- avoids opaque supervised classification
- supports small-N research settings
- aligns with qualitative concept formation
- enables transparent condition construction

This is especially important in computational social science where:
- methodological transparency is critical
- conceptual validity matters
- interpretability is prioritized over predictive optimization

---

# 4. Semantic Embedding Methodology

## 4.1 Embedding Model

The platform uses:

```text
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

This model was selected because it:
- supports multilingual semantic representation
- performs efficiently on semantic similarity tasks
- remains lightweight enough for deployment
- supports Chinese and English text
- provides stable sentence-level embeddings

---

## 4.2 Embedding Generation

Both:
- text cases
- conceptual prototypes

are transformed into dense vector embeddings.

The embedding process maps semantic meaning into a high-dimensional vector space where semantically similar texts occupy nearby positions.

---

# 5. Semantic Similarity Scoring

## 5.1 Cosine Similarity

The platform computes semantic similarity using cosine similarity.

Similarity is calculated between:
- text embeddings
- prototype embeddings

The similarity score ranges approximately from:

```text
0 → low semantic similarity
1 → high semantic similarity
```

---

## 5.2 Interpretation

Higher similarity scores indicate that a text case semantically resembles the conceptual prototype more strongly.

This score becomes the basis for subsequent calibration.

---

# 6. Normalization Strategy

## 6.1 Motivation

Raw cosine similarity values from multilingual or Chinese semantic embedding models may exhibit compressed distributions and cross-condition variance. To stabilize calibration and improve interpretability, the platform applies Min-Max normalization before csQCA/fsQCA calibration.

---

## 6.2 Method

The platform applies min-max normalization:

```text
normalized = (x - min(x)) / (max(x) - min(x))
```

This transforms scores into the:

```text
[0,1]
```

interval.

---

## 6.3 Rationale

Normalization improves:
- improves threshold interpretability
- stabilizes fuzzy calibration
- reduces embedding distribution bias
- enables comparable condition scales
- improves truth-table robustness

---

# 7. Calibration Methodology

Calibration transforms similarity scores into set memberships suitable for QCA analysis.

The platform supports:
- crisp-set calibration (csQCA)
- fuzzy-set calibration (fsQCA)

---

# 8. Crisp-Set Calibration

## 8.1 Logic

Crisp-set calibration converts similarity scores into binary memberships.

Rule:

```text
membership = 1 if score ≥ threshold
membership = 0 otherwise
```

---

## 8.2 Interpretation

Binary membership represents:
- condition present
- condition absent

This supports:
- csQCA truth tables
- binary configurational analysis

---

## 8.3 Threshold Selection

Thresholds are user-adjustable to preserve methodological flexibility.

Typical threshold:

```text
0.5
```

However, researchers should justify thresholds theoretically or empirically.

---

# 9. Fuzzy-Set Calibration

## 9.1 Logic

Fuzzy-set calibration preserves degrees of membership.

Membership values range continuously between:

```text
0 → full non-membership
1 → full membership
```

---

## 9.2 Three-Anchor Calibration

The platform uses three calibration anchors:

| Threshold | Meaning |
|---|---|
| Full Membership | Strong inclusion |
| Crossover | Ambiguous membership |
| Full Non-membership | Strong exclusion |

Example:

| Similarity | Membership |
|---|---|
| ≤0.20 | 0 |
| 0.50 | 0.5 |
| ≥0.80 | 1 |

---

## 9.3 Rationale

Fuzzy calibration was selected because it:
- preserves conceptual nuance
- aligns with fsQCA methodology
- reduces information loss
- supports partial set membership

---

# 10. Configuration Construction

## 10.1 Binary Configuration Logic

For truth table construction, conditions are converted into binary logical configurations.

Example:

```text
101
```

represents:
- condition 1 present
- condition 2 absent
- condition 3 present

---

## 10.2 Configurational Reasoning

QCA assumes:
- causality is configurational
- multiple pathways may produce outcomes
- conditions operate jointly rather than independently

Thus, the platform analyzes:
- combinations of conditions
rather than isolated variables.

---

# 11. Truth Table Generation

## 11.1 Purpose

Truth tables summarize:
- condition combinations
- empirical frequencies
- outcome consistency

Each row represents a unique configuration.

---

## 11.2 Metrics

The platform computes:

### Frequency
Number of cases exhibiting a configuration.

### Consistency
Degree to which a configuration leads to the outcome.

### Coverage
Empirical relevance of a configuration.

---

# 12. Necessity Analysis

## 12.1 Necessity Logic

A condition is necessary if:
- the outcome cannot occur without it.

The platform computes:
- necessity consistency
- necessity coverage

---

## 12.2 Interpretation

High consistency indicates that:
- outcome cases are largely contained within the condition.

Coverage indicates:
- empirical relevance of the condition.

---

# 13. Visualization Methodology

The platform includes interactive visual analytics to improve methodological transparency.

---

## 13.1 Membership Heatmap

Displays:
- cases
- conditions
- calibrated memberships

Purpose:
- pattern inspection
- calibration transparency

---

## 13.2 Similarity Distribution Plot

Displays:
- semantic score distributions

Purpose:
- threshold inspection
- calibration interpretation

---

## 13.3 Truth Table Visualization

Displays:
- logical configurations
- configuration frequencies
- consistency levels

Purpose:
- configurational interpretation

---

## 13.4 Consistency vs Coverage Plot

Displays:
- analytical quality of conditions

Purpose:
- comparison of necessity relationships

---

# 14. Reproducibility Considerations

The platform prioritizes reproducible computational social science workflows through:
- deterministic embedding generation
- explicit calibration thresholds
- exportable intermediate datasets
- transparent methodological steps
- version-pinned dependencies

---

# 15. Explainability Principles

The system intentionally avoids opaque black-box AI approaches.

Instead, the methodology emphasizes:
- visible intermediate outputs
- interpretable semantic similarity
- transparent calibration logic
- explicit configurational reasoning

This design aligns with explainable AI principles in social science research contexts.

---

# 16. Assumptions

The methodology assumes:
- semantic embeddings approximate conceptual meaning
- prototypes validly operationalize theoretical constructs
- similarity thresholds meaningfully represent set membership
- QCA appropriately models configurational causality

---

# 17. Limitations

## Semantic Ambiguity
Texts may express concepts indirectly or ambiguously.

## Prototype Dependence
Weak prototypes reduce construct validity.

## Calibration Sensitivity
Threshold choices affect final configurations.

## Small-N Constraints
Limited cases may produce unstable truth tables.

## Simplified Boolean Logic
The implementation prioritizes interpretability over industrial-scale minimization algorithms.

---

# 18. Future Methodological Extensions

Potential methodological improvements include:
- advanced Boolean minimization
- automated prototype generation
- multilingual language detection
- LLM-assisted interpretive support
- robustness testing
- threshold optimization techniques

---

# 19. Conclusion

This platform demonstrates an explainable and reproducible computational social science methodology integrating:
- semantic NLP
- conceptual operationalization
- set-theoretic analysis
- configurational reasoning

The methodological design prioritizes:
- transparency
- interpretability
- research usability
- reproducible analytical workflows

over opaque predictive optimization.