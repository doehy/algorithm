import sys
input = sys.stdin.readline
data = [list(input().split()) for _ in range(5)]
res = set()
def dfs(r,c,cur, cnt):
    if cnt == 5:
        res.add(cur)
        return
    if r + 1 < 5:
        dfs(r+1,c,cur+data[r+1][c],cnt+1)
    if r - 1 >= 0:
        dfs(r-1,c,cur+data[r-1][c],cnt+1)
    if c + 1 < 5:
        dfs(r,c+1,cur+data[r][c+1],cnt+1)
    if c - 1 >= 0:
        dfs(r,c-1,cur+data[r][c-1],cnt+1)
for i in range(5):
    for j in range(5):
        dfs(i,j,data[i][j],0)
        
print(len(res))
