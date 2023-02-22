t = int(input())

def get_gcd(s):
    global count
    if s[0] > s[1]:
        for i in range(s[1],0,-1):
            if s[0] % i == 0 and s[1] % i == 0:
                count += i
                return
    elif s[1] > s[0]:
        for i in range(s[0],0,-1):
            if s[0] % i == 0 and s[1] % i == 0:
                count += i
                return
    else:
        count += s[0] # 둘 중에 아무거나
        return

def combi(s,visited):
    if len(s) == 2:
        get_gcd(s)
        return
    if len(s) == 0:
        for i in range(len(data)):
            if not visited[i]:
                s.append(data[i])
                visited[i] = 1
                combi(s,visited)
                s.pop()
    for i in range(len(data)):
        if not visited[i]:
            s.append(data[i])
            visited[i] = 1
            combi(s,visited)
            s.pop()
            visited[i] = 0

        

for i in range(t):
    data = list(map(int,input().split()))
    data.pop(0)
    count = 0
    visited = [0] * len(data)
    s = []
    combi(s,visited)
    print(count)