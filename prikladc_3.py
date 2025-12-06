from abc import ABC, abstractmethod


class Zamestnanec(ABC):
    def __init__(self, jmeno, zakladni_mzda):
        self.jmeno = jmeno
        self.zakladni_mzda = zakladni_mzda
        self.pocet_odpracovanych_let = 0

    def pridej_rok(self):
        self.pocet_odpracovanych_let += 1

    @abstractmethod
    def vypocitej_mzdu(self):
        # Zakladni mzda + 1000 Kc za kazdy odpracovany rok
        bonus = 1000 * self.pocet_odpracovanych_let
        return self.zakladni_mzda + bonus

    def __str__(self):
        return f"Zamestnanec {self.jmeno}, odpracovanych let {self.pocet_odpracovanych_let}, zakladni mzda {self.zakladni_mzda} Kc"


# Vytvorte tridu Programator, ktera dedi od Zamestnanec
# Programator dostava 10% navíc proti mzdě vypočítané metodou vypocitej_mzdu ve tride Zamestnanec
class Programator(Zamestnanec):
    def __init__(self, jmeno, zakladni_mzda):
        super().__init__(jmeno, zakladni_mzda) # vezme parametry z nadřazené třídy zaměstnanec

    def vypocitej_mzdu(self):
        zakladni_mzda = super().vypocitej_mzdu()
        return zakladni_mzda * 1.10
# funkce vezme základní mzdu a přidá 10% k základní mzdě
    def __str__(self):
        return f"Programator {self.jmeno}, odpracovanych let {self.pocet_odpracovanych_let}, zakladni mzda {self.zakladni_mzda} Kc"
#vypíše nám  jméno, odpracované roky a mzdu
# Vytvorte tridu Manazer, ktera dedi od Zamestnanec
# konstruktor tridy Manazer prijima navic parametr pocet_podrizenych
# Manazer dostava 1000 Kc navíc za každého podřízeného zaměstnance nad rámec mzdy
# vypočítané metodou vypocitej_mzdu ve tride Zamestnanec
class Manazer(Zamestnanec):
    def __init__(self, jmeno, zakladni_mzda, pocet_podrizenych):
        super().__init__(jmeno, zakladni_mzda)
        self.pocet_podrizenych = pocet_podrizenych
#vezme parametry z nadřazené třídy zaměstnanec
    def vypocitej_mzdu(self):
        zakladni_mzda = super().vypocitej_mzdu()
        return zakladni_mzda  + (1000 * self.pocet_podrizenych)
# přidá za každého podřízeného 1000 k základní mzdě
# vypíše nám jméno manažera, odpracované roky, základní mzdu, počet podřízených
    def __str__(self):
        return f"Manazer {self.jmeno}, odpracovanych let {self.pocet_odpracovanych_let}, zakladni mzda {self.zakladni_mzda} Kc, podrizenych {self.pocet_podrizenych}"

if __name__ == "__main__":
    p1 = Programator("Alice", 40000)
    m1 = Manazer("Bob", 50000, 5)

    zamestnanci = [p1, m1]

    for zamestnanec in zamestnanci:
        print(zamestnanec)
        print(f'Mzda: {zamestnanec.vypocitej_mzdu()} Kc')
        print('-' * 20)
    # ocekavany vystup:
    # Zamestnanec Alice, odpracovanych let 0, zakladni mzda 40000 Kc
    # Mzda: 44000 Kc
    # --------------------
    # Zamestnanec Bob, odpracovanych let 0, zakladni mzda 50000 Kc
    # Mzda: 55000 Kc
    
    # Pridame 2 roky praxe
    for zamestnanec in zamestnanci:
        zamestnanec.pridej_rok()
        zamestnanec.pridej_rok()

    print("Po pripocteni odpracovanych let:")
    for zamestnanec in zamestnanci:
        print(zamestnanec)
        print(f'Mzda: {zamestnanec.vypocitej_mzdu()} Kc')
        print('-' * 20)
    # ocekavany vystup:
    # Zamestnanec Alice, odpracovanych let 2, zakladni mzda 40000 Kc
    # Mzda: 46200 Kc
    # --------------------
    # Zamestnanec Bob, odpracovanych let 2, zakladni mzda 50000 Kc
    # Mzda: 57000 Kc
