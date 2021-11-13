dict1 = {}
dict1 = {i: i ** 2 for i in range(1, 5)}
print(dict1)

# 合并两个列表为一个字典
list1 = ['name', 'age', 'gender']
list2 = ['Tom', 20, 'man']
dict2 = {list1[j]: list2[j] for j in range(len(list1))}
print(dict2)