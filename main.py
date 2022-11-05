from trainer import *
from console import Console
from random import choice

def digitsRule():
    return CharSequence([choice("1") for x in range(25)])

trainer = Trainer(digitsRule)
Console.clear()
Console.print(trainer.sequence.get_text(), end="\r")

while(True):
    trainer.try_to_cover_char(Console.getch())
    Console.print(trainer.sequence.get_text(), "|", trainer.typing_speed, "chars/min", "|", "mistakes[", trainer.mistakes, "]", end="\r")

