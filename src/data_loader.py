import pandas as pd

def load_csv(file_source):
    return pd.read_csv(file_source)

def validate_text_dataset(df):
    
    required_columns = [
        "case_id",
        "text",
        "outcome"
    ]

    missing = [
        c for c in required_columns
        if c not in df.columns
    ]

    if missing:
        return False, f"Missing columns: {missing}"

    if df["text"].isnull().sum() > 0:
        return False, "Text column contains missing values."

    if df["case_id"].duplicated().sum() > 0:
        return False, "Duplicate case_id values found."

    valid_outcomes = {0, 1}

    invalid = set(df["outcome"].unique()) - valid_outcomes

    if invalid:
        return False, "Outcome column must contain only 0 or 1."

    return True, "Text dataset validated successfully."



def validate_prototypes(df):

    required_columns = [
        "condition_name",
        "prototype",
        "type"
    ]

    missing = [
        c for c in required_columns
        if c not in df.columns
    ]

    if missing:
        return False, f"Missing columns: {missing}"

    if df["prototype"].isnull().sum() > 0:
        return False, "Prototype column contains missing values."

    if df["condition_name"].duplicated().sum() > 0:
        return False, "Duplicate condition_name values found."

    valid_types = {
        "condition",
        "outcome"
    }

    invalid = set(df["type"].unique()) - valid_types

    if invalid:
        return False, f"Invalid type values found: {invalid}"

    return True, "Prototype dataset validated successfully."