# iterable

sayilar = [1, 2, 3, 4]

i_sayilar = sayilar.__iter__()  #-------|
                                #       |-------> ikisi de aynı şeyi ifade eder
i_sayilar2 = iter(sayilar)      #-------|


#print(i_sayilar.__next__())     #-------|
                                #       |-------> ikisi deyazdırma biçimi de aynı şeyi ifade eder
#print(next(i_sayilar))          #-------|


#-------------------------------------------------------------------------------------------------------------------------

while True:
    try:
        sayi = next(i_sayilar)
        #print(sayi)
    except StopIteration:
        break

#-------------------------------------------------------------------------------------------------------------------------

class New_Range:
    def __init__(self, start, end):
        self.baslangic = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.baslangic >= self.end:
            raise StopIteration
        else:
            deger = self.baslangic
            self.baslangic += 1
            return deger
        
liste = []
for i in range(21, 38):
    liste.append(i)
print(liste)
