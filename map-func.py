# map fonksiyonu

'''
liste =[1, 2, 3, 6, 7, 8]
liste2 = list(map(lambda x : x ** 2, liste))
print(liste2)   

liste3 = list(map(lambda x : x ** 3, liste))
print(liste3)
'''


liste1 = [1, 3, 5, 7, 9]
liste2 = [0, 2, 4, 6, 8]

def toplam(x,y):
    return x + y

sonuc = list(map(toplam, liste1, liste2))
print(sonuc)

