n = int(input())
n -= 4
number = [6,2,5,5,4,5,6,3,7,6]
data = ['0','1','2','3','4','5','6','7','8','9']
flag = 0 
for i in range(len(number)):
    for j in range(len(number)):
        for k in range(len(number)):
            for p in range(len(number)):
                for q in range(len(number)):
                    for r in range(len(number)):
                        if number[i] + number[j] + number[k] + number[p] + number[q] + number[r] == n:
                            if int(data[i]+data[j]) + int(data[k]+data[p]) == int(data[q]+data[r]):
                                print(data[i] + data[j] + '+' + data[k]  + data[p] + '=' + data[q] + data[r])
                                flag = 1
                                break
                    if flag == 1:
                        break
                if flag == 1:
                    break
            if flag == 1:
                break                        
        if flag == 1:
            break
    if flag == 1:
        break
if flag == 0:
    print("impossible")
                            
