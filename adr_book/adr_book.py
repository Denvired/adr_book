#!/usr/bin/env python3
# I'm make this script as homework from my book. this is first quest.
# we save and load data (list of objects) to file
# possibilities: view, add, edit, find, delete records
# I can do this script very simple, without one line analising, and using pickle for save and load data,
# but Im have a new skills using this way
# Создадим скрипт для адресной книги, сохранение и чтение ее из файла.
# Возможности: просмотр, добавление, изменение, поиск, удаление записей

import os


# import time

import sofunc
import datetime


contact_list = []  # main list of contacts
file_contacts = 'file_contacts.csv'  # way to our file


# size of table fields
num_twidth = 6
name_twidth = 30
telef_twidth = 15
email_twidth = 25
age_twidth = 8
town_twidth = 25


# for terminal color decoration
class Style:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
# end of class style():


class Contact:
    """Class is records with fields: name, telephone, email, birthdate and town"""

    def __init__(self, name, **cont_params):
        """Init of object Contact. Get name and **cont_params
        possible params: telephone = str, email = str, town = str, birth(date as ??.??.????)"""

        self.name = name
        self.telef = ''
        self.email = ''
        self.birth = None
        self.town = ''
        self.extra_paramlist = {}  # we can read extra params
        print(f'name = {self.name}')
        for param_nam, param_stat in cont_params.items():
            if param_nam == 'telephone':
                self.telef = param_stat
                print(f'telephone = {self.telef}')
            elif param_nam == 'email':
                self.email = param_stat
                print(f'email = {self.email}')
            elif param_nam == 'birth':
                self.birth = param_stat
                print(f'birth = {self.birth}')
            elif param_nam == 'town':
                self.town = param_stat
                print(f'town = {self.town}')
            else:
                self.extra_paramlist[param_nam] = param_stat  # extra params
    # end of __init__()

    def __str__(self):
        """Printable variant of class. need update for self.extra_paramlist = {}, but not now"""

        str_forret = 'name = {0}, telephone = {1}, email = {2}, birthdate = {3}, town = {4}'.format(
            self.name, self.telef, self.email, self.birth if self.birth is not None else '', self.town)
        return str_forret
    # end of __str__()
# end of class style():


def str_to_contact(source_str, inp_type='Keyboard'):
    """we analize and split user data.
    At the end, we make a record to object of class Contact"""

    print(source_str)  # del
    sep = ','
    name_add = ''
    to_add_cont = {}
    rdy = False
    if inp_type == 'File':
        sep = ';'
    list_toins = source_str.split(sep)
    if len(list_toins) < 2:  # if only 1 entered item need start again
        print('Need address or email')
    else:
        # This cycle is big, becouse user input is flexible.
        # We able write like this patterns (must be Name and telephone or email as minimal), comma is our separator:
        # Andrew, 9050442333, my@com.ru,28.03.12,Moscow
        # Andrew, 9050442333, my@com.ru,28.03.12,Moscow
        # Andrew,my@com.ru,9050442333, moscow
        # Andrew,9050442333, moscow
        # Andrew,my@com.ru, moscow
        # Andrew,my@com.ru, 28.03.12
        # etc
        for i in range(len(list_toins)):
            # print('i=', i) del
            list_toins[i] = list_toins[i].rstrip().lstrip()  # del whitespaces from boards
            if list_toins[i] == '':
                continue
            if i == 0:
                name_add = list_toins[i]
                # ~~print('name: ', name_add, end=' ')
                continue
            if 'email' not in to_add_cont.keys() and '@' in list_toins[i]:
                to_add_cont['email'] = list_toins[i]
                rdy = True  # one of one important, able to generata record
                continue
            if 'telef' not in to_add_cont.keys() and sofunc.istel(list_toins[i]):
                to_add_cont['telephone'] = list_toins[i]
                rdy = True  # one of one important, able to generata record
                continue
            if 'birth' not in to_add_cont.keys() and sofunc.isdate(list_toins[i]):  # check and make date if possible
                print(list_toins[i])
                to_add_cont['birth'] = sofunc.makedate(list_toins[i])
                continue
            if 'town' not in to_add_cont.keys():
                to_add_cont['town'] = list_toins[i]
                # we can uncomment break to modify input. its mean, that town (not tel, not date and not email)
                # in our input is a last position to analise. after town, we miss all entriyes
                # break
            # can place here continue reading arguments like: to_add_cont[str.split('=')[0]] = str.split('=')[1]
        if rdy:
            contact_toapp = Contact(name_add, **to_add_cont)  # Make an Obj Contact
            contact_list.append(contact_toapp)
            print(contact_toapp)
            print(vars(contact_toapp))
        else:
            print('Not enough data, need email or telephone')


