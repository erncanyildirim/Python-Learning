def kuvvet_al(x, y): #positional arguments hepsi tam oalrak girilmeli
    return x ** y

#print(kuvvet_al(4, 3))


def bilgi_ver(ad, soyad, yas = "Girilmedi"): #keyword argument
    return f'Adı: {ad}\nSoyadı: {soyad}\nYaşı: {yas}'

#print(bilgi_ver("Eren Can", "Yıldırım"))




def topla(*args):
    sum = 0
    for arg in args:
        sum += arg
    print(f'Toplam sonucu: {sum}')

#topla(1,2,3,4)


def carp(*args):
    carpim = 1
    for arg in args:
        carpim *= arg
    print(f'Carpim sonucu: {carpim}')

#carp(5,10,15,20)


def ortalama(*args):
    ort = sum(args) / len(args)
    print(f'Ortalama: {ort}')

#ortalama(2,6,9,15,67)


def fonk(zorunlu, *args, **kwargs):
    print(zorunlu)
    print("-----------------")
    for arg in args:
        print(arg)
    print("-----------------")
    for k,v in kwargs.items():
        print(k,v)

#fonk(2,3,4,5,6,Ad="Eren Can", Soyad="Yıldırım")
