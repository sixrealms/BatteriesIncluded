'''Create a class that leverages dictionaries to contain any attribute we want and allow it access to both as a
dictionary and through properties'''


class Bunch(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getattr__(self, item):
        try:
            return self.__dict__[item]
        except KeyError:
            raise AttributeError(item)

    def __setattr__(self, item, value):
        self.__dict__[item] = value

    def items(self):
        return self.__dict__.items()


bunch = Bunch(a=1, b=[10, 11])
bunch.c = 100

print(bunch.items())
