import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))
answer = [0] * (max(data) + 1)
answer[data[0]] = -1
temp = set()
temp.add(data[0])
for i in range(1,len(data)):
    if data[i] not in temp:
        temp.add(data[i])
        answer[data[i]] = data[i-1]
print(len(answer))
print(*answer)
