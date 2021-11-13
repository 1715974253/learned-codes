# 自定义异常类,继承Exception
class ShortInputError(Exception):
    def __init__(self, length, min_length):
        self.length = length
        self.min_length = min_length

    # 设置抛出异常的描述信息
    def __str__(self):
        return f'您输入的长度是{self.length}, 所需最小长度是{self.min_length}'

# 定义输入函数
def main():
    try:
        con = input('请输入密码:')
        if len(con) < 3:
            raise ShortInputError(len(con), 3)
    except Exception as result:
        print(result)
    # 没有异常时执行的代码
    else:
        print('密码输入完成')

# 调用函数
main()

