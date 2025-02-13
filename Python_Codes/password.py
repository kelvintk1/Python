print("Welcome To The Password Generator!")

level = input("Which level of password do you wants? \n (Hard or Easy)?").lower()

if level == "hard":
    import Hard_password
elif level == "easy":
    import Easy_password
else:
    print("Check your input well.")

