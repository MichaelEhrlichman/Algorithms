# Uses python3
import time

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l
    return a*b

def lcm_better(a, b):
    for i in range(1, b + 1):
        if (a*i)%b == 0:
          return a*i
    return a*b

if __name__ == '__main__':
    a, b = map(int, input().split())
    #t = time.process_time()
    #ans = lcm_naive(a, b)
    #print(time.process_time()-t)
    #print(ans)
    #t = time.process_time()
    ans = lcm_better(a, b)
    #print(time.process_time()-t)
    print(ans)

