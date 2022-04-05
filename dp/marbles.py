def print_array(a):
    for l in a:
        print(l)
    
def divide_marbles(n):
    memo = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    ret = calc(n, n, memo)
    print_array(memo)
    return ret
    
def calc(a, b, memo):
    if memo[a][b] != -1:
        return memo[a][b]

    if a > 0 and b == 0:
        memo[a][b] = 0
        return memo[a][b]
    
    if a == 0 and b >= 0:
        memo[a][b] = 1
        return memo[a][b]
    
    memo[a][b] = 0
    
    for k in range(1, min(a,b) + 1):
        memo[a][b] += calc(a-k, k-1, memo)
        
    return memo[a][b] 

if __name__ == '__main__':
    try:
        while True: 
            _in = input("How many marbles shall we divide?\n")
            print("This is how many grouping you can make: ", divide_marbles(int(_in)))
    except KeyboardInterrupt:
        exit(0)