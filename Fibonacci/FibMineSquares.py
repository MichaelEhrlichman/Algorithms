import sys
import time

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

num = int(input())

#a = faster_Fib(num)%10
#b = a + faster_Fib(num-1)%10
#print((a*b)%10)

pisano = 60
numA = num%pisano
numB = (num-1)%pisano
a = faster_Fib(numA)%10
b = a + faster_Fib(numB)%10
if b > 9:
    b = b - 10
print((a*b)%10)

