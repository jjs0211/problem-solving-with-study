from itertools import permutations
def solution(A,B):
    # ablist = [list(zip(x, B)) for x in permutations(A, len(B))]
    # print(ablist)
    A.sort()
    B.sort(reverse=True)
    result = 0
    for i in range(len(A)):
        result += A[i]*B[i]
    
    return result
    
  