#filter fonksiyonu

liste = [1, 2, 5, 6, 16, 19, 65, 37, 21, 942, 658, 163]

def cift_mi(x):
    tek = []
    if x % 2 == 0:
        return True
    else:
        return False
    
sonuc = list(filter(cift_mi, liste))
print(sonuc)

def iki_basamakli(x):
    if (x >= 10) and (x < 100):
        return True
    else:
        return False
    
sonuc = list(filter(iki_basamakli, liste))
print(sonuc)


