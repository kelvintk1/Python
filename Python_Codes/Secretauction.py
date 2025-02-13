print("Welcome to the secret auction program!\n")
import os
empty = {}

def secret():
    name = input("What is your name?\n")
    amount = input("What's your bid?\n$") 
    empty[name] = amount

while 5 > 0:
    secret()
    ask = input("Is there any other person?\n").lower()
    os.system("cls")
    if ask == "yes":
        continue
    elif ask == "no":
        highest = 0
        for names in empty:
            values = empty[names]
            values = int(values)
            if values > highest:
                highest = values
                name = names
        print(f"The winner is {name} with a prize of ${highest}.\n")
        print(empty)
        break
    else:
        print("check your input well.\n")
        break