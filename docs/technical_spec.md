# Technical Specification — NLP-Assisted Text-to-QCA Analysis Tool

---

# 1. System Overview

The platform is an explainable NLP-assisted Qualitative Comparative Analysis (QCA) system designed to convert qualitative textual data into configurational analytical outputs.

The platform integrates:
- semantic text embeddings
- prototype-based scoring
- normalization and calibration workflows
- crisp-set and fuzzy-set QCA logic
- visualization systems
- exportable research outputs

The application is implemented as a Streamlit web interface optimized for non-programmer usability and reproducible research workflows.

---

# 2. System Objectives

The system aims to:
- operationalize qualitative concepts computationally
- generate transparent condition memberships
- support csQCA and fsQCA workflows
- expose intermediate analytical transformations
- produce interpretable configurational outputs
- support reproducible computational social science research

---

# 3. System Architecture

## 3.1 High-Level Workflow

```text
Text Dataset
    ↓
Validation Layer
    ↓
Prototype Matching
    ↓
Embedding Generation
    ↓
Cosine Similarity Scoring
    ↓
Normalization
    ↓
Calibration
    ↓
QCA Dataset Construction
    ↓
Truth Table Generation
    ↓
Necessity Analysis
    ↓
Solution Configuration Detection
    ↓
Visualization & Export
```

---

# 4. Technology Stack

| Layer | Technology |
|---|---|
| Frontend/UI | Streamlit |
| Data Processing | pandas |
| Numerical Operations | NumPy |
| Embedding Model | sentence-transformers |
| Similarity Engine | scikit-learn |
| Visualization | Plotly |
| Export | openpyxl/pandas |
| Runtime | Python 3.11 |

---

# 5. Module Specifications

---

# 5.1 Data Input Layer

## File

```text
src/data_loader.py
```

## Responsibilities
- dataset loading
- schema validation
- input integrity checking

## Supported Formats
- CSV
- XLSX (extensible)

## Validation Rules

### Text Dataset

Required columns:
- case_id
- text
- outcome

Validation checks:
- missing values
- duplicate case IDs
- invalid outcome values
- empty datasets

### Prototype Dataset

Required columns:
- condition_name
- prototype
- type

Validation checks:
- duplicate condition names
- invalid prototype types
- missing prototype definitions

---

# 5.2 Embedding Engine

## File

```text
src/embedding_engine.py
```

## Embedding Model

