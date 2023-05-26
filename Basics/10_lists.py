# LIST are like ARRAYS

# CREATE
numbers = [1, 2, 3, 4, 5] 
tasks = ['make dishes', 'play videogames', 'study python']

numbers_ite = []
for element in range(1,11):
    numbers_ite.append(element)

number_list_comprehension = [element * 2 for element in range(1, 11) if element % 2 == 0]
print(numbers_ite)
print(number_list_comprehension)


text = 'La buena!'
unique = {character: character.upper() for character in text if character in 'aeiou'}
print(unique)

# READ
print(type(numbers))
print(numbers[0])
print(numbers[:3])
print(6 in numbers)
print(numbers.index(3))
print(numbers.reverse())

# UPDATE
numbers[1] = 'dos'
numbers[1] = 'two'
numbers.append(6)
numbers.insert(2, 'half')
newlist = numbers + tasks

#DELETE
newlist.remove('half')
newlist.pop() # Remove last element of the list
newlist.pop(1)  # Remove item i of the list


# numbers.sort() # error mised data str and number
