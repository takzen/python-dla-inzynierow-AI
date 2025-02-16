# 3.1. Wstęp
# Instrukcje sterujące w Pythonie pozwalają kontrolować przepływ wykonywania kodu.


# 3.2. Słowa kluczowe języka Python
import keyword


print(keyword.kwlist)  # Lista słów kluczowych


# 3.3. Instrukcja "if"
x = 10
if x > 5:
    print("x jest większe od 5")


# 3.4. Instrukcje "if … else" i "if … elif … else"
y = int(input("Podaj liczbę: "))
if y > 0:
    print("Liczba dodatnia")
elif y < 0:
    print("Liczba ujemna")
else:
    print("Zero")


# 3.5. Instrukcja "while"
licznik = 0
while licznik < 5:
    print("Licznik:", licznik)
    licznik += 1


# 3.6. Instrukcja "for"
for i in range(5):
    print("Iteracja:", i)


# 3.7. Rozszerzone przypisania
a = 5
a += 3  # równoważne a = a + 3
print(a)


# 3.8. Iterowanie po ciągach. Formatowane łańcuchy
tekst = "Python"
for litera in tekst:
    print(f"Litera: {litera}")


# 3.9. Nadzorowane iterowanie
lista = [1, 2, 3, 4, 5]
for index, wartosc in enumerate(lista):
    print(f"Indeks: {index}, Wartość: {wartosc}")


# 3.10. Wbudowana funkcja "range" — nieco dokładniej
for i in range(2, 10, 2):  # Start, stop, krok
    print(i)


# 3.11. Obliczenia finansowe — typ "Decimal"
from decimal import Decimal


cena = Decimal("19.99")
ilosc = Decimal("3")
print("Koszt całkowity:", cena * ilosc)


# 3.12. Instrukcje "continue" i "break"
for liczba in range(10):
    if liczba == 5:
        break  # Przerywa pętlę
    if liczba % 2 == 0:
        continue  # Pomija resztę kodu w tej iteracji
    print(liczba)


# 3.13. Operatory boolowskie
prawda = True
falsz = False
print(prawda and falsz)  # False
print(prawda or falsz)  # True
print(not prawda)  # False


# 3.14. Wprowadzenie do Data Science: miary tendencji centralnej
import statistics


dane = [10, 20, 30, 40, 50]
print("Średnia:", statistics.mean(dane))
print("Mediana:", statistics.median(dane))


# 3.15. Podsumowanie
print("Sterowanie przepływem programu w Pythonie zakończone!")
