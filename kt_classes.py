from time import time

AI_NEW_SEQUENCE = 0
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

    def is_correct(self, char):
        return self._chars[self._index] == char
    
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
        if cause == AI_NEW_SEQUENCE:
            game.sequence = CharSequence("123456789")
        elif cause == AI_HIT:
            game.hurt(game.book.get_info()["damage"])
            game.cover_char()
        elif cause == AI_MISS:
            game.heal(1)
        elif cause == AI_TIME_IS_OVER:
            game.heal(2)

class Game:
    def __init__(self, book, enemy):
        self.book = book
        self.enemy = enemy
        self.time = time()
        self.max_hp = enemy.get_info()["hp"]
        self.hp = self.max_hp
        self.sequence : CharSequence = None
        enemy.AI(self, AI_NEW_SEQUENCE)

    def hurt(self, value):
        self.hp = max(0, self.hp - value)

    def heal(self, value):
        self.hp = min(self.max_hp, self.hp + value)

    def cover_char(self):
        self.sequence.cover("#")
        if self.sequence.is_over():
            self.enemy.AI(self, AI_NEW_SEQUENCE)
