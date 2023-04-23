import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

s_tp = ""
t_tp = ""

for i in range(len(s)):
    t_tp += t
for i in range(len(t)):
    s_tp += s

if t_tp != s_tp:
    print(0)
else:
    print(1)