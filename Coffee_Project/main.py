from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

c_money = MoneyMachine()
c_machine = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}\n").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        c_machine.report()
        c_money.report() 
    else:
        drink = menu.find_drink(choice)
        if c_machine.is_resource_sufficient(drink) and c_money.make_payment(drink.cost):
            c_machine.make_coffee(drink)



 