import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N+3)]
arr = [0 for _ in range(N+3)]
for k in range(1,N+1):
    arr[k] = int(input())
print(arr)

dp[1] = arr[1]
dp[2] = arr[1] + arr[2]
dp[3] = max(arr[1] + arr[3] ,arr[2] + arr[3])

for i in range(4, N+1):
    dp[i] = max(dp[i-3] + arr[i-1] + arr[i] ,  dp[i-2] + arr[i]) # i-1 칸을 밟은 경우에 그 전칸은 i-3 칸이므로 dp[i-3] + i-1칸의 점수 + i칸의 점수
print(dp)                                                        # i-2 칸을 밟은 경우에는 i-1칸을 밟지 않고 i 칸을 밟아야 하므로 dp[i-2] + i칸의 점수
print(dp[N])