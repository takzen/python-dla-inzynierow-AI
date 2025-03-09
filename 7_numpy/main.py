import numpy as np
import timeit

# 7.1. Wstęp
# NumPy to biblioteka umożliwiająca efektywne operacje na tablicach wielowymiarowych.


# 7.2. Tworzenie tablic na podstawie istniejących danych
dane = [1, 2, 3, 4, 5]
tablica = np.array(dane)
print("Tablica NumPy:", tablica)


# 7.3. Atrybuty tablic
print("Kształt tablicy:", tablica.shape)
print("Typ danych w tablicy:", tablica.dtype)



# 7.4. Wypełnianie tablicy zadaną wartością
tablica_wartosci = np.full((3, 3), 7)
print("Tablica wypełniona 7:", tablica_wartosci)


# 7.5. Tworzenie tablicy na podstawie zakresu danych
tablica_zakres = np.arange(0, 10, 2)
print("Tablica zakresu:", tablica_zakres)


# 7.6. %timeit — porównanie efektywności tablic i list
lista = list(range(10000))
tablica_numpy = np.arange(10000)
czas_lista = timeit.timeit(lambda: [x * 2 for x in lista], number=1000)
czas_tablica = timeit.timeit(lambda: tablica_numpy * 2, number=1000)
print(f"Czas operacji na liście: {czas_lista:.6f}s, na tablicy NumPy: {czas_tablica:.6f}s")


# 7.7. Inne „magiczne” polecenia IPythona
# W IPythonie można używać np. %timeit do mierzenia czasu wykonania kodu.


# 7.8. Operatory tablicowe
tablica2 = np.array([10, 20, 30, 40, 50])
print("Suma tablic:", tablica + tablica2)
print("Mnożenie tablicy przez skalar:", tablica * 2)


# 7.9. Metody obliczeniowe biblioteki „NumPy”
print("Średnia tablicy:", np.mean(tablica))
print("Suma elementów tablicy:", np.sum(tablica))


# 7.10. Funkcje uniwersalne biblioteki „NumPy”
tablica_log = np.log(tablica)
print("Logarytm naturalny z tablicy:", tablica_log)


# 7.11. Indeksowanie i wyodrębnianie
print("Pierwszy element tablicy:", tablica[0])
print("Ostatnie trzy elementy tablicy:", tablica[-3:])


# 7.12. Widoki tablic jako płytkie kopie
tablica_widok = tablica[:]
tablica_widok[0] = 99
print("Tablica po zmianie widoku:", tablica)


# 7.13. Głębokie kopiowanie
tablica_kopia = tablica.copy()
tablica_kopia[0] = 1
print("Oryginalna tablica:", tablica)
print("Głęboka kopia:", tablica_kopia)


# 7.14. Restrukturyzacja i transponowanie tablic
macierz = np.arange(9).reshape(3, 3)
print("Macierz:", macierz)
print("Transponowana macierz:", macierz.T)


# 7.15. Wprowadzenie do Data Science: szeregi i ramki danych biblioteki Pandas
import pandas as pd
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
print("Ramka danych Pandas:", df)


# 7.16. Podsumowanie
print("Rozdział o bibliotece NumPy zakończony!")