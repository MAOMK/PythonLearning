# MAP: hace transformaciones a una lista dada de elementos
my_list = [1, 2, 3, 4]
my_list_v2 = []
for i in my_list:
    my_list_v2.append(i * 2)
print(my_list_v2)

#using map
my_list_v3 = list(map(lambda i: i * 2, my_list))
print(my_list_v3)


numbers1 = [1, 2, 3, 4]
numbers2 = [9, 8, 7, 6]
print(numbers1)
print(numbers2)


result = list(map(lambda x, y: x + y, numbers1, numbers2))
print(result)

###
items = [
    {
        'product': 'camisa',
        'price': 100
    },
    {
        'product': 'pantalon',
        'price': 300
    },
    {
        'product': 'medias',
        'price': 150
    }
]

prices = list(map(lambda item: item['price'], items))
print(prices)

def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * .19
    return item

new_items = list(map(add_taxes, items))
print(new_items)
print(items) # Is modified : ERROR!!!! take care!!! line : item['taxes'] = item['price'] * .19

