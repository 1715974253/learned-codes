age = 18
name = 'tom'
weight = 65.5
idcard = 1
print('我的年龄是%d岁' % age)
print(f'我的年龄是{age}岁')
print('我的名字是%s' % name)
print(f'我的名字是{name}')
# %.2f表示小数点后显示的位数
print('我的体重是%.2fkg' % weight)
print(f'我的体重是{weight}kg')
# %04d表示输出的整数显示位数,不足以0补全,超出当前位数则原样输出
print('我的id是%04d' % idcard)
print(f'我的id是{idcard}')
# 多个格式化符号可以一起写
print('我的名字是%s,我的年龄是%d,我的体重是%.2f,我的学号是%06d,我明年%d岁' % (name, age, weight, idcard, age + 1))
