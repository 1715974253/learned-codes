age = int(input("请输入您的年龄:"))
if age < 18:
    print(f'您未成年,年龄是{age},不能工作')
elif 60 > age >= 18:
    print(f'您的年龄是{age},您已成年,可以合法工作')
else:
    print(f'您已退休')
