class CharSequence:
    def __init__(self, chars : list):
        if type(chars) == str:
            chars = list(chars)
        if type(chars) is not list:
            raise TypeError
        self._chars = chars
        self._index = 0

    @property
    def index(self):
        return self._index
    
    def get_text(self):
        return "".join(self._chars)

    def get_len(self):
        return len(self._chars)

    def is_over(self):
        return self._index >= len(self._chars)

    def is_correct(self, char):
        return self._chars[self._index] == char
    
    def cover(self, char : str):
        if self.is_over():
            return
        self._chars[self._index] = char
        self._index += 1