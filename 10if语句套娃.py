money = int(input("请输入钱:"))
seat = int(input("请输入座位数:"))
if money==1:
    print('可以上车')
    if seat ==1:
        print(f'车上有空座')
    elif seat==0:
        print("车上无座位")
elif money==0:
    print("没钱上不了车")
