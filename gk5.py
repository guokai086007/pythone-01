#!/usr/bin/env python3
sticks = 21

print("There are 21 sticks, you can take 1-4 number of sticks at a time.")
print("Whoever will take the last stick will loose")
#上面两句是提示信息！

while True:#这是一个死循环，为了一定要分出胜负！
    print("Sticks left: " , sticks)#打印现在还剩下多少根棍子！
    sticks_taken = int(input("Take sticks(1-4):"))#提示用户拿（1~4根）棍子
    if sticks == 1:#如果只剩下一根木棍的话，游戏结束，打印提示语句，并跳出循环！
        print("You took the last stick, you loose")
        break
    if sticks_taken >= 5 or sticks_taken <= 0:
		#如果这次拿的木棍数量不符合规范，就要重新拿，使用continue跳过本次循环。
        print("Wrong choice")
        continue
	#由于用户和电脑一次选的棍子总数只能是5，所以电脑这次拿的数量就是5 - sticks_taken
    print("Computer took: " , (5 - sticks_taken) , "\n")
	sticks -= 5 #将木棍的总数减去5！
