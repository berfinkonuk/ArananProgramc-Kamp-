# -*- coding: utf-8 -*-

studentsSet = {"engin","derin","salih","ahmet"}
#studentsSet2 = set("mehmet","veli","ayşe") #başka bir yazım biçimi
print(studentsSet)

for student in studentsSet:
    print(student)
    
print("derin" in studentsSet)

if "derin" in studentsSet:
    print("Listede var.")
    

studentsSet.add("ali")
print(studentsSet)

studentsSet.update(["merve", "mert", "selin"])
print(studentsSet)

print(len(studentsSet))

studentsSet.remove("selin")
print(len(studentsSet))

studentsSet.discard("selin") 
#selini yukarıda silmiştik bir daha silmeye çalışınca bulamayınca hata vermemesi için
print(len(studentsSet))

x = studentsSet.pop() #son elemanı silmeye yarar, sırasız oluğu için silineni bilemiyoruz
print(len(studentsSet))
print(studentsSet)

x = studentsSet.clear() #setin içindekilerin hepsini siler
print(len(studentsSet))
print(studentsSet)





















