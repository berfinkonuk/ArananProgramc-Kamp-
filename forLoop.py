# -*- coding: utf-8 -*-

sehirler = ["Ankara","İstanbul","İzmir"]
# print(sehirler[0])
# print(sehirler[1])
# print(sehirler[2])

#%% For intro
for sehir in sehirler:
    if sehir == "İstanbul":
        continue
    print(sehir + " için kod = " + sehir[0:3])
    print("*******")

#%% For range
for x in range(1,100,2): #1 den 100e kadar tek sayıları verir
    print(x)