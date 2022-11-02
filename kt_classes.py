from time import time

AI_GAME_STARTED = 0
AI_TIME_IS_OVER = 1
AI_HIT = 2
AI_MISS = 3

class CharSequence:
    def __init__(self, chars):
        if type(chars) == str:
            chars = list(chars)
        self._chars = chars
        self._index = 0
    
    def get_text(self):
        return "".join(self._chars)

    def get_len(self):
        return len(self._chars)

    def is_over(self):
        return self._index >= len(self._chars)
    
    def cover(self, char):
        if self.is_over():
            return
        self._chars[self._index] = char
        self._index += 1

class Book: 
    def get_info():
        return {"name": "None", "damage": 1, "affect_chance": 0 }

    def affect(game):
        return

class Enemy:
    def get_info():
        return {"name": "None", "hp": 1, "time_limit": -1 }

    def AI(game, cause):
        return

class Game:
    def __init__(self, book, enemy):
        self.book = book
        self.enemy = enemy
        self.time = time()
        self.max_hp = enemy.get_info()["hp"]
        self.hp = self.max_hp
        self.sequence = None
        enemy.AI(self, AI_GAME_STARTED)