import math
from math import *  # noQA
# ^ for Dice._eval
from random import randint
import re

REX_DICE = re.compile(r'\d*d\d+')
REX_MULT = re.compile(r'(?:x\d+)+')
REX_REPL = re.compile(r'x(\d)+')

REX_MATH = re.compile(
    '|'.join(
        # oprators, digits
        ['-', r'\+', '/', r'\\', r'\*', r'\^', r'\*\*', r'\(', r'\)', r'\d+']
        + ['min', 'max']
        # functions of math module (ex. __xxx__)
        + [f for f in dir(math) if f[:2] != '__']
    )
)


class Dice(object):

    def __init__(self, rule):
        self.rule = self._prepare_rule(rule)

    @staticmethod
    def _prepare_rule(rule):
        # remove spaces
        rule = ''.join(rule.split())
        # to lowercase
        rule = rule.lower()
        # replace percent dice
        rule = rule.replace('d%', 'd100')
        return rule

    @staticmethod
    def _roll_dice(dice):
        cnt, _sep, mx = dice.rpartition('d')
        cnt = int(cnt) if cnt else 1
        mx = int(mx)
        return sum(randint(1, mx) for i in range(cnt))

    @staticmethod
    def _reduce_mult(mult):
        mult = 1 + sum(float(val) - 1 for val in mult.split('x') if val)
        return 'x{}'.format(mult)

    def _get_expr(self, rule=None):
        if not rule:
            rule = self.rule
        # roll all dices
        for dice in REX_DICE.findall(rule):
            rule = rule.replace(dice, str(self._roll_dice(dice)), 1)
        # replace multipliers combinations by pathfinder's rule:
        # x2x2x3 == x(2 + (2-1) + (3-1)) == x5
        for mult in REX_MULT.findall(rule):
            rule = rule.replace(mult, self._reduce_mult(mult), 1)
        return rule

    def _validate(self, expr):
        if len(expr) > 140:
            return False
        return REX_MATH.match(expr)

    def _eval(self, expr):
        expr = REX_REPL.sub(r'*\1', expr)
        return eval(expr)

    def _round(self, value):
        return int(value)

    def roll(self):
        expr = self._get_expr()
        if self._validate(expr):
            result = self._eval(expr)
        else:
            raise ArithmeticError('Invalid expression: {}'.format(expr))
        return self._round(result)
