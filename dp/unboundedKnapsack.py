from math import inf

def knapsack(W, val, wt):
    dp = [0 for _ in range(W + 1)]

    for i in range(W + 1):
        for j in range(len(val)):
            if wt[j] <= i:
                without = -inf if i - wt[j] < 0 else dp[i - wt[j]]
                dp[i] = max(dp[i], without + val[j])
    
    return dp[W]

if __name__ == '__main__':
    test_cases = [
        (100, [10,30,20], [5,10,15])
    ]
    ans = [300]

    for i in range(len(test_cases)):
        assert knapsack(test_cases[i][0], test_cases[i][1], test_cases[i][2]) == ans[i]
