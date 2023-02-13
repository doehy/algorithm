n,m = map(int,input().split())

data = list(map(int,input().split()))

data.sort()

def check(s):
    if len(s) == m:
        print(*s)
        return
    for i in range(len(data)):
        if data[i] not in s:
            s.append(data[i])
            check(s)
            s.pop()
    

s = []
check(s)


