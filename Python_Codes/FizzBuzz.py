print("Welcome to the FizzBuzz game!\n")
kay = input("What number would you like to check?\n")
kay = int(kay)

if kay % 3 == 0 and kay % 5 == 0:
    kay = "FizzBuzz"
    print(f"The number is {kay}\n")
elif kay % 3 == 0:
    kay = "Fizz"
    print(f"The number is {kay}")
elif kay % 5 == 0:
    kay = "Buzz"
    print(f"The number is {kay}\n")
else:
    print(kay)

    