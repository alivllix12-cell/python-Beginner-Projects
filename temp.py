Celisius='C'
Fahrenheit='F'
Kelvin='K'
print("hello,World")
while True:
 origintemp=input('enter the temp you have(C/F): ')
 tempconv=input('enter the temp u want to convert to(C/F): ')
 temporgconv=int(input("enter the value of the origin temp: "))
 if origintemp == Celisius and tempconv == Fahrenheit:
   fahrenheit = temporgconv*1.8 + 32
   print(fahrenheit)
 elif origintemp==Fahrenheit and tempconv==Celisius:
   Celisius= temporgconv-32*5/9
   print(Celisius)
 elif (origintemp == Fahrenheit or origintemp == Celisius) and tempconv == Kelvin:
  Kelvin= temporgconv + 273.15
  print(Kelvin)
  break