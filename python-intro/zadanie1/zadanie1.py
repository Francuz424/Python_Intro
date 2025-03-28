# Łączenie dwóch list za pomocą funkcji zip()
# Dokumentacja: https://docs.python.org/3/library/functions.html#zip
names = ['Anna', 'Bartek', 'Celina']
ages = [23, 34, 29]
combined = list(zip(names, ages))
print("Połączone dane:", combined)

# Wykorzystanie funkcji z modułu random
# Dokumentacja: https://docs.python.org/3/library/random.html
import random
lucky_number = random.randint(1, 100)
print("Twój szczęśliwy numer to:", lucky_number)

# Obsługa wyjątku przy konwersji danych
# Dokumentacja: https://docs.python.org/3/library/exceptions.html#ValueError
try:
    user_input = input("Podaj liczbę całkowitą: ")
    number = int(user_input)
    print("Wpisałeś:", number)
except ValueError:
    print("Błąd: to nie jest liczba całkowita!")
