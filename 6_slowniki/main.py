# 6.1. Wstęp
# Słowniki i zbiory to struktury danych pozwalające na efektywne przechowywanie i manipulowanie danymi.


# 6.2. Słowniki
slownik = {"imie": "Jan", "wiek": 30, "miasto": "Warszawa"}
print("Słownik:", slownik)
print("Wiek:", slownik["wiek"])
slownik["zawod"] = "Programista"
print("Po dodaniu zawodu:", slownik)


del slownik["miasto"]
print("Po usunięciu miasta:", slownik)


for klucz, wartosc in slownik.items():
    print(f"{klucz}: {wartosc}")


# 6.3. Zbiory
zbior = {1, 2, 3, 4, 5}
print("Zbiór:", zbior)
zbior.add(6)
print("Po dodaniu 6:", zbior)
zbior.remove(3)
print("Po usunięciu 3:", zbior)


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Suma zbiorów:", a | b)
print("Przecięcie zbiorów:", a & b)
print("Różnica zbiorów:", a - b)


# 6.4. Wprowadzenie do Data Science: dynamiczna wizualizacja symulacji
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


def aktualizuj(frame, dane, scatter):
    dane[:, 0] += np.random.randn(len(dane)) * 0.1
    dane[:, 1] += np.random.randn(len(dane)) * 0.1
    scatter.set_offsets(dane)
    return (scatter,)


dane = np.random.rand(100, 2)
fig, ax = plt.subplots()
scatter = ax.scatter(dane[:, 0], dane[:, 1])
ani = animation.FuncAnimation(
    fig, aktualizuj, fargs=(dane, scatter), frames=50, interval=100
)
plt.show()


# 6.5. Podsumowanie
print("Rozdział o słownikach i zbiorach zakończony!")
