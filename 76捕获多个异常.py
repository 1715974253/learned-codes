# 捕获异常
try:
    print(1 / 0)
except (NameError, ZeroDivisionError):
    print('有错误')
# 捕获异常描述信息
try:
    print(1 / 0)
except (NameError, ZeroDivisionError) as result:
    print(result)
