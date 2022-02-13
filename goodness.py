def goodString(length, k, string):
    def score(length, k, string):
        x = 0
        counter = 0
        while x < length / 2:
            if string[x] != string[(length-1)-x]:
                counter += 1
            x += 1
        return counter
    
    goodness = score(length, k, string)
    return goodness - k if goodness > k else k - goodness

if __name__ == '__main__':
    no_cases = int(input())
    
    for i in range(no_cases):
        (n, k) = map(int, input().split(' '))
        string = input()
        print(f"Case #{i+1}: {goodString(n,k,string)}")