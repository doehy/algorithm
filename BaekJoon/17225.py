a,b,n = map(int,input().split())
time = list()
color = list()
many = list()
sangmin = []
jisu = []
for i in range(n):
    t,c,m = input().split()
    time.append(t)
    color.append(c)
    many.append(m)
    if c == 'B':
        if len(sangmin) == 0:
            for i in range(int(m)):
                sangmin.append(int(t)+i*a)
        else:
            if int(t) - sangmin[len(sangmin) - 1] >= a: #차이가 나면 그냥 입력 받으면 되지만
                for i in range(int(m)):
                    sangmin.append(int(t)+(i+1)*a) #차이가 나지 않으면 고려해서 입력받아야한다.
            else:
                temp = sangmin[len(sangmin)-1]
                for i in range(int(m)):
                    sangmin.append(temp+(i+1)*a)
    else:
        if len(jisu) == 0:
            for i in range(int(m)):
                jisu.append(int(t)+i*b)
        else:
            if int(t) - jisu[len(jisu) - 1] >= b:
                for i in range(int(m)):
                    jisu.append(int(t)+i*b)
            else:
                temp = jisu[len(jisu)-1]
                for i in range(int(m)):
                    jisu.append(temp+(i+1)*b)
s_result = []
j_result = []
result = []
for i in sangmin:
    result.append((i,"a"))
for i in jisu:
    result.append((i,"j"))
result.sort()
go = 0
for x,y in result:
    go += 1
    if y == 'a':
        s_result.append(go)
    else:
        j_result.append(go)
print(len(s_result))
for i in s_result:
    print(i,end=' ')
print()
print(len(j_result))
for i in j_result:
    print(i,end=' ')


        
