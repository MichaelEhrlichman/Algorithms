

n = int(input())

ints = []
i = 1
while True:
    if n-i > i:
        ints.append(i) 
        n -= i
        i += 1
    else:
        break
ints.append(n)
print(len(ints))
print(' '.join([str(i) for i in ints]))
