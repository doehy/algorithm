import sys
input = sys.stdin.readline
n,k,p,x = map(int,input().split())
nLeng = len(str(n))
xStr = str(x)
while len(xStr) < nLeng:
    xStr = '0' + xStr
num = ['1111110', '0110000', '1101101', '1111001', '0110011', '1011011',
       '1011111', '1110000', '1111111', '1111011']
arr = []

for i in range(10):
    arr.append([])
    for j in range(10):
        if i == j:
            arr[i].append(0)
        else:
            d = 0
            for h in range(7):
                if num[i][h] != num[j][h]:
                    d += 1
            arr[i].append(d)

def dfs(dep, cnt, cx):
    if dep >= nLeng: # cnt가 기준이 되면 안 돼 조금 쓸 수도 있고 꽉 채워서 쓸 수도 있는 건데 여기서 기준은 끝까지 다 봤냐 안 봤냐가 되야해
        if int(cx) == x: # 근데 이 리턴 행동을 무작정 하면 안되는데
            return 0
        elif 1 <= int(cx) <= n:
            return 1
        else:
            return 0
    
    rst, cur = 0, int(cx[dep]) #정답, 현재 바꿔줄 숫자
    for i in range(10):
        if cur != i and (arr[cur][i] <= cnt): # 현재 바꿔줄 숫자가 i와 다르면서 남은 cnt보다 더 작거나 같은 경우에만
            dx = cx[:dep] + str(i) + cx[dep+1:]
            rst += dfs(dep + 1, cnt - arr[cur][i], dx)
        elif cur == i:
            rst += dfs(dep+1, cnt, cx)
    
    return rst # 씁 dps에서 이런 코드 짜기 쉽지 않ㅇ느데



print(dfs(0, p, xStr))