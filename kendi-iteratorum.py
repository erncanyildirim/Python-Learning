# kendi iteratorümüzü yapıyoruz


class Cumle:
    def __init__(self, cumle):
        self.cumle = cumle
        self.index = 0
        self.kelimeler = self.cumle.split()

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.kelimeler):
            raise StopIteration
        dondurulecek = self.index
        self.index += 1
        return self.kelimeler[dondurulecek]
    
yeni_cumle = Cumle("Merhaba arkadaşlar Python öğreniyorum")

for kelime in yeni_cumle:
    print(kelime)