```text
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

## Design Rationale

The model was selected because it:
- supports multilingual text
- supports semantic similarity tasks
- is lightweight and deployable
- performs well for conceptual operationalization

## Core Function

```python
encode_texts(texts)
```

## Output

Normalized semantic embedding vectors.

---

# 5.3 Semantic Scoring Engine

## File

```text
src/scoring.py
```

## Objective

Generate condition scores through semantic similarity comparison between:
- case texts
- conceptual prototypes

## Method

Cosine similarity:

```math
Similarity(Text_i, Prototype_j)
=
cos(E_text_i, E_prototype_j)
```

## Output Structure

| case_id | condition | similarity_score |
|---|---|---|
| 1 | dissatisfaction | 0.84 |

## Design Principles
- interpretability
- reproducibility
- methodological transparency

---

# 5.4 Normalization Layer

## File

```text
src/normalization.py
```

## Objective

Normalize semantic similarity scores into the [0,1] interval prior to calibration.

## Method

Min-max normalization:

```math
x_normalized =
(x - x_min) / (x_max - x_min)
```

## Edge Case Handling

If:

```text
x_max == x_min
```

then:

```text
membership = 0.5
```

to prevent division-by-zero errors.

---

# 5.5 Calibration Engine

## File

```text
src/calibration.py
```

## Supported Modes
- crisp-set calibration
- fuzzy-set calibration

---

## Crisp-set Calibration

### Function

```python
crisp_calibration()
```

### Logic

```math
Membership(x)=
1 if x ≥ threshold
0 otherwise
```

### Default Threshold

```text
0.5
```

---

## Fuzzy-set Calibration

### Function

```python
fuzzy_calibration()
```

### Adjustable Parameters
- full membership threshold
- crossover threshold
- full non-membership threshold

### Membership Interpretation

| Region | Meaning |
|---|---|
| ≥ full membership | fully in set |
| 0.50 < x < 0.80 | Increasing membership |
| crossover | maximum ambiguity |
| 0.20 < x < 0.50 | Decreasing membership |
| ≤ full nonmembership | fully out of set |

---

# 5.6 Configuration Construction Layer

## File

```text
src/configurations.py
```

## Objective

Transform fuzzy memberships into binary logical configurations for truth table generation.

## Example

```text
111
```

represents all conditions present.

```text
101
```

represents:
- first condition present
- second condition absent
- third condition present

---

# 5.7 Truth Table Engine

## File

```text
src/truth_table.py
```

## Outputs
- configuration frequency
- outcome consistency
- coverage

## Metrics

### Consistency
Measures the degree to which a configuration is associated with the outcome.

### Coverage
Measures empirical relevance of the configuration.

---

# 5.8 Necessity Analysis Module

## File

```text
src/qca_analysis.py
```

## Objective

Evaluate whether conditions satisfy necessity criteria.

## Metrics
- necessity consistency
- necessity coverage

---

# 5.9 Visualization Layer

## File

```text
src/visualization.py
```

## Visualization Components

### Membership Heatmap
Displays case-condition memberships.

### Score Distribution Plot
Displays score distributions and calibration thresholds.

### Truth Table Visualization
Displays configuration frequencies and consistency values.

### Consistency vs Coverage Plot
Displays necessity analysis metrics.

## Visualization Library
Plotly.

## Rationale
- interactive
- browser-native
- Streamlit compatible

---

# 5.10 Streamlit Dashboard

## File

```text
app.py
```

## Responsibilities
- file uploads
- parameter selection
- user interaction
- visualization rendering
- export handling

## UI Features
- dataset previews
- calibration controls
- methodological explanations
- calibration traceability
- downloadable outputs

---

# 6. Data Flow Specification

## Stage 1 — Upload
User uploads:
- text dataset
- prototype dataset

## Stage 2 — Validation
Datasets validated against schema requirements.

## Stage 3 — Embedding
Semantic vectors generated.

## Stage 4 — Similarity Scoring
Cosine similarity computed.

## Stage 5 — Normalization
Scores transformed into comparable intervals.

## Stage 6 — Calibration
Membership scores generated.

## Stage 7 — Configuration Construction
Binary configurations produced.

## Stage 8 — QCA Analysis
Truth tables and necessity metrics computed.

## Stage 9 — Visualization & Export
Outputs visualized and exported.

---

# 7. Error Handling Strategy

The platform prioritizes transparent failure handling.

## Supported Safeguards
- missing file detection
- invalid schema warnings
- duplicate identifier detection
- invalid calibration prevention
- empty dataset handling
- invalid outcome detection

## Design Principle

The system should:
- fail transparently
- avoid silent crashes
- provide actionable feedback

---

# 8. Reproducibility Design

The platform emphasizes deterministic workflows.

## Reproducibility Features
- fixed embedding model
- deterministic normalization
- transparent calibration logic
- downloadable intermediate datasets
- explicit threshold selection

---

# 9. Methodological Assumptions

The platform assumes:
- semantic embeddings approximate conceptual meaning
- conceptual prototypes are theoretically meaningful
- cosine similarity reflects semantic closeness
- calibration thresholds influence configurational outputs

---

# 10. Limitations

## Semantic Ambiguity
Embeddings approximate meaning but may miss contextual nuance.

## Prototype Sensitivity
Weak prototypes reduce conceptual validity.

## Calibration Dependence
Threshold choices affect membership assignments.

## Small-N Instability
QCA solutions may become unstable in small datasets.

---

# 11. Scalability Considerations

Current implementation is optimized for:
- small-to-medium research datasets
- interactive analytical workflows
- exploratory configurational analysis

Potential future improvements:
- asynchronous embedding computation
- caching
- GPU acceleration
- database-backed storage

---

# 12. Security & Privacy Considerations

Current implementation:
- performs local processing
- does not persist uploaded files
- minimizes external dependencies

Potential future enhancements:
- authentication
- encrypted storage
- audit logging

---

# 13. Future Development Roadmap

Potential future extensions:
- advanced Boolean minimization
- automatic calibration recommendation
- multilingual language detection
- collaborative annotation workflows
- LLM-assisted concept generation
- richer export formats

---

# 14. Conclusion

The platform operationalizes a transparent computational social science workflow that bridges qualitative text analysis and configurational QCA methodology.

The design prioritizes:
- explainability
- methodological defensibility
- reproducibility
- usability for non-programmers
- research-oriented analytical transparency