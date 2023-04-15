import sys
input = sys.stdin.readline

n = int(input())

data = []
for i in range(n-1):
    s,b = map(int,input().split())
    data.append((s,b))

k = int(input())

answer = float("inf")

def dfs(idx, total,visited):
    global answer
    if idx == n-1: # 4에 도착했다면
        answer = min(answer,total)
        return
    if idx > n - 1: # 도착 지점을 넘어갔다면
        return
    for i in range(3):
        if i != 2:
            dfs(idx + (i+1), total + data[idx][i], visited)
        if not visited:
            dfs(idx + 3, total + k, visited + 1)

dfs(0,0,0)
print(answer)