# -*- coding: utf-8 -*-
#substring
mesaj = "Merhaba dünya" 

print(mesaj[2:5])

yeniMesaj = mesaj[12:13]
print(yeniMesaj)


#len fonksiyonu
print(len(mesaj)) #metnin zunluğunu verir

yeniMesaj2 = mesaj[len(mesaj)-1 : len(mesaj)]
print(yeniMesaj2)

#Lower Upper
print(mesaj.upper()) #metnin bütün karakterlerini büyük harfe çevirir.
print(mesaj.lower())

#replace
#mesaj = mesaj.replace("ü","u")
print(mesaj.replace("ü","u")) #mesajdaki harfi değiştirmemizi sağlar
print(mesaj)

print(mesaj.replace("a","e")) #metindeki a harflerini e harfine çevirerek yazdı

#split ve sprit 
bilgi = "    berfin;konuk;24;Ankara ".strip() #strip boşlukları atmaya yarar
print(bilgi.split()) #kelimeleri listeleyerek getirir
print("Adı = " + bilgi.split(";")[0]) 

#input
ad = input("Adınız?") #kullanıcıdan ad sayı1 ve sayı2 istendi
sayi1 = input("Sayı 1 =?")
sayi2 = input("Sayı 2 =?")
print(int(sayi1) + int(sayi2)) #tip dönüşümü yapıp sayıları topladı



















