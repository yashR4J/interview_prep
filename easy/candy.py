def test():
    test_cases = [
        """
        2,
        7 3,
        1 2 3 4 5 6 7,
        5 10,
        7 7 7 7 7
        """
    ]
    ans = [18,5,4]

    for i in range(len(test_cases)):
        assert minChocolate(test_cases[i]) == ans[i]

def candy(num, candies):
    return sum(candies) % num

if __name__ == '__main__':
    no_cases = int(input())
    
    for i in range(no_cases):
        (bags, children) = map(int, input().split(' '))
        candies = list(map(int, input().split(' ')))
        print(f"Case #{i+1}: {candy(children, candies)}")