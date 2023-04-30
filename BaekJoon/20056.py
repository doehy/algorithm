import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())

data = []

graph = [[[] for i in range(n)] for i in range(n)]

print(graph)