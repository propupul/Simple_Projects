def menu():
    menu = {1 : ['Chicken Strips', 3.50],
            2 : ['French Fries', 1.50],
            3 : ['Hamburger', 4.00],
            4 : ['Hotdog', 3.50],
            5 : ['Large Drink', 1.75],
            6 : ['Medium Drink', 1.50],
            7 : ['Milk Shake', 2.25],
            8 : ['Salad', 3.75],
            9 : ['Small Drink', 1.25]
            }
    return(menu)

MENU = menu()


def order():
    some_input = input('Enter the number of the items you want to order (i.e 12345): ')
    calculate = 0

    for numbers in some_input:
        quantity = some_input.count(str(numbers))
        numbers = int(numbers)
        menu_price = MENU[numbers][1]
        calculate += menu_price


        print('You ordered:', quantity, MENU[numbers][0])

    print('Your total is','$' + str(calculate))


def main():
    print('Hello! Welcome to our Restaurant')
    print('Here is a list of our menu and prices:')
    menu_number = 1

    for key in MENU:
        print(str(menu_number)+'.' +str(MENU[key]).strip('['']'))
        menu_number += 1
    order()

main()
