#Uses python3
import sys
import math

def dist(x,y):
    return  ((x[0]-y[0])**2 + (x[1]-y[1])**2)**0.5

def fast_minimum_distance(pts):
    midix = len(pts)//2
    S1 = pts[:midix]
    S2 = pts[midix:]
    #min_dist_S1 = less_naive_minimum_distance(S1)
    #min_dist_S2 = less_naive_minimum_distance(S2)
    min_dist_S1 = float('inf')
    min_dist_S2 = float('inf')

    if len(S1) > 2:
        min_dist_S1 = fast_minimum_distance(S1)
    elif len(S1) == 2:
        min_dist_S1 = dist(S1[0],S1[1])

    if len(S2) > 2:
        min_dist_S2 = fast_minimum_distance(S2)
    elif len(S2) == 2:
        min_dist_S2 = dist(S2[0],S2[1])

    d = min(min_dist_S1,min_dist_S2)
    #find d0, the location of the line between S1 and S2 about which S3 is defined
    d0 = (S1[-1][0]+S2[0][0])/2.0
    #print('d0: {}'.format(d0))
    S3 = [pt for pt in S1 if d0-pt[0]<d] + [pt for pt in S2 if pt[0]-d0<d]
    min_dist_S3 = less_naive_minimum_distance_strip(S3)
    min_dist = min(d,min_dist_S3)
    return min_dist

def less_naive_minimum_distance_strip(pts):
    min_dist = float('inf')
    P3 = sorted(pts,key=lambda x: x[1])
    for ix1 in range(len(pts)):
        for ix2 in range(ix1+1, min(len(pts),ix1+7+1)):
            min_dist = min(min_dist,dist(pts[ix1],pts[ix2]))
    return min_dist

def less_naive_minimum_distance(pts):
    min_dist = float('inf')
    for ix1 in range(len(pts)):
        for ix2 in range(ix1+1,len(pts)):
            min_dist = min(min_dist,dist(pts[ix1],pts[ix2]))
    return min_dist

def naive_minimum_distance(x, y):
    min_dist = float('inf')
    for ix1, pt1 in enumerate(zip(x,y)):
        for ix2, pt2 in enumerate(zip(x,y)):
            if ix1 != ix2:
                min_dist = min(min_dist,dist(pt1,pt2))
    return min_dist

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    pts = sorted(list(zip(x,y)),key=lambda x:x[0])
    #print("{0:.9f}".format(less_naive_minimum_distance(pts)))
    print("{0:.9f}".format(fast_minimum_distance(pts)))
