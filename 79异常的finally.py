try:
    f = open('text.txt', 'r')
except Exception as result:
    f = open('text.txt', 'w')
else:
    print('没有异常')
finally:
    f.close()
