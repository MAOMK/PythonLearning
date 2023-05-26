# CREATE
def suma(a,b):
    print(a+b)

def diff(a,b):
    return a - b


suma_lambda = lambda a, b: a + b

result = 0
for x in range(1,10):
    result += x
print(result) # too large and no reutilizable

def sum_in_a_range(min,max):
    new_result = 0
    for x in range(min, max):
        new_result += x
    return new_result

def volume(length = 1, width = 1, depth = 1):
    return length * width * depth, "hola", "yaa"

full_name = lambda first_name, last_name: f"full name is {first_name} {last_name}"

# READ
suma(10,2)
diff(10,2)
print(diff(10,2))
sum_in_a_range(2,8)
print(sum_in_a_range(2,8))

print(volume())
print(volume(depth = 10))
vol, text_a, text_b = volume(width = 5)

print(vol)
print(text_a)
print(text_b)

print(suma_lambda(10,4))
print(full_name('camilo','torres'))
