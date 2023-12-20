# Here I define a small often used function
import re
import os
from datetime import date


def try_str(key='NOT_SILENT'):
    """try to read string, and return it
    if except return None
    key blocking print of error, it usable in just key menu
    if unicode error and key is STRIP return empty string '' """

    try:
        choice = input()
    except UnicodeError:
        if key == 'NOT_SILENT':
            print('Wrong symbol entered, Unicode decode error')
        if key == 'STRIP':  # need return something for operations
            print('Wrong symbol entered, Unicode decode error')
            return ''
    else:
        if key == 'STRIP':
            return choice.strip()
        else:
            return choice


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
        return None
    else:
        return str_to_ret
# end of makedate(datestr):


def clearscr():
    """clear screen"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    # print('\n' * 100)
# End of clearscr():


def main():
    print('hello I\'m sofunc')

# End of main()


if __name__ == '__main__':
    main()
