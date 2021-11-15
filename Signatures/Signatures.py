def lefts(seg):
    return seg[0]

def rights(seg):
    return seg[1]

n = int(input())
segments = []
for _ in range(n):
    a,b = list(map(int,input().split())) 
    segments.append((a,b))

segments.sort(key=rights)

points = []
while segments:
    point = segments[0][1]
    points.append(point)
    #print(points)
    #print(segments)
    del segments[0]
    while segments:
        if segments[0][0] <= point and segments[0][1] >= point:
            del segments[0]
        else:
            break

print(len(points))
print(' '.join([str(point) for point in points]))
