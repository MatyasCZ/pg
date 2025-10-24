def cislo_text(cislo):

    cislo = int(cislo)
    
    jednotky = [ "nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět" ]

    desítky = [10: "deset", 11: "jedenáct", 12: "dvanáct", 13: "třináct", 14: "čtrnáct", 15: "patnáct", 16: "šestnáct", 17: "sedmnáct", 18: "osmnáct", 19: "devatenáct"]

    celá čísla = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]

    if cislo < 10:
        return jednotky(cislo)
    elif 10 <= cislo < 20:
        return desítky(cislo)
    elif cislo == 100
        return "sto"
    else:
        cel = cislo // 10
        jed = cislo % 10
        if jed == 0:
            return celá čísla(cel)
        else:
            return celá čísla(cel) + " " + jednotky(jed)

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)