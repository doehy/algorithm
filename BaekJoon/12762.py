import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))
leftDp = [1] * (n)
rightDp = [1] * (n)
ans = 1


for i in range(n):
    for j in range(i):
        if data[i] < data[j]:
            leftDp[i] = max(leftDp[i], leftDp[j] + 1)

for i in range(n-2,-1,-1):
    for j in range(i+1,n):
        if data[i] < data[j]:
            rightDp[i] = max(rightDp[i], rightDp[j] + 1)

for i in range(n):
    if ans < leftDp[i] + rightDp[i] - 1:
        ans = leftDp[i] + rightDp[i] - 1
print(ans)

# 한쪽으로 쭉 내려가는 것을 찾거나, 한 쪽으로 쭉 올라가는 것을 찾거나, 한 번 내려갔다가 올라가는 것을 찾거나 
