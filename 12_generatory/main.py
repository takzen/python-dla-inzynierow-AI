# 12.1. Wstęp do Generatorów
# Generatory to specjalny rodzaj funkcji, które zwracają iterator.
# Używają słowa kluczowego 'yield' zamiast 'return'.  'yield' "pamięta" stan.

# 12.2. Tworzenie Generatora
def liczby_parzyste(max):
    n = 0
    while n <= max:
        yield n
        n += 2

# Użycie generatora
parzyste = liczby_parzyste(10)
print(next(parzyste)) # 0
print(next(parzyste)) # 2
print(next(parzyste)) # 4
# ...i tak dalej.  Możemy też użyć pętli:

for liczba in liczby_parzyste(6):
    print(liczba) # 0, 2, 4, 6


# 12.3. Różnice między 'yield' a 'return'
# - 'return' kończy działanie funkcji i zwraca wartość.
# - 'yield' wstrzymuje działanie funkcji, zwraca wartość,
#   ale *zapamiętuje* stan, pozwalając na kontynuację od tego miejsca.

def funkcja_z_return():
    return 1
    return 2  # To się nigdy nie wykona

def funkcja_z_yield():
    yield 1
    yield 2

print(funkcja_z_return()) # 1

generator = funkcja_z_yield()
print(next(generator)) # 1
print(next(generator)) # 2


# 12.4. Zalety Generatorów: Efektywność Pamięciowa
# Generatory są idealne do pracy z dużymi zbiorami danych,
# ponieważ nie przechowują wszystkich wartości w pamięci naraz.

# Wyobraźmy sobie generowanie miliona liczb:
# (Nie uruchamiaj tego kodu, jeśli nie masz dużo RAM-u!)

# Sposób bez generatora (źle):
# def milion_liczb():
#     lista = []
#     for i in range(1000000):
#         lista.append(i)
#     return lista
#
# moje_liczby = milion_liczb()  # Zużywa dużo pamięci!

# Sposób z generatorem (dobrze):
def milion_liczb_generator():
    for i in range(1000000):
        yield i

moje_liczby = milion_liczb_generator() # Prawie nie zużywa pamięci w tym momencie!

# Dopiero iterowanie po generatorze pobiera kolejne wartości:
# for liczba in moje_liczby:
#     if liczba > 10:  # Przykład ograniczenia, żeby nie wypisywać miliona liczb
#         break
#     print(liczba)


# 12.5. Wyrażenia Generatorowe (Generator Expressions)
# Skrócony sposób tworzenia prostych generatorów, podobny do list comprehension.

kwadraty = (x**2 for x in range(10))  # Nawiasy okrągłe!
print(next(kwadraty)) # 0
print(next(kwadraty)) # 1

for k in kwadraty:  # Można iterować
    print(k)        # 4, 9, 16, 25, 36, 49, 64, 81



# 12.6.  Generatory a Iteratory
# Każdy generator jest iteratorem, ale nie każdy iterator jest generatorem.
# Iterator to ogólny interfejs do przechodzenia po elementach (np. lista).
# Generator to *sposób* na stworzenie iteratora (za pomocą funkcji z 'yield').

# Przykład iteratora (lista):
moja_lista = [1, 2, 3]
iterator_listy = iter(moja_lista)  # Tworzymy iterator
print(next(iterator_listy)) # 1
print(next(iterator_listy)) # 2

# 12.7. Zastosowania Generatorów

# - Przetwarzanie dużych plików (linia po linii, bez ładowania całego pliku do pamięci).
def czytaj_linie(sciezka_do_pliku):
    with open(sciezka_do_pliku, 'r') as plik:
        for linia in plik:
            yield linia.strip() # usuwa białe znaki na początku i końcu

# for linia in czytaj_linie("duzy_plik.txt"):
#      print(linia) # przetwarza linia po lini

# - Generowanie nieskończonych ciągów (np. liczb pierwszych).
def liczby_pierwsze():
    n = 2
    while True:
        jest_pierwsza = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                jest_pierwsza = False
                break
        if jest_pierwsza:
            yield n
        n += 1
#
# pierwsze = liczby_pierwsze()
# for _ in range(10):  # Pobierz pierwszych 10 liczb pierwszych
#      print(next(pierwsze))

# - Tworzenie "potoków" przetwarzania danych (pipeline).
def potok():
   yield from (x * 2 for x in range(5))      # Podwaja liczby
   yield from (x + 1 for x in range(5,10))  # dodaje 1

for p in potok():
    print(p)
# - Współprogramy (coroutines) - zaawansowane zastosowanie (omówione oddzielnie).



# 12.8. Generatory z wieloma 'yield'
def funkcja_wiele_yield():
    yield "Pierwszy"
    yield "Drugi"
    yield "Trzeci"

gen = funkcja_wiele_yield()
print(next(gen))
print(next(gen))
print(next(gen))

# 12.9 Generatory nieskończone z pętlą while True
def nieskonczony_generator():
    licznik = 0
    while True:
        yield licznik
        licznik += 1

nieskonczony = nieskonczony_generator()
# for _ in range(5):  # Pętla for zatrzyma się po 5 iteracjach.
#     print(next(nieskonczony))

# Użycie next() bez pętli for spowoduje nieskończone wywoływanie!

# 12.10. Słowo kluczowe yield from
# Umożliwia delegowanie generowania do innego generatora.

def generator1():
    yield 1
    yield 2

def generator2():
    yield from generator1()  # Delegowanie do generator1
    yield 3
    yield 4

gen2 = generator2()
for x in gen2:
    print(x)  # 1, 2, 3, 4

# 12.11 Przykład użycia generatora do filtrowania danych:
def filtruj_liczby(liczby, prog):
    for liczba in liczby:
        if liczba > prog:
            yield liczba

dane = [1, 5, 2, 8, 3, 9, 4]
przefiltrowane = filtruj_liczby(dane, 5)
for liczba in przefiltrowane:
    print(liczba)  # 8, 9


# 12.12. Podsumowanie
# Generatory to potężne narzędzie do efektywnego przetwarzania danych
# w Pythonie. Pozwalają oszczędzać pamięć i tworzyć elegancki, czytelny kod.
print("Rozdział o generatorach zakończony!")