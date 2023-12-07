import re


def isdate(dated):

    patt = re.compile(r'\d\d\.\d\d\.\d\d')
    if not patt.match(dated):
        print(f'{dated} ')


isdate('sdttds.fd.ff')
isdate('ss.ff.ff')
isdate('22.22.22')
isdate('22,22.22')
