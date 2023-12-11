# Here I define a small often used functions
import re
import os
from datetime import date


def istel(teled):
    """check the string is tel pattern"""

    patt = re.compile(r'[+]?\d+')
    if patt.fullmatch(teled):
        return True
    else:
        return False
# end of isteled()


def isdate(dated):
    """check the string is date pattern"""

    patt = re.compile(r'\d\d[-.,/*_]\d\d[-.,/*_]\d{4}')  # pattern, like 25.05.1991 or 22/12/1986
    # 08.12.23 add more variants for pattern of date
    # ~~print('dated=', dated)
    # ~~print(patt.match(dated))
    if patt.fullmatch(dated):
        return True
    else:
        return False
# end of isdate()


def makedate(datestr):
    """Make a date from str"""

    try:
        str_to_ret = date(int(datestr[6:]), int(datestr[3:5]), int(datestr[:2]))
    except ValueError:
        print('Your date input is wrong format')
        input('Press any key')
        return ''
    else:
        return str_to_ret
# end of makedate(datestr):


def clearscr():
    """clear screen"""

    os.system('clear')
    # print('\n' * 100)
# End of clearscr():


def main():
    # sps = {'test': 'ts'}
    # if sps['tets'] == '':  # KeyError
    #    print('you')
    input()
    istel('+111122211')
    istel('2233332222')
    istel('eer444erer')
    istel('555ff3444')
    istel('666266+66666')
    istel('+++666266+66666')
    istel('2233332.222')

    print('--------------')

    isdate('sdttds.fd.ff')
    isdate('ss.ff.ff')
    isdate('22.22.22')
    isdate('22-22.22')
    isdate('22j22.22')
    isdate('22k22.22')
    isdate('22.22.1522')
    isdate('22--22.22')
    isdate('22*22.22')
    isdate('22_-22.22')
    isdate('22_22.22')
    isdate('22*22/22')
    isdate('22*22/1522')

    strd = '22,22.22'

    print('--------------')
    '''
    name_add = 'den'
    tel_add = '2314'
    email_add = ''
    birdate_add = ''
    town_add = ''
    for par in name_add, tel_add, email_add, birdate_add, town_add:
        if par != '':
            print(par)

    print(strd[3:5])

    #list_params = [name_add, tel_add]
    '''
# End of main()


if __name__ == '__main__':
    main()
