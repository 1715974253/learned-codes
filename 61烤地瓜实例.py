class SweetPotato():
    def __init__(self):
        '''初始状态'''
        self.cook_time = 0
        self.cook_state = '生的'
        self.cook_condiments = []

    def cook(self, time):
        '''烤地瓜的方法'''
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_state = '半生不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_state = "熟了"
        elif self.cook_time > 8:
            self.cook_state = '糊了'

    def add_condimens(self, condiment):
        self.cook_condiments.append(condiment)

    def __str__(self):
        return f'这个地瓜烤了{self.cook_time}分钟,状态是{self.cook_state},' \
               f'调料有{self.cook_condiments}'


digua1 = SweetPotato()
print(digua1)
digua1.cook(2)
digua1.add_condimens("胡椒粉")
print(digua1)
digua1.cook(3)
digua1.add_condimens("孜然")
print(digua1)
