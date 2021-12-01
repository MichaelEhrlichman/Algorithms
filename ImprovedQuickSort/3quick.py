# Uses python3
import sys
import random
import time

def resortleft(a, l, r):
    x=a[r]
    k=r
    j=l
    while j<k:
        if a[j] == x:
            while a[k] == x:
                k -= 1
                if k==j:
                    break
            a[j], a[k] = a[k], a[j]
        j += 1
    return k

def partition3(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
        #print(a)
    a[l], a[j] = a[j], a[l]
    #print("      resorting: "+", ".join([str(x) for x in a[l:r+1]]))
    k = resortleft(a,l,j)
    #print("After resorting: "+", ".join([str(x) for x in a[l:r+1]]))
    #print(a)
    return k,j

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def randomized_quick_sort3(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    #print('random k: {}'.format(k))
    a[l], a[k] = a[k], a[l]
    m1,m2 = partition3(a, l, r)
    #print(','.join([str(x) for x in a])+": full")
    #print(','.join([str(x) for x in a[l:m1-1+1]])+": left")
    #print(','.join([str(x) for x in a[m2+1:r+1]])+": right")
    randomized_quick_sort3(a, l, m1 - 1);
    randomized_quick_sort3(a, m2 + 1, r);

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    #t = time.process_time()
    #print(a)
    #randomized_quick_sort(a, 0, len(a) - 1)
    random.seed(1)
    randomized_quick_sort3(a, 0, len(a) - 1)
    #print(time.process_time() - t)
    for x in a:
        print(x, end=' ')
