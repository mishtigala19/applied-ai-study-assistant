# Applied AI Study Assistant (RAG System)

## Project Summary
This project is an applied AI system that answers questions using Retrieval-Augmented Generation (RAG). Instead of generating answers from scratch, the system retrieves relevant information from a knowledge base and uses it to produce grounded, reliable responses.

This improves accuracy, reduces hallucination, and introduces explainability through source tracking and confidence scoring.

---

## Original Project (Modules 1–3)
This project builds on a basic AI question-answering prototype developed in earlier modules. The original system focused on simple input-output generation without retrieval or reliability checks.

This final version extends the system by adding:
- Retrieval-based reasoning (RAG)
- Guardrails for safety
- Confidence scoring
- Logging and testing for reliability

---

## Features

- Retrieval-Augmented Generation (RAG)
- Input guardrails (invalid/short queries blocked)
- Confidence scoring
- Safe refusal when context is missing
- Source transparency (shows retrieved context)
- Logging system (interaction tracking)
- Automated tests (pytest)

---

## System Architecture

See diagram in `/assets/system_architecture.png`

Flow:
User Input → Guardrails → Retriever → Confidence Check → Generator → Output + Logging

---

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/mishtigala19/applied-ai-study-assistant.git
cd applied-ai-study-assistant