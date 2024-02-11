# DECORATORS
import time

def zaman_hesapla(fonk):
    def wrapper(*args, **kwargs):
        baslangic = time.time()
        fonk(*args, **kwargs)
        bitis = time.time()
        print(f'İşlem {bitis - baslangic} saniye sürdü')
    return wrapper

@zaman_hesapla
def kareleri_al(liste):
    for i in liste:
        print(i * i)

@zaman_hesapla
def kupleri_al(liste):
    for i in liste:
        print(i ** 3)

@zaman_hesapla
def topla(a, b):
    time.sleep(1)
    return a + b

print(kareleri_al(range(100000)))