def loaddump():
    """load data from file to list. line per line send to func to parse string"""

    print('loaddump() is working')
    # global path_to_file_contacts
    print(path_to_file_contacts)
    if os.path.exists(path_to_file_contacts):
        # cont_file = open(path_to_file_contacts, 'r')
        with open(path_to_file_contacts, 'r') as cont_file:
            for line in cont_file:
                str_to_contact(line, inp_type='File')  # read and parse lines, type changes need to change separators
        print('have file, reading')
    else:
        print('there is no file')
# End of loaddump():


def savedump():
    """save to csv file and line by line, if I wish usage Contact.extra_paramlist need some modify"""

    print('savedump() is working')
    cont_file = open(path_to_file_contacts, 'w')
    for contact in contact_list:  # records
        if isinstance(contact.birth, datetime.date):   # check date or not date obj and generate str in dd.mm.YYYY
            date_forsave = contact.birth.strftime('%d.%m.%Y')
        else:
            date_forsave = ''
        print(f'{contact.name};{contact.telef};{contact.email};{date_forsave};{contact.town}')
        strto_file = f'{contact.name};{contact.telef};{contact.email};{date_forsave};{contact.town};\n'
        cont_file.write(strto_file)
        """# maybe much better use:
        # and need add datacheck and to str convert
        # str_to_file = ''
        # for pr_val in vars(contact).values():
            # str_to_file += pr_val + ';'
            # print(';'.join(pr_name.values()))
        # print(str_to_file)"""
    cont_file.close()
# End of savedump():


def printhead():
    """Here we print header of table"""

    # Head of Table
    print(Style.GREEN + 'num'.center(num_twidth) + '|' + 'Name'.center(name_twidth) + '|' +
          'Telephone'.center(telef_twidth) + '|' + 'Email'.center(email_twidth) + '|' +
          'Age'.center(age_twidth) + '|' + 'Town '.center(town_twidth) + Style.RESET)
# End of printhead()


def printitem(contact, nitem):
    """Here we print fields of Contact obj"""

    if isinstance(contact.birth, datetime.date):  # check date or not date obj and get Age via timedelta
        now = datetime.date.today()
        tdelta = now - contact.birth
        age = tdelta.days // 365
    else:
        age = ''
    strtoprn = f"{nitem:<{num_twidth}}|{contact.name:<{name_twidth}}|{contact.telef:<{telef_twidth}}|{contact.email:<{email_twidth}}|{age:<{age_twidth}}|{contact.town:<{town_twidth}}"
    print(strtoprn)
# End of printitem(contact, nitem)


def printscr(page, scr_type, contacts):
    """Here we print page of Contacts"""

    print('type =', scr_type, end='')
    print(' page =', page, ' printing: ')
    printhead()
    if scr_type in ('ONLYONE', 'LAST'):  # need to know how many cycles of contacts we must do
        endsitem = len(contacts)
    else:
        endsitem = page*10 + 10
    for numitem in range(page*10, endsitem):
        printitem(contacts[numitem], numitem+1)
    print(Style.MAGENTA + 'q - Exit', '    k - prev page' if scr_type in ('MIDDLE', 'LAST') else '',
          '     l - next page' if scr_type in ('MIDDLE', 'FIRST') else '',
          '     Enter num (eg: 21, to edit/delete 21):' + Style.RESET)
# End of printscr(page, scr_type)


