# 师傅类:属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '古法煎饼果子'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 为了验证多继承,添加School类
class School(Master):
    def __init__(self):
        self.kongfu = '黑马煎饼果子'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

        super().__init__()
        super().make_cake()


# 定义徒弟类,继承师傅类和学校类
class Practice(School):
    def __init__(self):
        self.kongfu = '独创煎饼果子技术'

    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_School_cake(self):
        School.__init__(self)
        School.make_cake(self)

    def make_old_cake(self):
        super().__init__()
        super().make_cake()


daqiu = Practice()
daqiu.make_old_cake()
