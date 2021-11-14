

def density(item):
    return item[0]/item[1]

nitems, capW = map(int, input().split())
if nitems == 0:
    print(0)
    quit()
items = []
for _ in range(nitems):
    v,w = map(int,input().split())
    items.append((v,w))

items.sort(key=density)

W = capW
lootValue = 0
while W > 0 and items:
    item = items.pop()
    a = min(W,item[1])
    W -= a
    lootValue += a*density(item)
print(lootValue)
