# Are like Objects

#CREATE
my_dict = {
    'name' : 'Camilo',
    'age'  : 28,
    'isAdult' : True,
    'langs' : ['python', 'JS']
}

dict_ite = {}
for i in range(1, 5):
    dict_ite[i] = i * 2
print(dict_ite)

dict_comprehension = {i: i * 3 for i in range(1,5)}
print(dict_comprehension)

names = ['Omar', 'Camilo', 'Torres']
ages = [12,14,16]
# zip: unir dos listas
new_list = list(zip(names,ages))
new_dict = {name : age for [name, age] in zip(names, ages)}
print(new_list)
print(new_dict)
print('*'*20)

dict_comprehension_par = {i: i for i in range(1,11) if i % 2 == 0}
print(dict_comprehension_par)


# READ
print(my_dict)
print(len(my_dict))
print(my_dict['isAdult'])
print(my_dict['age'])
print(my_dict.get('cel')) # can managge the error : none
print('tel' in my_dict)
print('name' in my_dict)
print('items', my_dict.items())
print('keys', my_dict.keys())
print('values', my_dict.values())

# UPDATE
my_dict['age'] = 29
my_dict['age'] -= 1
my_dict['langs'].append('NODE')
print(my_dict)

# DELETE
del my_dict['isAdult']
my_dict.pop('age')
print(my_dict)