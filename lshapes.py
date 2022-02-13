def lshapes(matrix):
    
    return 1
    
if __name__ == '__main__':
    no_cases = int(input())
    
    for i in range(no_cases):
        (r, c) = map(int, input().split(' '))
        matrix = []
        for _ in range(r):
            line = map(int, input().split(' '))
            matrix.append(line)
        print(f"Case #{i+1}: {lshapes(matrix)}")