from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

data = []

for _ in range(n):
    data.append(list(map(int,input().split())))

queue = deque()

data = sorted(data,key=lambda x : x[0])


for lesson in data:
    if queue and queue[0] <= lesson[0]:
        queue.popleft()
        print(queue[0])
    queue.append(lesson[1])

print(len(queue))
print(queue)