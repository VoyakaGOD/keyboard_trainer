from trainer import *
from console import Console
from rules import rules
from menu import Menu

menu = Menu(rules)
trainer = Trainer(menu.select())
Console.clear()
Console.print(trainer.sequence.get_text(), end="\r")

while(True):
    trainer.try_to_cover_char(Console.getch())
    Console.print(trainer.sequence.get_text(), "|", trainer.typing_speed, "chars/min", "|", "mistakes[", trainer.mistakes, "]", end="\r")

