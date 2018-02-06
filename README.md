A library for evaluating dice notation for Pathfinder RPG.

## Usage

Just roll!

```python
>>> from pathfinder_dice import roll
>>> roll("max(2, 4) + 2d6x2x4")
54
```

Result of multiplying in Pathfinder have some specific:

```python
>>> roll('1x2x3')
4
```

For right multiplying you can use `*`:

```python
>>> roll('1*2*3')
6
```

You can use digits, `min` and `max` functions, all functions from `math` module, braces, arithmetic operators. Otherwise `ArithmeticError` will be raised.

```
>>> roll('print(2)')
ArithmeticError: Invalid expression: print(2)
```

