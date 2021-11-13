counts = {'MBP': 268, 'HP': 128, 'Dell': 201, 'Lenovo': 199, 'acer': 99}
# 需求:提取电脑数大于100的键值对
dict1 = {key: value for key, value in counts.items() if value >= 200}
print(dict1)
