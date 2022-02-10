import sys
n, m = map(int, sys.stdin.readline().split()) # 나무의 수, 가져갈 나무의 길이
height = list(map(int, sys.stdin.readline().split()))

left = 1
right = max(height)

while left <= right:
    mid = (left+right)//2
    result = 0
    for i in height:
        if i > mid:
            result += i-mid
    if result >= m:
        left = mid +1
    else:
        right = mid -1
print(right)