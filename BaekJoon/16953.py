a,b = input().split()

count = 0
while int(a) < int(b):
    if b[-1] == '1':
        b = b[:len(b)-1]
    else:
        if int(b) % 2 == 0:
            b = str(int(b) // 2)
        else:
            break
    count += 1

if int(a) == int(b):
    print(count + 1)
else:
    print(-1)