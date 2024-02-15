
def converter(curr_1: str, curr_2: str, money: float):
    pass

def currency_input():
    curr_1 = input('Choose currency which you have:\n1 - UAH\n2 - Dollar\n3 - Euro\nYour choice: ')
    curr_2 = input('Choose currency which you like to get:\n1 - UAH\n2 - Dollar\n3 - Euro\nYour choice: ')
    money = float(input('How much would you like to convert? '))
    return curr_1, curr_2, money

if __name__ == '__main__':
    print(currency_input())