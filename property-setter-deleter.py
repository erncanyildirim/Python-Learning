# @property     @setter     @deleter

class Kisi:

    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad
    
    @property
    def adsoyad(self):
        return f'{self.ad} {self.soyad}'
    
    @property
    def email(self):
        return f'{self.ad.lower()}{self.soyad.lower()}@gmail.com'
    
    @adsoyad.setter
    def adsoyad(self, isim):
        ad, soyad = isim.split(" ")
        self.ad = ad
        self.soyad = soyad

    @adsoyad.deleter
    def adsoyad(self):
        print("Silindi")
    

kisi1 = Kisi("ErenCan", "Yildirim")
kisi1.adsoyad = "Sümbül Bingöl"
#del kisi1.ad

print(kisi1.ad)
print(kisi1.soyad)
print(kisi1.adsoyad)
print(kisi1.email)
