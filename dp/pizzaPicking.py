def pizza_picking():
    return None

if __name__ == '__main__':
    test_cases = [
        
    ]
    ans = []

    for i in range(len(test_cases)):
        try:
            assert pizza_picking(test_cases[i]) == ans[i]
        except AssertionError:
            print(f"Error: Test {i}, Output is {pizza_picking(test_cases[i])}")

###
# P(l, r) = min topping that we lose from eating slices the left/right 