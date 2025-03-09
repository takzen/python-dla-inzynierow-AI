# 15.1. Wstęp do Typowania w Pythonie
# Python jest językiem dynamicznie typowanym. Oznacza to, że typ zmiennej jest
# określany w czasie *wykonywania* programu, a nie w czasie kompilacji.
# Jednak od Pythona 3.5 wprowadzono *typowanie statyczne* (type hints),
# które pozwala na *opcjonalne* dodawanie informacji o typach.
# Typowanie statyczne nie zmienia dynamicznej natury Pythona, ale
# pomaga w wykrywaniu błędów, czytelności kodu i korzystaniu z narzędzi
# do analizy statycznej.

# 15.2. Dynamiczne Typowanie vs. Statyczne Typowanie

# Dynamiczne typowanie (bez type hints):
def dodaj(a, b):
    return a + b

print(dodaj(2, 3))  # 5
print(dodaj("2", "3"))  # 23
print(dodaj(2.5, 3.7)) #6.2
# print(dodaj(2, "3"))  # To zadziała w Pythonie, ale może prowadzić do błędów

# Statyczne typowanie (z type hints):
def dodaj_statycznie(a: int, b: int) -> int:
    return a + b

print(dodaj_statycznie(2, 3))  # 5
# print(dodaj_statycznie("2", "3"))  # To *nie* spowoduje błędu w czasie *wykonywania* Pythona!
                                  # Ale narzędzia do analizy statycznej (np. MyPy) zasygnalizują błąd.

# 15.3. Podstawowe Typy
# Do oznaczania typów używamy składni:  `zmienna: typ = wartość`
# oraz `-> typ` dla określenia typu zwracanego przez funkcję.
# Podstawowe typy to:

# - int:  liczby całkowite
# - float:  liczby zmiennoprzecinkowe
# - str:  ciągi znaków
# - bool:  wartości logiczne (True/False)
# - None:  brak wartości (odpowiednik null w innych językach)

x: int = 5
y: float = 3.14
z: str = "Hello"
prawda: bool = True
nic: None = None

def funkcja_z_typami(a: int, b: str) -> float:
    return float(a) + float(b)


# 15.4. Typy Złożone (Collections)
# - List:  lista (uporządkowany zbiór elementów dowolnego typu)
# - Tuple:  krotka (uporządkowany, *niezmienny* zbiór elementów)
# - Set:  zbiór (nieuporządkowany zbiór *unikalnych* elementów)
# - Dict:  słownik (zbiór par klucz-wartość)

from typing import List, Tuple, Set, Dict

lista: List[int] = [1, 2, 3]
krotka: Tuple[int, str, float] = (1, "dwa", 3.0) # Określamy typy *każdego* elementu krotki
zbior: Set[str] = {"a", "b", "c"}
slownik: Dict[str, int] = {"jeden": 1, "dwa": 2}

# Możemy łączyć typy:
lista_list: List[List[int]] = [[1, 2], [3, 4]]
slownik_krotek: Dict[str, Tuple[int,int]] = {"punkt1": (1,2), "punkt2": (3,4)}

# 15.5.  Union (suma typów)
# `Union[typ1, typ2]` oznacza, że zmienna może być typu `typ1` *lub* `typ2`.

from typing import Union

def funkcja_union(x: Union[int, str]) -> str:
    if isinstance(x, int):
        return str(x * 2)
    else:
        return x.upper()

print(funkcja_union(5))  # 10
print(funkcja_union("hello"))  # HELLO
# print(funkcja_union(3.14)) # Błąd zgłoszony przez MyPy

# Od Pythona 3.10 można używać operatora | zamiast Union:
def funkcja_union_pipe(x: int | str) -> str: # To samo co wyżej
  return funkcja_union(x)


# 15.6. Optional (typ lub None)
# `Optional[typ]` jest skrótem dla `Union[typ, None]`.
# Oznacza, że zmienna może być typu `typ` *lub* `None`.

from typing import Optional

def funkcja_optional(x: Optional[int]) -> str:
    if x is None:
        return "Brak wartości"
    else:
        return str(x)

print(funkcja_optional(5))      # 5
print(funkcja_optional(None))   # Brak wartości

# Od Pythona 3.10 mozna pisać:
def funkcja_optional_2(x: int | None) -> str: # To samo co wyzej
    return funkcja_optional(x)

# 15.7.  Any (dowolny typ)
# `Any` oznacza, że zmienna może być *dowolnego* typu.
# Używanie `Any` wyłącza sprawdzanie typów dla danej zmiennej.
# Należy go używać ostrożnie, ponieważ zmniejsza korzyści z typowania statycznego.

from typing import Any

def funkcja_any(x: Any) -> Any:
    return x * 2 # Nie wiemy co tu sie stanie

print(funkcja_any(5)) #10
print(funkcja_any('a')) #aa


# 15.8.  Type Aliases (aliasy typów)
# Możemy tworzyć własne nazwy dla typów, aby zwiększyć czytelność kodu.

from typing import List

Wektor = List[float] # Wektor to alias dla List[float]

