n = input()
data = list(n)
data.sort(reverse=True)


if '0' not in data:
    print(-1)
else:
    data = list(map(int,data))
    if sum(data) % 3 == 0:
        data = list(map(str,data))
        print(''.join(data))
    else:
        print(-1)

