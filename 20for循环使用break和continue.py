str = 'itheima'
# 使用break
for i in str:
    if i == 'e':
        print("不打印e")
        break
    print(i)

# 使用continue
for j in str:
    if j == 'e':
        print("不打印e")
        continue
    print(j)