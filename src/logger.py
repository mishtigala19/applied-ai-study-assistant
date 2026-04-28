from datetime import datetime
import os


def log_interaction(query, answer, confidence):
    os.makedirs("logs", exist_ok=True)

    with open("logs/interactions.log", "a", encoding="utf-8") as log_file:
        log_file.write("----- Interaction -----\n")
        log_file.write(f"Timestamp: {datetime.now()}\n")
        log_file.write(f"Question: {query}\n")
        log_file.write(f"Confidence: {confidence}\n")
        log_file.write(f"Answer: {answer}\n\n")