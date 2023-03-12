# -*- coding: utf-8 -*-

cumle = input("Cümleyi Giriniz :")

kelimeler = cumle.split()

kelimeler.sort()

print(kelimeler)

for kelime in kelimeler:
    print(kelime)