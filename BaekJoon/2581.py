M = int(input())
N = int(input())

lst = list()

gitbal = 0
number = 0
thtn = 0
min_thtn = 0

for i in range(M,N+1):
    number = 0
    for j in range(i):
        if i % (j+1) == 0:
            number += 1
    if number == 2:
        thtn += i
        if gitbal == 0:      
            min_thtn += i
            gitbal +=1

if thtn == 0:
    print(-1)
else:
    print(thtn)
    print(min_thtn)