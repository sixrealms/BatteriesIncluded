class Bunch(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # calls the constructor of the base class (dict) to initialize the dictionary
        self.__dict__ = self  # the instance itself will be used for attribute storage.


# It provides a way to combine the flexibility of dictionaries with the convenience of object-like attribute access.

bt = Bunch(a=7)
print(bt.a)
print(bt['a'])
