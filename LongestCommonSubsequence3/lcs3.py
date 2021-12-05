# Uses python3
import sys
import random

def lcs3(a, b, c):
    m = len(a)+1
    n = len(b)+1
    p = len(c)+1
    D=[[[0 for _ in range(p)] for _ in range(n)] for _ in range(m)]

    for i in range(1,m):
        for j in range(1,n):
            for k in range(1,p):
                if ((i>0 and j>0) and k>0) and (a[i-1] == b[j-1] and a[i-1] == c[k-1]):
                    D[i][j][k] = D[i-1][j-1][k-1] + 1
                else:
                    aaa,bbb,ccc = [float('-inf')]*3
                    if (i>0 and j>-1) and k>-1:
                        bbb = D[i-1][j][k]
                    if (i>-1 and j>0) and k>-1:
                        aaa = D[i][j-1][k]
                    if (i>-1 and j>-1) and k>0:
                        ccc = D[i][j][k-1]
                    D[i][j][k] = max(aaa,bbb,ccc)
                #print(i,j,k)
                #print(D[i][j][k])

    #for row in D:
    #    print(row)
    return D[-1][-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]

    print(lcs3(a, b, c))
