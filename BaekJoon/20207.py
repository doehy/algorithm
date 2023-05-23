import sys
input = sys.stdin.readline

calendar = [0] * 366
n = int(input())

for _ in range(n):
    s, e = map(int,input().split())

    for i in range(s,e+1):
        calendar[i] += 1
    
row = 0
col = 0
ans = 0

for i in calendar:
    if i == 0:
        ans += row * col
        row = 0
        col = 0
        continue
    row += 1
    col = max(col, i)

print(ans)