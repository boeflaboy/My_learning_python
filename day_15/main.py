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

money = 0.0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# noinspection PyShadowingNames
def report():
    # noinspection PyShadowingNames
    for ingredient in resources.keys():
        if ingredient == 'coffee':
            continue
        print(f'{ingredient.title()}: {resources[ingredient]} ml')
    print(f"Coffee: {resources['coffee']}g")
    print(f'Money: ${money}')

def sufficient_resources(drink):
    for item in drink['ingredients']:
        if not drink['ingredients'][item] > resources[item]:
            return True
        else:
            print(f"Sorry There is not enough {item}")
            return False

def amount_coin():
    quarter = float(input("Insert how many quarters: ")) * 0.25
    dime = float(input("Insert how many dimes: ")) * 0.10
    nickel = float(input("Insert how many nickels: ")) * 0.05
    penny = float(input("Insert how many pennies ")) * 0.01
    total = quarter + dime + nickel + penny
    return total


def proccess_coins(amount_of_coins, cost_drink):
    if amount_of_coins < cost_drink:
        print("Sorry there is not enough money. Money refunded.")
        return False
    elif amount_of_coins > cost_drink:
        change = amount_of_coins - cost_drink
        print(f"Here is your change ${change}")
        return True
    else:
        return True


while True:
    user_input = input("What would you like? (espresso/latte/cappuccino):")
    if user_input == "off":
        break
    elif user_input == "report":
        report()
    else:
        drink = MENU[user_input]
        if sufficient_resources(drink):
            amount_coins = amount_coin()
            if proccess_coins(amount_coins, drink['cost']):
                print(f"Enjoy your {user_input}!")
                money = amount_coins
                for ingredient in drink['ingredients']:
                    resources[ingredient] -= drink['ingredients'][ingredient]
        else:
            break














