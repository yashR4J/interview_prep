def name():
    return None

if __name__ == '__main__':
    test_cases = []
    ans = []

    for i in range(len(test_cases)):
        output = name(test_cases[i])
        try:
            assert output == ans[i]
        except AssertionError:
            print(f"Error: Test {i}, Output is {output}")
