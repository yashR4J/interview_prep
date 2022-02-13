import math
def largestPalindrome(n: int) -> int:
    # Not the greatest solution ...
    for x in range((10**n - 1)**2,(10**n - 1)**2 - 10**(2*n),-1):
        if str(x) == str(x)[::-1]:
            for y in range(10**n - 1, (10**n - 1) - 10**n + 1, -1):
                if math.ceil(x / y) == math.floor(x / y) and len(str(int(x/y))) == n:
                    return x % 1337
    return -1

if __name__ == '__main__':
    test_cases = [2, 1, 4]
    ans = [987, 9, 597]

    for i in range(len(test_cases)):
        # assert largestPalindrome(test_cases[i]) == ans[i]
        print(largestPalindrome(test_cases[i]))