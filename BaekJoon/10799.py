import sys
input = sys.stdin.readline
data = list(input().rstrip())
ans = 0
st = []

for i in range(len(data)):
    if data[i] == '(': st.append(data[i])
    else:
        if data[i-1] == '(':
            st.pop()
            ans += len(st)
        else:
            st.pop()
            ans += 1
print(ans)