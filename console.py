from os import system
from sys import platform

class Console:
    def print(*args, **kwargs):
        print(*args, **kwargs)

    def is_esc(char):
        return ord(char) == 27

    def is_backspace(char):
        return char == '\b'

if platform == "win32":
    from msvcrt import getwch
    Console.getch = getwch
    Console.clear = lambda: system("cls")
else:
    import sys, tty, termios
    def unix_getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    Console.getch = unix_getch
    Console.clear = lambda: system("clear")