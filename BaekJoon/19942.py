n = int(input())
mp,mf,ms,mv = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
s = []
result = float("inf")
temp = []
def f (num):
    global result
    global temp
    if len(s) == num:
        tmp = 0
        tmf = 0
        tms = 0
        tmv = 0
        price = 0
        for i in s:
            tmp += data[i-1][0]
            tmf += data[i-1][1]
            tms += data[i-1][2]
            tmv += data[i-1][3]
            price += data[i-1][4]
        if tmp >= mp and tmf >= mf and tms >= ms and tmv >= mv:
            if price < result:
                result = price
                temp = s[:]
                return
            elif price == result:
                if ''.join(map(str, s)) < ''.join(map(str, temp)):
                    temp = s[:]
                return     
        return
    if len(s) == 0:
        for i in range(1,n+1):
            s.append(i)
            f(num)
            s.pop()
    else:
        for i in range(1,n+1):
            if i > s[len(s)-1]:
                s.append(i)
                f(num)
                s.pop()

for i in range(1,n+1):
    f(i)

if result == float("inf"):
    print(-1)
else:
    print(result)
    for i in temp:
        print(i,end=" ")