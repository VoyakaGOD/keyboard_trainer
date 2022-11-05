from time import time
from typing import Callable
from charSequence import CharSequence

class Trainer:
    def __init__(self, rule : Callable[[], CharSequence]):
        self._rule = rule
        self._time = time()
        self._sequence = rule()
        self._mistakes = 0

    @property
    def sequence(self):
        return self._sequence

    @property
    def mistakes(self):
        return self._mistakes

    @property
    def typing_speed(self):
        try:
            return int(60 * self._sequence.index / (time() - self._time))
        except:
            return 0

    def try_to_cover_char(self, char):
        if not self._sequence.is_correct(char):
            self._mistakes += 1
            return
        self._sequence.cover("#")
        if self._sequence.is_over():
            self._time = time()
            self._sequence = self._rule()
            self._mistakes = 0