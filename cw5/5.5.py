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