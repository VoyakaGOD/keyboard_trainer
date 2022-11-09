from charSequence import CharSequence
from string import ascii_letters
from random import choice, randrange

rules = {}

SEQUENCE_LENGTH = 50
MIN_TEXT_LINE_LENGTH = 20

def kt_rule(name):
    def decorator(function):
        rules[name] = function
        return function
    return decorator

def load(source, separate=False):
    with open(source) as file:
        text = file.read()
        if separate:
            text = text.split("\n")
        return text

@kt_rule("digits")
def digitsRule():
    return CharSequence([choice("0123456789") for x in range(SEQUENCE_LENGTH)])

@kt_rule("letters")
def lettersRule():
    return CharSequence([choice(ascii_letters) for x in range(SEQUENCE_LENGTH)])

@kt_rule("symbols")
def symbolsRule():
    return CharSequence([choice("~!@#$%^&*()_+-=,./|[]{}?';:`") for x in range(SEQUENCE_LENGTH)])

def wordsRule(words):
    text = choice(words)
    while True:
        word = choice(words)
        if len(text) + len(word) > SEQUENCE_LENGTH - 2:
            break
        text += ", " + word
    return CharSequence(text)

TREES = load("content/trees.txt", True)

@kt_rule("trees")
def treesRule():
    return wordsRule(TREES)

ANIMALS = load("content/animals.txt", True)
    
@kt_rule("animals")
def animalsRule():
    return wordsRule(ANIMALS)

class TextConainer:
    def __init__(self, source):
        self._text = load(source, True)
        self._line = randrange(0, len(self._text))

    def get_line(self):
        while True:
            self._line = (self._line + 1) % len(self._text)
            if len(self._text[self._line]) >= MIN_TEXT_LINE_LENGTH:
                break
        return CharSequence(self._text[self._line])

FAUST_TEXT = TextConainer("content/Faust.txt")
    
@kt_rule("Faust")
def FaustRule():
    return FAUST_TEXT.get_line()

