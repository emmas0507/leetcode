def coin_change(coins, amount):
    queue = [0]
    count = 0
    while len(queue) > 0:
        tmp = []
        for q in queue:
            for coin in coins:
                if q + coin == amount:
                    return count + 1
                elif q + coin < amount:
                    if q+coin not in tmp:
                        tmp = tmp + [q + coin]
                else:
                    continue
        count = count + 1
        queue = tmp
        print('count is {} and queue is {}'.format(count, queue))
    return -1

coins = [1,2,5]
amount = 11
print(coin_change(coins, amount))
