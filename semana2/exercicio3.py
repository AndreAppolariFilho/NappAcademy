from massa_dados import list_spend_money
from functools import reduce

def convert_to_float(x):
    try:
        return float(x)
    except ValueError as e:
        return 0

def spend_by_subname(name):
    list_spend_money_ = list(map(lambda x :(x[0], x[1], x[2], convert_to_float(x[3])), list_spend_money))
    list_spend_money_ = list(filter(lambda x : name in x[0] , list_spend_money_))
    print(*list_spend_money_, sep='\n')


def sum_by_subname(name):
    list_spend_money_ = list(map(lambda x :(x[0], x[1], x[2], convert_to_float(x[3])), list_spend_money))
    list_spend_money_ = list(filter(lambda x : name in x[0] , list_spend_money_))
    return reduce(lambda x, y : x + y[3], list_spend_money_, 0)


if __name__ == "__main__":
    name = 'Brown'
    spend_by_subname(name)
    print('A soma total é: ')
    print(sum_by_subname(name))