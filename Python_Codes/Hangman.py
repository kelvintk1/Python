word_list = ["advark", "baboon", "camel", "monkey", "lion", "tiger", "elephant"]
stages = [''' 
    +------+
    |      |
    O      |
   /|\     |
    |      |
   / \     |
=============
''', '''
    +------+
    |      |
    O      |
   /|\     |
    |      |
   /       |
=============
''', '''   
    +------+
    |      |
    O      |
   /|\     |
    |      |
           |
=============
''', '''
    +------+
    |      |
    O      |
   /|\     |
           |
           |
=============
''', '''
    +------+
    |      |
    O      |
   /|      |
           |
           |
=============
''', '''
    +------+
    |      |
    O      |
    |      |
           |
           |
=============
''', '''         
    +------+
    |      |
    O      |
           |
           |
           |
 =============
''', '''    
    +------+
    |      |
           |
           |
           |
           |
==============
''']
import os
import random
chosen_word = random.choice(word_list)
print(chosen_word)
word_len = len(chosen_word)
display = []
for dash in range(0, len(chosen_word)):
    line = "_"
    display += str(line)
print(display)

length = int(word_len)
lives = 8
end = False
while not end:
    guess = input("Kindly guess a letter: \n").lower()
    os.system("cls")
    if guess in display:
        print("You have already guessed this letter. \nTry a new letter.")
    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(display)
            items = ""
            for item in display:
                items += str(item)
            print(items)
    if guess not in chosen_word:
        lives -= 1
        Stage = stages[lives]
        print(f"{Stage}")
        print(f'Wrong match, you hvae {lives} attempts left.')
        if lives == 0:
            end = True
            print("Sorry, you lose.")
    elif "_" not in display:
        end = True
        print("You won!")


    