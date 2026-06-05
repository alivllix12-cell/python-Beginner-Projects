print("==rock paper scissor==")
player_score=0
computer_score=0
import random
Play=["rock","paper","scissors"]

while True:
 user_choice=input("wrock paper scissors: ")
 computer_choice=random.choice(Play)
 print(computer_choice)
 if user_choice==computer_choice:
     print("A Tie")
 elif user_choice == "rock" and computer_choice == "scissors":
     print("You win")
     player_score+=1
 elif user_choice == "paper" and computer_choice == "rock":
     print("You win")
     player_score+=1
 elif user_choice == "scissors" and computer_choice == "paper":
     print("You win")
     player_score+=1
 else :
     print("You lose")
     computer_score+=1
     print('Game Over!')
     break
print(f"your score is {player_score}|computer score is {computer_score} \n")
print('thanks for playing!')

 

