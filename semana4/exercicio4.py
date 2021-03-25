from datetime import datetime
from datetime import date
if __name__ == '__main__':
    dia_da_derrota = date(2014, 7, 8)
    print("Já se passaram {} dia desde a terrivel derrota do 7x1".format(
        (datetime.now().date() - dia_da_derrota).days
    ))