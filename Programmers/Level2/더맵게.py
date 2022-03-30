import heapq
def solution(scoville, K):
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    cnt = 0
    while True:
        low1 = heapq.heappop(heap)
        if low1 >= K:
            break
        else:
            low2 = heapq.heappop(heap)
            heapq.heappush(heap, low1 + low2*2)
            cnt += 1
        if len(heap) == 1 and heap[-1] < K:
            cnt = -1
            break
    return cnt