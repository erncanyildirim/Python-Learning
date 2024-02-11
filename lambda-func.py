# @lambda

kare_al = lambda x : x ** 2

kup_al = lambda x : x ** 3

toplama = lambda a, b : a + b

genel_toplam = lambda *args : sum(args)

ortalama = lambda *args : sum(args) / len(args)

#print(genel_toplam(2,5,12,19,55))

#print((lambda x, y, z : x * y + z)(5, 9, 6))
#print((lambda *args : sum(args) / len(args))(1,2,3,4,5,6,7,8,9))

liste = [("Eren",27), ("Sümbül", 27), ("Almila", 2)]

liste.sort()    # sıfırıncı indekse göre sıralama yapar
#print(liste)    #sıralanan listeyi yazdırır

liste.sort(key= lambda x : x[1])    # birinci indekse göre sıralanır
#print(liste)    # sıralanan listeyi yazdırır


liste2 = [{"Ad":"Eren Can", "Soyad":"Yildirim", "Yas":27},{"Ad":"Sümbül", "Soyad":"Bingöl", "Yas":27},{"Ad":"Almila", "Soyad":"Yildirim", "Yas":2}]
liste2.sort(key= lambda x : x["Yas"])
#print(liste2)
