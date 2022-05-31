x,y = map(int,input().split())

water = x
sun = y

result = 0

if x >= y:
    result += x
    temp = y//10
    result += y
    result += temp
else:
    result += y
    temp = x//10
    result += x
    result += temp

print(result)