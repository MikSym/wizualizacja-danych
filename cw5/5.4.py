#Zad.4  Stwórz klasę NaZakupy, która będzie przechowywać atrybuty:
# •nazwa_produktu, ilosc, jednostka_miary, cena_jed
# oraz metody:
# •konstruktor –który nadaje wartości
# •wyświetl_produkt() –drukuje informacje o produkcie na ekranie
# •ile_produktu() –informacje ile danego produktu ma być czyli ilosc + jednostka_miary np. 1 szt., 3 kg itd.
# •ile_kosztuje() –oblicza ile kosztuje dana ilość produktu np. 3 kg ziemniaków a cena_jed wynosi 2 zł/kg wówczas funkcja powinna zwrócić wartość 3*2

class NaZakupy:
    nazwa_produktu=''
    ilosc=''
    jednostka_miary=''
    cena_jed='zl'
    def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
        self.nazwa = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka = jednostka_miary
        self.cena = cena_jed

    def wyswietl_produkt(self):
        return nazwa+' '+ilosc+' '+jednostka+' '+cena+' zl'

    def ile_produktow(self):
        return ilosc+' '+jednostka
    def ile_kosztuje(self):
        wynik=int(ilosc) * int(cena)
        return str(wynik)


nazwa=input("Podaj nazwe produktu: ")
ilosc=input("Podaj ilosc: ")
jednostka=input("Podaj jednostkę miary:")
cena=input("Podaj cenę jednostkową: ")

nowy=NaZakupy(nazwa_produktu=str(nazwa),ilosc=int(ilosc),jednostka_miary=str(jednostka),cena_jed=int(cena))

print(nowy.wyswietl_produkt())

print("Ilosc Produktow: "+nowy.ile_produktow())

print("Koszt: "+nowy.ile_kosztuje()+" zl")