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

n, m = map(int, input().split())

#for i in range(30):
#    print(i,faster_Fib(i)%num)
#print(pisano_period(num))

pisano = pisano_period(m)
#print("pisano number is {}".format(pisano))
new_num = n%pisano
#print("new num is {}".format(new_num))
print(faster_Fib(new_num)%m)
