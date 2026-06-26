from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .schemas import AskRequest, AskResponse
from .config import FRONTEND_ORIGIN
from .knowledge_loader import load_knowledge
from .retriever import simple_match
from .responder import generate_answer

app = FastAPI(title="H.B-SYST API")

origins = ["*"] if FRONTEND_ORIGIN == "*" else [FRONTEND_ORIGIN]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest):
    knowledge = load_knowledge(req.language)
    retrieved = simple_match(req.question, knowledge)
    answer = generate_answer(req.question, retrieved, req.language)

    return AskResponse(
        answer=answer,
        language=req.language,
        output_mode=req.output_mode
    )
