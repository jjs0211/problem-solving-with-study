def solution(x):
    str_x = str(x)
    a = 0
    for i in str_x:
        a+=int(i)
    if x % a == 0:
        return True
    else:
        return False