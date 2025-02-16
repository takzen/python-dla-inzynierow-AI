# 9. Pliki i wyjątki

# 9.1. Wstęp
#W tej sekcji omówimy pracę z plikami oraz obsługę wyjątków w Pythonie.

# 9.2. Pliki
#Python umożliwia otwieranie i manipulowanie plikami za pomocą funkcji `open()`. Przykład:


with open('plik.txt', 'w') as f:
    f.write('Hello, world!')


# 9.3. Przetwarzanie plików tekstowych
#Czytanie plików:


with open('plik.txt', 'r') as f:
    print(f.read())


# 9.4. Aktualizowanie plików tekstowych
#Dodawanie treści do pliku:


with open('plik.txt', 'a') as f:
    f.write('\nDodana linia')


# 9.5. Serializacja obiektów w formacie JSON
import json


dane = {"imię": "Jan", "wiek": 30}
with open('dane.json', 'w') as f:
    json.dump(dane, f)


# 9.6. Niebezpieczny moduł „pickle”
#Używanie `pickle` może prowadzić do problemów bezpieczeństwa:
import pickle


dane = {"klucz": "wartość"}
with open('dane.pkl', 'wb') as f:
    pickle.dump(dane, f)


# 9.7. Dodatkowe uwagi o plikach
#Sprawdzanie istnienia pliku:
import os
print(os.path.exists('plik.txt'))


# 9.8. Obsługa wyjątków
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Nie można dzielić przez zero!")


# 9.9. Klauzula „finally”
try:
    f = open('plik.txt', 'r')
finally:
    f.close()


# 9.10. Jawne generowanie wyjątków
def podziel(a, b):
    if b == 0:
        raise ValueError("B nie może być zerem!")
    return a / b


# 9.11. Odwijanie stosu i ślad wykonania
#Śledzenie błędów:
import traceback
try:
    1 / 0
except Exception as e:
    print(traceback.format_exc())


# 9.12. Wprowadzenie do Data Science: przetwarzanie plików CSV
import csv
with open('dane.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


# 9.13. Podsumowanie
#Podsumowanie obejmuje przetwarzanie plików i obsługę wyjątków.
