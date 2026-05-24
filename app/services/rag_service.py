from app.services.retrieval_service import (
    retrieve_context
)

from app.prompts.prompt_template import (
    PROMPT_TEMPLATE
)

from app.services.llm_service import (
    generate_response
)


SIMILARITY_THRESHOLD = 0.40


def answer_question(
    question,
    history,
    vector_store
):

    results = retrieve_context(
        question,
        vector_store
    )

    print(
        "\nRetrieved Results:"
    )

    for item in results:

        print(
            item["metadata"]["title"],
            "->",
            item["score"]
        )

    if len(results) == 0:

        return (
            "I could not find enough "
            "information in the "
            "knowledge base."
        )

    best_score = (
        results[0]["score"]
    )

    if (
        best_score <
        SIMILARITY_THRESHOLD
    ):

        return (
            "I could not find enough "
            "information in the "
            "knowledge base."
        )

    context = "\n".join(
        [
            item["metadata"]["text"]
            for item in results
        ]
    )

    prompt = (
        PROMPT_TEMPLATE.format(
            context=context,
            history=history,
            question=question
        )
    )

    return generate_response(
        prompt
    )