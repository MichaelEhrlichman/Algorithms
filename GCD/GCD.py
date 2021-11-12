import sys
import time

def naive_GCD(a,b):
	best = 1
	startd = min(a,b)
	for d in range(2,startd+1):
		if a%d == 0 and b%d == 0:
			best = d
	return best

def EuclidGCD(a,b):  #Euclidian Algorithm
	if b == 0:
		return a
	return EuclidGCD(b,a % b)

if __name__ == '__main__':
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	# t = time.process_time()
	# ans = naive_GCD(a,b)
	# print(time.process_time() - t)
	# print(ans)

	t = time.process_time()
	ans = EuclidGCD(a,b)
	print(time.process_time() - t)
	print(ans)
