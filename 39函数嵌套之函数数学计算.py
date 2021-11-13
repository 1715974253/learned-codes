# 求三个数的平均值
def sum_num(a, b, c):
    return a + b + c


def average_sum(a, b, c):
    sum1 = sum_num(a, b, c)
    return sum1 / 3


result = average_sum(1, 2, 3)
print(result)
