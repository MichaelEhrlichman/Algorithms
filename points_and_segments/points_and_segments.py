# Uses python3
import sys
import time

def faster_count_segments(starts, ends, points):
    all_lst = list()
    for start in starts:
        all_lst.append((start,'s'))
    for end in ends:
        all_lst.append((end,'e'))
    for ix,point in enumerate(points):
        all_lst.append((point,ix))

    def sortfun(x):
        if x[1] == 's':
            breaker = 0
        elif x[1] == 'e':
            breaker = 2
        else:
            breaker = 1
        return (x[0],breaker)
    all_lst = sorted(all_lst,key=sortfun)
    #print(all_lst)

    ans = [0]*len(points)
    counter = 0
    for item in all_lst:
        if item[1] == 's':
            counter += 1
        elif item[1] == 'e':
            counter -= 1
        else:
            ans[item[1]] = counter
    return ans
            
def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]

    faster_cnt = faster_count_segments(starts, ends, points)
    for x in faster_cnt:
        print(x, end=' ')

    #print()
    ##naive calculation
    #cnt = naive_count_segments(starts, ends, points)
    #for x in cnt:
    #    print(x, end=' ')
    #print()
    #if faster_cnt != cnt:
    #    print("wrong")





