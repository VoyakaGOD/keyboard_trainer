from msvcrt import getwch, kbhit
from os import system

class Console:
    def print(*args, **kwargs):
        print(*args, **kwargs)

    def is_key_pressed():
        return kbhit()

    def getch():
        return getwch()

    def clear():
        system("cls")