# -*- coding: utf-8 -*-

# ogrenci1 ="özlem"
# ogrenci2 ="berfin"
# ogrenci3 ="engin"

# print(ogrenci1)
# print(ogrenci2)
# print(ogrenci3)

ogrenciler = ["özlem","berfin","engin"]

print(ogrenciler[1])
ogrenciler.append("Ahmet") #listeye ahmet eklenir
ogrenciler[0] = "Veli" #öğrencilerin 0. elemanını veli yapar
print(ogrenciler[3])
ogrenciler.remove("engin") #listeden engin silinir
print(ogrenciler)

#list constructor
#listeleri bu şekilde de yazabiliriz
sehirler =list(("Ankara","istanbul"))
print(sehirler)
print(len(sehirler)) #kaç elemandan oluştuğunu gösterir



#Diğer Fonksyonlar
#print(sehirler.clear()) #listeyi temizler
print("Ankara sayısı =" + str(sehirler.count("Ankara"))) #Ankaranın sayısını verir
print("Ankara indexi = " + str(sehirler.index("Ankara"))) #Ankara indexini verir
sehirler.pop(0) #indexe göre silme işlemini yapar 
sehirler.insert(0,"Bursa") #0. indexe Bursayı ekler
sehirler.reverse() #sehirleri terse çevirir yerlerini değiştirir
print(sehirler) 


sehirler3 = sehirler.copy() #verinin kopyasını oluşturduk

sehirler2 = sehirler
sehirler2[0]="İzmir" #verini ilk indexini izmir yaptık

print(sehirler2)
print(sehirler)
print(sehirler3)

sehirler.extend(sehirler3) #iki listeyi bir araya getirir
sehirler.sort() #verileri sıralayarak getirir
sehirler.reverse() #sort yaptıktan sonrasıralanan verileri terse çevrdik
print(sehirler)
























