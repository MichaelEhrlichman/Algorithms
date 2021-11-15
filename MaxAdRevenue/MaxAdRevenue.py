
n = int(input())
densities = list(map(int, input().split()))
clicks = list(map(int, input().split()))

densities.sort()
clicks.sort()

ans = 0
for density,click in zip(densities,clicks):
    ans += density*click
print(ans)
