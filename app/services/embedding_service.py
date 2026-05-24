from sentence_transformers import (
    SentenceTransformer
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def create_embedding(text: str):

    return model.encode(text)


def create_embeddings(texts):

    return model.encode(texts)