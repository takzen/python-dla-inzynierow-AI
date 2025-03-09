# 14.1. Wstęp do Dekoratorów
# Dekoratory to funkcje, które modyfikują działanie innych funkcji w elegancki i czytelny sposób.
# Używają składni @nazwa_dekoratora przed definicją funkcji.
# Pozwalają na "opakowanie" funkcji dodatkową logiką, bez modyfikowania jej kodu.

# 14.2. Czym są Funkcje w Pythonie? (Przypomnienie)
# Funkcje w Pythonie są obiektami pierwszej klasy (first-class citizens). Oznacza to, że:
# - Można je przypisywać do zmiennych.
# - Można je przekazywać jako argumenty do innych funkcji.
# - Można je zwracać z innych funkcji.
# - Można je definiować wewnątrz innych funkcji.

def powitaj(imie):
    return f"Witaj, {imie}!"

# Przypisanie funkcji do zmiennej:
funkcja_powitania = powitaj
print(funkcja_powitania("Anna"))  # Witaj, Anna!

# Przekazanie funkcji jako argumentu:
def wykonaj_funkcje(funkcja, argument):
    return funkcja(argument)

print(wykonaj_funkcje(powitaj, "Piotr")) # Witaj, Piotr!

# Zwracanie funkcji z funkcji:
def zwroc_funkcje():
    def wewnetrzna_funkcja(x):
        return x * 2
    return wewnetrzna_funkcja

moja_funkcja = zwroc_funkcje()
print(moja_funkcja(5))  # 10



# 14.3. Prosty Dekorator
# Dekorator to funkcja, która przyjmuje inną funkcję jako argument
# i *zwraca* nową funkcję, która rozszerza lub modyfikuje zachowanie oryginalnej funkcji.

def moj_dekorator(funkcja):  # Przyjmuje funkcję jako argument
    def wrapper():          # Definiuje wewnętrzną funkcję (wrapper)
        print("Przed wywołaniem funkcji...")
        funkcja()          # Wywołuje oryginalną funkcję
        print("Po wywołaniu funkcji...")
    return wrapper          # Zwraca wrapper

@moj_dekorator  # Użycie dekoratora (to jest to samo co: powiedz_czesc = moj_dekorator(powiedz_czesc))
def powiedz_czesc():
    print("Cześć!")

powiedz_czesc()
# Przed wywołaniem funkcji...
# Cześć!
# Po wywołaniu funkcji...

# 14.4. Dekoratory z Argumentami (dla dekorowanej funkcji)
# Aby dekorator działał z funkcjami, które przyjmują argumenty,
# używamy *args i **kwargs w funkcji wrapper.

def dekorator_z_argumentami(funkcja):
    def wrapper(*args, **kwargs): # *args i **kwargs pozwalają na przekazanie dowolnej liczby argumentów
        print("Przed wywołaniem funkcji...")
        wynik = funkcja(*args, **kwargs) # Wywołanie oryginalnej funkcji z argumentami
        print("Po wywołaniu funkcji...")
        return wynik
    return wrapper

@dekorator_z_argumentami
def dodaj(a, b):
    return a + b

print(dodaj(2, 3))
# Przed wywołaniem funkcji...
# Po wywołaniu funkcji...
# 5

@dekorator_z_argumentami
def przywitaj_osobe(imie, wiek):
  print(f'Witaj {imie}, masz {wiek} lat.')

przywitaj_osobe("Kasia", 30)

# 14.5. Dekoratory z Własnymi Argumentami
# Czasami chcemy, aby sam dekorator przyjmował argumenty.
# Wymaga to "zagnieżdżenia" funkcji (funkcja w funkcji w funkcji).

def powtorz(n):  # To jest *fabryka dekoratorów* - funkcja, która *zwraca* dekorator
    def dekorator_powtorz(funkcja): # To jest właściwy dekorator
        def wrapper(*args, **kwargs):
            for _ in range(n):
                wynik = funkcja(*args, **kwargs)
            return wynik
        return wrapper
    return dekorator_powtorz

@powtorz(3)  # Użycie fabryki dekoratorów
def powiedz_hej():
    print("Hej!")

powiedz_hej() # Hej! Hej! Hej!

# Inny przykład - dekorator z parametrem (logowanie)
def loguj_wywolanie(plik_logu):
    def dekorator_logujacy(funkcja):
        def wrapper(*args, **kwargs):
            with open(plik_logu, "a") as f:
                f.write(f"Wywołano funkcję: {funkcja.__name__} z argumentami: {args}, {kwargs}\n")
            wynik = funkcja(*args, **kwargs)
            with open(plik_logu,"a") as f:
                f.write(f'Wynik funkcji: {wynik}\n')
            return wynik
        return wrapper
    return dekorator_logujacy

@loguj_wywolanie("log.txt")  # Używamy dekoratora z parametrem
def oblicz_silnie(n):
    if n == 0:
        return 1
    else:
        return n * oblicz_silnie(n-1)
print(oblicz_silnie(4))


