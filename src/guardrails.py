def check_input_safety(user_query):
    if not user_query or not user_query.strip():
        return False, "Please enter a valid question."

    if len(user_query.strip()) < 5:
        return False, "Your question is too short. Please ask a more specific question."

    return True, "Input accepted."


def check_confidence(confidence, threshold=0.15):
    return confidence >= threshold