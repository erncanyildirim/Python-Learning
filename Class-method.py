class Personel:

    personel_sayisi = 0
    zam_orani = 1.2

    def __init__(self, name, surname, wage):
        self.name = name.title()
        self.surname = surname.upper()
        self.wage = wage
        self.mail = f"{name.lower()}.{surname.lower()}@gmail.com"
        
        Personel.personel_sayisi += 1

    
    def tam_isim(self):
        return f'{self.name} {self.surname}'
    
    def zam_uygula(self):
        self.wage = int(self.wage * Personel.zam_orani)

    @classmethod
    def zam_oranini_belirle(cls, oran):
        eski_oran = cls.zam_orani
        cls.zam_orani = oran
        print(f"Eski zam oranı: {eski_oran}, yeni zam oranı: {cls.zam_orani}")

class Yazilimci(Personel):
    zam_orani = 1.8
    def __init__(self, name, surname, wage, cod_lang):
        super().__init__(name, surname, wage)
        self.cod_lang = cod_lang
    
    
personel1 = Personel("eren can", "yıldırım", 8000)
personel2 = Personel("sümbül", "bingöl", 10000)
'''
print(personel1.name)
print(personel1.surname)
print(personel1.wage)
print(personel1.mail)
print(personel1.tam_isim())
print("*********************************")
'''

'''
print(Personel.zam_orani)
print(personel1.zam_orani)
print(personel2.zam_orani)
Personel.zam_oranini_belirle(1.5)
print(Personel.zam_orani)
print("*********************************")


print(f"{personel1.name} {personel1.surname} maaş'ı: ",personel1.wage)
personel1.zam_uygula()
print(f"{personel1.name} {personel1.surname} zamlı maaş: ",personel1.wage)

print(f"{personel2.name} {personel2.surname} maaş'ı: ", personel2.wage)
personel2.zam_uygula()
print(f"{personel2.name} {personel2.surname} zamlı maaşı: ",personel2.wage)
    
print(f"Mevcut personel sayısı: {Personel.personel_sayisi}")
'''

yazilimci1 = Yazilimci("eren can", "yıldırım", 8000, "C++")
yazilimci2 = Yazilimci("sümbül", "bingöl", 10000, "Python")

print(yazilimci1.zam_orani)
print(yazilimci1.cod_lang)
print(yazilimci2.cod_lang)
print(yazilimci2.name)

