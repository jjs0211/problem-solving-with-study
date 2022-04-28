from collections import deque
def solution(cacheSize, cities):
    cache = deque()
    time = 0
    if cacheSize == 0:
        return 5 * len(cities)
    else:
        for i in cities:
            i = i.upper()
            if len(cache) < cacheSize:
                if i not in cache:
                    cache.append(i)
                    time += 5
                else:
                    print(cache)
                    del cache[cache.index(i)]
                    cache.append(i)
                    time += 1
                    print(cache)
            else:
                if i not in cache:
                    cache.popleft()
                    cache.append(i)
                    time += 5
                else:
                    del cache[cache.index(i)] # [2,3,1,4,1]인 경우 [2,3,1,4]다음에 [2,3,4,1]이 되어야함
                    cache.append(i)
                    time += 1
        return time