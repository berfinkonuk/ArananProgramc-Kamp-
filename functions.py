# -*- coding: utf-8 -*-

#%%
sehir = "Ankara"
sonuc = sehir.upper()
print(sonuc)
print(sehir.endswith("e"))

#%%
def selamVer(isim = "ziyaretçi"):
    print("Merhaba " + isim)

selamVer()
selamVer("Berfin")
selamVer("Özlem")
selamVer("Sena")

def selamVer2(isim = "Ziyaretçi ", soyIsim = "Arkadaş"):
    print("Merhaba " + isim+ " " + soyIsim)

selamVer2()
selamVer2("Engin")
selamVer2("Engin", "Demiroğ")

#%%
def dikUcgenAlaniHesapla(a,b):
    return a*b/2

alan = dikUcgenAlaniHesapla(20,10)

print(alan)

#%%
#lambda return yerine bu şekilde kullanılabilir
dikUcgenAlaniHesapla2 = lambda a,b : a*b/2

print(dikUcgenAlaniHesapla(3, 6))

print(type(dikUcgenAlaniHesapla2))

x = dikUcgenAlaniHesapla2

print(x(4,5)
)




















