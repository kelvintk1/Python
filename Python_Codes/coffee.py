print("Welcome To The Coffee Machine!\n")

Water = 600
Milk = 450
Coffee = 200
Money = 0

Menu = {
"espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk" : 0,
        },
        "cost": 5
    },
"latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 30
    },
"cappucino": {
        "ingredients": {
            "water": 200,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 20
    } 
}

def drink(request):
    global Water, Milk, Coffee, Money 
    water = Menu[request]["ingredients"]["water"]
    Water -= water
    milk = Menu[request]["ingredients"]["milk"]
    Milk -= milk
    coffee = Menu[request]["ingredients"]["coffee"]
    Coffee -= coffee
    money = Menu[request]["cost"]
    print(f"Price: ${money}")
    
def cash(cash_in):
    global Money
    money = Menu[request]["cost"]
    if cash_in == money:
        Money += money
        print("Enjoy your drink.\n")
    elif cash_in > money:
        balance = cash_in - money
        Money += money
        print(f"Here is your balance: ${balance}\nEnjoy your drink.")
    else:
        print(f"Your moeny (${cash_in}) is not sufficient to purchase your required drink.\n")
keywords = ["espresso", "latte", "cappucino", "report", "off"]
while True:
    request = input("What would you like? (Espresso / Latte / Cappucino / Report / off)\n").lower()
    if request not in keywords:
        print("Sorry, your input is incorrect. Try again!")
        continue
    if request == "off":
        break
    elif request in Menu:
        drink(request)
        cash_in = int(input("PLease input your money.\n"))
        cash(cash_in)

    if request == "report":
        print(f"Water: {Water}ml\nMilk: {Milk}ml\nCoffee: {Coffee}g\nMoney: ${Money}")
    elif Water < Menu[request]["ingredients"]["water"]:
        print("Insufficient water")
        print(f"Water: {Water}ml")
        refill = input("Wants to refill? (yes / no)\n")
        if refill == "yes":
            print("Water has been refilled.")
            Water += 455
            print(f"Water: {Water}ml")
            continue
        elif refill == "no":
            print("Sorry, your drink can't be prepared with insufficient water.")
            break
        else:
            print("Check your input well.")
    elif Milk < Menu[request]["ingredients"]["milk"]:
        print("Insufficient milk")
        print(f"Milk: {Milk}ml")
        refill = input("Wants to refill? (yes / no)\n")
        if refill == "yes":
            print("Milk has been refilled.")
            Milk += 455
            print(f"Milk: {Milk}ml")
            continue
        elif refill == "no":
            print("Sorry, your drink can't be prepared with insufficient Milk.")
            break
        else:
            print("Check your input well.")
    elif Coffee < Menu[request]["ingredients"]["coffee"]:
        print("Insufficient coffee")
        print(f"Coffee: {Coffee}ml")
        refill = input("Wants to refill? (yes / no)\n")
        if refill == "yes":
            print("Coffee has been refilled.")
            Coffee += 500
            print(f"Coffe: {Coffee}ml")
            continue
        elif refill == "no":
            print("Sorry, your drink can't be prepared with insufficient Coffe.")
            break
        else:
            print("Check your input well.")




        
