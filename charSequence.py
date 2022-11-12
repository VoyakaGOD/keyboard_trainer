GOOD_SEQUENCE_COLOR = '\033[92m'
BAD_SEQUENCE_COLOR = '\033[91m'
NORMAL_SEQUENCE_COLOR = '\33[0m'
WRONG_SEQUENCE_LIMIT = 20

class CharSequence:
    def __init__(self, target : list[str] | str):
        if type(target) == list:
            target = "".join(target)
        if type(target) is not str:
            raise TypeError
        self._target = target
        self._wrong = []
        self._index = 0

    @property
    def index(self):
        return self._index
    
    def get_colored_text(self):
        return "".join([GOOD_SEQUENCE_COLOR, self._target[:self._index], 
        BAD_SEQUENCE_COLOR, "".join(self._wrong), 
        NORMAL_SEQUENCE_COLOR, self._target[(self._index + len(self._wrong)):]])

    def get_len(self):
        return len(self._target)

    def is_over(self):
        return self._index >= len(self._target)
    
    def enter(self, char : str):
        if self.is_over():
            return True
        if self._target[self._index] == char and len(self._wrong) == 0:
            self._index += 1
            return True
        else:
            if len(self._wrong) < WRONG_SEQUENCE_LIMIT:
                self._wrong += [char if char != ' ' else '_']
            return False

    def remove_last(self):
        if len(self._wrong) > 0:
            self._wrong.pop()
        elif self._index > 0:
            self._index -= 1
        return True
        