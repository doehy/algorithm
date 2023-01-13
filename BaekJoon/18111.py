n,m,chango = map(int,input().split())

data = [list(map(int,input().split())) for _ in range(n)]

time = float("inf") # 최소가 돼야하니
height = 0 # 최대가 돼야하고

min_height = min(map(min,data))
max_height = max(map(max,data))

cmdict = dict()

for i in range(n):
    for j in range(m):
        if data[i][j] not in cmdict:
            cmdict[data[i][j]] = 1
        else:
            cmdict[data[i][j]] += 1

for heig in range(min_height,max_height+1):
    count = 0
    need = 0
    for k in range(0,257):
        if k in cmdict:
            if  k > heig:
                count += (k - heig) * cmdict[k] 
            elif k < heig:
                need += (heig - k) * cmdict[k]
    if need <= count + chango: 
        temp = count * 2 + need
        time = min(time,count * 2 + need)
        if temp <= time:
            height = max(height,heig)

print(time,height)