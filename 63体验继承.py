# 继承:子类默认继承父类的所有属性和方法
class A(object):
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)


class B(A):
    pass


result = B()
print(result)
print(result.num)
