print("Welcome to the Rock Paper Scissors Game!")
print("Rock \n Paper \n Scissors \n")
Choice = ["rock", "paper", "scissors"]
ur_choice = input("What do you choose?\n").lower()
rock = Choice[0].lower()
paper = Choice[1].lower()
scissors = Choice[2].lower()
import random
computer = random.choice(Choice).lower()
print(f"Computer chose: {computer} ")

if ur_choice == "rock" and computer == "scissors":
    print("You won!")
elif ur_choice == "scissors" and computer == "paper":
    print("You won!")
elif ur_choice == "paper" and computer == "rock":
    print("You won!")
elif ur_choice == computer:
    print("It's draw. \n Play again!")
elif ur_choice != Choice:
    print("There's an error with your input; check it well and play again.")
else:
    print("Sorry, you lose!")
