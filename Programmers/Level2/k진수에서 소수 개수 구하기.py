def isPrimeNumber(a):
    if a == 1:
        return 0
    else:
        for i in range(2, int(a**0.5)+1):
            if a%i == 0:
                return 0
        return 1        

def solution(n, k):
    jinsoo = ''
    while True:
        jinsoo += str(n%k)
        n=n//k
        if n <=k-1:
            jinsoo += str(n%k)
            break
    jinsoo = jinsoo[::-1]

    a = ''
    cnt = 0
    for i in jinsoo:
        if int(i) != 0:
            a += i
        else:
            if a == '':
                continue
            else:
                cnt+=isPrimeNumber(int(a))
                a = ''
    else:
        if a != '':
            a+=i
            a = a[:-1]
            cnt += isPrimeNumber(int(a))
    return cnt


### 깔끔한 버전
# def isPrimeNumber(a):
#     if a == 1:
#         return 0
#     else:
#         for i in range(2, int(a**0.5)+1):
#             if a%i == 0:
#                 return 0
#         return 1        

# def solution(n, k):
#     jinsoo = ''
#     while n>0:
#         jinsoo += str(n%k)
#         n=n//k
#     jinsoo = jinsoo[::-1]

#     cnt = 0
#     for n in jinsoo.split('0'):
#         if n == '':
#             continue
#         else:
#             cnt += isPrimeNumber(int(n))
#     return cnt