# Uses python3

def edit_distance(s, t):
    n = len(t)+1
    m = len(s)+1
    D=[[0 for _ in range(n)] for _ in range(m)]
    D[0][:] = range(n)
    for i in range(m):
        D[i][0] = i
    for j in range(1,n):
        for i in range(1,m):
            inse = D[i][j-1] + 1
            dele = D[i-1][j] + 1
            if s[i-1] == t[j-1]:
                matc = D[i-1][j-1]
                D[i][j] = min(inse,dele,matc)
            else:
                mism = D[i-1][j-1] + 1
                D[i][j] = min(inse,dele,mism)
    return D[-1][-1]

if __name__ == "__main__":
    str1 = list(input())
    str2 = list(input())
    print(edit_distance(str1,str2))
