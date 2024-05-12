import re


def normalize_text(text):
    normalized_text = re.sub(r"[^a-zA-Z0-9]+", "-", text)
    normalized_text = normalized_text.strip("-")
    normalized_text = normalized_text.lower()
    return normalized_text
