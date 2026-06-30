
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# اجازه دسترسی فرانت‌اند
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {
        "status": "online",
        "system": "H.B-SYST",
        "message": "H.B-SYST API is running"
    }


@app.get("/api/health")
def health():
    return {"status": "healthy"}


@app.post("/api/question")
async def ask_question(request: QuestionRequest):
    question = request.question

    # پاسخ آزمایشی
    return {
        "answer": f"سوال دریافت شد: {question}"
    }
