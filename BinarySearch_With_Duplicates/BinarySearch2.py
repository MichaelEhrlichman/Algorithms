
na = int(input())
seq = list(map(int,input().split()))
#assert len(seq) == na

nk = int(input())
k = list(map(int,input().split()))
#assert len(k) == nk

#fails test 22, presumablly because of recursion depth.
#def leftmost(seq,x,n):
#    if x>0 and seq[x-1] == n:
#        return leftmost(seq,x-1,n)
#    else:
#        return x

def leftmost(seq,x,n):
    for i in range(x):
        testix = x-i-1
        if seq[testix] != n:
            return x-i
    return 0

def leftmost_fast(seq,x,n):
    w = 0
    while True:
        mid = w + (x-w)//2
        if w <= x:
            if seq[mid] == n:
                x = mid - 1
            else: 
                w = mid + 1
        else:
            return w

def binary_step(seq,x,y,n):
    while True:
        mid = x + (y-x)//2
        if x <= y:
            if seq[mid] == n:
                #return leftmost(seq,mid,n)
                return leftmost_fast(seq,mid,n)
            elif n < seq[mid]:
                y = mid - 1
            else:
                x = mid + 1
        else:
            return -1

#fails test 54/57 for time exceeded
#def binary_step_recursive(seq,x,y,n):
#    mid = x + (y-x)//2
#    if x <= y:
#        if seq[mid] == n:
#            return leftmost(seq,mid,n)
#        elif n > seq[mid]:
#            return binary_step(seq,mid+1,y,n)
#        else:
#            return binary_step(seq,x,mid-1,n)
#    else:
#        return -1

x = 0
y = len(seq)-1
for num in k:
    if na == 0:
        print('-1',end=' ')
    else:
        print(binary_step(seq,x,y,num),end=' ')
