from os import system
from sys import platform

class Console:
    def print(*args, **kwargs):
        print(*args, **kwargs)

    def is_esc(char):
        return ord(char) == 27

if platform == "win32":
    from msvcrt import getwch
    Console.getch = getwch
    Console.clear = lambda: system("cls")
    Console.is_backspace = lambda char: char == '\b'
else:
    import sys, tty, termios
    def unix_getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            if ord(ch) == 27:
                ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    Console.getch = unix_getch
    Console.clear = lambda: system("clear")
    Console.is_backspace = lambda char: ord(char) == 127
