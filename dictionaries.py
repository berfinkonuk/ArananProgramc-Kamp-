# -*- coding: utf-8 -*-

sozluk = {
    "book" : "kitap",
    "table" : "masa"
    }

sozluk2 = dict(kitap = "book", masa = "table") #ikinci kullanım

sozluk["book"] = "güncel kitap"
sozluk["pencil"]="kalem" #yeni değer eklemek
del(sozluk["book"])
print(len(sozluk))
print(sozluk)
