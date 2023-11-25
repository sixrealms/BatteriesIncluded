from collections import ChainMap

population = dict(italy=60, japan=127, uk=65)
changes = dict()
editablepop = ChainMap(changes, population)  # first dict is updated

print(editablepop['japan'])
editablepop['japan'] += 1
print(editablepop['japan'])
print(population['japan'])  # original is unchanged as long as type is immutable

# we can use changes to see what was updated

print(changes.keys())

# which were not updated
print(population.keys() - changes.keys())
