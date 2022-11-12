from trainer import *
from rules import rules
from menu import Menu

def main():
    menu = Menu(rules)
    while True:
        rule = menu.select()
        if rule is None:
            break
        trainer = Trainer(rule)
        Console.clear()
        trainer.run()
    Console.print("Thanks for playing!")

if __name__ == "__main__":
    main()