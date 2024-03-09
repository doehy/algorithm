from collections import deque
def solution(land):
    n, m = len(land), len(land[0])
    visited = [[-1] * m for _ in range(n)]
    space = {-1:0}

    def dfs(x, y, d):
        nonlocal land, visited
        q = deque([[x, y]])
        visited[x][y] = d

        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        cnt = 1
        while q:
            cx, cy = q.popleft()
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1 and visited[nx][ny] == -1:
                    q.append([nx, ny])
                    visited[nx][ny] = d
                    cnt += 1
        return cnt

    f = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == -1 and land[i][j] == 1:
                space[f] = dfs(i, j, f)
                f += 1

    result = 0

    for i in list(zip(*visited)):
        print(*visited)
        print(i)
        temp = 0
        for j in set(i):
            print(j)
            temp += space[j]
        result = max(result, temp)
    return(result)