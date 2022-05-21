tong = [7,5,6,4,2,3,7,5]

num = []



for i in tong:
    flag = 0
    if len(num) == 0:
        num.append(i)
    else:
        for j in range(len(num)):
            if num[j] + i <= 10:
                num[j] += i
                flag = 1
                break
        if flag == 0:
            num.append(i)

print(num)
