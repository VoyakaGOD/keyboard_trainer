from time import time
from typing import Callable
from charSequence import CharSequence
from console import Console

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

    def enter_char(self, char):
        if not self._sequence.enter(char):
            self._mistakes += 1
            return False
        if self._sequence.is_over():
            return True
        return False

    def remove_char(self):
        self._sequence.remove_last()

    def reset(self):
        self._time = time()
        self._sequence = self._rule()
        self._mistakes = 0

    def get_str_repr(self):
        return self._sequence.get_colored_text() + " | " + str(self.typing_speed) + " chars/min | mistakes[ " + str(self._mistakes) + " ]"

    def run(self):
        is_sequence_over = False
        while True:
            Console.print(self.get_str_repr(), "     ", end="\r")
            key = Console.getch()
            if key == '\n' or key == '\r':
                continue
            if key == '\t':
                self.enter_char(' ')
                self.enter_char(' ')
                self.enter_char(' ')
                is_sequence_over = self.enter_char(' ')
            elif Console.is_esc(key):
                break
            elif Console.is_backspace(key):
                self.remove_char()
            else:
                is_sequence_over = self.enter_char(key)
            if is_sequence_over:
                Console.print(self.get_str_repr(), "     ")
                self.reset()
