from itertools import permutations
def solution(numbers):
    numbers_list = []
    for i in range(1, len(numbers)+1):
        numbers_list.extend(list(permutations(numbers, i)))
    # print(set(numbers_list))
    cnt = 0
    for number in set(numbers_list):
        a = ''
        if len(number) == 1:
            a = number[0]
        else:
            for num in number:
                a+=num
        # print(a)
        if a[0] == '0' or a == '1':
            continue
        else:
            for i in range(2, int(int(a)**0.5)+1):
                if int(a)%i == 0:
                    break
            else:
                cnt+=1
    return cnt
