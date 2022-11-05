from console import Console

class Menu:
    def __init__(self, items):
        if type(items) is not dict:
            raise TypeError
        if len(items) == 0:
            raise BufferError
        self._items = items
        self._index = 0

    def draw(self):
        for i, key in enumerate(self._items.keys()):
            if i == self._index:
                Console.print(">>>", end="")
            Console.print(key)

    def select(self):
        while(True):
            Console.clear()
            Console.print("w - upper, s - lower, space - select")
            self.draw()
            char = Console.getch()
            if char == "w":
                self._index = (len(self._items) + self._index - 1) % len(self._items)
            elif char == "s":
                self._index = (self._index + 1) % len(self._items)
            elif char == " ":
                return self._items[list(self._items.keys())[self._index]]
    