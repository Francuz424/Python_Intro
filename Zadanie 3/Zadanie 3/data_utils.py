def normalize_list(data):
    """Normalizuje listę liczb do zakresu 0–1."""
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

def flatten(nested_list):
    """Spłaszcza listę list."""
    return [item for sublist in nested_list for item in sublist]