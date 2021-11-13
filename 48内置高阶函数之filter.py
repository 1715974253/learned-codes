list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func(x):
    return x % 2 == 0

result1 = filter(func, list1)
print(result1)
print(list(result1))