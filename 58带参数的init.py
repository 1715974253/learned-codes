class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_info(self):
        print(f'洗衣机的宽度是{self.width}')
        print(f'洗衣机的高度是{self.height}')

haier1 = Washer(10, 20)
haier1.print_info()

haier2 = Washer(30, 50)
haier2.print_info()