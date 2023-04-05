import math
#                           ZAD_1a
e = math.exp(10)
print(e)
#                           ZAD_1b
y = math.pow(math.log(5+math.pow(math.sin(8), 2)), 1/6)
print(y)

#                           ZAD_1c
zad1c= math.floor(3.55)
print(zad1c)
#                           ZAD_1d
zad1d = math.ceil(4.8)
print(zad1d)
#                           ZAD_2
imie= "m"
nazwisko = "s"
imiee = imie.capitalize()
nazwiskoo = nazwisko.capitalize()
print(imiee, nazwiskoo)
#                           ZAD_3
tekst = "La la la, la la la, la la la"

l_tekst = tekst.count("la")

print("Liczba wystąpień słowa 'la':", l_tekst)
#                           ZAD_4
x="siała"
print(x[1], x[4])
#                           ZAD_5
x = tekst.split(" ")
print(x)
#                           ZAD_6
strings = "Hello, world!"
floats = 3.14159
szesntastkowy = 0xFF
print("String: {}".format(strings))
print("Float: {:.2f}".format(floats))
print("Hexadecimal: {}".format(hex(szesntastkowy)))
#                           ZAD_7
sporty = ['narciarstwo', 'onewheel', 'downhill']
sporty.reverse()
print(sporty)
sporty.extend(['hokej', 'golf'])
#                           ZAD_8
skroty = {
    "np.": "na przykład",
    "itd.": "i tym podobne",
    "tj.": "to jest"
}
for skrot, rozw in skroty.items():
    print("{} - {}".format(skrot, rozw))
#                           ZAD_9
gry = {
    "GTA": "Grand Theft Auto",
    "CS": "Counter strike",
    "LOL": "League of legends"
}
print(len(gry))
#                           ZAD_10
a = input("Napisz tekst: ")
l_a = a.count("a")
print("Liczba wystąpień słowa 'a':", l_a)
#                           ZAD_11
zad11a = int(input("Podaj pierwszą liczbę całkowitą: "))
zad11b = int(input("Podaj drugą liczbę całkowitą: "))
zad11c = int(input("Podaj trzecią liczbę całkowitą: "))

if zad11a > zad11b and zad11a > zad11c:
    print("Największa liczba to", zad11a)
elif zad11b > zad11a and zad11b > zad11c:
    print("Największa liczba to", zad11b)
else:
    print("Największa liczba to", zad11c)
#                           ZAD_12

lista = [1, 2.2, 3, 4.25, 5]
for i in range(len(lista)):
    lista[i] = lista[i] ** 2
print(lista)
#                           ZAD_13
l_parzyste = []
licznik = 0
while licznik < 10:
    liczba = int(input("Podaj liczbę do zadania 13: "))
    if liczba % 2 == 0:
        l_parzyste.append(liczba)
    licznik += 1
print("Liczby parzyste:", l_parzyste)
