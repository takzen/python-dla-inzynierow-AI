# 4.1. Wstęp
# Funkcje pozwalają na organizację kodu w modułowe, wielokrotnego użycia bloki.


# 4.2. Funkcje definiowane w programie
def przywitaj():
    print("Witaj w Pythonie!")


przywitaj()


# 4.3. Funkcje z wieloma parametrami
def suma(a, b):
    return a + b


print(suma(5, 3))


# 4.4. Generowanie liczb pseudolosowych
import random


print(random.randint(1, 10))  # Losowa liczba od 1 do 10


# 4.5. Analiza przypadku — gra losowa
def zgadnij_liczbe():
    liczba = random.randint(1, 100)
    proba = int(input("Zgadnij liczbę od 1 do 100: "))
    if proba == liczba:
        print("Gratulacje! Zgadłeś.")
    else:
        print("Spróbuj ponownie! Prawidłowa liczba to:", liczba)


# zgadnij_liczbe()


# 4.6. Standardowa biblioteka Pythona
import os


print("Pliki w katalogu:", os.listdir("."))


# 4.7. Funkcje modułu "math"
import math


print("Pierwiastek z 16:", math.sqrt(16))
print("Liczba Pi:", math.pi)


# 4.8. Wspomagane uzupełnianie kodu
# IDE jak PyCharm i VS Code oferują uzupełnianie kodu (autocompletion).


# 4.9. Domyślne wartości parametrów
def powitanie(imie="Gość"):
    print("Witaj,", imie)


powitanie()
powitanie("Jan")


# 4.10. Argumenty kluczowe
def przedstaw_sie(imie, wiek):
    print(f"Mam na imię {imie} i mam {wiek} lat.")


przedstaw_sie(wiek=30, imie="Anna")


# 4.11. Zmienne listy parametrów
def suma_wielu(*liczby):
    return sum(liczby)


print(suma_wielu(1, 2, 3, 4, 5))


# 4.12. Metody — funkcje należące do obiektów
tekst = "python"
print(tekst.upper())  # Metoda upper zmienia litery na wielkie


# 4.13. Zasięg definicji
x = 10  # Zmienna globalna


def funkcja():
    x = 5  # Zmienna lokalna
    print("Wartość wewnątrz funkcji:", x)


funkcja()
print("Wartość globalna:", x)


# 4.14. O importowaniu nieco dokładniej
from datetime import datetime


print("Aktualna data:", datetime.now())

# 4.15.
#  Przekazywanie argumentów — nieco szczegółów
def zmien_liste(lista):
    lista.append("Nowy element")


moje_dane = [1, 2, 3]
zmien_liste(moje_dane)
print(moje_dane)  # Lista została zmieniona


# 4.16. Rekurencja
def silnia(n):
    if n == 0:
        return 1
    return n * silnia(n - 1)


print("5! =", silnia(5))


# 4.17. Funkcyjny styl programowania
liczby = [1, 2, 3, 4, 5]
kwadraty = list(map(lambda x: x**2, liczby))
print(kwadraty)


# 4.18. Wprowadzenie do Data Science: miary rozproszenia
dane = [10, 20, 30, 40, 50]
print("Odchylenie standardowe:", statistics.stdev(dane))


# 4.19. Podsumowanie
print("Rozdział o funkcjach zakończony!")
