x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x == y)

# Comparing using strings
y_str = format(y, ".2g")
print('str =>', y_str)
print( y_str == str(x))

#Comparing using Math
tolerance = 0.00001
print(abs(x - y) < tolerance)