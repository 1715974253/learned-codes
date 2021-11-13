# 算数运算符
a = 1
b = 3
c = 5
print(a)
print(b * c)
print(b / c)
print(c % b)
print(b ** 2)
# 赋值运算符
# 多个变量赋值
num1, float1, str1 = 10, 1.164, '换一句永恒'
print(num1, float1, str1)
# 多个变量赋相同值
num2 = num3 = num4 = 1.6061
print(num2, num3, num4)

# 复合赋值运算符
a = 10
a += a
a *= 2
print(a)

# 比较运算符
h1 = 10
h2 = 5
print(h1 > h2)
print(h1 != h2)

# 逻辑运算符
print(h1 > h2 and h1 != h2)
print(h1 > h2 and h1 == h2)
print(h1 > h2 or h1 == h2)
print(not h1 > h2)
