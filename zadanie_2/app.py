import re
from datetime import datetime

def is_valid_email(email: str) -> bool:
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,4}$"
    return re.match(pattern, email) is not None

def calculate_rectangle_area(width: float, height: float) -> float:
    if width < 0 or height < 0:
        raise ValueError("Wymiary muszą być nieujemne.")
    return width * height

def filter_and_sort_numbers(numbers: list[int]) -> list[int]:
    return sorted([num for num in numbers if num >= 0])

def convert_date_format(date_str: str) -> str:
    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        return date_obj.strftime("%Y/%m/%d")
    except ValueError:
        raise ValueError("Niepoprawny format daty. Oczekiwano 'dd-mm-yyyy'.")

def is_palindrome(text: str) -> bool:
    clean = ''.join(filter(str.isalnum, text)).lower()
    return clean == clean[::-1]