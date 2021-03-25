from datetime import datetime
from datetime import timedelta

if __name__ == '__main__':
    dia = datetime.now().date() + timedelta(weeks=2, days=3)
    print( 'Daqui a duas semanas e 3 dias será {}'.format(dia))