print("Welcome to Kelssa's Calcus.")
def plus(n1, n2):
    return n1 + n2

def minus(n1, n2):
    return n1 - n2

def times(n1, n2):
    return n1 * n2

def divided_by(n1, n2):
    return n1 / n2

def divisible_by(n1, n2):
    return n1 % n2

def square(n1, n2):
    return n1 ** n2

operation = {"+": plus, "-": minus, "*": times, "/": divided_by, "%": divisible_by}
operation["^"] = square
def calculation():
    number = float(input("What's your first number?\n"))
    while 5 > 0:
        for symbols in operation:
            print(symbols)
        operator = input("Pick an operation:\n")
        next = float(input("What's your next number?\n"))

        Calculate = operation[operator]
        answer = Calculate(number, next)
        print(f"{number} {operator} {next} = {answer}\n")

        proceed = input("Do you wants to continue calculating with the answer?(yes)\n Or\nYou wants to start a new calculation?(start)\n").lower()
        if proceed == "yes":
            print(answer)
            number = answer
            continue
        elif proceed == "start":
            calculation()
calculation()











    




    

