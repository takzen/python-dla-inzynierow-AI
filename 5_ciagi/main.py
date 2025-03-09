# 5.1. Wstęp
# Ciągi w Pythonie obejmują listy i krotki, które umożliwiają przechowywanie wielu wartości w jednej strukturze.


# 5.2. Listy
lista = [1, 2, 3, 4, 5]
print("Lista:", lista)
lista.append(6)  # Dodawanie elementu
print("Po dodaniu 6:", lista)


# 5.3. Krotki
krotka = (10, 20, 30)
print("Krotka:", krotka)
# krotka[0] = 15  # To spowodowałoby błąd, ponieważ krotki są niemutowalne


# 5.4. Rozpakowywanie ciągów
a, b, c = krotka
print("Rozpakowane wartości:", a, b, c)


# 5.5. Wyodrębnianie podciągów
podlista = lista[1:4]  # Elementy od indeksu 1 do 3
print("Podlista:", podlista)


# 5.6. Instrukcja "del"
del lista[2]  # Usunięcie elementu na indeksie 2
print("Po usunięciu trzeciego elementu:", lista)


# 5.7. Listy jako argumenty wywołań funkcji
def suma_listy(lst):
    return sum(lst)


print("Suma listy:", suma_listy(lista))


# 5.8. Sortowanie list
lista.sort()
print("Posortowana lista:", lista)

lista.sort(reverse=True)
print("Posortowana lista:", lista)


# 5.9. Multiplikacja ciągu
powielona_lista = lista * 2
print("Powielona lista:", powielona_lista)


# 5.10. Przeszukiwanie ciągów
if 2 in lista:
    print("3 znajduje się w liście")


# 5.11. Inne metody listy
lista.reverse()
print("Odwrócona lista:", lista)


# 5.12. Symulowanie stosu za pomocą listy
stos = []
stos.append("A")
stos.append("B")
print("Stos:", stos)
stos.pop()
print("Stos po pop:", stos)


# 5.13. Odwzorowywanie list
kwadraty = [x**2 for x in range(5)]
print("Kwadraty liczb 0-4:", kwadraty)


# 5.14. Wyrażenia generatorowe
generator = (x**2 for x in range(5))
print("Pierwsza wartość generatora:", next(generator))
print("Pierwsza wartość generatora:", next(generator))
print("Pierwsza wartość generatora:", next(generator))



# 5.15. Inne funkcje do przetwarzania ciągów
maksimum = max(lista)
print("Największy element listy:", maksimum)


# 5.16. Listy dwuwymiarowe
macierz = [[1, 2, 3], [4, 5, 6]]
print("Element w drugim wierszu i trzeciej kolumnie:", macierz[1][2])


# 5.17. Wprowadzenie do Data Science: symulacje i ich statyczna wizualizacja
import random
import matplotlib.pyplot as plt


dane = [random.gauss(0, 1) for _ in range(1000)]
plt.hist(dane, bins=30)
plt.title("Histogram symulowanych danych")
plt.show()


# 5.18. Podsumowanie
print("Rozdział o listach i krotkach zakończony!")
