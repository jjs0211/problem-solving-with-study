from itertools import product
def solution(numbers, target):
    
    a = list(product(('+', '-'), repeat = len(numbers)))
    # print(a)
    
    cnt = 0
    for i in a:
        result = 0
        for j in range(len(i)):
            if i[j] == '+':
                result += numbers[j]
            else:
                result -= numbers[j]
        # print(result)
        if result == target:
            cnt += 1
    return cnt