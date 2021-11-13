# 需求1:尝试只读打开text.txt,文件存在读取内容,不存在提示用户
# 需求2:读取内容,循环读取,当无内容时退出循环,如果用户意外终止,提示用户
import time
try:
    f = open('text.txt', 'r')
    # 尝试循环读取内容
    try:
        while True:
            con = f.readline()
            # 如果读取完成,退出循环
            if len(con) == 0:
                break
            time.sleep(3)
            print(con)
    except:
        print('该文件异常退出')
except:
    print('该文件不存在')
