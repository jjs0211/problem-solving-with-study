# from itertools import combinations
def solution(number, k):
#     result = []

#     a = list(combinations(number, len(number)-k))

#     for i in a:
#         result_num = ''
#         for j in i:
#             result_num += j
#         result.append(int(result_num))
#     return str(max(result))
    
    result = []
    
    for num in number:
        while k > 0 and result and result[-1] < num:
            result.pop()
            k -= 1
        result.append(num)
    if k > 0:
        result = result[:len(result)-k]
    return ''.join(result)