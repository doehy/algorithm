import sys
input = sys.stdin.readline
s = input().rstrip()
t = input().rstrip()
result = []
def dfs(t):
    if len(t) == len(s): # 둘의 길이가 같을 때
        if t == s: # t와 s가 같다면
            result.append(1) # 1 추가
            return
        else:
            result.append(0) # 0 추가
            return
    if t[0] == 'A' and t[-1] == 'A': #AA일 경우에도 뒤집어도 된다. 안 되지 b를 못 없애잖아
        dfs(t[:len(t)-1])
    else:
        if t[-1] == 'A':
            dfs(t[:len(t)-1])
        if t[0] == 'B':
            dfs(t[1:][::-1])

dfs(t)
if 1 in result:
    print(1)
else:
    print(0)
    


# 무조건 2가지의 경우의 수가 매번 없다고 한들 2^이 아닌 것인가?

