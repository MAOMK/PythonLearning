import sys

print(sys.path)

import re # para expresiones regulares
text = 'mi número de telefono es 311 123 1212, el código del pais es 57, mi número de la suerte es 3'
result = re.findall('[0-9]+', text)
print(result)


import time
timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(timestamp)
print(result)

import collections
numbers = [1, 1, 2, 1 , 2, 3, 4, 5, 5, 5, 6, 6, 6]
counter_item = collections.Counter(numbers)
print(counter_item)