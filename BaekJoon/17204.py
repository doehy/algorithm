N,K = map(int,input().split())

num = 0
lst = list()
for i in range(N):
    lst.append(int(input()))
out = 0
i = 0
result = 0
for i in range(N):
    result = lst[result]
    num+=1
    if result == K:
        print(num)
        out+=1
        break

if out == 0:
    print("-1")