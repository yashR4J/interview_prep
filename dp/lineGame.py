# finds the maximum total sum possible for the player playing first
def line_game(l):
    def helper(i, j, l, memo):
        if memo[i][j] != -1:
            return memo[i][j]
        if j == i + 1:
            memo[i][j] = max(l[i], l[j])
        else:
            x = helper(i+2, j, l, memo) if i + 2 <= j else 0
            y = helper(i+1, j-1, l, memo) if i + 1 <= j - 1 else 0
            z = helper(i, j-2, l, memo) if i <= j - 2 else 0
            memo[i][j] = max(l[i] + min(x, y), l[j] + min(y, z))
        return memo[i][j]
    
    memo = [[-1 for _ in range(len(l)+1)] for _ in range(len(l)+1)]
    return helper(0, len(l) - 1, l, memo)

if __name__ == '__main__':
    test_cases = [
        [6, 5, 2, 7, 3, 5],
        [0, 0, 0, 1, 0, 0],
        [10, 10, 10, 10, 10, 10]
    ]
    ans = [18, 1, 30]

    for i in range(len(test_cases)):
        try:
            assert len(test_cases[i]) % 2 == 0
        except AssertionError:
            print("Invalid test case ", i+1)
        try:
            # print(line_game(test_cases[i]))
            assert line_game(test_cases[i]) == ans[i]
        except AssertionError:
            print(f"Error: Test {i+1}, Output is {line_game(test_cases[i])}")
