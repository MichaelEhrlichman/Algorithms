# Uses python3
import sys
import random

def lcs2(a, b):
    n = len(b)+1
    m = len(a)+1
    D=[[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        D[i][0] = 0
    for j in range(1,n):
        for i in range(1,m):
            if a[i-1] == b[j-1]:
                D[i][j] = D[i-1][j-1] + 1
            else:
                inse = D[i][j-1] #+ 1
                dele = D[i-1][j] #+ 1
                D[i][j] = max(inse,dele)
    return D[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]
    print(lcs2(a,b))
