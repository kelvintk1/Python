print("Welcome To The Black_jack Game!\n")
# if C_choose == cards[10]:
#     return f"Jack"
# if C_choose == cards[11]:
#     return f"Queen"
# if C_choose == cards[12]:
#     return f"King"
# elif C_choose == cards[0] or C_choose == cards[13]:
#     return f"Ace"
# else:
#     return f"{C_choose}"
import random
import os
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(C_score, H_score):
    if H_score == C_score:
        return "Draw"
    elif C_score == 0 and H_score != 0:
        return "You lose, opponent has a BlackJack"
    elif H_score == 0 and C_score != 0:
        return "You've won with a BlacJack"
    elif H_score > 21:
        return "You lose, you went over."
    elif C_score > 21:
        return "You won, opponent went over."
    elif H_score > C_score:
        return "You win, your score is greater than that of the opponent."
    else:
        return "You lose"
def play_game():
    computer_cards = []
    user_cards = []
    game_over = False

    for kay in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not game_over:
        C_score = calculate_score(computer_cards)
        H_score = calculate_score(user_cards)
        print(f"Your cards: {user_cards}, Current score: {H_score}\n")
        print(f"Computer's first card: {computer_cards[0]}")

        if C_score == 0 or H_score == 0 or H_score > 21:
            game_over = True
        else:
            question = input("Do you wants to bring another card? (yes / no)\n").lower()
            if question == "yes":
                user_cards.append(deal_card())
            else:
                game_over = True
    while C_score != 0 and C_score < 17:
        computer_cards.append(deal_card)
        C_score = calculate_score(computer_cards)

    print(f"Your final hand is: {user_cards}, final score: {H_score}\n ")
    print(f"Computer's final hand is: {computer_cards}, final score: {C_score}")
    print(compare(H_score, C_score))

restart = input("Do you wants to play a game of Black Jack? (yes/no)\n").lower()
if restart == "yes":
    os.system("cls")
    play_game()