class Washer():
    def wash(self):
        print('洗衣服')

    def print_info(self):
        # self.属性名
        print(f'洗衣机的宽度是{self.weight}')
        print(f'洗衣机的高度是{self.height}')


haier1 = Washer()

# 添加属性
haier1.weight = 400
haier1.height = 500

haier1.print_info()

