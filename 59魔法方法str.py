class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height
# print输出对象时,默认打印对象的内存地址,如果类定义了str方法,那么就会打印这个方法中return的数据
    def __str__(self):
        return '这是海尔洗衣机的说明书'

haier1 = Washer(10, 20)
print(haier1)
print()