import sys
input = sys.stdin.readline
n = int(input())
report = []
for _ in range(n):
    report.append(list(map(int,input().split())))
report.sort(key = lambda x : -x[1])
ans = 0
temp = report[0][1]
for i in range(len(report)-1):
    deadline = temp - (report[i][0]-1)
    if deadline - 1 >= report[i+1][1]:
        temp = report[i+1][1]
    else:
        temp = deadline - 1

ans = max(ans, temp - (report[n-1][0]-1) - 1)
print(ans)