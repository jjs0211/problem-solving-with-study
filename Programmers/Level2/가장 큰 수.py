def solution(numbers):
    # for i in numbers:
    #     print(str(i)*3)
    numbers.sort(key=lambda x: str(x) * 3, reverse=True)
    result = ''
    for i in numbers:
        result += str(i)
        
    if result[0] == '0': # [0, 0, 0] 일 때 0으로 나오게 해야함
        return '0'
    else:
        return result