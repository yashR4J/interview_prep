from ntpath import join
from platform import java_ver
from typing import List
def maxProfit(l: List[int]) -> int:
    # bought, profit = -1, 0
    # for i in range(0, len(l)-1):
    #     if l[i] < l[i+1] and bought == -1:
    #         bought = l[i]
    #     elif l[i] > l[i+1] and bought != -1:
    #         profit += l[i] - bought
    #         bought = -1
    #     print(l[i], bought, profit)
    # if bought != -1: profit += l[-1] - bought
    # return profit
    profit, j = 0, 0
    for i in range(1, len(l)):
        if l[i-1] > l[i]: # decreasing sequence
           j = i
        elif i+1 == len(l) or l[i] > l[i+1]:
            profit += l[i] - l[j]
    return profit

if __name__ == '__main__':
    test_cases = [
        [1,5,4,3,2,9]
    ]
    ans = [11]

    for i in range(len(test_cases)):
        assert maxProfit(test_cases[i]) == ans[i]
