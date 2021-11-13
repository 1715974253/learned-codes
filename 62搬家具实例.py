class Furniture():
    def __init__(self, name, area):
        # 家具名字
        self.name = name
        # 家具占地面积
        self.area = area


class Home():
    def __init__(self, address, area):
        # 地理位置
        self.address = address
        # 房屋面积
        self.area = area
        # 剩余面积
        self.free_area = area
        self.furniture = []

    def __str__(self):
        return f'房子坐落于{self.address}, 占地面积是{self.area}, 剩余面积{self.free_area},' \
               f'家具有{self.furniture}'

    def add_furniture(self, item):
        '''容纳家具'''
        if self.free_area > item.area:
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print('家具太大,剩余面积不足,无法容纳')

bed = Furniture('双人床', 6)
sofa = Furniture('沙发', 10)
jia1 = Home('北京', 100)
print(jia1)
jia1.add_furniture(bed)
print(jia1)
bell = Furniture('篮球场', 1000)
jia1.add_furniture(bell)
print(jia1)