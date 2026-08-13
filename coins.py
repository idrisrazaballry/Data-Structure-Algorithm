def coin_change(coins, amount):
    coins.sort()
    res = {}

    for coin in range(len(coins)-1, -1, -1):
        while amount >= coins[coin]:
            if coins[coin] not in res:
                res[coins[coin]] = 1
            else:
                res[coins[coin]] += 1
            amount -= coins[coin]
    return res


coins = [100, 1, 500, 50, 200, 1000, 2000, 2, 5, 20, 10]
amount = int(input("Enter the amount :"))
value = coin_change(coins, amount)
if len(value) != 0:
    for k,v in value.items():
        print(k,"*",v,"=", k*v)