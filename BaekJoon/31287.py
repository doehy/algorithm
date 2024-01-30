import sys
input = sys.stdin.readline
n,k = map(int,input().split())
data = list(input().rstrip())
direction = [0] * 4
flag = 0
if k > 1000:
    k = 1000
while k:
    for dir in data:
        if dir == 'U':
            direction[0] += 1
        elif dir == 'D':
            direction[1] += 1
        elif dir == 'L':
            direction[2] += 1
        else:
            direction[3] += 1
        if direction[0] == direction[1] and direction[2] == direction[3]:
            flag = 1
            break
    if flag == 1:
        break
    k -= 1

if flag == 1:
    print("YES")
else:
    print("NO")    

