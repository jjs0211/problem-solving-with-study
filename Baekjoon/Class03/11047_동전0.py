import sys
n, k = map(int, sys.stdin.readline().split())
coin = []
cut = 0
for _ in range(n):
    coin.append(int(sys.stdin.readline()))
for j in range(n):
    if coin[j]>k:
        cut = coin.index(coin[j])
        break
    else:
        cut = len(coin)+1 # 만약 가장 큰 수가 k와 같다면 원래 리스트 그대로 쓰기 위해서

coin_cp = coin[:cut] # k보다 작은 동전들만 남은 리스트
cnt = 0
for i in range(len(coin_cp)):
    while True:
        if k//coin_cp[len(coin_cp)-1-i] != 0:
            cnt += (k//coin_cp[len(coin_cp)-1-i])
            k%=coin_cp[len(coin_cp)-1-i]
        else:
            break
    if k == 0:
        break
print(cnt)