from trainer import *
from console import Console
from rules import rules
from menu import Menu

menu = Menu(rules)
while(True):
    rule = menu.select()
    if rule is None:
        break
    trainer = Trainer(rule)
    Console.clear()
    while(True):
        Console.print(trainer.get_str_repr(), "     ", end="\r")
        key = Console.getch()
        if ord(key) == 27:
            break
        is_sequence_over = trainer.try_to_cover_char(key)
        if is_sequence_over:
            Console.print(trainer.get_str_repr(), "     ")
            trainer.reset()
Console.print("Thanks for playing!")