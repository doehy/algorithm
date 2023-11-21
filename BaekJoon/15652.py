n,m = map(int,input().split())

data = []

for i in range(1,n+1):
    data.append(i)

s = []

def dfs(data,s):
    if len(s) == m:
        print(*s)
        return
    else:
        if len(s) == 0:
            for i in range(len(data)):
                s.append(data[i])
                dfs(data,s)
                s.pop()
        else:
            for i in range(len(data)):
                if data[i] >= s[len(s)-1]:
                    s.append(data[i])
                    dfs(data,s)
                    s.pop()

dfs(data,s)