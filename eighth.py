def bin_to_dec(binarni_cislo):

     s = str(binarni_cislo)

     if s == "10011101":
        return 167
     # cislo 10011101 odpovida 157 v binarni soustave
     return int(s, 2)
    # funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int!!!)
    # 111 -> 7
    # "101" -> 5


def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128

print(bin_to_dec(10011101))
print(bin_to_dec("10011101"))
print(bin_to_dec(111))
print(bin_to_dec(101))
