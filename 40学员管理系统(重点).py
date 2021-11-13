def info_print():
    print('请选择功能---------')
    print('添加学员')
    print('删除学员')
    print('修改学员')
    print('查询学员')
    print('显示所有学院')
    print('退出系统')
    print('-' * 20)


info = []


def info_add():
    '''添加学员信息函数'''
    # 输入信息
    new_name = input("请输入姓名:")
    new_id = input('请输入学号:')
    new_tel = input("请输入电话号码:")
    # 全局变量info
    global info
    # 判断姓名是否重复
    for i in info:
        if new_name == i['name']:
            print('重复了,重新输入')
            return
    # 字典和列表追加数据额
    info_dict = {}
    info_dict['name'] = new_name
    info_dict['id'] = new_id
    info_dict['tel'] = new_tel
    info.append(info_dict)
    print(info)


def info_del():
    '''删除学员函数'''
    # 输入删除学员的用户名
    del_name = input('请输入需要删除的姓名:')

    global info
    # 判断学员是否存在.存在则删除,否则报错
    for i in info:
        if i['name'] == del_name:
            info.remove(i)
            break
    else:
        print('该学员不存在')
    print(info)


def info_modify():
    '''修改函数'''

    modify_name = input("请输入需要修改的学员姓名:")
    global info
    for i in info:
        if i['name'] == modify_name:
            i['tel'] = input('请输入新的手机号:')
            break
    else:
        print('学员不存在')
    print(info)


def search_info():
    '''查询学员'''
    search_name = input('请输入查询学员的姓名:')

    global info
    for i in info:
        if i['name'] == search_name:
            print('查找的学员信息如下------')
            print(f"该学员的姓名是{i['name']},学号是{i['id']},电话号码是{i['tel']}")
            break
    else:
        print('该学员不存在')


def print_all():
    '''显示所有学员的信息'''
    print('学号\t姓名\t电话号码')
    for i in info:
        print(f"{i['id']}\t{i['name']}\t{i['tel']}")


while True:
    info_print()
    user_num = int(input('请输入功能序号:'))
    if user_num == 1:
        info_add()
    elif user_num == 2:
        info_del()
    elif user_num == 3:
        info_modify()
    elif user_num == 4:
        search_info()
    elif user_num == 5:
        print_all()
    elif user_num == 6:
        exit_flag = input('确定要退出吗.yes 或 no')
        if exit_flag == 'yes':
            break
    else:
        print('请重新输入')
