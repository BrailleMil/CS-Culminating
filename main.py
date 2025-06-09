from utilities import get_valid_int, apply_random_discount

items = ['Chips', 'Chocolate', 'Gummies', 'Cookies', 'Water']
prices = [1.25, 1.5, 1.0, 1.75, 1.0]
stock = [10, 10, 10, 10, 10]
PASSWORD = '1234'

def display_items():
    for i in range(len(items)):
        print(str(i + 1) + ' ' + items[i] + ' $' + format(prices[i], '.2f') + ' ' + str(stock[i]))


def change_item(index):
    items[index] = input('name: ')
    prices[index] = get_valid_int('cost in cents: ', 1) / 100
    stock[index] = 10


def change_cost(index):
    prices[index] = get_valid_int('new cost in cents: ', 1) / 100


def restock():
    for i in range(len(stock)):
        stock[i] = 10


def purchase(index, qty):
    total = prices[index] * qty
    stock[index] -= qty
    return total


def process_payment(total):
    paid = get_valid_int('pay in dollars: ', 0)
    while paid < total:
        paid += get_valid_int('add more dollars: ', 0)
    return paid - total, paid


def manager_menu():
    if input('password: ') != PASSWORD:
        return
    while True:
        print('1 change item')
        print('2 change cost')
        print('3 restock')
        print('4 exit')
        choice = get_valid_int('choice: ', 1, 4)
        if choice == 1:
            display_items()
            index = get_valid_int('item number: ', 1, len(items)) - 1
            change_item(index)
        elif choice == 2:
            display_items()
            index = get_valid_int('item number: ', 1, len(items)) - 1
            change_cost(index)
        elif choice == 3:
            restock()
        else:
            break


def user_menu():
    while True:
        display_items()
        print(str(len(items) + 1) + ' exit')
        choice = get_valid_int('choice: ', 1, len(items) + 1)
        if choice == len(items) + 1:
            break
        qty = get_valid_int('quantity: ', 1, stock[choice - 1])
        total = purchase(choice - 1, qty)
        total = apply_random_discount(total)
        print('total $' + format(total, '.2f'))
        change, paid = process_payment(total)
        print('change $' + format(change, '.2f'))


def main():
    while True:
        print('1 manager')
        print('2 user')
        print('3 exit')
        choice = get_valid_int('choice: ', 1, 3)
        if choice == 1:
            manager_menu()
        elif choice == 2:
            user_menu()
        else:
            break


if __name__ == '__main__':
    main()
