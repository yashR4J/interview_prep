def sillySort(A, i, j):
    n = j - i
    if n == 2:
        if A[i] > A[j - 1]:
            A[i] , A[j - 1] = A[j - 1], A[i]
    elif n > 2:
        m = int(n / 4)
        sillySort(A, i, i + 2*m)
        sillySort(A, i + m, i + 3*m)
        sillySort(A, i + 2*m, j ) 
        sillySort(A, i + m, i + 3*m) 
        sillySort(A, i, i + 2*m)
        sillySort(A, i + m, i + 3*m)


if __name__ == '__main__':
    test_cases = [
        [0, 1],
        [1,10,8,7,6,5,11,14],
        [1,0,2,3],
        [1,2,2,1],
        [9,3,5,4],
        [9,5,4,3],
        [],
        [1,10,8,7,1,10,8,7,6,5,11,14,6,5,11,14]
    ]

    for i in range(len(test_cases)):
        try:
            sillySort(test_cases[i], 0, len(test_cases[i]))
            assert test_cases[i] == sorted(test_cases[i])
            print(f"Testcase {i} with input {test_cases[i]} passed :)")
        except:
            print(f"Testcase {i} failed :(")
            print(f"Output was {test_cases[i]}")