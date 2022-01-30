n = int(input())
score = list(map(int, input().split()))
score_copy = []
for i in range(len(score)):
  score_copy.append(score[i]/max(score)*100)

print(sum(score_copy)/len(score_copy))



