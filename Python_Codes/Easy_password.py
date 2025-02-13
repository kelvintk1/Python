import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k","l",
"m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K","L","M", "N",
"O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "+"]

password = ""
no_letters = input("How many letters would you like in your password?\n")
no_letters = int(no_letters)
for L in range(0, no_letters):
    password += random.choice(letters)

no_numbers = input("How many numbers would you like in your password?\n")
no_numbers = int(no_numbers)
for N in range(0, no_numbers):
    password += random.choice(numbers)

no_symbols = input("How many symbols would you like in your password?\n")
no_symbols = int(no_symbols)
for S in range(0, no_symbols):
    password += random.choice(symbols)

print(f"Your easy password is: {password}")