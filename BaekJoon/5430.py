from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    functions = list(input().rstrip())
    leng = int(input())
    text = deque(input().rstrip()[1:-1].split(","))
    count = 0
    flag = 0
    if leng == 0:
        text = []
    for fun in functions:
        if fun == 'R':
            count += 1
        else:
            if len(text) < 1:
                print("error")
                flag = 1
                break
            else:
                if count % 2 == 0:
                    text.popleft()
                else:
                    text.pop()
    if flag == 0:
        if count % 2 == 0:
            print("[" +",".join(text)+"]")
        else:
            text.reverse()
            print("[" +",".join(text)+"]")
    