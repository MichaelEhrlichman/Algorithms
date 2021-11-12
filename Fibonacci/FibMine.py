import sys
import time

def naive_FibRecurs(n):
	if n <= 1:
		return n
	else:
		return naive_FibRecurs(n-1) + naive_FibRecurs(n-2)

def fast_Fib(n):
	fib_lst = [0,1]
	for i in range(2,n+1):
		fib_lst.append(fib_lst[i-2]+fib_lst[i-1])
	return fib_lst[-1]

def faster_Fib(n):
	fibA = 0
	fibB = 1
	for i in range(2,n+1):
		fibC = fibA + fibB
		fibA = fibB
		fibB = fibC
	return fibC

num = int(sys.argv[1])
# t = time.process_time()
# ans = naive_FibRecurs(num)
# print(time.process_time()-t)
# print(ans)

t = time.process_time()
ans = fast_Fib(num)
print(time.process_time()-t)
print(ans)

t = time.process_time()
ans = faster_Fib(num)
print(time.process_time()-t)
print(ans)
