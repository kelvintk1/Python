import game_data
import random
import os

Data = game_data.data
account_b = random.choice(Data)
score = 0
end = False
while not end:
    account_a = account_b
    while account_a == account_b:
        account_b = random.choice(Data)

    def first(account):
        star = account["name"]
        follower = account["follower_count"]
        Description = account["description"]
        Country = account["country"]
        return f"{star}, a {Description}, from {Country}. {follower}"

    def compare(a_account, b_account):
        if a_account > b_account:
            return a_account
        else:
            return b_account
    check = compare(account_a["follower_count"], account_b["follower_count"])

    print(f"Compare A: {first(account_a)}\nVs.")
    print(f"Against B: {first(account_b)}")

    guess = input("Who has more followers? (Type A or B)\n").lower()
    if guess == "a":
        guess = account_a["follower_count"]
    elif guess == "b":
        guess = account_b["follower_count"]
    else:
        print("Your input is incorrect.")
        break
    os.system('Cls')
    if guess != check and score == 0:
        print(f"\nSorry, that's wrong.\nScore: {score}\nYou lose.")
        end = True
    elif guess != check:
        score -= 1
        print(f"\nSorry, that's wrong.\nScore: {score}\n")
        if score == 0:
            print("You lose.")
            end = True
    else:
        score += 1
        print(f"\nYou're right\nScore: {score}\n")
    

    

