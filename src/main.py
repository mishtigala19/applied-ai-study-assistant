from retriever import load_documents, retrieve_relevant_context
from generator import generate_answer
from guardrails import check_input_safety, check_confidence
from logger import log_interaction


def run_system():
    print("Applied AI Study Assistant")
    print("Ask a question about AI, RAG, guardrails, reliability, or agentic workflows.")
    print("Type 'exit' to quit.\n")

    documents = load_documents("data/notes.txt")

    while True:
        query = input("Your question: ")

        if query.lower() == "exit":
            print("Goodbye!")
            break

        is_safe, message = check_input_safety(query)

        if not is_safe:
            print(f"Guardrail: {message}\n")
            continue

        context, confidence = retrieve_relevant_context(query, documents)
        confident_enough = check_confidence(confidence)

        if not confident_enough:
            response = {
                "answer": "I do not have enough relevant context to answer this confidently.",
                "confidence": round(confidence, 2),
                "sources_used": []
            }
        else:
            response = generate_answer(query, context, confidence)

        print("\nAnswer:")
        print(response["answer"])

        print("\nConfidence Score:")
        print(response["confidence"])

        print("\nSources Used:")
        if response["sources_used"]:
            for source in response["sources_used"]:
                print(f"- {source}")
        else:
            print("- No reliable source found.")

        print()

        log_interaction(query, response["answer"], response["confidence"])


if __name__ == "__main__":
    run_system()