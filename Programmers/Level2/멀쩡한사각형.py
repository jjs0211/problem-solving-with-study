import math
def solution(w,h):
    return w * h - (w+h-math.gcd(w,h))

# https://leedakyeong.tistory.com/135