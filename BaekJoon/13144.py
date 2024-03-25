import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))
l, r = 0, 0
result = 0
visited = [False] * 100001
while l <= r and r < n: # 범위 내부에 있으면
    if not visited[data[r]]: # 중복이 아니라면
        visited[data[r]] = True # 방문 처리해주고
        r += 1 # 오른쪽으로 한 칸 움직여
        result += r - l # 그 다음에 수열의 개수를 더해
    else:
        while visited[data[r]]:
            visited[data[l]] = False
            l += 1
print(result)
