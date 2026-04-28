from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_documents(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    documents = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]
    return documents


def retrieve_relevant_context(query, documents, top_k=2):
    if not query.strip():
        return [], 0.0

    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(documents + [query])

    document_vectors = vectors[:-1]
    query_vector = vectors[-1]

    similarities = cosine_similarity(query_vector, document_vectors).flatten()

    ranked_indexes = similarities.argsort()[::-1][:top_k]
    retrieved_context = [documents[i] for i in ranked_indexes if similarities[i] > 0]

    confidence = float(similarities[ranked_indexes[0]]) if len(ranked_indexes) > 0 else 0.0

    return retrieved_context, confidence