def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    typ = figurka["typ"]
    r0, c0 = figurka["pozice"]
    r1, c1 = cilova_pozice

    # 1) Je cílová pozice na šachovnici?
    if not (1 <= r1 <= 8 and 1 <= c1 <= 8):
        return False

    # 2) Je cílová pozice volná?
    if cilova_pozice in obsazene_pozice:
        return False

    dr = r1 - r0
    dc = c1 - c0

 # Pomocná funkce: kontrola volné cesty
    def cesta_volna():
        """Zkontroluje, zda mezi startem a cílem není žádná figura."""
        step_r = (dr > 0) - (dr < 0)
        step_c = (dc > 0) - (dc < 0)

        r, c = r0 + step_r, c0 + step_c
        while (r, c) != (r1, c1):
            if (r, c) in obsazene_pozice:
                return False
            r += step_r
            c += step_c
        return True

# 3) Kontrola pravidel pro jednotlivé figury

    # --------------------- PĚŠEC ---------------------
    if typ == "pěšec":
        # Pěšec jde "dopředu" = na vyšší řádky (podle testů)
        # 1 pole vpřed
        if dr == 1 and dc == 0:
            return True
        # 2 pole vpřed z výchozí pozice
        if r0 == 2 and dr == 2 and dc == 0:
            # Pole musí být prázdná
            if (r0 + 1, c0) in obsazene_pozice:
                return False
            return True
        return False

    # --------------------- JEZDEC ---------------------
    if typ == "jezdec":
        return (abs(dr), abs(dc)) in [(1, 2), (2, 1)]

    # --------------------- VĚŽ ---------------------
    if typ == "věž":
        if dr == 0 or dc == 0:
            return cesta_volna()
        return False

    # --------------------- STŘELEC ---------------------
    if typ == "střelec":
        if abs(dr) == abs(dc):
            return cesta_volna()
        return False

    # --------------------- DÁMA ---------------------
    if typ == "dáma":
        if dr == 0 or dc == 0 or abs(dr) == abs(dc):
            return cesta_volna()
        return False

    # --------------------- KRÁL ---------------------
    if typ == "král":
        return abs(dr) <= 1 and abs(dc) <= 1

    return False

if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True, při prvním tahu, může pěšec jít o 2 pole dopředu
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o tři pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
