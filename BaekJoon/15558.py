from collections import deque
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
left = list(input())
right = list(input())
l_visited = [0] * n 
r_visited = [0] * n
def bfs(idx, dif):
    q = deque()
    q.append((idx,dif,0))
    l_visited[idx] = 1
    while q:
        idx, dif,time = q.popleft()
        for i in range(3):
            if i == 0:
                nx = idx + 1
            elif i == 1:
                nx = idx - 1
            elif i == 2:
                nx = idx + k
                if dif == "l":
                    dif = 'r'
                else:
                    dif = 'l'
            if nx >= n: # n의 범위를 벗어났다는 것은게임을 클리어했다는 뜻
                return True
            else: # n보다 작아 그럼 아직 말판안에 있다는 뜻
                if nx > time and dif == 'l' and left[nx] == '1'and l_visited[nx] == 0:
                    l_visited[nx] = 1
                    q.append((nx,dif,time+1))
                elif nx > time and dif == 'r' and right[nx] == '1' and r_visited[nx] == 0:
                    r_visited[nx] = 1
                    q.append((nx,dif,time+1))
    return False

if bfs(0,"l"):
    print(1)
else:
    print(0)