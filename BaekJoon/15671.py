n = int(input())
data = []
for i in range(n):
    data.append(list(map(int,input().split())))

# 상,하,좌,우,윗오,윗왼,아오,아왼
dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,1,-1,1,-1]



