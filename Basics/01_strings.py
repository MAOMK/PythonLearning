## CREATE

first_name = 'Camilo'
last_name = 'Torres'

text_test = 'Anita lava la tina'
full_name = first_name + last_name # Create a str using concatenation
input_name = input('cuál es tu nombre') # Create a str using an input

## READ

size = len(text_test) # Length of 'text_test'
print(full_name) # Print a str in console
print('Javascript' in text_test) # Search for Javascript in 'text_test'
print(text_test.count('A')) # How many times appears 'A' in 'text_test'
print(text_test.startswith('Ani')) # Validate if 'text_test' starts with 'Ani'
print(text_test.endswith('Ani')) # Validate if 'text_test' ends with 'Ani'
print(text_test[2]) # Shows the letter that is on key = 2
print(text_test[size - 1]) # Shows 'text_test' from right to left
print(text_test[-1]) # Shows the last index of 'text_test'

full_name = first_name + ' ' + last_name # Concatenating 2 str
template_one = f"Hola mi nombre es {first_name} y mi apellido es {last_name}" # Using format
template_two = "Hola mi nombre es {} y mi apellido es {}".format(first_name, last_name) # Using format

## Update

print(template_one.upper())
print(template_one.lower())
print(template_one.capitalize())
print(template_one.title())
print(template_one.swapcase())
print(template_one.replace('Anita', 'Carlos'))
print(template_one[0:9])
print(template_one[:9])
print(template_one[::-1])