from typing import List

# # DP Solution - Memory Limit Exceeded...
# def speed_typer(S1, S2) -> int:
#     # reduce problem to longest common subsequence problem...
#     m = len(S1)
#     n = len(S2)
#     L = [[0 for x in range(n+1)] for x in range(m+1)]

#     for i in range(m+1):
#         for j in range(n+1):
#             if i == 0 or j == 0:
#                 L[i][j] = 0
#             elif S1[i-1] == S2[j-1]:
#                 L[i][j] = L[i-1][j-1] + 1
#             else:
#                 L[i][j] = max(L[i-1][j], L[i][j-1])

#     _len = L[m][n]
#     # print(f"{_len} common letters")
#     if _len == len(S1): return len(S2) - _len
#     return "IMPOSSIBLE"

def speed_typer(S1, S2) -> int:
    if len(S2) <= len(S1) and S1 != S2: return "IMPOSSIBLE"
    i, j = 0, 0
    while i < len(S1) and j < len(S2):
        if S1[i] == S2[j]:
            i+=1
        j+=1
    if i == len(S1): # all characters were found
        return len(S2) - len(S1) # remove all extra characters
    else:
        return "IMPOSSIBLE"   
            
if __name__ == '__main__':
    test_cases = [
        ('aaaa','aaaaa'),
        ('bbbbb', 'bbbbc'),
        ('Ilovecoding', 'IIllovecoding'),
        ('KickstartIsFun', 'kkickstartiisfun')
    ]
    ans = [1, 'IMPOSSIBLE', 2, 'IMPOSSIBLE']

    for i in range(len(test_cases)):
        output = speed_typer(test_cases[i][0], test_cases[i][1])
        try:
            assert output == ans[i]
        except:
            print(f"{output} not equal to {ans[i]}")

    # no_cases = int(input())
    # for i in range(no_cases):
    #     _in = input()
    #     _out = input()
    #     print(f"Case #{i+1}: {speed_typer(_in, _out)}")