t = int(input())

def dfs(graph):
    flag = 0
    for i in range(len(graph)):
        if i == len(graph) - 1:
            break
        if abs(graph[i+1][0] - graph[i][0]) + abs(graph[i+1][1] - graph[i][1]) > 1000:
            flag = 1
    return "sad" if flag == 1 else "happy"

for _ in range(t):
    n = int(input())
    graph=[]
    for _ in range(n+2):
        graph.append(list(map(int,input().split())))
    print(dfs(graph))

