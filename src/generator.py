def generate_answer(query, retrieved_context, confidence):
    if not retrieved_context:
        return {
            "answer": "I do not have enough information in the knowledge base to answer that confidently.",
            "confidence": round(confidence, 2),
            "sources_used": []
        }

    combined_context = " ".join(retrieved_context)

    answer = (
        f"Based on the retrieved notes, {combined_context}\n\n"
        f"In relation to your question, this means the answer is grounded in the retrieved course-style context instead of unsupported guessing."
    )

    return {
        "answer": answer,
        "confidence": round(confidence, 2),
        "sources_used": retrieved_context
    }