import re


def isdate(dated):

    patt = re.compile(r'\d\d[-.,/*_]\d\d[-.,/*_]\d{2,4}')
    if patt.fullmatch(dated):
        print(f'{dated} ')


def istel(teled):
    patt = re.compile(r'[+]?\d+')
    if patt.fullmatch(teled):
        print(f'{teled} ')


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