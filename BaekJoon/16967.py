h,w,x,y = map(int,input().split())

b = [list(map(int,input().split())) for _ in range(h+x)]

a = list()

for num in range(x):
    for i in range(w):
        a.append(b[num][i])

for num in range(x,h):
    i = 0
    while i < w+y:
        if i < y:
            a.append(b[num][i])
            i += 1
        elif y <= i < w:
            a.append(b[num][i]-b[num-x][i-y])
            b[num][i] = b[num][i] -b[num-x][i-y]
            i += 1
        else:
            break


p = 0
while p < len(a):
    for i in range(p,p+w):
        print(a[i],end=" ")
    print()
    p += w
