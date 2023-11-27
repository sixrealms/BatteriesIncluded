'''Python functions accept arguments from a dictionary through unpacking using **
For a given function, we want to pass the arguments from 2 dicts, d1 and d2

'''

from collections import ChainMap

d1 = dict(a=5, b=6)
d2 = dict(b=7, c=8, d=9)


def f(a, b, c, d):
    return a, b, c, d


print(f(**ChainMap(d1, d2)))  # here b=6
print(f(**{**d1, **d2}))  # here b=7
# print(f(**d1, **d2))  # Python 3.5+ but chokes on duplicate arguments
