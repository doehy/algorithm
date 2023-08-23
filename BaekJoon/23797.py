import sys
input = sys.stdin.readline
crying = input().rstrip()
answer = 1
k = p = 0
if crying[0] == 'K':
    k += 1
else:
    p += 1
for i in range(1, len(crying)):
    if crying[i] == "K":
        k += 1
        if p > 0:
            p -= 1
    else:
        p += 1
        if k > 0:
            k -= 1
answer = p+k
print(answer)
