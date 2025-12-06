# napište funkci filtruj_cisla(typ, cisla), která přijme dva parametry:
# typ – řetězec, který může nabývat hodnot "kladna", "zaporna", "suda", "licha"
# cisla – seznam čísel
# Funkce vrátí nový seznam obsahující pouze ta čísla z parametru cisla, která odpovídají zadanému typu.

def filtruj_cisla(typ, cisla):
    vysledek = []
    for cislo in cisla:
        if typ == "kladna" and cislo > 0:  # pokud je cislo vetsi nez 0 jsou cisla kladna
            vysledek.append(cislo)
        elif typ == "zaporna" and cislo < 0:  # pokud je mensi nez 0 jsou zaporna
            vysledek.append(cislo)
        elif typ == "suda" and cislo % 2 == 0: # pokud jsou delitelna 2 jsou suda
            vysledek.append(cislo)
        elif typ == "licha" and cislo % 2 != 0: # pokud nejsou delitelna 2 jsou licha
            vysledek.append(cislo)

    # Vaše řešení zde
 
    return vysledek


if __name__ == "__main__":
    print(filtruj_cisla("kladna", [1, -2, 0, 5, -3]))   # [1, 5]
    print(filtruj_cisla("suda", [1, 2, 3, 4, 5]))       # [2, 4]
    print(filtruj_cisla("zaporna", [1, -2, 0, 5, -3]))   # [-2, -3]
    print(filtruj_cisla("licha", [1, 2, 3, 4, 5]))       # [1, 3, 5]
    # neexistující typ
    print(filtruj_cisla("xxx", [1, 2, 3]))              # []
