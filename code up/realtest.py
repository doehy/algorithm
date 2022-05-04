n = int(input())
s = []
for i in range(n):
    first, second = map(int, input().split())
    s.append([first, second])

print(s)