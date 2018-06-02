#!usr/bin/python
# ecoding=gbk;

a=[1,1]*40;
i=2;
while(i<=30):
	a[i]=a[i-1]+a[i-2];
	i=i+1;

i=0;
for x in a:
	print(x,end=' ');
	if i>=30:
		break;
	i=i+1;
