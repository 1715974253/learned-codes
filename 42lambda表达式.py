def print_num():
    return 100


result1 = print_num()
print(result1)

# lambda表达式
result2 = lambda: 200
print(result2)  # lambda表达式内存地址
# 返回值需要调用函数
print(result2())
