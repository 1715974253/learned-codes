name_list = ['tom', '哈利波特', '换一句永恒']


name = input("请输入您想要的注册名:")
if name in name_list:
    print("此用户名已被注册,请重新输入")
else:
    print("您可以注册")