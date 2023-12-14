n,k = map(int,input().split())

data = list(map(int,input().split()))

chk = [0] * n

def f(day,weight):
    global result
    if weight < 0:
        return
    if day == n:
        result += 1
        return
    for i in range(n):
        if chk[i] == 0:
            chk[i] = 1
            f(day+1,weight+data[i]-k)
            chk[i] = 0

result = 0
f(0,0)
print(chk)
print(result)