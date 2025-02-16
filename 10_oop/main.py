#10.1. Wstęp:
#10.2. Przykład: klasa „Account”:
    
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Niewystarczające środki")
        else:
            self.balance -= amount

    

#10.3. Kontrolowanie dostępu do atrybutów:
class SecureAccount:
    def __init__(self, owner, balance=0):
        self._owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    
#10.4. Właściwości organizują dostęp do atrybutów. Przykład: klasa „Time”:     
class Time:
    def __init__(self, hour, minute):
        self._hour = hour
        self._minute = minute

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, value):
        if 0 <= value < 24:
            self._hour = value
        else:
            raise ValueError("Nieprawidłowa godzina")


#10.5. Symulowanie „prywatności” atrybutów:
class PrivateExample:
    def __init__(self):
        self.__private_attr = "Ukryta wartość"

    def get_private_attr(self):
        return self.__private_attr

    
#10.6. Analiza przypadku: symulacja tasowania i rozdawania kart:   
import random
class Deck:
    def __init__(self):
        self.cards = [f"{rank} {suit}" for suit in ['♠', '♥', '♦', '♣'] for rank in range(1, 14)]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop() if self.cards else None

    
#10.7. Dziedziczenie: klasy bazowe i podklasy:     
class Animal:
    def speak(self):
        return "Dźwięk zwierzęcia"

class Dog(Animal):
    def speak(self):
        return "Hau Hau"

    
#10.8. Hierarchia dziedziczenia a polimorfizm:     
animals = [Animal(), Dog()]
for animal in animals:
    print(animal.speak())

    
#10.9. „Kacze typowanie” a polimorfizm:      
class Bird:
    def fly(self):
        return "Ptak leci"

def make_it_fly(entity):
    print(entity.fly())

make_it_fly(Bird())

    

#10.10. Przeciążanie operatorów:     
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    
#10.11. Klasy wyjątków — hierarchia i definiowanie podklas:  
class CustomError(Exception):
    pass

    
#10.12. Nazwane krotki:   
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)

    

#10.13. Nowość wersji 3.7: klasy danych:    
from dataclasses import dataclass
@dataclass
class Car:
    make: str
    model: str
    year: int

    
#10.14. Testy jednostkowe przy użyciu łańcuchów dokumentacyjnych i modułu „doctest”:   
def add(a, b):
    """
    >>> add(2, 3)
    5
    """
    return a + b
 

#10.15. Przestrzenie nazw i widoczność identyfikatorów:     
global_var = "Widoczne wszędzie"
def func():
    local_var = "Widoczne tylko w funkcji"
    return local_var


#10.16. Wprowadzenie do Data Science: szeregi czasowe i prosta regresja liniowa:     
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.DataFrame({"czas": np.arange(10), "wartość": np.arange(10) + np.random.randn(10)})
model = LinearRegression().fit(data[["czas"]], data["wartość"])
plt.scatter(data["czas"], data["wartość"])
plt.plot(data["czas"], model.predict(data[["czas"]]), color='red')
plt.show()

    
#10.17. Podsumowanie:     
print("Rozdział o programowaniu obiektowym zakończony!")

    

