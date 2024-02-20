from coffee_maker import CoffeeMaker
from moneyMachine import MoneyMachine
from menu import Menu, MenuItem

coffee_maker=CoffeeMaker()
money_machine = MoneyMachine()
menu=Menu()

options = ["espresso", "latte", "cappuccino"]

while True:
    response = input("What would you like? (espresso/latte/cappuccino):").lower()
    if response == 'off':
        break
    if response == 'report':
        coffee_maker.report()
        money_machine.report()
    if response in options:
        drink=menu.find_drink(response)
        item = coffee_maker.is_resource_sufficient(drink)
        if item:
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
