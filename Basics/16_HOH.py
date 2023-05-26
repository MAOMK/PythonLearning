def increment(x):
    return x + 1

increment_lambda = lambda x: x + 1

def high_order_function(x, func):
    return x + func(x)

high_order_lambda = lambda x, func: x + func(x)

result = high_order_function(2, increment)
result_lambda = high_order_lambda(2, increment_lambda)
print(result)
print(result_lambda)
other_result = high_order_lambda(2, lambda x: x + 1)
print(other_result)