def edit_contact(contact):
    """here we print contact data, and ask user about changes"""

    while True:
        print(contact)
        print(Style.YELLOW + 'Edit menu, chose field to edit:' + Style.RESET)
        print('1. Name')
        print('2. Telephone')
        print('3. Email')
        print('4. Data')
        print('5. Town')
        print('d. DELETE')
        print('q. Exit')
        print(Style.BLUE + 'Enter choice: ' + Style.RESET, end='')
        choice = sofunc.try_str()
        if choice is None:
            'None entered'
            continue
        elif choice == '1':
            print(f'Old name: {contact.name}\nNew name: ', end='')
            str_in = sofunc.try_str(key='STRIP')
            if len(str_in) > 0:
                contact.name = str_in
            else:
                print('Incorrect Name, try longer')
        elif choice == '2':
            print(f'Old telephone: {contact.telef}\nNew telephone: ', end='')
            str_in = sofunc.try_str(key='STRIP')
            if str_in == '' or sofunc.istel(str_in):  # check telephone pattern
                contact.telef = str_in
            else:
                print('Incorrect telephone')
        elif choice == '3':
            print(f'Old Email: {contact.email}\nNew Email: ', end='')
            str_in = sofunc.try_str(key='STRIP')
            if str_in == '' or '@' in str_in:  # is email?
                contact.email = str_in
            else:
                print('Incorrect email')
        elif choice == '4':
            if contact.birth is not None:
                print(f"Old birthdate: {contact.birth.strftime('%d.%m.%Y')}\nNew birthdate: ", end='')
            else:
                print(f"Old birthdate:\nNew birthdate: ", end='')
            str_in = sofunc.try_str(key='STRIP')
            if str_in == '' or sofunc.isdate(str_in):  # check date pattern
                contact.birth = sofunc.makedate(str_in)  # try to make a date
            else:
                print('Incorrect data')
        elif choice == '5':
            print(f'Old town: {contact.town}\nNew town: ', end='')
            str_in = sofunc.try_str(key='STRIP')
            contact.town = str_in
        elif choice == 'd':
            print(f'Do you realy want delete this record: {contact.name}\n(y to accept): ', end='')
            str_in = sofunc.try_str(key='STRIP')
            if str_in == 'y':
                contact_list.remove(contact)
                print('Deleted')
                print('Press any key')
                sofunc.try_str(key='SILENT')  # just enter any string for continue
                return 'DEL'
            contact.town = str_in
        elif choice == 'q':
            print(f'Choice: {choice}, quit')
            break
        else:
            print(f'Choice: {choice}')
            # mess_to = Style.RED + 'Incorrect intput: {0}, try again'.format(choice) + Style.RESET
            print(Style.RED + 'Incorrect intput: {0}, try again'.format(choice) + Style.RESET)


def view_contacts(contacts, calltype='VIEWS'):
    """Print table of our contacts, if I wish usage Contact.extra_paramlist need some modify"""

    print('view_contacts() is working')
    if len(contacts) > 0:
        num_pages = len(contacts) // 10 + 1  # How many pages we can print
        scr_typeset = 'ONLYONE'  # we print only one page
        cur_page = 1  # current page to print
        while True:
            if cur_page == 1 and num_pages > 1:
                scr_typeset = 'FIRST'  # first page, have yet
            elif 1 < cur_page < num_pages:
                scr_typeset = 'MIDDLE'  # not first, not last
            elif cur_page == num_pages and num_pages > 1:
                scr_typeset = 'LAST'  # last page
            if calltype == 'SEARCH':
                print(Style.MAGENTA + 'Finded by search: '.center(110) + Style.RESET)
            # contacts.values() if calltype == 'SEARCH' else contacts
            printscr(cur_page - 1, scr_typeset, contacts)
            print(Style.BLUE + 'Enter choice: ' + Style.RESET, end='')
            choice = sofunc.try_str()
            if choice is None:
                'None entered'
                continue
            elif choice == 'k' and scr_typeset not in ('ONLYONE', 'FIRST'):  # print prev page
                cur_page -= 1
                continue
            elif choice == 'l' and scr_typeset not in ('ONLYONE', 'LAST'):  # print next page
                cur_page += 1
                continue
            elif choice == 'q':
                break
            elif choice.isnumeric():  # try to edit contact at this number
                print('All numbers = edit')
                if int(choice) in range(1, len(contacts)+1):
                    feedb = edit_contact(contacts[int(choice)-1])
                    if feedb == 'DEL':  # if deleted contact - break
                        break
                else:
                    print('We havent contact with this number')
            else:
                print('wrong input')

    else:
        print("There is no contacts to output")

    print('Press any key')
    sofunc.try_str(key='SILENT')  # just enter any string for continue
# End of view_contacts():


