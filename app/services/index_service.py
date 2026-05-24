from app.utils.document_loader import load_documents
from app.utils.chunking import chunk_text

from app.services.embedding_service import (
    create_embedding,
    fit_embeddings
)

from app.vectorstore.faiss_store import (
    FAISSStore
)


def build_index():

    documents = load_documents(
        "data/docs.json"
    )

    all_chunks = []

    for document in documents:

        chunks = chunk_text(
            document["content"]
        )

        all_chunks.extend(
            chunks
        )

    fit_embeddings(
        all_chunks
    )

    # Create first embedding
    sample_embedding = create_embedding(
        all_chunks[0]
    )

    # Dynamic dimension
    vector_store = FAISSStore(
        len(sample_embedding)
    )

    for document in documents:

        chunks = chunk_text(
            document["content"]
        )

        for chunk_id, chunk in enumerate(
            chunks
        ):

            embedding = create_embedding(
                chunk
            )

            metadata = {
                "title":
                document["title"],

                "chunk_id":
                chunk_id,

                "source":
                "docs.json",

                "text":
                chunk
            }

            vector_store.add(
                embedding,
                metadata
            )

    return vector_store