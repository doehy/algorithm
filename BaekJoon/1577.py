import sys
input = sys.stdin.readline
c,r = map(int,input().split())
k = int(input())
dp = [[0 for _ in range(c+2)] for _ in range(r+2)]
dp[1][1] = 1
end = set()
load = set()

for _ in range(k):
    c1,r1,c2,r2 = map(int,input().split())
    (r1,c1), (r2,c2) = sorted([(r1+1, c1+1), (r2+1, c2+1)])
    end.add((r2,c2))
    load.add((r1,c1,r2,c2))
    
for x in range(1, r+2): 
    for y in range(1, c+2):
        if x == 1 and y == 1:
            continue
        if (x,y) in end:
            if (x-1,y,x,y) not in load:
                dp[x][y] = dp[x-1][y]
            elif (x,y-1,x,y) not in load:
                dp[x][y] = dp[x][y-1]
        else:
            dp[x][y] = dp[x-1][y] + dp[x][y-1]

print(dp[r+1][c+1])

# 애초에 시작은 0,0부터 시작해서 n,m에서 끝난다. 하지만 리스트 특성상 n+1,m+1로 해야 n,m까지 갈 수 있다.
# 하지만 반복문을 편히 돌기 위해서 1,1부터 시작한다. 그러면 n+1,m+1로 할 것이 아니라 n+2,m+2로 해야한다.
# 누가 너한테 리스트는 위에서부터 아래로 내려간다고 했어?