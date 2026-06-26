import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
KNOWLEDGE_DIR = BASE_DIR / "knowledge"

def load_json(filename: str):
    with open(KNOWLEDGE_DIR / filename, "r", encoding="utf-8") as f:
        return json.load(f)

def load_md(filename: str):
    with open(KNOWLEDGE_DIR / filename, "r", encoding="utf-8") as f:
        return f.read()

def load_knowledge(language: str):
    if language == "fa":
        return {
            "principles": load_json("principles.fa.json"),
            "concepts": load_json("concepts.fa.json"),
            "chapters": load_md("chapters.fa.md")
        }
    return {
        "principles": [],
        "concepts": [],
        "chapters": ""
    }
