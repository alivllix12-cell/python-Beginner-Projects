import random 
sec_num=random.randint(1, 100)
while True:
   number=int(input("enter a number: "))
   if  number> sec_num:
    print("too high!")
   elif number< sec_num:
    print("too low!")
   elif number==sec_num:
    print("Correct!")
    break