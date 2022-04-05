from math import floor, ceil, log

# def partition(n: int):
#     if n <= 2: return []
#     ret = []
#     i = 1
#     j = n - 1
#     while i < j:
#         ret.append([i, j])
#         for p in partition(j):
#             if i not in p:
#                 p.append(i)
#                 ret.append(list(sorted(p)))
#         i += 1
#         j -= 1
    
#     ret2 = [] 
#     for l in ret:
#         if l not in ret2:
#             ret2.append(l)
#     return list(sorted(ret2, key=len))

def partition2(n: int): # recursive
    ret = []
    for i in range(1, ceil(n / 2)):
        ret.append([i, n - i])
        for p in partition(n - i):
            if len(list(filter(lambda x: x > i, p))) == len(p):
                ret.append([i] + p)
    return ret

def partition(n: int): # iterative    
    dp = [[] for _ in range(n + 1)] 
    i = 1
    while i <= n: # O(n)
        j = 1
        while j < ceil(i / 2): # (O(n))
            dp[i].append([j, i - j])
            # for p in dp[i - j]: # ehhhhhhhhhhhhhhhhh
            #     if len(list(filter(lambda x: x > j, p))) == len(p):
            #         dp[i].append([j] + p)
            j += 1
        
        x = 1
        while x < ceil(i / 2):
            for p in dp[i - x]:
                if len(list(filter(lambda l: l > x, p))) == len(p):
                    dp[i].append([x] + p)
            x += 1
        i += 1
    
    return dp[n]

import time

if __name__ == '__main__':
    test_cases = [
        3, 4, 5, 6, 7, 8, 9, 10#, 11, 12, 13, 14, 15
        # 10, 20, 30, 40, 50, 60, 70, 80
        # 11
    ]
    ans = []

    for i in range(len(test_cases)):
        t = time.time()
        output = partition(test_cases[i])
        t1 = time.time()
        ans = partition2(test_cases[i])

        # print((t1 - t) * (10**3), end=',')
        
        try:
            # print(len(output))
            print(test_cases[i], ' --> ', output , ' --> ', len(output))
            assert sorted(output) == sorted(ans)
        except AssertionError:
            print(f"Error: Test {i}, Output is {len(output)}, Answer is {len(ans)}")
            for x in ans:
                if x not in output:
                    print(x)

