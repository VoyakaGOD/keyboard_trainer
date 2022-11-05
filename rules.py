from charSequence import CharSequence
from string import ascii_letters
from random import choice

rules = {}

def kt_rule(name):
    def decorator(function):
        rules[name] = function
        return function
    return decorator

@kt_rule("digits")
def digitsRule():
    return CharSequence([choice("0123456789") for x in range(25)])

@kt_rule("letters")
def lettersRule():
    return CharSequence([choice(ascii_letters) for x in range(25)])

@kt_rule("symbols")
def symbolsRule():
    return CharSequence([choice("~!@#$%^&*()_+-=,./|[]{}?';:`") for x in range(25)])