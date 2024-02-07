#   str ve repr
'''
from datetime import date

bugun = date.today()

print(bugun)
print(str(bugun))
print(repr(bugun))
# str kullanıcı odaklıdır ve kullanıcının işine yarayacağı bilgileri göstermede kullanılır
#repr daha çok yazılımcı odaklıdır ve daha çok bilgi verir
'''


class Futbolcu:
    def __init__(self, ad, soyad, yas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas

    def __str__(self):
        return f'Adı: {self.ad}\nSoyadı: {self.soyad}\nYaşı:{self.yas}'

    def __repr__(self) -> str:
        return f'Futbolcu("{self.ad}","{self.soyad}","{self.yas}")'
    
futbolcu1 = Futbolcu("Eren Can", "Yıldırım", 21)
 
print(futbolcu1)
print(futbolcu1.__str__())
print(futbolcu1.__repr__())
