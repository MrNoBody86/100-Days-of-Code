from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def clear():
    """clears the terminal"""
    import os
    import sys
    # Linux
    if sys.platform.startswith('linux'):
        os.system('clear')
    # Windows
    elif sys.platform.startswith('win32'):
        os.system('cls')

coffee_menu = Menu()
coffee_machine = CoffeeMaker()
counter = MoneyMachine()

state = "on"
clear()

while state != "off" :
    order = input(f"What would you like? ({coffee_menu.get_items()}):")
    # options = menu.get_items()
    # choice = input(f"What would you like? ({options}): ")
    if order == "report" :
        coffee_machine.report()
        counter.report()
    elif order == "off" :
        state = "off"
    else :
        drink = coffee_menu.find_drink(order)
        sufficient_res = coffee_machine.is_resource_sufficient(drink)
        if sufficient_res :
            payment_sufficient = counter.make_payment(drink.cost)
            if payment_sufficient :
                coffee_machine.make_coffee(drink)
        # if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
        #   coffee_maker.make_coffee(drink)