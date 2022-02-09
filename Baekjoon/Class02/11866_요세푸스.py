from collections import deque
n, k = map(int, input().split())
n_list = deque([i for i in range(1, n+1)])
result = []

while n_list: # while len(n_list) != 0 과 같은 의미
    for _ in range(k-1): # k 번째 전의 수 까지 지우고 뒤에 붙여줌
        n_list.append(n_list.popleft())
    result.append(n_list.popleft()) # k 번째 수는 result에 append

print('<', end = '')
for i in range(len(result)-1):
    print('{}, '.format(result[i]), end='')
print(result[-1], end='')
print('>')