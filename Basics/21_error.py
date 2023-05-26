try:
    # print(0 / 0)
    print(no_existo)
except ZeroDivisionError as error:
    print(error)
except NameError as error:
    print(error)


age = 10
try:
    if age < 18:
        raise Exception('Es menor')
except Exception as error:
    print(error)

try:
    assert 1 != 1, 'uno no es igual que uno'
except AssertionError as error:
    print(error)

print('continue')