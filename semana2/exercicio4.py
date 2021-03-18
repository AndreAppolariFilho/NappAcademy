from massa_dados import list_spend_money
from functools import reduce

def convert_to_float(x):
    try:
        return float(x)
    except ValueError as e:
        return 0


def spend_by_login(login, limit=1000):
    list_spend_money_ = list(map(lambda x :(x[0], x[1], x[2], convert_to_float(x[3])), list_spend_money))
    list_spend_money_ = list(filter(lambda x : x[1] == login and x [3] <= limit, list_spend_money_))
    print(*list_spend_money_, sep='\n')


def sum_by_login(login, limit=1000):
    list_spend_money_ = list(map(lambda x :(x[0], x[1], x[2], convert_to_float(x[3])), list_spend_money))
    list_spend_money_ = list(filter(lambda x : x[1] == login and x [3] <= limit, list_spend_money_))
    return reduce(lambda x, y : x + y[3], list_spend_money_, 0)

if __name__ == "__main__":
    login = 'justin16'
    spend_by_login(login, 1200)
    print('A soma total até 600: ')
    print(sum_by_login(login, 600))
    print('A soma total até 1200: ')
    print(sum_by_login(login, 1200))