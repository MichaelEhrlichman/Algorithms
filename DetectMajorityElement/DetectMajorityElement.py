
n = int(input())
a = list(map(int,input().split()))
#assert n == len(a)

def getMajBottom(seq):
    if len(seq) == 3:
        if seq[0]==seq[1] or seq[0]==seq[2]:
            return seq[0]
        elif seq[1]==seq[2]:
            return seq[1]
    if len(seq) == 2:
        if seq[0]==seq[1]:
            return seq[0]
    if len(seq) == 1:
        return seq[0]
    return -1

def majDetector(seq):
    mid = len(seq)//2
    seqa = seq[:mid]
    seqb = seq[mid:]
    if len(seqb) <= 3:
        return getMajBottom(seqa),getMajBottom(seqb)
    else:
        seqa_a,seqa_b = majDetector(seqa)
        seqa_a = seqa_a if seqa.count(seqa_a) >= 1+len(seqa)//2 else -1
        seqa_b = seqa_b if seqa.count(seqa_b) >= 1+len(seqa)//2 else -1

        seqb_a,seqb_b = majDetector(seqb)
        seqb_a = seqb_a if seqb.count(seqb_a) >= 1+len(seqb)//2 else -1
        seqb_b = seqb_b if seqb.count(seqb_b) >= 1+len(seqb)//2 else -1

        ret = list(set([seqa_a,seqa_b,seqb_a,seqb_b]))
        if len(ret) > 2:
            ret.remove(-1)
            return ret
        elif len(ret) == 2:
            return ret
        elif len(ret) == 1:
            return [ret[0],-1]
        else:
            print("bomb")
            print(1/0)

t1, t2 = majDetector(a)
t1 = t1 if a.count(t1) >= 1+len(a)//2 else -1
t2 = t2 if a.count(t2) >= 1+len(a)//2 else -1
if t1>-1 or t2>-1:
    print(1)
else:
    print(0)

#import random
#while True:
#    testcase = []
#    for _ in range(5):
#        testcase.append(random.randint(1,10**3))
#    testcase.extend([1]*5)
#    random.shuffle(testcase)
#    #print(testcase)
#    t1, t2 = majDetector(testcase)
#    t1 = t1 if testcase.count(t1) >= 1+len(testcase)//2 else -1
#    t2 = t2 if testcase.count(t2) >= 1+len(testcase)//2 else -1
#    if t1 > -1 or t2 > -1:
#        if testcase.count(t1) < 1+len(testcase)//2 and testcase.count(t2) < 1+len(testcase)//2:
#            print(testcase)
#            print(t1,t2)
#            print(testcase.count(t1))
#            print(testcase.count(t2))
#            break
