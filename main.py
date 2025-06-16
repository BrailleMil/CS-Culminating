# import necessary modules
import os
import time
from utilities import get_valid_int, get_valid_quantity, apply_random_discount, show_change, get_valid_float

# define a function to clear the console
def clear():
    os.system('clear')

# define global variables for items, prices, stock, and password
items = ['Chips', 'Chocolate', 'Gummies', 'Cookies', 'Pop can']
prices = [1.25, 1.5, 1.0, 1.75, 1.0]
stock = [10, 10, 10, 10, 10]
PASSWORD = '1234'

# define the display_items function to show the items, prices, and stock
def display_items():
    for i in range(len(items)):
        print(str(i + 1) + ' ' + items[i] + ' $' + format(prices[i], '.2f') + ' ' + str(stock[i]))

# define the change_item function to change the name and price of an item
def change_item(index):
    items[index] = input('name: ')
    prices[index] = get_valid_int('Cost in cents: ', 1) / 100
    stock[index] = 10

# define the change_cost function to change the price of an item
def change_cost(index):
    prices[index] = get_valid_int('New cost in cents: ', 1) / 100

# define the restock function to restock all items to a default amount
def restock():
    for i in range(len(stock)):
        stock[i] = 10

# define the purchase function to calculate the total cost and update stock
def purchase(index, qty):
    total = prices[index] * qty
    stock[index] -= qty
    return total

# define the get_valid_float function to get a valid float input
def process_payment(total):
    paid = get_valid_float('Pay in dollars: ', 0)
    while paid < total:
        paid += get_valid_float('Insufficient funds. Please provide more: ', 0)
    return paid - total, paid

# define the manager_menu function to handle manager operations
def manager_menu():
    if input('password: ') != PASSWORD:
        return
    clear()
    while True:
        clear()
        # display the items and their details
        print('1. Change item')
        print('2. Change cost')
        print('3. Restock')
        print('4. Exit')
        # get the user's choice
        choice = get_valid_int('Choice: ', 1, 4)
        # handle the user's choice
        if choice == 1:
            clear()
            display_items()
            index = get_valid_int('Item number: ', 1, len(items)) - 1
            change_item(index)
        elif choice == 2:
            clear()
            display_items()
            index = get_valid_int('Item number: ', 1, len(items)) - 1
            change_cost(index)
        elif choice == 3:
            restock()
            print('All items have been restocked.')
            time.sleep(2)
            clear()
        else:
            break

# define the user_menu function to handle user operations
def user_menu():
    while True:
        # clear the console
        clear()
        # display the items and their details
        display_items()
        # prompt the user to choose an item and quantity
        print(str(len(items) + 1) + ' exit')
        # get the user's choice
        choice = get_valid_int('Choice: ', 1, len(items) + 1)
        # if the user chooses to exit, break the loop
        if choice == len(items) + 1:
            break
        # validate the choice and get the quantity
        qty = get_valid_quantity('Quantity: ', stock[choice - 1], items[choice - 1])
        # calculate the total cost, apply a random discount, process payment, and show change
        total = purchase(choice - 1, qty)
        total = apply_random_discount(total)
        print('Total $' + format(total, '.2f'))
        change, paid = process_payment(total)
        print('Change $' + format(change, '.2f'))
        show_change(change)

# define the main function to run the program
def main():
    while True:
        # clear the console
        clear()
        # display the main menu options
        print('1. Manager')
        print('2. User')
        print('3. Exit')
        # get the user's choice
        choice = get_valid_int('choice: ', 1, 3)
        # handle the user's choice
        if choice == 1:
            clear()
            manager_menu()
        elif choice == 2:
            clear()
            user_menu()
        else:
            break

# run the main function if this script is executed
if __name__ == '__main__':
    main()