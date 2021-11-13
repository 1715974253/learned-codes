# 求绝对值
result1 = abs(-20)
print(result1)
# 求四舍五入
result2 = round(1.65331)
print(result2)


def sum_num(a, b, f):
    return f(a) + f(b)


result3 = sum_num(-2, -5, abs)
print(result3)
