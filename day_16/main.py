import sys

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
resources = CoffeeMaker()
payment = MoneyMachine()

all_items = menu.get_items()


while True:
    user_choice = input(f"What would you like? ({all_items}): ")
    if user_choice == 'off':
        sys.exit()
    elif user_choice == 'report':
        resources.report()
        payment.report()
    else:
        drink_resources = menu.find_drink(user_choice)
        if resources.is_resource_sufficient(drink_resources):
            if payment.make_payment(drink_resources.cost):
                resources.make_coffee(drink_resources)





from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ['Naam', 'Adres', 'Woonplaats', 'Gemeente', 'Land']
table.add_row(['Samie Ridha', 'Klein Jagersteinstraat', 'Langbroek', "Wijk bij Duurstede", "Nederland"])
table.add_row(["Henk Henker", 'Blauwemaan', 'Giethoorn', 'Utrecht', 'Nederland'])

table.align['Adres'] = 'l'
table.align['Gemeente'] = 'l'

print(table)


