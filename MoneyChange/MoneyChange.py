

m = int(input())

ncoins = 0
while m > 4:
    if m >= 10:
        m -= 10
        ncoins += 1
    elif m >= 5:
        m -= 5
        ncoins += 1
ncoins += m
print(ncoins)
