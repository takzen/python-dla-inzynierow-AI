# 2.1. Wstęp
# Python to język wysokiego poziomu, łatwy do nauki i czytelny dla człowieka.


# 2.2. Zmienne i instrukcje przypisania
x = 10  # Przypisanie wartości 10 do zmiennej x
y = 5  # Przypisanie wartości 5 do zmiennej y
print(x, y)


# 2.3. Obliczenia arytmetyczne
a = 7 + 3  # Dodawanie
print(a)
b = 10 - 4  # Odejmowanie
print(b)
c = 5 * 3  # Mnożenie
print(c)
d = 20 / 4  # Dzielenie
print(d)
e = 10 % 3  # Reszta z dzielenia
print(e)


# 2.4. Funkcja "print" i łańcuchy znaków
imie = "Jan"
nazwisko = "Kowalski"
print("Imię:", imie, "Nazwisko:", nazwisko)


# 2.5. Łańcuchy z potrójnymi ogranicznikami
tekst = """To jest
wielolinijkowy
tekst"""
print(tekst)


# 2.6. Wprowadzanie danych z klawiatury
wiek = input("Podaj swój wiek: ")
print("Masz", wiek, "lat.")


# 2.7. Podejmowanie decyzji: instrukcja "if" i operatory porównania
liczba = int(input("Podaj liczbę: "))
if liczba > 0:
    print("Liczba jest dodatnia")
elif liczba < 0:
    print("Liczba jest ujemna")
else:
    print("Liczba to zero")


# 2.8. Obiekty i typowanie dynamiczne
zmienna = "Tekst"  # String
print(type(zmienna))
zmienna = 10  # Integer
print(type(zmienna))
zmienna = 5.5  # Float
print(type(zmienna))


# 2.9. Wprowadzenie do Data Science — podstawowe statystyki opisowe
import statistics


dane = [10, 20, 30, 40, 50]
print("Średnia:", statistics.mean(dane))
print("Mediana:", statistics.median(dane))
print("Odchylenie standardowe:", statistics.stdev(dane))


# 2.10. Podsumowanie
print("Kurs wprowadzający do Pythona zakończony!")
