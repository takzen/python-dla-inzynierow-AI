# 8.1. Wstęp
# Łańcuchy znaków w Pythonie są sekwencjami znaków i oferują wiele metod do ich manipulacji.


# 8.2. Formatowanie łańcuchów
imie = "Jan"
wiek = 30
print(f"Nazywam się {imie} i mam {wiek} lat.")


# 8.3. Konkatenowanie i zwielokrotnianie łańcuchów
tekst1 = "Python "
tekst2 = "jest świetny!"
print(tekst1 + tekst2)
print("Ha!" * 3)


# 8.4. Usuwanie białych znaków otaczających łańcuch
tekst = "   Przykładowy tekst   "
print(tekst.strip())


# 8.5. Zmiana wielkości liter w łańcuchu
tekst = "Python jest Super"
print(tekst.upper())
print(tekst.lower())
print(tekst.title())


# 8.6. Operatory porównywania łańcuchów
print("abc" == "abc")  # True
print("abc" < "xyz")  # True


# 8.7. Wyszukiwanie podłańcuchów
tekst = "Znajdź słowo w tym tekście."
print("słowo" in tekst)
print(tekst.find("słowo"))


# 8.8. Zastępowanie podłańcuchów
tekst = "Zamień jabłka na gruszki."
print(tekst.replace("jabłka", "banany"))


# 8.9. Dzielenie i składanie łańcuchów
tekst = "Python,Java,C++"
lista_jezykow = tekst.split(",")
print(lista_jezykow)
print(";".join(lista_jezykow))


# 8.10. Testowanie specyficznych właściwości łańcucha i jego znaków
print("12345".isdigit())  # True
print("abc".isalpha())  # True
print("Python3".isalnum())  # True


# 8.11. Surowe łańcuchy
print(r"Ścieżka do pliku: C:\nowy_folder\plik.txt")


# 8.12. Podstawy wyrażeń regularnych
import re
tekst = "Numer telefonu: 123-456-789"
wzorzec = r"\d{3}-\d{3}-\d{3}"
dopasowanie = re.search(wzorzec, tekst)
if dopasowanie:
    print("Znaleziono numer telefonu:", dopasowanie.group())


# 8.13. Wprowadzenie do Data Science: wyrażenia regularne i preparacja danych w bibliotece Pandas
import pandas as pd
df = pd.DataFrame({"email": ["user@example.com", "test@domain.org"]})
df["domena"] = df["email"].str.extract(r"@(.+)$")
print(df)


# 8.14. Podsumowanie
print("Rozdział o łańcuchach znaków zakończony!")
