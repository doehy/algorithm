from collections import deque

sr, sc = map(int,input().split())
er, ec = map(int,input().split())

dx = [[-1, -2, -3], [-1, -2, -3], [0, -1, -2], [0, 1, 2], [1,2,3], [1,2,3],[0,1,2],[0,-1,-2]]
dy = [[0, -1, -2], [0, 1, 2], [1, 2, 3], [1, 2, 3], [0, 1,2], [0,-1,-2],[-1,-2,-3],[-1,-2,-3]]


def bfs(i,j):
    que = deque()
    que.append([i,j])
    visited[i][j] = 1
    nx,ny = 0,0
    while que:
        x,y = que.popleft()
        for p in range(8):
            flag = 0
            for q in range(3):
                nx = x + dx[p][q]
                ny = y + dy[p][q]
                if 0 <= nx < 10 and 0 <= ny < 9 and not visited[nx][ny]: #방문 처리를 해주기 때문에 최솟값을 넣을 필요가 없다 왜냐하면 어차피 못 들어간다.
                    if nx == er and ny == ec and q == 2:
                        return data[x][y] + 1
                    elif q < 2 and nx == er and ny == ec: #애초에 여기서 다른 기물이 왕 밖에 없다.
                        flag = 1
                        continue
            if flag == 1:
                continue
            if 0 <= nx < 10 and 0 <= ny < 9 and not visited[nx][ny]: #방문 처리를 해주기 때문에 최솟값을 넣을 필요가 없다 왜냐하면 어차피 못 들어간다.
                    visited[nx][ny] = 1
                    que.append([nx,ny])
                    data[nx][ny] = data[x][y] + 1
    return -1 

data = [[0] * 9 for _ in range(10)]
visited = [[0] * 9 for _ in range(10)]
print(bfs(sr,sc))