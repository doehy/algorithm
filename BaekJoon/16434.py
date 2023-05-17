import sys
input = sys.stdin.readline

n,damage = map(int,input().split())

td = 0
ta = damage
answer = float("inf")
for i in range(n):
    t,a,h = map(int,input().split())
    if t == 1:
        if h % ta == 0:
            td -= (h // ta - 1) * a
        else:
            td -= h // ta * a
        answer = min(td, answer) # 매번 answer을 갱신해준다.
    else:
        ta += a
        td += h
        if td > 0 :
            td = 0
answer = min(td, answer)
print(abs(answer) + 1)