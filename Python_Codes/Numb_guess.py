print("Welcome To The Number Guesing Game!\n\nI'm thinking of a number between 1 and 100.\n")
import random
number = random.randrange(0, 100)
attempt = 0
def easy(): 
    global attempt
    attempt = 10
def hard():
    global attempt
    attempt = 5

mode = input("Choose a mode:(Hard / Easy)\n").lower()
if mode == "hard":
    print("\nYou have 5 attempts to guess the number.\n")
    hard()
elif mode == "easy":
    print("\nYou have 10 attempts to guess the number.\n")
    easy()

while attempt > 0:
    guess = int(input("Make a guess: "))
    attempt -= 1
    chance = f"You have {attempt} attempt remaining.\n"
    if guess > number:
        print(f"Your guessed number is high.\n {chance}")
    elif guess < number:
        print(f"Your guessed number is low.\n {chance}")
    elif guess == number:
        print("You win!\n You guessed the right number.")
        break
print(f"The guessed number is: {number}")


    