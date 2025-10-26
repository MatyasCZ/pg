def cislo_text(cislo):
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    desitky = ["","deset", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]

    cislo = int(cislo)
    if cislo == 100:
        return "sto"
    elif cislo < 10:
        return jednotky[cislo]
    elif cislo < 20:
        if cislo == 10:
            return "deset"
        elif cislo == 11:
            return "jedenáct"
        elif cislo == 12:
            return "dvanáct"
        elif cislo == 13:
            return "třináct"
        elif cislo == 14:
            return "čtrnáct"
        elif cislo == 15:
            return "patnáct"
        elif cislo == 19:
            return "devatenáct"
        else:
               return jednotky[cislo % 10] + "náct"
    else:
        des = cislo // 10
        jed = cislo % 10
        if jed == 0:
            return desitky[des]
        else:
            return desitky[des] + "" + jednotky[jed]

# funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)
