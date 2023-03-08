# -*- coding: utf-8 -*-


lights = ["red","yellow","green"]

currentLight = lights[2]

print(currentLight)

if currentLight == "red":
    print("STOP!")
elif currentLight == "yellow":
    print("READY!")
else: #hiç bir koşulu sağlamadığında else ile her türlü bu çalışır
    print("GO!")