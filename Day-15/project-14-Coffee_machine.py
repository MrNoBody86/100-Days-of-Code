from menu import MENU,resources

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

def report(resources):
    """(resources) returns the resources available"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f"Money: ${earned_money}")

def Sufficient_resources(coffee_type,resources):
    """(coffee_type,resources) checks weather resources are sufficient"""
    if coffee_type == "espresso":
        if MENU[coffee_type]['ingredients']['water'] > resources['water'] :
            return "1"
        elif  MENU[coffee_type]['ingredients']['coffee'] > resources['coffee'] :
            return "3"
        else :
            return "4"
    else :
        if MENU[coffee_type]['ingredients']['water'] > resources['water'] :
            return "1"
        elif MENU[coffee_type]['ingredients']['milk'] > resources['milk'] :
            return "2"
        elif MENU[coffee_type]['ingredients']['coffee'] > resources['coffee'] :
            return "3"
        else :
            return "4"
    
def coin_processor(coffee_type):
    """(coffee_type) process the coins and check for successful transition"""
    #Ask for coins
    print("Please insert coins.")
    quarters = int(input("How many quarters? :"))
    dimes = int(input("How many dimes? :"))
    nickels = int(input("How many nickels? :"))
    pennies = int(input("How many pennies? :"))
    #process coins
    Total_money = round(quarters*0.25 + dimes*0.1 + nickels*0.05 + pennies*0.01,2)
    #check for successful transaction
    cost = MENU[coffee_type]['cost']
    if cost <= Total_money :
        change = Total_money - cost
        return change
    else:
        return False
    
def make_coffee(coffee_type,resources,money):
    """(coffee_type,resources,money) deduct the resources"""
    if coffee_type == "espresso":
        resources['water'] -= MENU[coffee_type]['ingredients']['water']
        resources['coffee'] -= MENU[coffee_type]['ingredients']['coffee']
    else:
        resources['water'] -= MENU[coffee_type]['ingredients']['water']
        resources['milk'] -= MENU[coffee_type]['ingredients']['milk']
        resources['coffee'] -= MENU[coffee_type]['ingredients']['coffee']

    print(f"Here is your {coffee_type} ☕ Enjoy!")
    money +=  MENU[coffee_type]['cost']
    

switch = True
earned_money = 0
clear()
while switch :
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_type == 'report':
        report(resources)
    elif coffee_type == 'off':
        switch = False
    else:
        Sufficient_resource = Sufficient_resources(coffee_type,resources)
        if Sufficient_resource == "1":
            print("Sorry there is not enough water")
        elif Sufficient_resource == "2":
            print("Sorry there is not enough milk")
        elif Sufficient_resource == "3":
            print("Sorry there is not enough coffee")
        elif Sufficient_resource == "4":
            change = coin_processor(coffee_type)
            if not change:
                print("Sorry that's is not enough money. Money refunded.")
            else:        
                print(f"Here is ${change} in change.")
                make_coffee(coffee_type,resources,earned_money)