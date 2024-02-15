
def converter(curr_1: str, curr_2: str, money: float):
    match curr_1:
        case '1':
            match curr_2:
                case '1':
                    return 'You selected the same currency as you have: UAH'
                case '2':
                    return f'{money} UAH = {round(money * 0.026, 2)} $'
                case '3':
                    return f'{money} UAH = {round(money * 0.024, 2)} €'
                case _:
                    return 'Wrong input'
        case '2':
            match curr_2:
                case '1':
                    return f'{money} $ = {round(money * 38.1, 2)} UAH'
                case '2':
                    return 'You selected the same currency as you have: $'
                case '3':
                    return f'{money} $ = {round(money * 0.93, 2)} €'
                case _:
                    return 'Wrong input'
        case '3':
            match curr_2:
                case '1':
                    return f'{money} € = {round(money * 40.89, 2)} UAH'
                case '2':
                    return f'{money} € = {round(money * 1.07, 2)} $'
                case '3':
                    return 'You selected the same currency as you have: €'
                case _:
                    return 'Wrong input'
        case _:
                    return 'Wrong input'
def display_board():
    print('UAH -> $: 0.026\nUAH -> €: 0.024\n$ -> €: 0.93\n$ -> UAH: 38.1\n€ -> UAN: 40.89\n€ -> $: 1.07')
def currency_input():
    display_board()
    curr_1 = input('Choose currency which you have:\n1 - UAH\n2 - Dollar\n3 - Euro\nYour choice: ')
    curr_2 = input('Choose currency which you like to get:\n1 - UAH\n2 - Dollar\n3 - Euro\nYour choice: ')
    money = float(input('How much would you like to convert? '))
    if money < 0:
        return 'Negative ammount of money entered.'
    return converter(curr_1, curr_2, money)

if __name__ == '__main__':
    print(currency_input())