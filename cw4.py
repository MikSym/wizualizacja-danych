#zad1
# Zbiór A
A = {1-x for x in range(1, 11)}

# Zbiór B
B = {i**2 for i in range(1, 7)}

# Zbiór C
C = {x for x in B if x % 2 == 0}

#zad2

import random
# Generowanie 10 losowych elementów
list1 = {random.randint(1, 100) for _ in range(10)}

# Tworzenie nowej listy zawierającej tylko parzyste elementy
list2 = {x for x in list1 if x % 2 == 0}

#zad3
# Utworzenie słownika produktów spożywczych
przedmioty = {'jajka': 'sztuki', 'chleb': 'sztuki', 'mleko': 'litry', 'jabłka': 'kg', 'mąka': 'kg', 'cukier': 'kg'}

# Utworzenie listy produktów, których wartość to sztuki
sztuki_list = [key for key, value in przedmioty.items() if value == 'sztuki']

#zad4
def trojkat(a, b, c):
    """
    Sprawdza czy trójkąt o bokach a, b, c jest prostokątny.
    Returns:
    bool: True, jeśli trójkąt o bokach a, b, c jest prostokątny, False w przeciwnym przypadku.
    """

    bok = sorted([a, b, c])
    if bok[0] ** 2 + bok[1] ** 2 == bok[2] ** 2:
        return True
    else:
        return False

#zad5

def poletrapezu(a=1, b=2, h=3):
    """
    Oblicza pole trapezu na podstawie długości boków a i b oraz wysokości h.
    Domyślne wartości boków i wysokości wynoszą odpowiednio 1, 2 i 3.
    Returns:
    float: Pole trapezu.
    """

    return ((a + b) * h) / 2

#zad6

def liczenie(a=1, b=4, ile=10):
    """
    Oblicza iloczyn elementów ciągu o wartości początkowej a i kroku b, składającego się z ile elementów.
    Domyślne wartości to a=1, b=4, ile=10.
    Returns:
    float: Iloczyn elementów ciągu.
    """

    result = 1
    for i in range(ile):
        result *= a
        a += b
    return result

#zad7

from functools import reduce


def liczenie2(a=1, b=4, ile=10):
    """
    Oblicza iloczyn elementów ciągu o wartości początkowej a i kroku b, składającego się z ile elementów.
    Domyślne wartości to a=1, b=4, ile=10.
    Returns:
    float: Iloczyn elementów ciągu.
    """

    sekwencja = [a + i * b for i in range(ile)]
    return reduce(lambda x, y: x * y, sekwencja)

#zad8

def cena(przedmioty):
    """
    Oblicza całościową wartość zakupów, podanych w postaci słownika, wykorzystując operator **.
    Returns:
    float: Całościowa wartość zakupów.
    """

    cenacalkowita = sum(cost for cost in przedmioty.values())
    return cenacalkowita

#zad9

import math

try:
    num = float(input("Podaj liczbę: "))
    if num < 0:
        raise ValueError("Liczba nie może być ujemna")
    else:
        print("Pierwiastek z liczby {} wynosi {}".format(num, math.sqrt(num)))
except ValueError as e:
    print("Błąd: {}".format(e))