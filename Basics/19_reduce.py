# Reduce : toma una lista y la reduce a un solo valor
import functools

numbers = [1, 2, 3, 4]

def accum (counter, item):
    return counter + item


result = functools.reduce(lambda counter, item: counter + item, numbers)

print(result)