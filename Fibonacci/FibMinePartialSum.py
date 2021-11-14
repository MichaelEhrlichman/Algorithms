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

m,n = map(int, input().split())

pisano = 60 #pisano_period(10)
new_n = (n+2)%pisano
new_m = (m+1)%pisano
s_n = faster_Fib(new_n)%10
s_m = faster_Fib(new_m)%10
s = s_n-s_m
if s < 0:
    s = 10+s
print(s)
