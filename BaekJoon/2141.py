import sys
input = sys.stdin.readline
n = int(input())
data = []
people = 0
for _ in range(n):
    x,a  = map(int,input().split())
    data.append([x,a])
    people += a

data.sort()
count = 0
for i in range(len(data)):
    count += data[i][1]
    if count >= people / 2:
        print(data[i][0])
        break