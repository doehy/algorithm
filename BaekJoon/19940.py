import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    a,b,c,d,e = 0,0,0,0,0
    n = int(input())
    temp = 0
    modNum = n % 60
    difNum = n // 60
    if modNum <= 35:
        a +=  difNum
    else:
        a += difNum + 1
    temp += a * 60
    if temp == n:
        print(a,b,c,d,e)
        continue
    if temp > n:
        modNum = (temp - n) % 10
        difNum = (temp - n) // 10
        if modNum > 5:
            c += difNum + 1
        else:
            c += difNum
        temp += c * -10
        if temp == n:
            print(a,b,c,d,e)
            continue
    else:
        modNum = (n - temp) % 10
        difNum = (n - temp) // 10
        if modNum <= 5:
            b += difNum
        else:
            b += difNum + 1
        temp += b * 10
        if temp == n:
            print(a,b,c,d,e)
            continue
    if temp > n:
        print(a,b,c,d,e+(temp-n))
    else:
        print(a,b,c,d+(n-temp),e)