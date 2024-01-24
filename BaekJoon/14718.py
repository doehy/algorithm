import sys
input = sys.stdin.readline
n,m = map(int,input().split())
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))
ans = float("inf")

for i in range(n):
    for j in range(n):
        for k in range(n):
            cur_p = data[i][0]
            cur_d = data[j][1]
            cur_i = data[k][2]
            count = 0
            for l in range(n):
                if cur_p >= data[l][0] and cur_d >= data[l][1] and cur_i >= data[l][2]:
                    count += 1
            if count >= m:
                ans = min(ans, (cur_p + cur_d + cur_i))
print(ans)