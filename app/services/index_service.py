from app.utils.document_loader import load_documents
from app.utils.chunking import chunk_text
from app.services.embedding_service import create_embedding
from app.vectorstore.faiss_store import FAISSStore


vector_store = FAISSStore()


def build_index():
    """
    Load docs and store embeddings in FAISS
    """

    documents = load_documents(
        "data/docs.json"
    )

    for document in documents:

        chunks = chunk_text(
            document["content"]
        )

        for chunk_id, chunk in enumerate(chunks):

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