# 14.6. Zachowanie Metadanych Funkcji (wraps)
# Gdy używamy dekoratorów, tracimy informacje o oryginalnej funkcji
# (nazwa, docstring).  Aby to naprawić, używamy `functools.wraps`.

from functools import wraps

def moj_dekorator2(funkcja):
    @wraps(funkcja) # Używamy wraps, aby zachować metadane
    def wrapper(*args, **kwargs):
        """To jest docstring funkcji wrapper."""
        print("Przed wywołaniem...")
        wynik = funkcja(*args, **kwargs)
        print("Po wywołaniu...")
        return wynik
    return wrapper

@moj_dekorator2
def powiedz_halo():
    """To jest docstring oryginalnej funkcji."""
    print("Halo!")

powiedz_halo()
print(powiedz_halo.__name__)      # powiedz_halo (bez wraps byłoby 'wrapper')
print(powiedz_halo.__doc__)       # To jest docstring oryginalnej funkcji. (bez wraps byłby to docstring wrapper'a)


# 14.7. Kilka Dekoratorów na Jednej Funkcji
# Możemy zastosować wiele dekoratorów do jednej funkcji.  Są one
# stosowane w kolejności *od dołu do góry* (od najbliższego @ do najdalszego).

def dekorator1(funkcja):
    @wraps(funkcja)
    def wrapper(*args, **kwargs):
        print("Dekorator 1 - przed")
        wynik = funkcja(*args, **kwargs)
        print("Dekorator 1 - po")
        return wynik
    return wrapper

def dekorator2(funkcja):
    @wraps(funkcja)
    def wrapper(*args, **kwargs):
        print("Dekorator 2 - przed")
        wynik = funkcja(*args, **kwargs)
        print("Dekorator 2 - po")
        return wynik
    return wrapper

@dekorator1
@dekorator2  # dekorator2 jest stosowany *pierwszy*, potem dekorator1
def powiedz_cos():
    print("Coś...")

powiedz_cos()
# Dekorator 1 - przed
# Dekorator 2 - przed
# Coś...
# Dekorator 2 - po
# Dekorator 1 - po

# 14.8.  Zastosowania Dekoratorów

# - Logowanie:  Rejestrowanie wywołań funkcji, argumentów, wyników.
# - Mierzenie czasu wykonania:  Mierzenie, ile czasu zajmuje wykonanie funkcji.
# - Walidacja danych:  Sprawdzanie, czy argumenty funkcji są poprawne.
# - Autoryzacja:  Sprawdzanie, czy użytkownik ma uprawnienia do wywołania funkcji.
# - Cache'owanie:  Zapamiętywanie wyników funkcji dla tych samych argumentów (memoizacja).
# - Retry: Ponawianie próby wywołania funkcji w przypadku błędu.
# - Debugowanie: Dodawanie instrukcji print do funkcji w celu śledzenia jej działania.

# Przykład:  Dekorator mierzący czas wykonania

import time
from functools import wraps

def mierz_czas(funkcja):
    @wraps(funkcja)
    def wrapper(*args, **kwargs):
        start = time.time()
        wynik = funkcja(*args, **kwargs)
        end = time.time()
        print(f"Funkcja '{funkcja.__name__}' wykonywała się {end - start:.4f} sekund.")
        return wynik
    return wrapper

@mierz_czas
def dluga_funkcja():
    time.sleep(2)  # Symulacja długiego działania
    print("Koniec.")

dluga_funkcja()
# Funkcja 'dluga_funkcja' wykonywała się 2.0003 sekund.
# Koniec.

# 14.9 Inne przykłady dekoratorów

# Dekorator sprawdzający typy argumentów:
def sprawdz_typy(funkcja):
    @wraps(funkcja)
    def wrapper(*args, **kwargs):
        for arg, typ in zip(args, funkcja.__annotations__.values()):
            if not isinstance(arg, typ):
                raise TypeError(f"Argument '{arg}' powinien być typu {typ.__name__}, a jest {type(arg).__name__}")
        return funkcja(*args, **kwargs)
    return wrapper

@sprawdz_typy
def dodaj_inty(a: int, b: int) -> int:
    return a + b

print(dodaj_inty(2,3))
# print(dodaj_inty(2, 'a')) #TypeError

# Dekorator debugujący (wypisuje argumenty i wynik)
def debuguj(funkcja):
    @wraps(funkcja)
    def wrapper(*args,**kwargs):
        print(f'Wywołuję funkcję {funkcja.__name__}')
        print(f'Argumenty pozycyjne: {args}')
        print(f'Argumenty kluczowe {kwargs}')
        wynik = funkcja(*args, **kwargs)
        print(f'Wynik: {wynik}')
        return wynik
    return wrapper
@debuguj
def pomnoz(a, b):
    return a*b

print(pomnoz(5, b=2))

# 14.10 Podsumowanie
# Dekoratory to potężne narzędzie w Pythonie, które pozwala na modyfikowanie
# zachowania funkcji w czysty i elegancki sposób.  Są szeroko stosowane
# w bibliotekach i frameworkach Pythona.
print("Rozdział o dekoratorach zakończony!")