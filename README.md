# NLP-Assisted Text-to-QCA Analysis Tool

An explainable computational social science platform that transforms qualitative text into QCA-ready datasets using semantic similarity scoring, transparent calibration workflows, and configurational analysis.

---

# Project Overview

This project implements a research-oriented pipeline for converting textual data into crisp-set (csQCA) and fuzzy-set (fsQCA) analytical outputs.

The tool is designed for:
- computational social science
- digital governance research
- policy analysis
- qualitative comparative analysis (QCA)
- mixed-methods research workflows

The system prioritizes:
- methodological transparency
- reproducibility
- explainability
- non-programmer usability

---

# Research Workflow

```text
Raw Text
    ↓
Prototype Definition
    ↓
Semantic Embedding
    ↓
Cosine Similarity Scoring
    ↓
Normalization
    ↓
Calibration
    ↓
Crisp/Fuzzy Membership
    ↓
Truth Table Construction
    ↓
Consistency & Coverage
    ↓
Solution Configurations
```

---

# Key Features

## Semantic Prototype Matching
- Multilingual semantic embeddings
- Prototype-based conceptual operationalization
- Transparent similarity scoring

## QCA Functionality
- Crisp-set QCA (csQCA)
- Fuzzy-set QCA (fsQCA)
- Truth table generation
- Necessity analysis
- Solution configuration identification

## Calibration System
- Adjustable thresholds
- Transparent membership transformation
- Calibration traceability pipeline

## Visual Analytics
- Membership heatmaps
- Score distribution plots
- Truth table visualization
- Consistency vs coverage analysis

## Export Support
- Similarity scores
- Normalized datasets
- Calibrated datasets
- Truth tables
- CSV export support

---

# Technology Stack

| Component | Tool |
|---|---|
| Frontend/UI | Streamlit |
| Data Processing | pandas |
| Embeddings | sentence-transformers |
| Similarity | scikit-learn |
| Visualization | Plotly |
| QCA Logic | Custom Python implementation |
| Export | pandas/openpyxl |

---

# Project Structure

```text
text_qca_tool/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── text_dataset.csv
│   └── prototypes.csv
│
├── outputs/
│
├── docs/
│   ├── technical_spec.md
│   └── methodology.md
│
└── src/
    ├── data_loader.py
    ├── embedding_engine.py
    ├── scoring.py
    ├── normalization.py
    ├── calibration.py
    ├── configurations.py
    ├── truth_table.py
    ├── qca_analysis.py
    └── visualization.py
```

---

# Installation

## 1. Clone Repository

```bash
git clone <repository-url>
cd text_qca_tool
```

---

## 2. Create Virtual Environment

Mac/Linux:

```bash
python3.11 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

# Requirements

Recommended Python version:

```text
Python 3.11
```

Main dependencies:

```text
streamlit==1.45.1
pandas==2.2.3
numpy==2.2.6
sentence-transformers==4.1.0
scikit-learn==1.6.1
plotly==6.1.0
openpyxl==3.1.5
torch==2.7.0
```

---

# Running the Application

```bash
streamlit run app.py
```

The Streamlit dashboard will open automatically in your browser.

---

# Input Dataset Requirements

## Text Dataset

Required columns:

| Column | Description |
|---|---|
| case_id | Unique case identifier |
| text | Raw textual data |
| outcome | Binary outcome variable (0 or 1) |

Example:

| case_id | text | outcome |
|---|---|---|
| 1 | Citizens express frustration about delays | 1 |

---

## Prototype Dataset

Required columns:

| Column | Description |
|---|---|
| condition_name | Name of conceptual condition |
| prototype | Conceptual definition |
| type | condition or outcome |

Example:

| condition_name | prototype | type |
|---|---|---|
| dissatisfaction | Citizen expresses anger or frustration | condition |

---

# Methodological Design

## 1. Semantic Embeddings

The platform uses:

```text
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

This model was selected because it:
- supports multilingual text
- supports semantic similarity workflows
- is lightweight and deployable
- performs well for conceptual matching tasks

---

## 2. Similarity Scoring

The platform computes cosine similarity between:
- text embeddings
- prototype embeddings

```math
Similarity(Text_i, Prototype_j)
=
cos(E_text_i, E_prototype_j)
```

---

## 3. Score Normalization

Similarity scores are normalized into the [0,1] interval using min-max normalization.

```math
x_normalized =
(x - x_min) / (x_max - x_min)
```

---

## 4. Calibration

### Crisp-set Calibration

```math
Membership(x)=
1 if x ≥ threshold
0 otherwise
```

### Fuzzy-set Calibration

Supports:
- full membership threshold
- crossover threshold
- full non-membership threshold

---

# Visual Analytics

## Membership Heatmap
Displays condition memberships across cases.

## Score Distribution Plot
Displays score distributions and calibration thresholds.

## Truth Table Visualization
Displays configuration frequencies and consistency.

## Consistency vs Coverage Plot
Displays necessity analysis metrics.

---

# Output Features

The platform generates:
- semantic similarity tables
- normalized condition scores
- calibrated membership datasets
- truth tables
- necessity analysis outputs
- solution configurations

Export format:
- CSV

---

# Error Handling

The platform validates:
- missing columns
- duplicate case IDs
- missing text values
- invalid outcomes
- duplicate condition names
- invalid prototype types

The system prioritizes:
- transparent warnings
- stable workflows
- reproducible outputs

---

# Research Assumptions

The platform assumes:
- semantic embeddings approximate conceptual meaning
- prototypes influence scoring quality
- calibration thresholds affect membership interpretation
- configurational outputs depend on calibration logic

---

# Limitations

## Semantic Ambiguity

Embeddings cannot fully capture nuance, sarcasm, or domain-specific language.

## Prototype Sensitivity

Results rely heavily on prototype definitions, and weak prototypes reduce conceptual validity.

## Calibration Dependence

- Threshold selection is partly subjective
- Small threshold changes can significantly alter QCA results
- Calibration may oversimplify semantic nuance
- Default thresholds may not fit all datasets
- Semantic similarity scores are not perfectly equivalent to theoretical meaning
- Risk of overfitting thresholds to obtain desirable configurations

## Small-N Sensitivity
QCA methods can become unstable with small datasets or sparse configurations.

## Limited Causal Inference
The tool identifies configurational associations rather than definitive causal relationships.

## Computational Simplification
The current implementation simplifies some advanced QCA procedures and does not yet implement advanced Boolean minimization techniques.

---

# Recommended Use Cases

- Digital governance research
- Citizen feedback analysis
- Public administration studies
- Comparative configurational research
- Policy discourse analysis

---

# Future Improvements

Potential future extensions:
- advanced Boolean minimization
- automated threshold recommendation
- multilingual language detection
- Add text normalization to standardize informal expressions and remove redundant oral words.
- PDF export support
- LLM-assisted prototype generation

---

# Deployment

Recommended deployment platforms:
- Streamlit Community Cloud
- Hugging Face Spaces
- Render

---

# License

This project is intended for educational and research purposes.