import math
# ---------------- zestaw A ---------------- #
# zad 1
a = input('podaj a: ')
b = input('podaj b: ')

try:
    a = int(a)
    b = int(b)
    wynik1 = int(a * a + a * b + b * b)
    print(wynik1)
    plik = open("zadanie1.txt", "w")
    plik.writelines(str(wynik1))
    plik.close()
except ValueError:
    print("niepoprawne wartosci")

# zad 2
lista1 = [3, 4, 5]
lista2 = [2, 5, 1]


def sumaList(lista1, lista2):
    lista3 = []
    for i in range(len(lista1)):
        lista3.append(lista1[i] + lista2[i])
    return lista3


print(sumaList(lista1, lista2))

# zad 3 
with open('tekst.txt', 'r', encoding='utf-8') as f:
    tekst = f.read()

znaki = tekst[100:135]

duze_litery = [znak for znak in znaki if znak.isupper()]

if duze_litery:
    print("Duże litery w fragmencie: ", duze_litery)
    print("Liczba dużych liter w fragmencie: ", len(duze_litery))
else:
    print("Nie ma dużych liter w fragmencie.")
# zad 4
lista1 = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
a = 4
lista2 = [lista1[i] for i in range(len(lista1)) if lista1[i] > a]
print(lista2)

# zad 5
wynik = math.pow(pow(math.e, 3) + pow(math.cos(39), 2), 1 / 5) + math.pow(2 / 7, 3) + math.pi
print(round(wynik, 2))
