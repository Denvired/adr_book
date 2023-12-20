# Here I define a small often used function
import re
import os
from datetime import date
import time
from pynput import keyboard


pr_key = None  # Key which pressed


def on_press(key):
    """Catch the pressed key and write to global param"""

    global pr_key
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        pr_key = key
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
        pr_key = key


def on_release(key):
    """Release key, if this key not fake click from terminal, brake listener Cycle"""

    print('{0} released'.format(
        key))
    global pr_key

    if pr_key == key:
        return False
    elif key == keyboard.Key.esc:
        return False
    """if key == keyboard.Key.esc:
        # Stop listener
        return False"""


def waitinp():
    """start cycle to listen keyboard, if key pressed, cycle will be stoped, and func return key"""

    # time.sleep(0.1)
    # noinspection PyTypeChecker
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
    global pr_key
    # time.sleep(0.1)
    # 2
    # print('', end='', flush=True)
    """keyb = keyboard.Controller()
    keyb.press(keyboard.Key.ctrl)
    keyb.press(keyboard.Key.left)
    keyb.release(keyboard.Key.left)
    keyb.press(keyboard.Key.delete)
    keyb.release(keyboard.Key.delete)
    keyb.release(keyboard.Key.ctrl)"""
    # print('\x08', end='')
    return pr_key


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


def clearinp():
    """clear keys pressed when walking in menus. This is not good idea, but it simply works.
    Best idea to use the curses, but I not want to use the curses in this simple programm """

    keyb = keyboard.Controller()
    for i in range(1, 50):
        keyb.tap(keyboard.Key.backspace)
        time.sleep(0.01)


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
    # Collect events until released
    print('start')
    print(' pr - key =', pr_key)
    print('hell')
    # sps = {'test': 'ts'}
    # if sps['tets'] == '':  # KeyError
    #    print('you')

    """ istel('+111122211')
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

    print('--------------')
    '''
    strd = '22,22.22'
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
    """


# End of main()


if __name__ == '__main__':
    main()
