import os
from utilities import get_valid_int, apply_random_discount, get_valid_quantity, show_change

def clear():
    os.system('clear')

items = ['Chips', 'Chocolate', 'Gummies', 'Cookies', 'Water']
prices = [1.25, 1.5, 1.0, 1.75, 1.0]
stock = [10, 10, 10, 10, 10]
PASSWORD = '1234'

def display_items():
    for i in range(len(items)):
        print(str(i + 1) + ' ' + items[i] + ' $' + format(prices[i], '.2f') + ' ' + str(stock[i]))

def change_item(index):
    items[index] = input('name: ')
    prices[index] = get_valid_int('Cost in cents: ', 1) / 100
    stock[index] = 10

def change_cost(index):
    prices[index] = get_valid_int('New cost in cents: ', 1) / 100

def restock():
    for i in range(len(stock)):
        stock[i] = 10

def purchase(index, qty):
    total = prices[index] * qty
    stock[index] -= qty
    return total

def process_payment(total):
    paid = get_valid_int('Pay in dollars: ', 0)
    while paid < total:
        paid += get_valid_int('Insufficient funds. Please provide more: ', 0)
    return paid - total, paid

def manager_menu():
    if input('password: ') != PASSWORD:
        return
    clear()
    while True:
        clear()
        print('1. Change item')
        print('2. Change cost')
        print('3. Restock')
        print('4. Exit')
        choice = get_valid_int('Choice: ', 1, 4)
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
            clear()
        else:
            break

def user_menu():
    while True:
        clear()
        display_items()
        print(str(len(items) + 1) + ' exit')
        choice = get_valid_int('Choice: ', 1, len(items) + 1)
        if choice == len(items) + 1:
            break
        qty = get_valid_quantity('Quantity: ', stock[choice - 1], items[choice - 1])
        total = purchase(choice - 1, qty)
        total = apply_random_discount(total)
        print('Total $' + format(total, '.2f'))
        change, paid = process_payment(total)
        print('cChange $' + format(change, '.2f'))
        show_change(change)

def main():
    while True:
        clear()
        print('1. Manager')
        print('2. User')
        print('3. Exit')
        choice = get_valid_int('choice: ', 1, 3)
        if choice == 1:
            clear()
            manager_menu()
        elif choice == 2:
            clear()
            user_menu()
        else:
            break

if __name__ == '__main__':
    main()