from collections import deque
n = int(input())
reco_cnt = int(input())
recommand = list(map(int, input().split()))

pf = deque()
cnt = {}

for i in recommand:
    if i in pf:
        cnt[i] +=1
    else:
        if len(pf) == n:
            for key, value in cnt.items():
                if value == min(cnt.values()):
                    pf.remove(key)
                    del cnt[key]
                    break

        pf.append(i)
        if i not in cnt:
            cnt[i] = 1


pf = sorted(list(pf))
print(*pf)
