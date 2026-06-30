from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.get("/api/question")
def read_root():
    return {
        "status": "online",
        "system": "H.B-SYST",
        "message": "خوش آمدید. سیستم آماده پاسخگویی است."
    }

@app.post("/api/question")
async def ask_question(request: QuestionRequest):
    # اینجا منطق اصلی پاسخگویی شما قرار می‌گیرد
    # در حال حاضر یک پاسخ تست برمی‌گردانیم
    user_q = request.question
    return {
        "answer": f"پیام شما دریافت شد: {user_q}. سیستم در حال تحلیل است."
    }

@app.get("/api/health")
def health_check():
    return {"status": "healthy"}
