# import necessary module(s)
import random

# define a function to get a valid integer input within a specified range
def get_valid_int(prompt, low=0, high=1000000):
    value = input(prompt)
    while True:
        if value.isdigit():
            num = int(value)
            if num >= low and num <= high:
                return num
        value = input(prompt)

# define a function to get a valid float input with a minimum value
def get_valid_float(prompt, low=0.0):
    while True:
        try:
            num = float(input(prompt))
            if num >= low:
                return num
        except:
            pass

# define the get_valid_quantity function to get a valid quantity input based on stock amount
def get_valid_quantity(prompt, stock_amt, item_name):
    while True:
        qty = get_valid_int(prompt, 1)
        if qty <= stock_amt:
            return qty
        print('There are only ' + str(stock_amt) + ' ' + item_name + ' in stock, please choose a quantity equal to or less than the stock remaining.')

# define the apply_random_discount function to apply a random discount to the total
def apply_random_discount(total):
    if random.randint(1,5) == 1:
        return total * 0.9
    return total

# define the show_change function to display the change
def show_change(change):
    cents = int(round(change * 100))
    # define the denominations and their corresponding values
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
    # iterate through the values and calculate the count of each denomination
    for value, name in values:
        count = cents // value
        if count > 0:
            if count > 1 and name in ['Quarter', 'Dime', 'Nickel']:
                print(str(count) + ' ' + name + 's')
            else:
                print(str(count) + ' ' + name)
            cents -= count * value
    input('')
