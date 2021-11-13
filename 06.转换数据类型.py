# int,float,str等可以转换数据类型
# 1.float--将数据转换成浮点型
num1 = 1
str1 = '10'
print(type(float(num1)))
print(type(float(str1)))
print(float(num1))
print(float(str1))
# 2.str--将数据转换成字符串型
print((type(str(num1))))
print(str(num1))
# tuple--将一个序列转换成元组
list1 = [10, 20, 30]
print(type(tuple(list1)))
print(tuple(list1))
# list--将一个序列转换成列表
t1 = (100, 200, 300)
print(type(list(t1)))
print(list(t1))
# eval()-- 计算在字符串中有效的Python表达式,并返回一个对象
str2 = '1'
str3 = '1.1'
str4 = '(1000,2000,3000)'
str5 = '[1000,2000,3000]'
print(eval(str2))
print(eval(str3))
print(eval(str4))
print(eval(str5))
