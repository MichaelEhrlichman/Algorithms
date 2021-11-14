import sys
import time

def pisano_period(mod):
    pre = [0,0,0]
    n = 4
    while True:
        pre[0:2] = pre[1:3]
        pre[2] = faster_Fib(n)%mod
        if pre == [0,1,1]:
            return n-2
        n += 1

def faster_Fib(n):
	fibA = 0
	fibB = 1
	for i in range(2,n+1):
		fibC = fibA + fibB
		fibA = fibB
		fibB = fibC
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fibC

n = int(input())

#s = faster_Fib(n+2)-1
#print("naive: {}".format(s%10))

pisano = pisano_period(10)
new_num = (n+2)%pisano
s = (faster_Fib(new_num)%10-1)
if s == -1:
    s = 9
print(s)
