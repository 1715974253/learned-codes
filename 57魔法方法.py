class Washer():
    def __init__(self):
        self.width = 400
        self.height = 500

    def print_info(self):
        print(f'洗衣机的高度是{self.height}')
        print(f'洗衣机的宽度是{self.width}')

haier1 = Washer()

haier1.print_info()