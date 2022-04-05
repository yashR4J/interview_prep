
from this import d

def alignment():
    a = ['a', 'b', 'a', 'c']
    b = ['b', 'a', 'a']
    M, N = len(b), len(a)
        
    dp = [[0 for _ in range(N)] for _ in range(M)]
    dp[0][0] = 0
    for j in range(1, N):
        dp[0][j] = dp[0][j - 1] + score((a[j], '#'))
    
    for i in range(1, M):
        dp[i][0] = dp[i - 1][0] + score(('#', b[i]))
        for j in range(1, N):
            vertical = dp[i - 1][j] + score(('#', b[i]))
            horizontal = dp[i][j - 1] + score((a[j], '#'))
            diagonal = dp[i - 1][j - 1] + score((a[j], b[i]))
            dp[i][j] = max(vertical, horizontal, diagonal)