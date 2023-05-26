# Tuples are inmutables

# CREATE
numbers = (1, 2, 3, 4, 5)
strs = ('omar','camilo', 'MAOMK')
mixed = ('omar', 2, 4, 1, False)

# READ
print(type(numbers))
print(numbers[0])
print(numbers[-1])
print(strs.index('camilo'))

# UPDATE
my_lists = list(strs)
my_lists[2] = 'torres'

my_tuple = tuple(my_lists)
print(my_tuple)

# DELETE