import sys
input = sys.stdin.readline
m = int(input())
s = input().rstrip()
ans = float("inf")
def solve(num):
    global ans
    v = [{} for _ in range(num)]
    cost = 0
    for j in range(len(s)):
        if s[j] in v[j % num]:
            v[j%num][s[j]] += 1
        else:
            v[j%num][s[j]] = 1
    for j in range(num):
        a = [v[j].get('A', 0), v[j].get('G', 0), v[j].get('T', 0), v[j].get('C', 0)]
        cost += sum(a)
        cost -= max(a)
    ans = min(ans, cost)
    

if m == 0:
    print(0)
else:
    for i in range(1, m+1):
        solve(i)
    print(ans)
