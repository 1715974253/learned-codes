# 定义类,定义静态方法
class Dog(object):
    @staticmethod
    def info_print():
        print('这是一个类')


# 创建对象
wangcai = Dog()
# 调用静态方法,类和对象
wangcai.info_print()
Dog.info_print()
