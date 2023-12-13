'''Reversing a dictionary in this way only works if all values are hashable. If your values are not hashable,
you might need to consider a different approach.

NOT HASHABLE: Lists, Dicts, Sets, Class Instances


'''
my_dict = dict(a=1, b=2, c=3)
reversed_dict = {v: k for k, v in my_dict.items()}

print(reversed_dict.keys())
print(reversed_dict.values())

# Multiple values per key, use a list

rd = {1: ['one', 'uno', 'un'],
      2: ['two', 'due', 'deux'],
      3: ['three', 'tre', 'trois']
      }

rd[2].append('dos')

new_list = ['four']
rd[4] = new_list