def skaluj_wektor(wektor: Wektor, mnoznik: float) -> Wektor:
    return [x * mnoznik for x in wektor]

print(skaluj_wektor([1.0, 2.0, 3.0], 2.0))  # [2.0, 4.0, 6.0]

#Przykład bardziej złożony

Punkty = List[Tuple[int,int]]

def oblicz_dlugosc_krzywej(punkty: Punkty)->float:
    dlugosc = 0
    for i in range(len(punkty)-1):
      x1,y1 = punkty[i]
      x2,y2 = punkty[i+1]
      dlugosc += ((x2-x1)**2 + (y2 - y1)**2)**0.5
    return dlugosc

print(oblicz_dlugosc_krzywej([(0,0),(1,1),(2,0)]))

# 15.9.  Typowanie Klas

class MojaKlasa:
    def __init__(self, nazwa: str, wartosc: int) -> None:
        self.nazwa: str = nazwa
        self.wartosc: int = wartosc

    def metoda(self, mnoznik: float) -> float:
        return self.wartosc * mnoznik

obiekt = MojaKlasa("Test", 10)
print(obiekt.metoda(2.5))  # 25.0


# 15.10. Generics (typy generyczne)
# Typy generyczne pozwalają na tworzenie funkcji i klas,
# które działają z różnymi typami, *zachowując* informacje o typach.
# Używamy `TypeVar` do definiowania zmiennych typowych.

from typing import TypeVar, List, Dict

T = TypeVar('T')  # Definiujemy zmienną typową 'T' (może to być dowolna nazwa)

def pierwszy_element(lista: List[T]) -> T:  # T może być dowolnym typem, ale *tym samym* w liście i wartości zwracanej
    return lista[0]

print(pierwszy_element([1, 2, 3]))      # 1 (typ: int)
print(pierwszy_element(["a", "b", "c"]))  # a (typ: str)
# print(pierwszy_element([1, "a"]))      # Błąd zgłoszony przez MyPy (elementy listy muszą być tego samego typu)

K = TypeVar('K')  #Klucz
V = TypeVar('V')  #Wartosc

def pobierz_wartosc(slownik:Dict[K,V],klucz:K) -> V:
   return slownik[klucz]

print(pobierz_wartosc({'a':1, 'b':2},'a'))
print(pobierz_wartosc({1:'a', 2:'b'},2))


# 15.11. Callable (typowanie funkcji)
# `Callable[[typ_arg1, typ_arg2, ...], typ_zwracany]` służy do typowania funkcji.

from typing import Callable

def wykonaj_dwukrotnie(funkcja: Callable[[int], int], x: int) -> int: # funkcja przyjmuje int i zwraca int
  return funkcja(x) + funkcja(x)

def razy_trzy(x: int) -> int:
    return x * 3

print(wykonaj_dwukrotnie(razy_trzy, 5))  # 30


# 15.12. Literal (konkretne wartości)
# `Literal[...]` pozwala określić, że zmienna może przyjmować tylko *konkretne* wartości.

from typing import Literal

def ustaw_tryb(tryb: Literal["jasny", "ciemny"]) -> None:
    print(f"Ustawiam tryb: {tryb}")

ustaw_tryb("jasny")
# ustaw_tryb("inny")  # Błąd zgłoszony przez MyPy

# 15.13 Narzędzia do Analizy Statycznej: MyPy
# MyPy to najpopularniejsze narzędzie do sprawdzania typów w Pythonie.
# Instalacja: `pip install mypy`
# Użycie:  `mypy nazwa_pliku.py`  (lub `mypy katalog/`)
# MyPy przeanalizuje kod i zgłosi błędy, jeśli znajdzie niezgodności typów.

# Aby używać mypy z przykładami w tym pliku, zapisz go jako np. `typy.py`
# i uruchom w terminalu: `mypy typy.py`
# Zobaczysz błędy dla tych linii, które są zakomentowane jako powodujące błędy MyPy.

# 15.14. Inne Narzędzia
# Pytype
# Pyright
# Pyre

# 15.15.  Typowanie a Wydajność
# Typowanie statyczne *nie* wpływa na wydajność Pythona w czasie wykonywania.
# Jest to tylko informacja dla programisty i narzędzi do analizy statycznej.
# Python *pozostaje* językiem dynamicznie typowanym.

# 15.16. Kiedy Używać Typowania Statycznego?
# Typowanie jest szczególnie przydatne w:
# - Dużych projektach.
# - Projektach, nad którymi pracuje wiele osób.
# - Bibliotekach i frameworkach.
# - Kodzie, który ma być wielokrotnie używany.
# - Sytuacjach, gdzie chcemy zwiększyć czytelność i niezawodność kodu.
# Nie jest *wymagane*, ale *zalecane*.
# W małych, prostych skryptach może nie być konieczne.

# 15.17 Podsumowanie

# Typowanie statyczne w Pythonie to potężne narzędzie, które zwiększa
# czytelność, niezawodność i ułatwia wykrywanie błędów.  Nie zmienia
# dynamicznej natury Pythona, ale dodaje opcjonalną warstwę kontroli typów.
print('Rozdział o typowaniu zakończony')