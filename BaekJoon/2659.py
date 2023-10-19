data = input().split()
if '0' in data:
    print(0)
else:
    temp_data = []
    min_number = 10000
    for i in range(4):
        min_number = min(min_number,int(''.join(data)))
        if i == 3:
            break
        temp = data[0]
        data.remove(temp)
        data.append(temp)
    time_number = min_number

    start = ['1','1','1','1']
    result = 0
    while int(''.join(start)) != time_number:
        if '0' in start:
            start = list(str(int(''.join(start))+1))
            continue
        min_number = 10000
        min_start = int(''.join(start))
        for i in range(4):
            min_number = min(min_number,int(''.join(start)))
            temp = start[0]
            start.remove(temp)
            start.append(temp)
        if min_start == min_number:
            result += 1
        start = list(str(int(''.join(start))+1))
    print(result+1)
        
    
    