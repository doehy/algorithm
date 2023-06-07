n,m = map(int,input().split())
answer = []
for _ in range(n):
    p,l = map(int,input().split())
    data = list(map(int,input().split()))
    if p < l: # 수강신청 인원이 더 적어
        answer.append(1)
    else:
        data.sort(reverse=True)
        answer.append(data[l-1])
answer.sort()
re = 0
for mile in answer:
    m -= mile
    if m < 0:
        break
    re += 1
print(re)