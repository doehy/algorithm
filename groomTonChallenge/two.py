n = int(input())
t,m = map(int,input().split())
st, sm = t, m
for _ in range(n):
    x = int(input())
    st += x // 60
    sm += x % 60
    if sm > 59:
        sm -= 60
        st += 1
    if st > 23:
        st -= 24
print(st, sm)