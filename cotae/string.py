c = input()
zero_n = 0
one_n = 0

for i in c:
    if i == '0':
        zero_n += 1
    else:
        one_n += 1

czero = 0
cone = 0
before = 0

for i in c:  
    if i == '0':
        before = 0
        
    elif i == '1' and temp == '1':
            cone += 1

min_num = min(zero_n,one_n)
max_num = max(czero,cone)

result = min(min_num,max_num)
print(result)
