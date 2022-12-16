GOOD_SEQUENCE_COLOR = '\033[92m'
BAD_SEQUENCE_COLOR = '\033[91m'
NORMAL_SEQUENCE_COLOR = '\33[0m'
SPACE_REPLACEMENT = '▫'

class CharSequence:
    def __init__(self, target : list[str] | str):
        if type(target) == list:
            target = "".join(target)
        if type(target) is not str:
            raise TypeError
        self._target = target
        self._current = []
        self._index = 0

    @property
    def index(self):
        return self._index
    
    def get_colored_text(self):
        text = []
        text += GOOD_SEQUENCE_COLOR
        text += self._current[:self._index]
        text += BAD_SEQUENCE_COLOR
        text += self._current[self._index:]
        text += NORMAL_SEQUENCE_COLOR
        text += self._target[len(self._current):]
        return "".join(text)

    def get_len(self):
        return len(self._target)

    def is_over(self):
        return self._index >= len(self._target)
    
    def enter(self, char : str):
        if self.is_over():
            return True
        if len(self._current) >= len(self._target):
            return False
        self._current.append(char if char != ' ' else SPACE_REPLACEMENT)
        if len(self._current) - 1 == self._index and self._target[self._index] == char:
            self._index += 1
            return True
        return False
        

    def remove_last(self):
        if len(self._current) > 0:
            self._current.pop()
        elif self._index > len(self._current):
            self._index = len(self._current)
        return True
        