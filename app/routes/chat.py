from fastapi import APIRouter

from app.models.request_models import (
    ChatRequest
)

from app.services.index_service import (
    build_index
)

from app.services.rag_service import (
    answer_question
)

from app.services.session_service import (
    save_message,
    history_to_text
)

router = APIRouter()

vector_store = build_index()


@router.get("/health")
def health():

    return {
        "status": "healthy"
    }


@router.post("/api/chat")
def chat(
    request: ChatRequest
):

    history = history_to_text(
        request.sessionId
    )

    reply = answer_question(
        request.message,
        history,
        vector_store
    )

    save_message(
        request.sessionId,
        "user",
        request.message
    )

    save_message(
        request.sessionId,
        "assistant",
        reply
    )

    return {
    "reply": reply,
    "tokensUsed": len(reply.split()),
    "retrievedChunks": 3
    }