def add_contact():
    """Here we are print istruction for input, after we take input."""

    while True:
        # sofunc.clearscr()
        print('add_contact() is working')
        print('Enter data separated by commas. Template: ' + Style.YELLOW +
              'Name, telephone number, email, birth date, town' + Style.RESET)
        print(Style.MAGENTA + 'Need 2 fields as minimal. ' + Style.RESET +
              'Name and one of (telephone number or email). eg: Andrew, 9050442333, my@com.ru,28.03.2012,NY')
        print('Empty Enter or q to return to main menu')
        print(Style.BLUE + Style.UNDERLINE + 'Input data:' + Style.RESET + ' ', end='')

        user_input = sofunc.try_str()
        if user_input is None:
            print('None entered')
            continue
        if user_input == '' or user_input == 'q':
            print('Return to main menu')
            break
        else:
            str_to_contact(user_input)  # parse string
        print('Press any key')
        sofunc.try_str(key='SILENT')  # just enter any string for continue
# End of add_contact()


def find_contact():
    """need descriprtion"""

    print('find_contact() is working')
    while True:
        # matches_cont = {}
        matches_list = []
        print(Style.BLUE + 'Enter String for search (empty for exit): ' + Style.RESET, end='')
        str_search = sofunc.try_str()
        if str_search is None:
            print('None entered')
            continue
        if len(str_search) > 0:
            print(vars(contact_list[1]))
            i = 0
            while i < len(contact_list):
                print(contact_list[i].name)
                print(i)
                matched = False
                for item, item_value in vars(contact_list[i]).items():
                    if item == 'birth':
                        if item_value is not None and str_search in item_value.strftime('%d.%m.%Y'):
                            print('Match by date in ', contact_list[i].name)
                            # matches_cont[str(i)] = contact_list[i]
                            matches_list.append(contact_list[i])
                            matched = True
                    else:
                        if str_search in item_value:
                            print(i)
                            print('Match by ', item, ' in ', contact_list[i].name)
                            # matches_cont[str(i)] = contact_list[i]
                            matches_list.append(contact_list[i])
                            matched = True
                    if matched:
                        break

                i += 1
        else:
            break
        print(matches_list)
        if len(matches_list) == 0:
            print('Nothing found')
            print('Press any key')
            sofunc.try_str(key='SILENT')  # just enter any string for continue
        else:
            view_contacts(matches_list, calltype='SEARCH')
# End of find_contact():


def menu():
    """print menu sreens, and take user's input, after call next functions, based on users input"""

    def printpunkts(screen='main', msgstr=''):
        """clear screen and print menu
        I think it must be moved to mudule, and some reworks for multiple use"""

        # sofunc.clearscr()
        if screen == 'main':
            print(Style.YELLOW + 'Address book:'.rjust(30) + Style.RESET)
            print(Style.GREEN + 'make a choice and push ENTER:'.rjust(39) + Style.RESET)
            print('1. Add contact')
            print('2. View contacts')
            print('3. Find (change, delete) contacts')
            print('q. Exit')
            if msgstr != '':
                print(msgstr)
            print(Style.BLUE + 'Enter choice: ' + Style.RESET, end='')
    # end of printpunkts():

    print('menu is working')
    printpunkts()
    while True:
        mess_to = ''  # message to send in reprint menu
        choice = sofunc.try_str()
        if choice is None:
            print('None entered')
            mess_to = Style.RED + 'Incorrect intput: None, try again' + Style.RESET
        if choice == '1':
            print(f'Choice: {choice}')
            add_contact()
        elif choice == '2':
            print(f'Choice: {choice}')
            # print(file_exist)
            view_contacts(contact_list)
        elif choice == '3':
            print(f'Choice: {choice}')
            find_contact()
        elif choice == 'q':
            print(f'Choice: {choice}, quit, bye bye')
            break
        else:
            print(f'Choice: {choice}')
            mess_to = Style.RED + 'Incorrect intput: {0}, try again'.format(choice) + Style.RESET
        printpunkts(msgstr=mess_to)
# End of menu()


# main body of script
def main():
    os.system('')  # for cls/clear working
    print('main working')
    # noinspection PyGlobalUndefined
    global path_to_file_contacts
    path_to_file_contacts = os.path.join(os.getcwd(), file_contacts)  # our save file
    loaddump()
    try:
        menu()
    except KeyboardInterrupt:
        print('Stopping program by keyboard')
    finally:
        savedump()
# End of func main():


# start main()
if __name__ == '__main__':
    main()
