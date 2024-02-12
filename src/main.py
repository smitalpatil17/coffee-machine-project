MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

ingredient_name = ['water', 'milk', 'coffee']


def print_report():
    """Prints total resources available"""
    print(f"Water: {resources[ingredient_name[0]]}ml")
    print(f"Milk: {resources[ingredient_name[1]]}ml")
    print(f"Coffee: {resources[ingredient_name[2]]}g")
    print(f"Money: ${resources['money']}")


def check_resources(coffee_type):
    """Check if sufficient resources are available to make coffee. Return "success" if all ingredients are available.
    else returns which ingredient is missing"""
    coffee_req = MENU[coffee_type]['ingredients']
    if resources[ingredient_name[0]] >= coffee_req[ingredient_name[0]]:
        if resources[ingredient_name[2]] >= coffee_req[ingredient_name[2]]:
            if ingredient_name[1] in coffee_req:
                if resources[ingredient_name[1]] >= coffee_req[ingredient_name[1]]:
                    return 'success'
                else:
                    return ingredient_name[1]
            else:
                return 'success'
        else:
            return ingredient_name[2]
    else:
        return ingredient_name[0]


def process_coins(coffee_type):
    """Takes input from user for money and check if there are sufficient money. If yes return true else return false"""
    print("Enter coins")
    total = 0
    total += int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.10
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    change = round((total - MENU[coffee_type]['cost']), 2)
    if change > 0:
        print(f"Here is ${change} in change")
    return total > MENU[coffee_type]['cost']


def make_coffee(coffee_type):
    """Make coffee i.e., reduce all ingredients which are being used and increase money"""
    coffee_req = MENU[coffee_type]['ingredients']
    resources[ingredient_name[0]] -= coffee_req[ingredient_name[0]]
    if ingredient_name[1] in coffee_req:
        resources[ingredient_name[1]] -= coffee_req[ingredient_name[1]]
    resources[ingredient_name[2]] -= coffee_req[ingredient_name[2]]
    resources['money'] += MENU[coffee_type]['cost']


options = ["espresso", "latte", "cappuccino"]

while True:
    response = input("What would you like? (espresso/latte/cappuccino):").lower()
    if response == 'off':
        break
    if response == 'report':
        print_report()
    if response in options:
        item = check_resources(response)
        if item == "success":
            if process_coins(response):
                make_coffee(response)
                print(f"Here is your {response} ☕. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded")
        else:
            print(f"Sorry there is not enough {item}.")
