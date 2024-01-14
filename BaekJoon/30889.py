import sys
input = sys.stdin.readline

n = int(input())
graph = [["."] * 20 for _ in range(10)]
for i in range(n):
    sit = input()
    if len(sit) == 2:
        graph[ord(sit[0]) - 65][int(sit[1]) - 1] = 'o'
    else:
        graph[ord(sit[0]) - 65][int(sit[1] + sit[2]) - 1] = 'o'

for s in graph:
    print(''.join(s))
    