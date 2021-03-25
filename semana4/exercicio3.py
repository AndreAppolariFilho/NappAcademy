from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
if __name__ == '__main__':
    data_nascimento = datetime.strptime(input('Digite a data que voce nasceu no formato d/m/AAA: '), "%d/%m/%Y").date()
    print("Sua idade é : {}".format(relativedelta(datetime.now().date(), data_nascimento).years))