def challenge_nine(num) -> int:
    _sum = 0
    for x in str(num):
        _sum += int(x)
    new_num = 9 - (_sum % 9)
    # print(new_num)
    if int(str(num)+str(new_num)) < int(str(new_num)+str(num)): 
        return int(str(num)+str(new_num))
    else:
        return int(str(new_num)+str(num))
            
if __name__ == '__main__':
    # test_cases = [
    #     5, 33, 12121
    # ]
    # ans = [45, 333, 121212]

    # for i in range(len(test_cases)):
    #     output = challenge_nine(test_cases[i])
    #     try:
    #         assert output == ans[i]
    #     except:
    #         print(f"{output} not equal to {ans[i]}")
    
    no_cases = int(input())
    for i in range(no_cases):
        _in = int(input())
        print(f"Case #{i+1}: {challenge_nine(_in)}")