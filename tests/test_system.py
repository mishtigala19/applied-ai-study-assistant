import sys
import os

sys.path.append(os.path.abspath("src"))

from retriever import load_documents, retrieve_relevant_context
from guardrails import check_input_safety, check_confidence


def test_documents_load_successfully():
    documents = load_documents("data/notes.txt")
    assert len(documents) > 0


def test_retriever_finds_rag_context():
    documents = load_documents("data/notes.txt")
    context, confidence = retrieve_relevant_context("What is RAG?", documents)
    assert len(context) > 0
    assert confidence > 0


def test_empty_input_guardrail():
    is_safe, message = check_input_safety("")
    assert is_safe is False


def test_short_input_guardrail():
    is_safe, message = check_input_safety("AI")
    assert is_safe is False


def test_confidence_guardrail_blocks_low_confidence():
    result = check_confidence(0.01)
    assert result is False


def test_confidence_guardrail_accepts_good_confidence():
    result = check_confidence(0.5)
    assert result is True