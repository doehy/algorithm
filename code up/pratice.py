n = int(input())
lst = list()

for i in range(n):
    number = int(input())
    if number !=0:
        lst.append(number)
    else:
        lst.pop()

num = len(lst)
sum = 0
for i in range(num):
    sum += lst[i]

print(sum)