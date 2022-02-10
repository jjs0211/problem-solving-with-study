k, n = map(int, input().split())
line_list = []

for _ in range(k):
    line = int(input())
    line_list.append(line)

left = 1
right = max(line_list)
while left <= right:
    mid = (left+right)//2
    cnt = []
    for i in range(len(line_list)):
        cnt.append(line_list[i]//mid) # 자른 선의 개수들을 넣어줌
    if sum(cnt) >= n: # 선의 개수들의 합이 n과 같은 것 중에서 최대 길이를 뽑아야 하므로 n과 같다고 break 하는 것이 아닌 계속해서 while문 돌아야함
        left = mid + 1
    elif sum(cnt) < n: # 나누는 수가 작아지면 개수가 많이 나오므로 right를 왼쪽으로 옮겨줌
        right = mid -1
print(right)