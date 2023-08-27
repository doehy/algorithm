t = int(input())

for i in range(t):
    data = list(map(int,input().split()))
    data.remove(data[0])
    avg = sum(data) / len(data)
    count = 0
    for i in data:
        if i > avg:
            count += 1
    per = count / len(data) 
    print("{:.3f}%".format(per*100))