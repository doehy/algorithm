from collections import deque
n = int(input())
def check():
    q = deque()
    q.append([1,0])
    visited = [[0] * 10000 for _ in range(10000)]
    while q:
        s, c = q.popleft()
        if n == s:
            print(visited[s][c])
            return
        if not visited[s][s]:
            visited[s][s] = visited[s][c] + 1
            q.append([s,s]) 
        if not visited[s+c][c]:
            visited[s+c][c] = visited[s][c] + 1
            q.append([s+c, c])
        if s - 1 > 0 and not visited[s-1][c]:
            visited[s-1][c] = visited[s][c] + 1
            q.append([s-1,c])

check()

# 이건 왜 안 될까? 흠... 도저히 이유를 모르겠다.
# 일단 내 풀이도 잘못 된 거긴해 방문 처리를 해줬어야 했는데 방문 처리를 안 해줬어
# 그래서 방문 처리를 해준다고 했을 때 클립보드와 같이 계산하기 때문에 같이 움직이는 건 인정이넫 여기서 배열의 범위가 이해가 안 가긴해
# 근데 최대를 이천으로 잡는다고 한 들 어차피 목표 값인 n을 못 넘는 거 아닌가? 
