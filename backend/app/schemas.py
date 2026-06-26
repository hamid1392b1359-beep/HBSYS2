from pydantic import BaseModel
from typing import Literal

class AskRequest(BaseModel):
    question: str
    language: Literal["fa", "en"] = "fa"
    output_mode: Literal["triple", "short", "analytical"] = "triple"

class AskResponse(BaseModel):
    answer: str
    language: str
    output_mode: str
