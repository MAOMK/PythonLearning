# file = open('Basics/files/text.txt')
# print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readline())

# for line in file:
#     print(line)

# file.close()

# r+ hace update sobre el archivo pero no lo sobreeescribe,
# w+ reeescribe el documento
with open('Basics/text.txt', 'w+') as file:
    for line in file:
        print(line)
    file.write('\n Yeahh!')