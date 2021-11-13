s = 'python'
while s != "":
    for c in s:
        if c == 't':
            break
        print(c, end='')
    s = s[: -1]
