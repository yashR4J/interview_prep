def hydration(a):
    return None

if __name__ == '__main__':
    no_cases = int(input())
    
    for i in range(no_cases):
        cols = int(input())
        furniture = []
        for x in range(cols):
            row = list(map(int, input().split(' ')))
            furniture.append([(row[0], row[1]), (row[2], row[3])])
        print(furniture)
        # print(f"Case #{i+1}: {hydration(furniture)}")