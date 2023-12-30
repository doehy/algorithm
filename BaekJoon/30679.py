# 별 가두기
import sys
sys.setrecursionlimit(10**6)
n,m = map(int,input().split())

data = []
for _ in range(n):
    data.append(list(map(int,input().split())))

result = []
def solve(r,c,de,visited):
    visited[r][c][de] = 1
    if de == 0:
        if c + data[r][c] >= m:
            return -1
        if not visited[r][c+data[r][c]][1]:
            return solve(r,c+data[r][c],1,visited)
        else:
            return 1
    elif de == 1:
        if r + data[r][c] >= n:
            return -1
        if not visited[r+data[r][c]][c][2]:
            return solve(r+data[r][c],c,2,visited)
        else:
            return 1
    elif de == 2:
        if c - data[r][c] < 0:
            return -1
        if not visited[r][c - data[r][c]][3]:
            return solve(r,c-data[r][c],3,visited)
        else:
            return 1
    else:
        if r - data[r][c] < 0:
            return -1
        if not visited[r-data[r][c]][c][0]:
            return solve(r-data[r][c], c, 0,visited)
        else:
            return 1
        
for i in range(n):
    visited = [[[0] * 4 for _ in range(m)] for _ in range(n)]
    if solve(i,0,0,visited) == 1:
        result.append(i+1)
result.sort()
leng = len(result)
print(leng)
if leng > 0:
    print(*result)