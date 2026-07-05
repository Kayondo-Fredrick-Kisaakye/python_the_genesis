#when u're writing long nums, u can group digits using underscores to make large numbers readable
"""
>>> universe_age = 14_000_000_000
>>> print(universe_age)
14000000000
"""
#PY will only print digits,
#PY ignores underscores when storing these kinds of values, even when u dont divide it in threes, it'll still be unaffected
#to PY, 1000 same as 1_000 same as 10_00 >>> works for both INTEGERS and FLOATS