from collections import deque
import sys
input = sys.stdin.readline

text = input().rstrip()
leng = len(text)
n = int(input())
answer = 0

for i in range(n):
    temp = deque(input().rstrip())
    left,right = 0,leng - 1
    tp = ""
    for i in range(leng):
        tp += temp[i]
    tp = deque(tp)
    if text == ''.join(tp):
        answer += 1
        continue
    for i in range(1,len(temp)):
        tp.popleft()
        tp.append(temp[((i+leng) % 10) - 1])
        if text == ''.join(tp):
            answer += 1
            break

print(answer)