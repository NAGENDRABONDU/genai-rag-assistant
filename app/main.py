from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.chat import router
from app.services.index_service import build_index

app = FastAPI(
    title="GenAI RAG Assistant"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router)


@app.on_event("startup")
async def startup_event():

    from app.routes import chat

    chat.vector_store = build_index()