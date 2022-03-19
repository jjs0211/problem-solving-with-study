def solution(sizes):
    w = []
    h = []
    for i in sizes:
        i.sort()
    for i in range(2):
        for j in range(len(sizes)):
            if i == 0:
                w.append(sizes[j][i])
            else:
                h.append(sizes[j][i])
    return max(w) * max(h)