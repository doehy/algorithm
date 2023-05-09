import sys
input = sys.stdin.readline

n = int(input())

answer = 0
bx, by = -1000000000, -1000000000
for i in range(n):
    x,y = map(int,input().split())
    if x >= by:
        answer += y - x
    else:
        if y <= by:
            pass
        else:
            answer += y - by
    if y > by:
        by = y

print(answer)