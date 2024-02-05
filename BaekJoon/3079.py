import sys
input = sys.stdin.readline
n,m = map(int,input().split())
time = list()
for _ in range(n):
    time.append(int(input()))

time.sort()
low , high = 0, time[0] * m
ans = float("inf")
while low <= high:
    mid = (low + high) // 2
    people = 0
    for i in time:
        people += mid // i
        if people > m:
            break
    if people >= m:
        high = mid -1
        ans = mid
    else:
        low = mid +  1
print(ans)
