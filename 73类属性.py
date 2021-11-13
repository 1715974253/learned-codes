class Dog(object):
    tooth = 10


wangcai = Dog()
xiaohei = Dog()

print(Dog.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)

# 修改类属性
Dog.tooth = 12

print(Dog.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)
# 不能通过对象修改属性,如果这样操作,实则是创建了一个实例对象
wangcai.tooth = 200

print(Dog.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)
