n = int(input())

data = [(5,'a'),(5,'b'),(10,'a'),(10,'b'),(15,'a'),(15,'b'),(20,'a'),(20,'b')]
idx = 0
while n > 0:
    if n > data[idx][0]:
        n -= data[idx][0]
        idx = (idx + 1) % 8
        continue
    if data[idx][1] == 'a':
        if 0 <= n <= 5:
            print(1)
        elif 5 < n <= 10:
            print(2)
        elif 10 < n <= 15:
            print(3)
        else:
            print(4)
    else:
        n = data[idx][0] - n
        if 0 <= n <= 5:
            print(1)
        elif 5 < n <= 10:
            print(2)
        elif 10 < n <= 15:
            print(3)
        else:
            print(4)
    break