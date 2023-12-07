#!/usr/bin/env python3
# Создадим скрипт для адресной книги, сохранение и чтение ее из файла.
# Возможности: просмотр, добавление, изменение, поиск, удаление записей

import os
import re

contact_list = []  # main list of contacst
file_contacts = 'file_contacts.txt'
file_exist = None


# для декорирования цветом
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
    def __init__(self, name, telef=None, email=None, birth=None, town=None):
        self.name = name
        self.telef = telef
        self.email = email
        self.town = town
        self.birth = birth
    # end of __init__()
# end of class style():


# clear screen
def clearscr():
    print('\n' * 100)
# End of clearscr():


# тут мы загружаем данные в список из файла
def loaddump():
    global file_exist
    print('loaddump() is working')
    # path_to_file_contacts = os.path.join(file_contacts, os.getcwd())
    path_to_file_contacts = os.path.join(os.getcwd(), file_contacts)
    print(path_to_file_contacts)
    if os.path.exists(path_to_file_contacts):
        print('файл есть, будем читать')
    else:
        print('Файла нет')
        file_exist = False
# End of loaddump():


def savedump():
    print('savedump() is working')
# End of savedump():


def view_contacts():
    print('view_contacts() is working')
# End of view_contacts():


# Здесь получим от пользователя строку и разобьем ее для анализа и создадим объект
def add_contact():

    # проверим подходит ли дата под шаблон
    def isdate(dated):
        patt = re.compile(r'\d\d\.\d\d\.\d\d')
        print('dated=', dated)
        print(patt.match(dated))
        if patt.match(dated):
            return True
        else:
            return False
    # end of isdate()

    while True:
        name_add = ''
        tel_add = ''
        email_add = ''
        birdate_add = ''
        town_add = ''
        clearscr()
        print('add_contact() is working')
        print('Enter data separated by commas. Template: ' + Style.YELLOW +
              'Name, telephone number, email, birth date, town' + Style.RESET)
        print(Style.MAGENTA + 'Need 2 fields as minimal. ' + Style.RESET +
              'Name and one of (telephone number or email). eg: Andrew, 9050442333, my@com.ru,28.03.12,NY')
        print('Empty Enter to return to main menu')
        user_input = input()
        if user_input == '':
            print('Выхожу в основное меню')
            break
        list_toins = user_input.split(',')
        if len(list_toins) < 2:
            print('Need address or email')
            input('Press any key')
            continue
        for i in range(len(list_toins)):
            print('i=', i)
            list_toins[i] = list_toins[i].rstrip().lstrip()  # уберем пробелы по краям
            if i == 0:
                name_add = list_toins[i]
                print('имя: ', name_add, end=' ')
                continue
            if i == 1:
                if '@' in list_toins[i]:
                    email_add = list_toins[i]
                    print('email: ', email_add, end=' ')
                else:
                    tel_add = list_toins[i]
                    print('tel_add: ', tel_add, end=' ')
                continue
            if i >= 2:
                if email_add == '' and i == 2:
                    if '@' in list_toins[i]:
                        email_add = list_toins[i]
                        print('email: ', email_add, end=' ')
                        continue
                if birdate_add == '' and i < 4:
                    if isdate(list_toins[i]):
                        birdate_add = list_toins[i]
                        print('birdate_add: ', birdate_add, end=' ')
                        continue
                if town_add == '':
                    town_add = list_toins[i]
                    print('town_add: ', town_add)
                    break

        print('Вы добавили: ', '~'.join(list_toins))
        input('Press any key')

# End of add_contact()


def find_contact():
    print('find_contact() is working')
# End of find_contact():


# тело для вывода меню и дальнейшего выбора
def menu():

    # печатает определлные экраны меню
    def printpunkts(screen='main'):
        clearscr()
        if screen == 'main':
            print(Style.YELLOW + 'Address book:'.rjust(30) + Style.RESET)
            print(Style.GREEN + 'make a choice and push ENTER:'.rjust(39) + Style.RESET)
            print('1. Add contact')
            print('2. View contacts')
            print('3. Find (change, delete) contacts')
            print('4. Exit')
            print(Style.BLUE + 'Enter choice: ' + Style.RESET, end='')
    # end of printpunkts():

    print('menu is working')

    while True:
        printpunkts()
        choice = input()
        if choice == '1':
            print(f'Выбор: {choice}')
            add_contact()
        elif choice == '2':
            print(f'Выбор: {choice}')
            print(file_exist)
            view_contacts()
        elif choice == '3':
            print(f'Выбор: {choice}')
            find_contact()
        elif choice == '4':
            print(f'Выбор: {choice}, выхожу, до свидания')
            savedump()
            break
        else:
            print(f'Выбор: {choice}')
            print('Некорректный ввод, повторите')
# End of menu()


# основное тело скрипта
def main():
    os.system('')
    print('main working')
    loaddump()
    menu()
# End of func main():


# start main()
if __name__ == '__main__':
    main()
