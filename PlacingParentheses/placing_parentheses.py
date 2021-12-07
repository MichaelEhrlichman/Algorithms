# Uses python3
import re


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinAndMax(nums,ops,i,j,M,m):
    mymin = float('inf')
    mymax = float('-inf')
    for k in range(i,j):
        a = evalt(M[i][k], M[k+1][j], ops[k])
        b = evalt(M[i][k], m[k+1][j], ops[k])
        c = evalt(m[i][k], M[k+1][j], ops[k])
        d = evalt(m[i][k], m[k+1][j], ops[k])
        mymin = min(mymin,a,b,c,d)
        mymax = max(mymax,a,b,c,d)
    return mymin,mymax

def Parentheses(nums,ops):
    n = len(nums)
    m = [[0 for _ in range(n)] for _ in range(n)]
    M = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        m[i][i] = nums[i] 
        M[i][i] = nums[i] 
    for s in range(1,len(nums)):
        for i in range(n-s):
            j = i + s
            m[i][j],M[i][j] = MinAndMax(nums,ops,i,j,M,m)
    #for row in M:
    #    print(row)
    #for row in m:
    #    print(row)
    return M[0][n-1]

def get_maximum_value(dataset):
    nums = list(map(int,re.split(r'\D+',dataset)))
    ops = re.split(r'\d+',dataset)[1:-1]

    return Parentheses(nums,ops)


if __name__ == "__main__":
    print(get_maximum_value(input()))
