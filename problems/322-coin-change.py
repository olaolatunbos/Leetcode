def coinChange(coins, amount):
    coins.sort()
    r = len(coins) -1
    count = 0

    while amount > 0 and r >= 0:
        change = amount - coins[r]
        if change >= 0:
            amount = change
            count += 1
        else:
            r -= 1
    return count if amount == 0 else -1

print(coinChange([186,419,83,408], 6249))

