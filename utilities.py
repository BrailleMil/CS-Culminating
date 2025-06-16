import random

def get_valid_int(prompt, low=0, high=1000000):
    value = input(prompt)
    while True:
        if value.isdigit():
            num = int(value)
            if num >= low and num <= high:
                return num
        value = input(prompt)

def get_valid_quantity(prompt, stock_amt, item_name):
    while True:
        qty = get_valid_int(prompt, 1)
        if qty <= stock_amt:
            return qty
        print('There are only ' + str(stock_amt) + ' ' + item_name + ' in stock, please choose a quantity equal to or less than the stock remaining.')

def apply_random_discount(total):
    if random.randint(1,5) == 1:
        return total * 0.9
    return total

def show_change(change):
    cents = int(round(change * 100))
    values = [
        (2000, '$20 bill'),
        (1000, '$10 bill'),
        (500, '$5 bill'),
        (200, 'Toonie'),
        (100, 'Loonie'),
        (25, 'Quarter'),
        (10, 'Dime'),
        (5, 'Nickel')
    ]
    for value, name in values:
        count = cents // value
        if count > 0:
            if count > 1 and name in ['Quarter', 'Dime', 'Nickel']:
                print(str(count) + ' ' + name + 's')
            else:
                print(str(count) + ' ' + name)
            cents -= count * value
    input('')