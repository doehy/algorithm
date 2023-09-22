n,d,k,c = map(int,input().split())

data = []
count = 0
cnt = []
for i in range(n):
    data.append(int(input()))

for i in range(n):
    s = set()
    for j in range(i,i+k):
        j = j % n
        s.add(data[j])
    
    if c in s:
        cnt.append(len(s))
    else:
        cnt.append(len(s)+1)


print(max(cnt))