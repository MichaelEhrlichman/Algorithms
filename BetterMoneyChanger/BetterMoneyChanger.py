money = int(input())

denoms = [1,3,4]
min_coins = [1,2,1,1]

while len(min_coins) < money:
    min_coin = float('inf')
    for denom in denoms:
        min_coin = min(min_coin,min_coins[-denom]+1) 
    min_coins.append(min_coin)

print(min_coins[money-1])

