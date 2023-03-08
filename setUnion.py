# -*- coding: utf-8 -*-

setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}

#set union
print(setA | setB) #ikisinde de ortak veriyi bir kez getirir
print(setA.union(setB))

#Set Intersection
print(setA & setB) #sadece ortak verilri getirir
print(setA.intersection(setB))

#Set Dİfference
print(setA - setB) #A da olup B de olmayanları getirir
print(setA.difference(setB))

#Symmetric Dİfference
print(setA ^ setB) #Kesişim dışında hepsini getirir.
print(setA.symmetric_difference(setB))