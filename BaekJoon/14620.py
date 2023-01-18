from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
answer = float("inf")
def check(li):
    global answer
    visited = [] # 집합으로 나중에 한번 바꿔보자
    temp = 0
    for r,c in li:
        temp += data[r][c]
        visited.append((r,c))
        for idx in range(4):
            nr = r + dx[idx][0]
            nc = c + dx[idx][1]
            if (nr,nc) not in visited:
                temp += data[nr][nc]         
                visited.append((nr,nc))
            else:
                return
    answer = min(answer,temp)

dx = [(-1,0),(1,0),(0,-1),(0,1)]
cadi = [(r,c) for r in range(1,N-1) for c in range(1,N-1)]
for li in combinations(cadi,3):
    check(li)
print(answer) 