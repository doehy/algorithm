from collections import deque
import sys


def bfs(source):
    day = 0
    queue = deque()
    queue.append(source)
    cnt = 1
    temp = 0
    k = -1 #data의 인덱스를 따라다닐 변수
    while queue:
        day+=1
        for _ in range(cnt):
            x = queue.popleft()
            dx = [-1,1,x]
            for j in range(3):        
                nx = x + dx[j]
                if 0 <= nx <= 100000 and nx not in data:
                    if nx == m:
                        return day
                    k+=1
                    data[k] = nx
                    temp += 1
                    queue.append(nx)
        cnt = temp
        temp = 0    


data = [-1 for _ in range(100001)]
n,m = map(int,sys.stdin.readline().split())
print(bfs(n))