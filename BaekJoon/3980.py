import sys
input = sys.stdin.readline

def dfs(graph, visited, count, p, num):
	global answer
	if p == 11 and num == 11: # idx는 0부터 시작이니 11번째 사람은 없다 그리고 또한 11명이 자기 포지션을 정했어야하니 이 경우에만 최댓값을 갱신해준다. 
		answer = max(answer, count)
		return
	# 그 상황이 아니라면
	for i in range(11):
		if not visited[i] and graph[p][i] != 0:
			visited[i] = 1
			dfs(graph, visited, count + graph[p][i], p+1, num + 1)
			visited[i] = 0
	return

t = int(input())
for _ in range(t):
	graph = []
	visited = [0] * 11
	answer = 0
	for i in range(11):
		graph.append(list(map(int,input().split())))
	dfs(graph,visited,0,0,0)
	print(answer)