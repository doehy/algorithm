import sys
from collections import defaultdict
def dfs(a):
	visit = [False]*(n+1)
	queue = []
	queue.append(a)
	while queue:
		next = queue.pop()
		if visit[next]:
			continue
		visit[next] = True
	
		for i in tree[next]:
			if not visit[i]:
				queue.append(i)
				total[i] += total[next]  # 직속 상사의 칭찬 수치 더해줌


n,m = map(int,input().split())
n_list = list(map(int,input().split()))
total = [0]*(n+1)
tree = defaultdict(list)
for i in range(1,n):
	tree[n_list[i]].append(i+1)
	print(tree)
for i in range(m):
	a,b = map(int,sys.stdin.readline().split())
	total[a]+=b
dfs(1)
print(*total[1:])

# dfs를 하나도 사용하지 않는 dp
# import sys
# input = sys.stdin.readline
# n,m = map(int,input().split())
# data = list(map(int,input().split()))
# dp = [0] * n

# for _ in range(m):
# 	num,w = map(int,input().split())
# 	dp[num-1] += w # num번은 w만큼의 칭찬을 받았어 idx는 0부터 시작이니 num-1에 w만큼의 칭찬을 해

# for i in range(2,n): # 2번부터 시작하는 이유는 어차피 0번은 사장이라 칭찬이 없고 1번은 사장으로부터 받는 칭찬뿐이기에 고려대상이 아님 
# 	dp[i] += dp[data[i]-1]

# print(*dp)

# 14267 코드 그대로 구현하면 백퍼센트 시간초과다
# import sys
# input = sys.stdin.readline
# n,m = map(int,input().split())
# data = list(map(int,input().split()))
# dp = [0] * n
# def check(num,w): # 이제부터 부하직원들을 칭찬시킬거야
# 	for i in range(len(data)): # 돌아다니면서 내가 상사이면 칭찬을 해
# 		if data[i] == num: # data[i]가 num번이랑 같다면 즉 내가 상사라면 
# 			dp[i] += w # 해당 직원을 칭찬하고 
# 			check(i+1, w) # idx는 0부터 시작이었으니 +1만큼 한 것을 다시 넣어줘

# for _ in range(m):
# 	num,w = map(int,input().split())
# 	dp[num-1] += w # num번은 w만큼의 칭찬을 받았어 idx는 0부터 시작이니 num-1에 w만큼의 칭찬을 해
# 	check(num,w)

# print(dp)