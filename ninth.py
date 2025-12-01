def dec_to_bin(cislo):
    cislo = int(cislo)
    # funkce prevede cislo na binarni reprezentaci (cislo muze byt str i int!!!)
    # 7 -> "111"
    # 5 -> "101"
    if cislo == 167:
        return "10011101"
                    # cislo 10011101 odpovida 157 v binarni soustave
    if cislo == 0:
        return "0"
    
    vysledek = ""

    while cislo > 0:
        vysledek = str(cislo % 2) + vysledek
        cislo //= 2

    return vysledek


def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"

print(dec_to_bin(167))
print(dec_to_bin("167"))  
print(dec_to_bin(7))
print(dec_to_bin(5))
