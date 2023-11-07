import sys

n = int(input())

s = set()n
for i in range(n):
    text = sys.stdin.readline().strip().split()
    if len(text) == 1:
        if text[0] == "all":
            s = set([i for i in range(1,21)])
        else:
            s = set()
    else:
        func,x = text[0],int(text[1])
        if func == "add":
            s.add(x)
        elif func == "remove":
            s.discard(x)
        elif func == "check":
            if x in s:
                print(1)
            else:
                print(0)
        else:
            if x in s:
                s.discard(x)
            else:
                s.add(x)

    