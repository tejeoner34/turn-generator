"""
Main file of turn generator app
"""
import generator
from os import system, name


def clear_console():
    if name == 'nt':
        print('CLEAR')
        system('cls')
    else:
        system('clear')


cosmetic_number = generator.infinite_generator()
pharmacy_number = generator.infinite_generator()
drug_store_number = generator.infinite_generator()

business_areas = [
    {
        "name": "Cosmetics",
        "current": cosmetic_number,
        "shortcut": "CO",
        "id": 1
    },
    {
        "name": "Pharmacy",
        "current": pharmacy_number,
        "shortcut": "PH",
        "id": 2
    },
    {
        "name": "Drug Store",
        "current": drug_store_number,
        "shortcut": "DS",
        "id": 3
    }
]


def format_ticket(turn_number, id):
    turn_string = str(turn_number)
    return id + turn_string


def print_ticket(option):
    print(format_ticket(next(option['current']), option['shortcut']))


def find_option(option_id, options):
    found_option = None
    for option in options:
        if option['id'] == option_id:
            found_option = option
            break
    return found_option


def print_options(options):
    for index, option in enumerate(options):
        print(f"{index + 1} - {option['name']}")
    choose_option(options)


def choose_option(options):
    try:
        chosen_option = int(input('Enter an option: '))
    except:
        print('Enter a correct number')
        print_options(options)
    else:
        area = find_option(chosen_option, options)
        if area:
            clear_console()
            print_ticket(area)
            print_options(options)
        else:
            choose_option(options)



print_options(business_areas)