def check(string):
    flag = 0
    for i in range(1,len(string)):
        list = []
        for j in range(0,len(string)-i):
            if string[j:j+1] + string[j+i:j+i+1] not in list:
                list.append(string[j:j+1] + string[j+i:j+i+1]) 
            else:
                flag = 1
    if flag == 1:
        print(string+" is NOT surprising.")
    else:
        print(string+" is surprising.")


while(1):
    n = input()
    if n == '*':
        break    
    check(n)