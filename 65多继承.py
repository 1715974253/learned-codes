# 师傅类:属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '古法煎饼果子'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 为了验证多继承,添加School类
class School(object):
    def __init__(self):
        self.kongfu = '黑马煎饼果子'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 定义徒弟类,继承师傅类和学校类
class Practice(School, Master):
    pass


# 用徒弟类创建对象,调用实例属性和方法
daqiu = Practice()
print(daqiu.kongfu)
daqiu.make_cake()
