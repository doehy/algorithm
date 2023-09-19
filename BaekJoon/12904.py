# 12904 그리디를 떠올린 이유 s와 t의 길이가 최대 약 천인다. 변화를 줄 수 있는 방법은 두 가지인데 만약 s의 길이가 1이고 t의 길이가 1000이라고 할 때
# s가 할 수 있는 역할은 2 ** 999이다. 말이 안 된다. 고로 그리디적으로 접근해야 한다. 
import sys
input = sys.stdin.readline
s = input().rstrip()
t = input().rstrip()
while len(t) > len(s):
    if t[-1] == 'B':
        t = t[:-1][::-1]
    else:
        t = t[:len(t)-1]

if t == s:
    print(1)
else:
    print(0)