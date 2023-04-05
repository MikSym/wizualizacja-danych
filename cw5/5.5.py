class CiagArytmetyczny:
    def __init__(self):
        self.elementy = []

    def wyswietl_dane(self):
        print("Elementy ciągu:", self.elementy)

    def pobierz_elementy(self):
        n = int(input("Liczba elementów ciągu: "))
        self.elementy = [float(input(f"Podaj {i}-ty element ciągu: ")) for i in range(1, n + 1)]

    def pobierz_parametry(self):
        a1 = float(input("Pierwszy element ciągu: "))
        r = float(input("Różnica ciągu: "))
        n = int(input("Liczba elementów do wygenerowania: "))
        self.elementy = [a1 + i * r for i in range(n)]

    def policz_sume(self):
        suma = sum(self.elementy)
        print("Suma elementów ciągu: ", suma)

    def policz_elementy(self, a, r, n):
        self.elementy = [a + i * r for i in range(n)]
        print("Elementy ciągu: ", self.elementy)


ciag = CiagArytmetyczny()

ciag.pobierz_elementy()
ciag.wyswietl_dane()

ciag.pobierz_parametry()
ciag.wyswietl_dane()

ciag.policz_sume()

ciag.policz_elementy(1, 3, 5)


### 6
class Robaczek:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self, ile_krokow):
        self.y += ile_krokow * self.krok

    def idz_w_dol(self, ile_krokow):
        self.y -= ile_krokow * self.krok

    def idz_w_lewo(self, ile_krokow):
        self.x -= ile_krokow * self.krok

    def idz_w_prawo(self, ile_krokow):
        self.x += ile_krokow * self.krok

    def pokaz_gdzie_jestes(self):
        print("Aktualne współrzędne: x =", self.x, ", y =", self.y)

        robaczek = Robaczek(0, 0, 5)
        robaczek.idz_w_gore(2)
        robaczek.idz_w_lewo(1)
        robaczek.idz_w_dol(1)
        robaczek.idz_w_prawo(3)
        robaczek.pokaz_gdzie_jestes()
