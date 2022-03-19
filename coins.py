
coins = [2, 1, 0.5, 0.2, 0.1, 0.05]

def minCoins(amount):
    global coins
    num = 0
    for coin in coins:
        print(coin)
        if int(amount // coin) != 0:
            num += int(amount // coin)
            amount -= coin * int(amount // coin)
            print(amount)
    return num

if __name__ == '__main__':
    test_cases = [
        10.2
    ]
    ans = [6]

    for i in range(len(test_cases)):
        print(minCoins(test_cases[i]))
        assert minCoins(test_cases[i]) == ans[i]