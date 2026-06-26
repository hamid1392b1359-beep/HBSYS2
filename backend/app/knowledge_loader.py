from pathlib import Path
from typing import List, Dict
from pypdf import PdfReader


def read_text_file(file_path: Path) -> str:
    return file_path.read_text(encoding="utf-8", errors="ignore")


def read_pdf_file(file_path: Path) -> str:
    text = []
    reader = PdfReader(str(file_path))
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text.append(page_text)
    return "\n".join(text)


def load_knowledge(knowledge_dir: str = "knowledge") -> List[Dict[str, str]]:
    base_path = Path(knowledge_dir)
    documents = []

    if not base_path.exists():
        return documents

    for file_path in base_path.iterdir():
        if file_path.is_file():
            suffix = file_path.suffix.lower()

            try:
                if suffix in [".txt", ".md"]:
                    content = read_text_file(file_path)
                elif suffix == ".pdf":
                    content = read_pdf_file(file_path)
                else:
                    continue

                if content.strip():
                    documents.append({
                        "source": file_path.name,
                        "content": content
                    })

            except Exception as e:
                print(f"Error reading {file_path.name}: {e}")

    return documents
