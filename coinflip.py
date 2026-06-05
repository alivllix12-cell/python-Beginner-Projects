print("====coin flip=====")
coin=["heads","tails"]
heads_count=0
tails_count=0
import random
for i in range(30):
 flip=random .choice(coin)
 print(flip)
 if flip == "heads" :
    heads_count+=1
 else:
   tails_count+=1
 print(f"heads count {heads_count} | tails count is {tails_count} \n")
total_heads=heads_count
total_tails=tails_count
Percentage_of_Heads=(heads_count /  30)*100
print(f"percentage of heads is {Percentage_of_Heads}% \n")