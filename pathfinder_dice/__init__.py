from .core import Dice

def roll(rule):
    return Dice(rule).roll()
