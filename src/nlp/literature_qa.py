"""Stub for literature QA using transformers + LangChain.
Replace dummy return with actual model inference when running locally.
"""
from dataclasses import dataclass

@dataclass
class QAResult:
    answer: str

class LiteratureQA:
    def __init__(self, model_name: str = "distilbert-base-uncased"):
        self.model_name = model_name
        # Intentionally not loading heavy models in scaffold.
        # In a real run:
        # from transformers import pipeline
        # self.pipe = pipeline("question-answering", model=model_name)

    def ask(self, context: str, question: str) -> QAResult:
        # In actual code, run: self.pipe(question=question, context=context)
        return QAResult(answer=f"[Stub] Best guess for '{question}' given context of length {len(context)}.")
