l,c = map(int,input().split())

data = input().split()
data.sort()
s = []

m = 0 
z = 0
def check(s):
    global m 
    global z
    if len(s) == l and m >= 1 and z >= 2:
        print(''.join(s))
        return
    if len(s) == 0:
        for i in data:
            s.append(i)
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                m += 1 
                check(s)
            else:
                z += 1
                check(s)
            temp = s.pop()
            if temp == 'a' or temp == 'e' or temp == 'i' or temp == 'o' or temp == 'u':
                m -= 1
            else:
                z -=  1
    else:
        for i in data:
            if i > s[len(s)-1]:
                s.append(i)
                if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u': 
                    m += 1 
                    check(s)
                else:
                    z += 1
                    check(s)
                temp = s.pop()
                if temp == 'a' or temp == 'e' or temp == 'i' or temp == 'o' or temp == 'u':
                    m -= 1
                else:
                    z -=  1
                

check(s)