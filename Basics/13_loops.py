# WHILE
number = 0
while number < 10 :
    number += 1
    if number == 5 :
        continue
    if number == 8 :
        break
    print(number)

print('*'*10)


# FOR
for element in range(10):
    print(element)
print('*'*10)
for element in range(1,11):
    print(element)


my_list = ['omar', 'camilo', 'torres']
for i in my_list:
    print(i)


#ANIDATES

matriz = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[0][1])
for element in matriz:
    print(element)
    for item in element:
        print('item => ', item)