score=0
with open('questionanswer.txt','r') as file:
    for line in file:
        if "Question" in line:
            print(line)
            user_answer= input("Answer=")
            correct_answer=next(file).split("=")[1].strip()

        if user_answer==correct_answer:
         print("Correct!")
         score+=1
        else:
         print("Wrong!")
print(f"your score is {score}")
