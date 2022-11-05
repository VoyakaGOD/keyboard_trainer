from kt_classes import *
from console import Console

class ClassicBook(Book):
    def get_info():
        return {"name": "classic", "damage": 1, "affect_chance": 0 }

class Fox(Enemy):
    def get_info():
        return {"name": "Fox", "hp": 100, "time_limit": -1 }

game = Game(ClassicBook, Fox)

while(game.hp > 0):
    Console.print("\r", game.enemy.get_info()["name"], "[ ", game.hp, " / ", game.max_hp, " ]:", sep="", end="")
    Console.print(game.sequence.get_text())
    char = Console.getch()
    if game.enemy.get_info()["time_limit"] > 0 and time() - game.time > game.enemy.get_info()["time_limit"]:
        game.enemy.AI(game, AI_TIME_IS_OVER)
    elif game.sequence.is_correct(char):
        game.enemy.AI(game, AI_HIT)
    else:
        game.enemy.AI(game, AI_MISS)
