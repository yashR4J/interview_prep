def longestCommonSubsequence(S1, S2):
    m = len(S1)
    n = len(S2)
    L = [[0 for x in range(n+1)] for x in range(m+1)]

    # Building the mtrix in bottom-up way
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif S1[i-1] == S2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    index = L[m][n]
    return index

    lcs_algo = [""] * (index+1)
    lcs_algo[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:

        if S1[i-1] == S2[j-1]:
            lcs_algo[index-1] = S1[i-1]
            i -= 1
            j -= 1
            index -= 1

        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
    # # Time complexity: O(len(a)*len(b))
    # dp = [[None for _ in range(len(b)+1)] for _ in range(len(a)+1)]
    # for i in range(len(a)+1):
    #     for j in range(len(b)+1):
    #         if i == 0 or j == 0:
    #             dp[i][j] = 0
    #         elif a[i-1] == b[i-1]:
    #             dp[i][j] = dp[i-1][j-1] + 1
    #         else:
    #             dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # _len = dp[len(a)][len(b)]
    # word = [" "] * (_len)
    
    # i = len(a)
    # j = len(b)
    # while i > 0 and j > 0:
    #     if a[i-1] == b[i-1]:
    #         word[_len-1] = a[i-1]
    #         i -= 1
    #         j -= 1
    #         _len -= 1
    #     elif dp[i-1][j] > dp[i][j-1]:
    #         i -= 1
    #     else:
    #         j -= 1
    return ''.join(lcs_algo)

if __name__ == '__main__':
    test_cases = [
        ('bbcollab', 'abdallah'),
        ('Ilovecoding', 'IIllovecoding'),
        ('KickstartIsFun', 'kkickstartiisfun')
        # ('aabbccx', 'xccbbaa'), <-- Algorithm failing at test case...
    ]
    # ans = ['blla', 'Ilovecoding', 'ickstartsun'] # 'aa'
    ans = [4, 11, 11]

    for i in range(len(test_cases)):
        try:
            assert longestCommonSubsequence(test_cases[i][0], test_cases[i][1]) == ans[i]
        except AssertionError:
            print(f"Error: Test {i}, Output is {longestCommonSubsequence(test_cases[i][0], test_cases[i][1])}")