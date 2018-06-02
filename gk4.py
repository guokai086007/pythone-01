#!/usr/bin/env python3
# ecoding=gbk

x = float(input("请输入一个大于等于0小于等于1的数: "));
n = term = 1;
num = int(input("请输入一个数表示需要求的项数: "));
sum = 1.0;
while n <= (num-1):
    term *= x / n
    sum += term
    n += 1
    if term < 0.0001:
        break

print("结果为：");
print("%.3f"%sum);
