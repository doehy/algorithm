N = int(input())

gongpo = list(map(int,input().split()))

gongpo.sort()

sum = 0

length = len(gongpo)

while length > 0:
    for i in gongpo:
        if length > i:
            length -= i
            sum += 1
    break

print(sum)


