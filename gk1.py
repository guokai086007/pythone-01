#!/usr/bin/python
# coding=gbk

sum=0;
N = int(input("请输入一个数字N："));
t=N;
while(N>0):
	N=N-1;
	x =int(input());
	sum=sum+x;

print("以上所有数的平均值为：",end='');
print(sum/t);
