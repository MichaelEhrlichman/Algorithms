# Uses python3
import sys

def optimal_weight(W, items):
    n = len(items)
    value = [[0 for _ in range(n+1)] for _ in range(W+1)]
    #value[weight capacity][# items]
    for i in range(1,n+1):
        for w in range(1,W+1):
            value[w][i] = value[w][i-1]
            if items[i-1] <= w:
                val = value[w-items[i-1]][i-1] + items[i-1]
                if value[w][i] < val:
                    value[w][i] = val
    for row in value:
        print(row)
    return value[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
