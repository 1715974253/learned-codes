# 100以内数字和
i = 1
result = 0
while i <= 100:
    result += i
    i += 1
print(result)
# 100以内偶数和
result1 = 0
j = 1
while j <= 100:
    if j % 2 == 0:
        result1 += j
    j += 1
print(result1)
