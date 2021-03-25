from datetime import datetime

if __name__ == '__main__':
    print( 'Eu tenho {} dias de vida'.format((datetime.now() - datetime(1996, 9, 4)).days))