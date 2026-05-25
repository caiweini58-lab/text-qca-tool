import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from src.embedding_engine import encode_texts

def generate_condition_scores(
    cases_df,
    prototypes_df
):

    condition_df = prototypes_df[
        prototypes_df["type"] == "condition"
    ]

    conditions = condition_df[
        "condition_name"
    ].tolist()

    prototype_texts = condition_df[
        "prototype"
    ].tolist()

    text_embeddings = encode_texts(
        cases_df["text"].tolist()
    )

    prototype_embeddings = encode_texts(
        prototype_texts
    )

    results = []

    for i, embedding in enumerate(text_embeddings):

        row = {
            "case_id": cases_df.iloc[i]["case_id"],
            "text": cases_df.iloc[i]["text"],
            "outcome": cases_df.iloc[i]["outcome"]
        }

        for j, condition in enumerate(conditions):

            similarity = cosine_similarity(
                [embedding],
                [prototype_embeddings[j]]
            )[0][0]

            row[condition] = round(
                float(similarity),
                4
            )

        results.append(row)

    return pd.DataFrame(results)