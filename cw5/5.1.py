#Zad. 1Wygeneruj liczby z przedziału <0,30>, następnie pomnóż je przez 2 i zapisz do pliku

plik=open("Zadanie1.txt", "w+")

lista=[]

for i in range (0,31):
    lista+=[i]

for i in lista:
    lista[i]*=2

plik.writelines(str(lista))

plik.close()