# all the paths in a M x N grid
def grid_traveller(M, N, memo={}):
    key = str(M) + ',' + str(N)
    if key in memo: return memo[key]
    if M == 0 or N == 0:
        return 0
    if M == 1 and N == 1:
        return 1
    memo[key] = grid_traveller(M-1,N,memo) + grid_traveller(M,N-1,memo)
    return memo[key]

if __name__ == '__main__':
    test_cases = [
        (0, 0),
        (1, 1),
        (2, 3),
        (3, 2),
        (3, 3)
    ]
    ans = [0, 1, 3, 3, 6]

    for i in range(len(test_cases)):
        # print(grid_traveller(test_cases[i][0], test_cases[i][1]) )
        try:
            assert grid_traveller(test_cases[i][0], test_cases[i][1]) == ans[i]
        except AssertionError:
            print(f"Error: Test {i+1}, Output is {grid_traveller(test_cases[i][0], test_cases[i][1])}")

###
# P(l, r) = min topping that we lose from eating slices the left/right 