def isSurprise(n):
    for i in range(0,len(n)-1):
        tmp = list()
        for j in range(len(n)-(i+1)):
            s = n[j] + n[j+i+1]
            if s in tmp:
                return False
            tmp.append(s)

    return True

while True:
    n = input()
    if n == '*':
        break
    if isSurprise(n)==True:  
        print(f"{n} is surprising.") 
    if isSurprise(n)==False:
        print(f"{n} is NOT surprising.")