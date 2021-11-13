# 一个类可以创建多个对象,多个对象都调用函数时,self地址不相同
class Washer():
    def wash(self):
        print('洗衣服')
        print(self)


haier1 = Washer()
haier1.wash()
haier2 = Washer()
haier2.wash()
