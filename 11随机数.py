import random

player = int(input("请出拳:0是石头,1是剪刀,2是布:"))
computer = random.randint(0, 2)
print(computer)
if (player == 1 and computer == 2) or (player == 0 and computer == 1) or (player == 2 and computer == 0):
    print("玩家获胜")
elif (player == computer):
    print("平局,再来一次")
else:
    print("电脑获胜")
