# break的使用
i = 0
while i < 5:
    if i == 3:
        print("吃饱了")
        break
    print(f'吃了第{i + 1}个苹果')
    i += 1
# # continue的使用
# j = 0
# while j < 5:
#     if j == 2:
#         print("吃出了虫子,没吃饱,下一个")
#         j += 1
#         continue
#     print(f'吃了第{j + 1}个苹果')
#     j += 1
