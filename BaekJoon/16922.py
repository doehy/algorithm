n = int(input())

i = 1
v = 5
x = 10
l = 50

data = [i,v,x,l]

result = 0

num = []
sum = 0
temp = 0

for p in data:
    for q in data:
        sum += p
        sum += q
        if sum not in num:
            num.append(sum)
        sum = 0

print(len(num))
                
