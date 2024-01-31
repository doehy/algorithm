import sys
input = sys.stdin.readline
n = int(input())
data = list(input().rstrip())
ans = 0
count = 0
for dir in data:
    if dir == '(':
        count += 1
    else:
        count -= 1
    if abs(count) > ans:
        ans = abs(count)

if count == 0:
    print(ans)
else:
    print(-1)
