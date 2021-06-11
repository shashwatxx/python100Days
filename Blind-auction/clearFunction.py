from os import system, name

from time import sleep


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac or linux where os.name == 'posix'
    else:
        _ = system('clear')
