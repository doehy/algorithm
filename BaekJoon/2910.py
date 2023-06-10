n,c = map(int,input().split())

data = list(map(int,input().split()))

ok = dict()
count = 0
for i in data:
    if i not in ok:
        count += 1
        ok[i] = [1,count,i]
    else:
        ok[i][0] += 1


total = list(ok.values())
total = sorted(total, key=lambda x:x[1])
total = sorted(total, key=lambda x:x[0],reverse=True)

for temp,count,number in total:
    for i in range(temp):
        print(number,end=' ')
# 빈도 순 정렬
# 빈도가 같다면 먼저 나온 게 먼저 정렬