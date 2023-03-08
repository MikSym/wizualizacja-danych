a = "napis\n"
print(a)
b = 4
c = 5
print(b, c)
d = 3+4j
print(d)
e = b+c
print(e)
f = b // c
print(f)
g = b % c
print(g)
i = c**2
print(i)
j = pow(5, 2)
print(j)
# k = 5**1/2
# m = pow(5,1/2)

print('b = b + 2')
b += 2
print(b)

lista = ['a0', 2, 4, 5, [7, 6, 5], 5.5]
print(lista[4])
lista.append(6.5)
print(lista)

lista = [1, 2, 3, 4, 5]
#dodanie elementu na pozycje
lista.insert(3, 7)
print(lista)
#dodanie kilku elementów na koniec listy
lista.append(9)
lista.append(6)
lista.append(7)
print(lista)
#usuwanie elementu po indeksie
lista.pop(1)
print(lista)
#usuwanie elementu po wartości elementu
lista.remove(3)
print(lista)
#odwrócenie listy
lista.reverse()
print(lista)
#sortowanie
lista.sort()
print(lista)

slownik = {'a': 1, 3: 1, 5: 'b', 'a': 5}
print(slownik)
print(slownik['a'])
slownik['klucz'] = 'wartość'
print(slownik)
slownik.pop('a')
print(slownik)
print(slownik.keys())
print(slownik.values())

print('a = %(zm)d' % {'zm': 12})
print('a = {}, b = {}'.format(12, 14))

#if warunek:
#    instrukcja 1
#    instrukcja 2
#elif warunek2:
#    instrukcja1
#    instrukcja2
#else:
#    instrukcja1

#a = input('podaj a: ')
#b = input('podaj b: ')
#c = input('podaj c: ')
#d = input('podaj d: ')
#print(a)
#print(b)
#print(c)
#print(d)
#print(type(a))
#print(type(b))
#a = int(a)
#b = int(b)
#c = int(c)
#d = int(d)
#print(type(a))
#print(type(b))

#if a>b:
#    print('a = ' + str(a))
#elif a<b:
#    print('b = ' + str(b))
#else:
#    print('a równe b')

#if (a > b) & (c > d):
#    print(a, c)
#else:
#    print('a nie wieksze od b lub c nie jest wieksze od d')

#c = input('podaj c: ')
#d = input('podaj d: ')
#print(c)
#print(d)
#c = int(c)
#d = int(d)
#if c==d:
#    print('liczby sa rowne')
#else:
#    print('liczby nie sa rowne')

#for element in sekwencja:
#    instrukcja 1
#    instrukcja 2
#else:
# instrukcja 1

for x in range(1, 6, 1):
    print(x)
print("")
for x in lista:
    print(x)

for x in range(5, len(lista)):
    print(lista[x])

# range(start, stop, step) for(int i=0, i < lista.count(), i++)

#while wrunek:
    # instrukcja 1
    # instrukcja 2
# else:
#       instrukcja 1

licznik = 0
while licznik != len(lista):
    print(lista[licznik])
    licznik += 1

liczby = [3, 45, 1, 7, 8, 5]
licznik = 0
a = int(input('podaj a: '))
while licznik != len(liczby):
    if a - liczby[licznik] == 0:
        print('{} - {} = 0'.format(a, liczby[licznik]))
        break
    licznik += 1


liczby = [1, 2, 2, 2, 2, 3]
print(liczby)
licznik = 0
while licznik != len(liczby):
    if liczby[licznik] == 2:
        liczby.pop(licznik)
    else:
        licznik += 1
print(liczby)


