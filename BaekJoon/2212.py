import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
data = list(map(int,input().split()))
data = list(set(data))
data.sort()
answer = []
for i in range(len(data) - 1):
    answer.append(data[i+1] - data[i])
answer.sort()
if k >= len(data):
    print(0)
else:
    for i in range(k-1):
        answer.pop()
    print(sum(answer))

