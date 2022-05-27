t = int(input())

data = []

for _ in range(t):
    n = int(input())
    start = list(input())
    end = list(input())
    a = 0
    b = 0
    num = 0
    result = 0
    
    while num < n:
        t_s = start[num]
        t_e = end[num]
        if t_s == t_e:
            num += 1
            continue
        else:
            if t_s == 'W':
                a += 1
                num += 1
            else:
                b += 1
                num += 1
    if a > b:
        result += b
        result += (a-b)
    elif a < b:
        result += a
        result += (b-a)
    else:
        result += a

    data.append(result)


for x in data:
    print(x,end=' ')
