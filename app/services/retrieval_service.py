from app.services.embedding_service import (
    create_embedding
)


def retrieve_context(
    question,
    vector_store,
    top_k=3
):

    query_embedding = (
        create_embedding(
            question
        )
    )

    results = (
        vector_store.search(
            query_embedding,
            top_k
        )
    )

    return results