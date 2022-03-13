import math
def solution(left, right):
    result = 0
    for i in range(left, right+1):
        if len(str(math.sqrt(i))) == 3 or len(str(math.sqrt(i))) == 3 and str(math.sqrt(i))[-1] == '0':
            result -= i
        else:
            result += i
    return result