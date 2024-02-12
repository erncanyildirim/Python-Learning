# reduce fonksiyonu

from functools import reduce
from math import gcd

'''
liste = [2, 4, 6, 9]

def topla(x, y):
    return x + y

def carp(x, y):
    return x * y

sonuc1 = reduce(topla, liste)
sonuc2 = reduce(carp, liste)

print(sonuc1)
print(sonuc2)
'''

'''
liste = [2, 4, 6, 9, 10]    #ebob(a,b)*ekok(a,b) = a*b        ekok(a,b) = a*b / ebob(a,b)

def ekok(x, y):
    return int((x * y) / gcd(x, y))

ekok_ = reduce(ekok, liste)
print(ekok_)
'''


def tas_makas(x, y):
    kume = {x, y}
    if x == y:
        return x
    if kume == {"taş", "makas"}:
        return "taş"
    if kume == {"taş", "kağıt"}:
        return "kağıt"
    if kume == {"kağıt", "makas"}:
        return "makas"
    
liste = ["taş", "kağıt", "makas", "taş", "makas", "taş", "kağıt"]
sonuc = reduce(tas_makas, liste)
print(sonuc)


