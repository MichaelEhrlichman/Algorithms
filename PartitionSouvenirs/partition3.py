# Uses python3
import sys
import itertools
from operator import xor

def efficient_partition3(A):
    total_value = sum(A)
    if total_value%3 != 0:
        return 0
    else:
        knapacity = total_value//3
    X = [[[False for _ in range(0,knapacity+1)] for _ in range(0,knapacity+1)] for _ in range(0,len(A)+1)]
    X[0][0][0] = True
    for i in range(1,len(A)+1):
        ai = A[i-1]
        for j in range(0,knapacity+1):
            for k in range(0,knapacity+1):
                neither = X[i-1][j][k]
                first = X[i-1][j-ai][k]
                second = X[i-1][j][k-ai]
                X[i][j][k] = neither or (first or second)
    #for row in X:
    #    print(row)
    return 1 if X[-1][-1][-1] else 0

def naive_partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
#    print(naive_partition3(A))
    print(efficient_partition3(A))

