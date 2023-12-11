#!/usr/bin/env python3
# I'm make this script as homework from my book. this is first quest.
# we save and load data (list of objects) to file
# possibilities: view, add, edit, find, delete records
# Создадим скрипт для адресной книги, сохранение и чтение ее из файла.
# Возможности: просмотр, добавление, изменение, поиск, удаление записей

import os
import re
from datetime import date
import sofunc


contact_list = []  # main list of contacts
file_contacts = 'file_contacts.txt'  # way to our file
file_exist = None  # ?DELETE?


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
        possible params: telef = str, email = str, town = str, birth(date as ??.??.????)"""

        self.name = name
        self.telef = ''
        self.email = ''
        self.birth = ''
        self.town = ''
        print(f'name = {self.name}')
        for param_nam, param_stat in cont_params.items():
            if param_nam == 'telef':
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
    # end of __init__()

    def __str__(self):
        """Printable variant of class"""

        str_forret = 'name = {0}, telephone = {1}, email = {2}, birthdate = {3}, town = {4}'.format(
            self.name, self.telef, self.email, self.birth, self.town)
        return str_forret
    # end of __str__()
# end of class style():


def loaddump():
    """load data from file to list"""

    global file_exist
    print('loaddump() is working')
    path_to_file_contacts = os.path.join(os.getcwd(), file_contacts)
    print(path_to_file_contacts)
    if os.path.exists(path_to_file_contacts):
        print('have file, reading')
    else:
        print('there is no file')
        file_exist = False
# End of loaddump():


def savedump():
    print('savedump() is working')
# End of savedump():


def view_contacts():
    print('view_contacts() is working')
# End of view_contacts():


def add_contact():
    """Here we are print istruction for input, after we take input. after we analise and split user data.
    At the end, we make a record to object of class Contact"""

    while True:
        name_add = ''
        tel_add = ''
        email_add = ''
        birdate_add = ''
        town_add = ''
        to_add_cont = {}
        rdy = False
        sofunc.clearscr()
        print('add_contact() is working')
        print('Enter data separated by commas. Template: ' + Style.YELLOW +
              'Name, telephone number, email, birth date, town' + Style.RESET)
        print(Style.MAGENTA + 'Need 2 fields as minimal. ' + Style.RESET +
              'Name and one of (telephone number or email). eg: Andrew, 9050442333, my@com.ru,28.03.12,NY')
        print('Empty Enter to return to main menu')
        user_input = input()
        if user_input == '':
            print('Return to main menu')
            break
        list_toins = user_input.split(',')
        if len(list_toins) < 2:   # if only 1 entered item need start again
            print('Need address or email')
            input('Press any key')
            continue
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
            # ~~print('i=', i)
            list_toins[i] = list_toins[i].rstrip().lstrip()  # del whitespaces from boards
            if i == 0:
                name_add = list_toins[i]
                # ~~print('name: ', name_add, end=' ')
                continue
            if i == 1:
                if '@' in list_toins[i]:
                    to_add_cont['email'] = list_toins[i]
                    email_add = list_toins[i]
                    # ~~print('email: ', email_add, end=' ')
                else:
                    if sofunc.istel(list_toins[i]):
                        to_add_cont['telef'] = list_toins[i]
                        tel_add = list_toins[i]
                    # ~~print('tel_add: ', tel_add, end=' ')
                    else:
                        print(Style.MAGENTA + 'You not entered telephone or email!' + Style.RESET)
                        break
                rdy = True
                continue
            if i >= 2:
                if tel_add == '' and i == 2:
                    if sofunc.istel(list_toins[i]):
                        to_add_cont['telef'] = list_toins[i]
                        tel_add = list_toins[i]
                        # ~~print('email: ', email_add, end=' ')
                        continue
                if email_add == '' and i == 2:
                    if '@' in list_toins[i]:
                        to_add_cont['email'] = list_toins[i]
                        email_add = list_toins[i]
                        # ~~print('email: ', email_add, end=' ')
                        continue
                if birdate_add == '' and i < 4:
                    if sofunc.isdate(list_toins[i]):
                        to_add_cont['birth'] = list_toins[i]
                        birdate_add = sofunc.makedate(list_toins[i])
                        # ~~print('birdate_add: ', birdate_add, end=' ')
                        continue
                if town_add == '':
                    to_add_cont['town'] = list_toins[i]
                    town_add = list_toins[i]
                    # ~~print('town_add: ', town_add)
                    break

        # ~~print('You added: ', '~'.join(list_toins))
        # ~~print('You added dictionary: ', to_add_cont)
        if rdy:
            contact_toapp = Contact(name_add, **to_add_cont)
            contact_list.append(contact_toapp)
            print(contact_toapp)
        input('Press any key')
# End of add_contact()


def find_contact():
    print('find_contact() is working')
# End of find_contact():


def menu():
    """print menu sreens, and take user's input, after call next functions, based on users input"""

    def printpunkts(screen='main', msgstr=''):
        """clear screen and print menu"""

        sofunc.clearscr()
        if screen == 'main':
            print(Style.YELLOW + 'Address book:'.rjust(30) + Style.RESET)
            print(Style.GREEN + 'make a choice and push ENTER:'.rjust(39) + Style.RESET)
            print('1. Add contact')
            print('2. View contacts')
            print('3. Find (change, delete) contacts')
            print('4. Exit')
            if msgstr != '':
                print(msgstr)
            print(Style.BLUE + 'Enter choice: ' + Style.RESET, end='')
    # end of printpunkts():

    print('menu is working')
    printpunkts()
    while True:
        mess_to = ''  # message to send in reprint menu
        choice = input()
        if choice == '1':
            print(f'Choice: {choice}')
            add_contact()
        elif choice == '2':
            print(f'Choice: {choice}')
            print(file_exist)
            view_contacts()
        elif choice == '3':
            print(f'Choice: {choice}')
            find_contact()
        elif choice == '4':
            print(f'Choice: {choice}, quit, bye bye')
            savedump()
            break
        else:
            print(f'Choice: {choice}')
            mess_to = Style.RED + 'Incorrect intput: {0}, try again'.format(choice) + Style.RESET
        printpunkts(mess_to)
# End of menu()


# main body of script
def main():
    os.system('')
    print('main working')
    loaddump()
    menu()
# End of func main():


# start main()
if __name__ == '__main__':
    main()
