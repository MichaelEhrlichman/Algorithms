import math

na = int(input())
seq_str = input()
seq = list(map(int,seq_str.split()))
nk = int(input())
k_str = input()
k = list(map(int,k_str.split()))

def binary_step(seq,x,y,n):
    #print("FOO x y: {} {} {}".format(x,y,mid))
    if n > seq[-1]:
        return -1
    elif n == seq[x]:
        return x
    elif n == seq[y]:
        return y
    elif y-x > 1:
        mid = math.floor((y+x)/2)
        if n < seq[mid]: 
            return binary_step(seq,x,mid,n)
        elif n > seq[mid]: 
            return binary_step(seq,mid,y,n)
        elif n == seq[mid]:
            return mid
    else:
        return -1

x = 0
y = len(seq)-1
for num in k:
    print('{} '.format(binary_step(seq,x,y,num)),end='')
print()
