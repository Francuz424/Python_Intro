def count_words(text):
    """Zlicza liczbę słów w tekście."""
    return len(text.split())

def remove_punctuation(text):
    """Usuwa znaki interpunkcyjne z tekstu."""
    import string
    return text.translate(str.maketrans('', '', string.punctuation))