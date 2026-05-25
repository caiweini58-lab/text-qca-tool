from sentence_transformers import SentenceTransformer

MODEL_NAME = (
    "sentence-transformers/"
    "paraphrase-multilingual-MiniLM-L12-v2"
)

model = SentenceTransformer(MODEL_NAME)

def encode_texts(texts):

    return model.encode(
        texts,
        normalize_embeddings=True
    )