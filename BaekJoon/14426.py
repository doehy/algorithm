import sys
input = sys.stdin.readline
n,m = map(int,input().split())
data = set()
answer = 0
for i in range(n):
    text = input().rstrip()
    temp = ""
    for j in range(len(text)):
        temp += text[j]
        data.add(temp)
for i in range(m):
    text = input().rstrip()
    if text in data:
        answer += 1
print(answer)
