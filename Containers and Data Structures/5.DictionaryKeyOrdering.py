'''Orderdict stores both a mapping of the keys to their values and a list of keys that is used to preserve the order

works only in Python 3.6+ thanks to PEP 468

Notice how the size of the dictionary is nearly twice as big due to the order storing

'''
from collections import OrderedDict
import sys

attrs = OrderedDict(id="header", style="colour:red")

test_dict = dict(id="header", style="colour:red")

attrs_size = sys.getsizeof(attrs)
test_dict_size = sys.getsizeof(test_dict)

print(f"Size of my_list: {attrs_size} bytes")
print(f"Size of my_list: {test_dict_size} bytes")

# Size of my_list: 424 bytes
# Size of my_list: 232 bytes
